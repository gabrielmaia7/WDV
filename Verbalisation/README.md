# WDV's Verbalisation

In this folder we store all the scripts, models, and data produced/used in verbalising the Wikidata claims obtained from parsing the dumps. This is followed by the crowdsourcing stage, and is thus the *second* step in our approach.

The models and respective scripts used here were slightly adapted from [Ribeiro et al.'s code](https://github.com/UKPLab/plms-graph2text) for their paper *"Investigating Pretrained Language Models for Graph-to-Text Generation"*.

This folder contains the following files and sub-folders:

- *sampled_df_pre_verbalisation.csv*: Data produced at the end of the previous stage, Wikidata Claim Acquisition.
- *pilot_sampled_df_verbalised.csv*: Subset from *sampled_df_pre_verbalisation.csv* and verbalised for crowdsourcing pilot.
- *campaign_sampled_df_verbalised.csv*: The *sampled_df_pre_verbalisation.csv* data verbalised.
- *campaign_sampled_df_verbalised_english.csv*: A susbet of *campaign_sampled_df_verbalised.csv* where all labels are in English.
- *T5-Verbalisation-For-Crowdsourcing.ipynb*: A notebook that applies the verbalisation model on the Wikidata claims. Here we also replace unknown tokens the model does not recognise, and split the generated verbalisations into different groups that will be annotated separately due to crowdsourcing budget constraints.
- *verbalisation_module.py*: Encapsulates the verbalisations and unk-replacement functions from the *T5-Verbalisation-For-Crowdsourcing.ipynb* notebook into an importable Python module.
- *\_\_init\_\_.py*: File to make the verbalisation module findable from outside.
- *graph2text*: Folder with the implementation of the verbalisation model in PyTorch. Altered version from [Ribeiro et al.'s code](https://github.com/UKPLab/plms-graph2text). Check their documentation for more info (plus the code should be somewhat understandable if you have a grasp of PyTorch). On *graph2text/outputs/test_model* are the outputs from the model testing right after training on WebNLG. On *graph2text/outputs/t5-base_13881* is where we have stored the best-trained model that we used for our verbalisations alongside its validation metrics, both in `model.bin` and `.ckpt` formats. 

Two model files were compressed and split due to size:
- *graph2text/outputs/t5-base_13881/val_avg_bleu=68.1000-step_count=5.ckpt* was compressed into *best_model.ckpt.tar.gz* and split into *best_model.ckpt.tar.gz.partXX* files using `split`.
  - You can join them with `cat best_model.ckpt.tar.gz.parta* > best_model.ckpt.tar.gz` and unpack it with `tar -xzvf best_model.ckpt.tar.gz`
- *graph2text/outputs/t5-base_13881/best_tfmr/pytorch_model.bin* was compressed into *pytorch_model.bin.tar.gz* and split into *pytorch_model.bin.tar.gz.partXX* files using `split`.
  - You can join them with `cat pytorch_model.bin.tar.gz.parta* > pytorch_model.bin.tar.gz` and unpack it with `tar -xzvf pytorch_model.bin.tar.gz`