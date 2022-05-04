# WDV

## About
WDV is a dataset for the verbalisation of Wikidata triples. It is thoroughly described in the paper that accompanies it.

It consists of a large partially annotated dataset of over 7.6k entries that align a broad collection of Wikidata claims with their respective verbalisations.

The attributes seen in each entry consist of: attributes describing the claim, such as its Wikidata ID (claim id ) and its rank (normal, deprecated or preferred); attributes from the claim’s components (subject, predicate, and object), including their Wikidata IDs (e.g. subject id ), labels (e.g. subject label ), descriptions (e.g. subject desc), and aliases (e.g. subject alias); a JSON representation of the object alongside its type (object datatype) as defined by Wikidata; attributes from the claim’s theme such as its root class’ Wikidata ID (theme root class id) and label (theme label); the aligned verbalisation, before and after replacement of tokens unknown to the model (verbalisation unk replaced ); the sampling weight from the stratified sampling process; and the crowdsourced annotations and their aggregations, for those entries (∼1.4k) that are annotated. 

WDV is a 3 star dataset according to the 5 star deployment scheme for Linked Data. It is available on the web in a structured, machine-readable, and non-proprietary format. WDV is aimed at directly helping with managing reference quality in Wikidata by allowing us to close the gap in form between the data in the KG and the data in its sources. It has already made possible efforts towards automated fact verification in Wikidata.

## This Repository

This repository contains all the data and scripts used in the construction of WDV. It is structured as follows:
- *WikidataClaims*: This folder contains the scripts that parse Wikidata dumps and assemble the stratified sample of Wikidata claims for all three partitions used in the study (WebNLG_SEEN, WebNLG_UNSEEN, WD_UNSEEN). 
- *Verbalisation*: This folder contains the scripts and model used in the verbalisation of the claims obtained from the *WikidataClaims* scripts.
- *Crowdsourcing*: This folder contains all scripts, html templates, crowdsourcing results and data artefacts from the crowdsourcing done to measure fluency and adequacy of verbalisations.

There are individual README.md files inside each folder for more detailed descriptions of their contents.


## The Paper and the Data

You can check our paper here: [link to paper at ArXiv](TBD)
You can also find the data at figshare here: [link to data at Figshare](TBD)

## Citation

```
TBD
```

## Contact

For more details and questions, contact Gabriel at [mailto:gabriel.amaral@kcl.ac.uk](gabriel.amaral@kcl.ac.uk) 

