# WDV's Wikidata Claimset Acquisition

In this folder we store all the scripts used in parsing Wikidata to construct a representative set of broad claims. This is the *first* step in our approach. It is followed by the verbalisation of these claims, and the crowdsourcing of their annotations for fluency and adequacy. Here we also store all data by-products of the process.

This folder contains the following files and sub-folders:

- *1. WebNLG_Classes_To_Wikidata_Mapping.ipynb*: Maps WebNLG classes from DBpedia to Wikidata. This is done so that we can test how the verbalisation models trained in WebNLG behave in Wikidata by looking at data that follows similar themes of semantic information carried. This notebook performs this mapping, which is not trivial due to the very different structures of both DBpedia and Wikidata, as is documented in the paper.
- *2. Getting_Wikidata_Entities_With_WebNLG_Themes.ipynb*: Retrieves Wikidata entities within the WebNLG themes (and also some in additional classes outside of WebNLG) from a parsed Wikidata dump. The notebook describes the process.
- *3. Creating_Wikidata_Claim_Datasets_Themed.ipynb*: Retrieves a balanced dataset of claims from the Wikidata entities obtained in the previous notebook.
- *wikidata_parser.py*: A script that parses a downloaded Wikidata dump (*.json.bz2 format) and stores parsed claims and references into a local SQL database for quick access.
- *wikidata_utils.py*: A module with functionalities that help us query Wikidata's SPARQL engine while maintaining a local cache file.
- *Check_Extracted_Picks.ipynb*: Purely for debugging of the parsing process.
- *data*: A subfolder to hold all the by-products of this dataset processing/creation, as well as the end-results.
    - *sampled_df_pre_verbalisation.csv*: Balanced claim sample obtained from this data acquisition process. The next step is to feed it to the verbalisation process.