# WDV's Verbalisation

In this folder we store all the scripts, models, and data produced/used in verbalising the Wikidata claims obtained from parsing the dumps. This is followed by the crowdsourcing stage, and is thus the *second* step in our approach.

The models and respective scripts used here were slightly adapted from [Ribeiro et al.'s code](https://github.com/UKPLab/plms-graph2text) for their paper "Investigating Pretrained Language Models for Graph-to-Text Generation".

This folder contains the following files and sub-folders:

- *sampled_df_pre_verbalisation.csv*: Data produced at the end of the previous stage, Wikidata Claim Acquisition.
- *pilot_sampled_df_verbalised.csv*: Subset from *sampled_df_pre_verbalisation.csv* and verbalised for crowdsourcing pilot.
- *campaign_sampled_df_verbalised.csv*: The *sampled_df_pre_verbalisation.csv* data verbalised.
- *campaign_sampled_df_verbalised_english.csv*: A susbet of *campaign_sampled_df_verbalised.csv* where all labels are in English.
- *T5-Verbalisation-For-Crowdsourcing.ipynb*: A notebook that applies the verbalisation model on the Wikidata claims. Here we also replace unknown tokens the model does not recognise, and split the generated verbalisations into different groups that will be annotated separately due to crowdsourcing budget constraints.
- *verbalisation_module.py*: Encapsulates the verbalisations and unk-replacement functions from the *T5-Verbalisation-For-Crowdsourcing.ipynb* notebook into an importable Python module.