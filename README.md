# MolE molecular embeddings

MolE, Recursions foundation model for molecular graphs, learns embeddings using a transformer with disentangled attention adapted from DeBERTa. Pretraining first predicts each atoms local environment in a self-supervised step, then refines embeddings on ~456,000 ChEMBL compounds across 1310 bioactivity tasks. The original study self-supervised on up to 842 million molecules and showed finetuned MolE topped 10 of 22 ADMET benchmarks from the Therapeutic Data Commons. Since Recursion never released those full weights, Ersilia instead serves the smaller GuacaMol/ChEMBL-pretrained checkpoint.

This model was incorporated on 2025-06-23.


## Information
### Identifiers
- **Ersilia Identifier:** `eos1tt2`
- **Slug:** `mole-embeddings`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`, `Chemical graph model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `768`
- **Output Consistency:** `Fixed`
- **Interpretation:** 768-dimensional vector encoding a molecules structure and biological information learned during MolE pretraining.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_000 | float |  | MolE embedding dimension 0 from the pretrained transformer's CLS token |
| feat_001 | float |  | MolE embedding dimension 1 from the pretrained transformer's CLS token |
| feat_002 | float |  | MolE embedding dimension 2 from the pretrained transformer's CLS token |
| feat_003 | float |  | MolE embedding dimension 3 from the pretrained transformer's CLS token |
| feat_004 | float |  | MolE embedding dimension 4 from the pretrained transformer's CLS token |
| feat_005 | float |  | MolE embedding dimension 5 from the pretrained transformer's CLS token |
| feat_006 | float |  | MolE embedding dimension 6 from the pretrained transformer's CLS token |
| feat_007 | float |  | MolE embedding dimension 7 from the pretrained transformer's CLS token |
| feat_008 | float |  | MolE embedding dimension 8 from the pretrained transformer's CLS token |
| feat_009 | float |  | MolE embedding dimension 9 from the pretrained transformer's CLS token |

_10 of 768 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1tt2.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1tt2.zip)

### Resource Consumption
- **Model Size (Mb):** `996`
- **Environment Size (Mb):** `2633`


### References
- **Source Code**: [https://github.com/recursionpharma/mole_public](https://github.com/recursionpharma/mole_public)
- **Publication**: [https://doi.org/10.1038/s41467-024-53751-y](https://doi.org/10.1038/s41467-024-53751-y)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Non-commercial](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos1tt2
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos1tt2
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
