# imports
import os
import sys
import numpy as np
from rdkit import Chem
from ersilia_pack_utils.core import read_smiles, write_out
from mole.cli.mole_predict import encode

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoint_path = os.path.join(root, "..", "..", "checkpoints", "MolE_GuacaMol_27113.ckpt")

EMBEDDING_DIM = 768


def my_model(smiles_list):
    # MolE's own dataset raises on an unparseable SMILES (no internal validity
    # check), so invalid molecules are filtered out here and reinserted as
    # None rows afterwards to keep the output aligned with the input.
    valid_idx, valid_smiles = [], []
    for i, smi in enumerate(smiles_list):
        if Chem.MolFromSmiles(smi) is not None:
            valid_idx.append(i)
            valid_smiles.append(smi)

    results = [[None] * EMBEDDING_DIM for _ in smiles_list]
    if valid_smiles:
        embeddings = encode(
            smiles=valid_smiles,
            pretrained_model=checkpoint_path,
            batch_size=32,
            num_workers=0,
            accelerator="cpu",
        )
        for pos, idx in enumerate(valid_idx):
            results[idx] = embeddings[pos].tolist()

    return results


# read SMILES from .csv file
_, smiles_list = read_smiles(input_file)

# run model
outputs = my_model(smiles_list)

# check input and output have the same length
assert len(smiles_list) == len(outputs)

# write output in a .csv file
headers = ["feat_{0}".format(str(i).zfill(3)) for i in range(EMBEDDING_DIM)]
write_out(outputs, headers, output_file, np.float32)
