from pymongo import MongoClient
from pprint import pprint
import click

class search:

    def __init__(self):

    def getOrganization(self, id):

        mongoConnectionString = "mongodb://localhost:27017"

        # client = MongoClient(mongoConnectionString)
        # db=client.admin
        # # Issue the serverStatus command and print the results
        # serverStatusResult=db.command("serverStatus")
        # pprint(serverStatusResult)

        client = MongoClient(mongoConnectionString)
        db=client.test
        targetOrg = db.organizations.find_one({'_id': id})
        pprint(targetOrg)


