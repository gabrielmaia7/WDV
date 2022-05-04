import json
import boto3
import xmltodict
from datetime import datetime

class MTurk():

    def __init__(self):
        with open('./config/amazon_credentials.json')  as f:
            cfg = json.load(f)

        self.access_key = cfg['access_key']
        self.secret_key = cfg['secret_key']

        self.environments = {
          "production": {
            "endpoint": "https://mturk-requester.us-east-1.amazonaws.com",
            "preview": "https://www.mturk.com/mturk/preview"
          },
          "sandbox": {
            "endpoint": 
                  "https://mturk-requester-sandbox.us-east-1.amazonaws.com",
            "preview": "https://workersandbox.mturk.com/mturk/preview"
          },
        }

    def launch_client(self, production = False):
        self.mturk_environment = self.environments["production"] if production else self.environments["sandbox"]
        try:
            session = boto3.Session(profile_name='mturk')
        except:
            session = boto3.Session(
                #profile_name='mturk',
                aws_access_key_id  = self.access_key,
                aws_secret_access_key  = self.secret_key
            )
        self.client = session.client(
            service_name= 'mturk',
            region_name= 'us-east-1',
            endpoint_url= self.mturk_environment['endpoint'],
        )
        print(self.client.get_account_balance()['AvailableBalance'])

    def create_hit(self, html_layout, **TaskAttributes):
        QUESTION_XML = """<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd"><HTMLContent><![CDATA[{}]]></HTMLContent><FrameHeight>650</FrameHeight></HTMLQuestion>"""
        question_xml = QUESTION_XML.format(html_layout)

        response = self.client.create_hit(
        **TaskAttributes,
            Question=question_xml
        )

        return response

    def get_hit_status(self, HITId):
        hit = self.client.get_hit(HITId=HITId)
        hit_status = hit['HIT']['HITStatus']
        return hit_status

    def get_hit_answers(self, HITId, approve=False):

        # Get list and number of Assignments that have been completed
        hit_assignmentsList = self.client.list_assignments_for_hit(
            HITId=HITId,
            AssignmentStatuses=['Submitted','Approved']
        )

        assignments = hit_assignmentsList['Assignments']

        # Get details and results of each Assignment and add to answers array
        answers = []
        for assignment in assignments:
            worker_id = assignment['WorkerId']
            assignment_id = assignment['AssignmentId']

            answer_dict = xmltodict.parse(assignment['Answer'])['QuestionFormAnswers']['Answer']
            values = {}
            for entry in answer_dict:
                try:
                    values[entry['QuestionIdentifier']] = json.loads(entry['FreeText'])
                except ValueError:
                    values[entry['QuestionIdentifier']] = entry['FreeText']
                except TypeError:
                    values[entry['QuestionIdentifier']] = None

            answer = {
                'worker_id' : worker_id,
                'assignment_id' : assignment_id,
                'values' : values,
                'HITId' : HITId
            }
            answers.append(answer)

            if approve:
                # Approve or not assignments
                if assignment['AssignmentStatus'] == 'Submitted':
                    self.client.approve_assignment(
                        AssignmentId = assignment_id,
                        OverrideRejection = False
                    )

        return answers

    """
    Much better for you to run the last cell on the ExperimentRunner notebook

    def delete_hits(self):
        for hit in self.client.list_hits(MaxResults = 100)['HITs']:
            try:
                self.client.update_expiration_for_hit(
                    HITId = hit['HITId'], ExpireAt=datetime(2017, 1, 1)
                )
                self.client.delete_hit(HITId = hit['HITId'])
            except Exception as e:
                print(e, hit['HITId'])
                continue
    """
