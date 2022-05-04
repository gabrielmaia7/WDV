import pandas as pd
import json
import mturk
import time
import pymongo
import sys
from datetime import datetime
import botocore
import pdb

""" 
    Run this with 'python update_db.py x y z' where:
    x is 0 if using the sandbox, 1 if using the marketplace;
    y is the amount of seconds to wait between loops;
    z is 0 if not approving assignments as they come, 1 otherwise
    
"""

with open('./config/mongodb_credentials.json','r') as f:
    mongodb_credentials = json.load(f)

create_hits_in_production = (sys.argv[1] == '1')
time_between_updates = sys.argv[2]
to_approve = (sys.argv[3] == '1')
# Change the string in MongoClient to a connection string to a Mongodb base/cluster of your choice

db_client = pymongo.MongoClient(mongodb_credentials["connection_string"])

db = db_client['verbalisations']
is_pilot = False

suffix = ''
if not create_hits_in_production:
    suffix = suffix + '_sandbox'
if is_pilot:
    suffix = suffix + '_pilots'

print('hit_results' + suffix)
hit_result_collection = db['hit_results' + suffix]

mt = mturk.MTurk()
mt.launch_client(create_hits_in_production)

fails = 0
sleep_exp = 0
while True:
    ''' Update all hits in the database with correct results '''
    hit_result_collection_list = list(hit_result_collection.find({'hit.HITStatus': {'$not': {'$eq': 'Disposed'}}}))
    for i, hit in enumerate(hit_result_collection_list):
        try:
            hit_result_collection.update_one(
                {'_id': hit['_id']},
                {
                    "$set": {
                        "hit": mt.client.get_hit(HITId = hit['_id'])['HIT'],
                        'answers': mt.get_hit_answers(hit['_id'], approve=to_approve)
                    }
                })
            print(f'{100*(i+1)/len(hit_result_collection_list)}%'+' '*20, end='\r')
            fails = 0
            sleep_exp = 0
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'ThrottlingException':    
                print(e)            
                time.sleep(2**sleep_exp)
                fails = fails + 1
                if fails > 4:
                    sys.exit(-1)
                continue
            else:
                print(e)            
                time.sleep(1)
                fails = fails + 1
                if fails > 4:
                    sys.exit(-1)
                continue
        except Exception as e:
            print(e)            
            time.sleep(1)
            fails = fails + 1
            if fails > 4:
                sys.exit(-1)
            continue
    print('{}: Updated db has {} non-disposed entries'.format(datetime.now(),len(hit_result_collection_list)))
    time.sleep(int(time_between_updates))
