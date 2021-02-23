from tinydb import TinyDB, Query, where
from pprint import pprint
import click
import json
import os

class SearchTinyDb:

    def __init__(self):
        os.remove("../data/tinyDb.json")
        self.db = TinyDB('../data/tinyDb.json')
        self.userTable = self.db.table('Users')
        self.ticketTable = self.db.table('Tickets')
        self.organizationTable = self.db.table('Organizations')
        self.loadData()

    def loadData(self):
        with open('../data/users.json') as json_file:
            data = json.load(json_file)
            self.userTable.insert_multiple(data)

        with open('../data/tickets.json') as json_file:
            data = json.load(json_file)
            self.ticketTable.insert_multiple(data)

        with open('../data/organizations.json') as json_file:
            data = json.load(json_file)
            self.organizationTable.insert_multiple(data)

        # UserQuery = Query()
        # result = self.userTable.search(UserQuery['_id'] == 2)
        # # result = self.db.search(UserQuery['external_id'] == '74341f74-9c79-49d5-9611-87ef9b6eb75f')
        # pprint(result)

    def getResult(self, searchOptions):

        print(searchOptions)
        if searchOptions['searchOption'] == "Organizations":
            targetData = self.organizationTable.search(where(searchOptions['searchTerm']) == searchOptions['searchValue'])
        elif searchOptions['searchOption'] == "Users":
            targetData = self.userTable.search(where(searchOptions['searchTerm']) == searchOptions['searchValue'])
        elif searchOptions['searchOption'] == "Tickets":
            targetData = self.ticketTable.search(where(searchOptions['searchTerm']) == searchOptions['searchValue'])

        return targetData


if __name__ == '__main__':
    search = Search()
    search.loadData()
