from pymongo import MongoClient
from pprint import pprint
import click

class Search:

    def __init__(self):
        self.mongoConnectionString = "mongodb://localhost:27017"

    def getResult(self, searchOptions):

        print(searchOptions)

        client = MongoClient(self.mongoConnectionString)
        db=client.test

        if searchOptions['searchOption'] == "Organizations":
            targetData = db.organizations.find_one({searchOptions['searchTerm']: searchOptions['searchValue']})
        elif searchOptions['searchOption'] == "Users":
            targetData = db.users.find_one({searchOptions['searchTerm']: searchOptions['searchValue']})
        elif searchOptions['searchOption'] == "Tickets":
            targetData = db.tickets.find_one({searchOptions['searchTerm']: searchOptions['searchValue']})

        return targetData


