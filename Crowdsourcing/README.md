# WDV's Crowdsourcing

In this folder we store all data and scripts used in our crowdsourcing. This is the *third* step in our approach and is to be executed right after the verbalisation step.

## adequacy_task

This directory holds the HTMLs for the adequacy task. It consists of:

- *adequacy_mockup.html*: This is an HTML file filled with a random set of claim/verbalisation pairs to serve as a mockup during development. It portrays an example of the task which you can run on you browser right now.
- *adequacy_template.html*: This is the same as *adequacy_mockup.html*, but the pairs do be judged and the language test are replaced by placeholders. Upon release of the crowdsourcing experiment, these placeholders are filled with claim-verbalisation pairs to be annotated by the crowd.

## fluency_task

This directory holds the HTMLs for the fluency task. It consists of:

- *fluency_mockup.html*: This is an HTML file filled with a random set of claim/verbalisation pairs to serve as a mockup during development. It portrays an example of the task which you can run on you browser right now.
- *fluency_template.html*: This is the same as *fluency_mockup.html*, but the pairs do be judged and the language test are replaced by placeholders. Upon release of the crowdsourcing experiment, these placeholders are filled with claim-verbalisation pairs to be annotated by the crowd.

## task_deploy_and_analysis

This directory holds the data, scripts, and configuration files to actually run the crowdsourcing. It consists of:

- *config*: This folder contains configuration files needed for the crowdsourcing.
    - *config/campaign/batch_1_and_2/task_config_adequacy.json*: A json file with specific configurations for the adequacy task, when run as part of the entire crowdsourcing campaign, following Mechanical Turk configuration keywords. Applicable for both batches of the campaign.
    - *config/campaign/batch_1_and_2/task_config_fluency.json*: A json file with specific configurations for the fluency task, when run as part of the entire crowdsourcing campaign, following Mechanical Turk configuration keywords. Applicable for both batches of the campaign.
    - *config/pilot/task_config_adequacy.json*: A json file with specific configurations for the adequacy task, when run as part of the pilot experiments, following Mechanical Turk configuration keywords.
    - *config/pilot/task_config_fluency.json*: A json file with specific configurations for the fluency task, when run as part of the pilot experiments, following Mechanical Turk configuration keywords. Applicable for both batches of the campaign.
    - *amazon_credentials.json*: Credentials for your AWS account, needed to run MTurk crowdsourcing tasks. Is empty and should be filled by you with your own credentials.
    - *mongodb.json*: Credentials for your Mongodb cluster, needed to store the results from crowdsourcing for analysis. Is empty and should be filled by you with your own credentials. Feel free to modify the code to use any other database of your preference.
    - *banlist.json*: AWS Worker IDs suspected of being spammers/bots. Keep this updated as new spamming/bot accounts are created constantly.
- *data*: This folder stores the data that is used in crowdsourcing, which includes the claim-verbalisation pairs sent to the crowd, golden data, and results collected.
    - *pilot*: Data used in and collected from the crowdsourcing pilot:
        - *pilot_sampled_df_verbalised.csv*: The claims sampled from Wikidata after passing through verbalisation. This is a small subset used for the pilot.
        - *verbalisations.json*: Claim-verbalisation pairs parsed from *pilot_sampled_df_verbalised.csv*, except for those selected to be golden data.
        - *verbalisations_gd_1.json*: Claim-verbalisation pairs parsed from *pilot_sampled_df_verbalised.csv* and selected to be golden data.
        - *verbalisations_gd_2.json*: An augmented set of claim-verbalisation pairs generated from *pilot_sampled_df_verbalised.csv* specifically to be golden data.
        - *TaskSets_pilot_run_1.json*: The data sent to the crowd in the first pilot run.
        - *TaskSets_pilot_run_2.json*: The data sent to the crowd in the second pilot run.
        - *hit_results_pilots.json*: The raw data and metadata gathered from the crowd during both pilot runs.
    - *campaign*: Data used in and collected from the crowdsourcing pilot:
        - *campaign_sampled_df_verbalised.csv*: The claims sampled from Wikidata after passing through verbalisation.
        - *campaign_sampled_df_verbalised_english.csv*: Subset of *campaign_sampled_df_verbalised.csv* with only claim-verbalisation pairs where all labels are in English. Broken down in multiple proportionaly represented campaign groups in order to better manage crowdsourcing expenses.
        - *campaign_sampled_df_verbalised_unk_fixed.csv*: The data from *campaign_sampled_df_verbalised.csv* with *unk* tokens corrected.
        - *campaign_sampled_df_verbalised_unk_fixed.csv*: The data from *campaign_sampled_df_verbalised_unk_fixed.csv* merged with the aggregated annotations from the crowd.
        - *crowdsourced_campaign_sampled_df_verbalised_english.csv*: A subset of the the data from *campaign_sampled_df_verbalised_english.csv* alongside aggregated annotations from the crowd, but only those entries that were annotated.
        - *batch_1*: Data used in the first batch of the crowdsourcing campaign.
            - *verbalisations.json*: Claim-verbalisation pairs parsed from *campaign_sampled_df_verbalised_english.csv*, except for those selected to be golden data. Campaign groups 1 to 3 were used in batch 1.
            - *TaskSets_adequacy.json*: The data sent to the crowd in the campaign's first batch, on the adequacy task.
            - *TaskSets_fluency.json*: The data sent to the crowd in the campaign's first batch, on the fluency task.
        - *batch_2*: Data used in the first batch of the crowdsourcing campaign.
            - *verbalisations.json*: Claim-verbalisation pairs parsed from *campaign_sampled_df_verbalised_english.csv*, except for those selected to be golden data. Campaign groups 10, 15, 20, 25, 30, and 35 were used in batch 2.
            - *TaskSets_adequacy.json*: The data sent to the crowd in the campaign's second batch, on the adequacy task.
            - *TaskSets_fluency.json*: The data sent to the crowd in the campaign's second batch, on the fluency task.
        - *verbalisations_df.json*: Claim-verbalisation pairs parsed from *campaign_sampled_df_verbalised_english.csv* and selected to be golden data.
        - *verbalisations_gd_plus_fluency.json*: Claim-verbalisation pairs parsed from *campaign_sampled_df_verbalised_english.csv* and selected to be golden data, plus augmented cases of bad fluency.
        - *verbalisations_gd_plus_adequacy.json*: Claim-verbalisation pairs parsed from *campaign_sampled_df_verbalised_english.csv* and selected to be golden data, plus augmented cases of bad adequacy.
        - *hit_results.json*: The raw data and metadata gathered from the crowd during both campaign batches.
        - *WDV_JSON.json*: The entire data from the sampled claims + crowdsourcing campaign in JSON format as decribed by the paper.
    - *language_tests.json*: The collection of language test questions for attention checking.
    - *bad_quality_analysis*: A directory with all verbalisations deemed by the crowd as either bad fluency or bad adequacy, which was later manually investigated and annotated.
        - *claims_crowd_df_results_not_adequate.csv*: Claim-Verbalisation pairs with low adequacy for coding of possible sources of low adequacy.
        - *claims_crowd_df_results_not_fluent.csv*: Claim-Verbalisation pairs with low fluency for coding of possible sources of low fluency.
        - *low_adequacy_coded_report.pdf*: Results from coding of possible sources of low adequacy.
        - *low_fluency_coded_report.pdf*: Results from coding of possible sources of low fluency.
        - *LowScoringVerbalisations_NVIVO_Project.nvp*: NVIVO project used to perform the coding.
- *imgs*: Images outputed by the scripts in *notebooks*, used in the paper.
- *notebooks*: Jupyter notebooks and Python notebooks that ran the crowdsourcing, as well as processed and analysed the data from the crowdsourcing.
    - *Full_Dataset_(Not_Only_English)_Breakdown.ipynb*: Analysis of full dataset before engaging with crowdsourcing. 
    - *Full_English_Dataset_Stratification_Analysis_(PreCrowdsourcing).ipynb*: Checks each campaign group in the English-only portion of the data to see if they have the same representation of claim types.
    - *GenerateTaskSets.ipynb*: Notebook responsible for taking the data in CSV format straight from the verbalisation stage and transforming it into the TaskSets seen in the data folder. Includes generation of golden data and split of data into separate task sets.
    - *ExperimentRunner.ipynb*: Notebook responsible for putting the tasksets into the HTML templates and sending them to MTurk.
    - *Pilot_Results.ipynb*: Explores the results from the pilots.
    - *Campaign_Results.ipynb*: Explores the results from the campaign.
    - *krippendorff_alpha.py*: Implementation of Krippendorff's Alpha.
    - *fleiss.py*: Implementation of Fleiss' Kappa.
    - *mturk.py*: A module with interfaces to Amazon's Mechanical Turk implemented.
    - *update_db.py*: A script responsible for automatically (every X seconds) checking on crowdsourced submissions, approving them, and updating the database. If lots of HITs are deployed, to avoid this script from updating already-Diposed (either completed or timed-out) HITs, run one of the last cells in *ExperimentRunner.ipynb*, which cleans those HITs from the queue.