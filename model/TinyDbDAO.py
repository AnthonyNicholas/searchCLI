from tinydb import TinyDB, Query, where
import json
import os
from pathlib import Path
from time import sleep

class TinyDbDAO:

    def __init__(self):
        currentDir = os.getcwd()

        if os.path.isfile(currentDir + "/data/tinyDb.json"):
            self.db = TinyDB(currentDir + '/data/tinyDb.json')
            self.userTable = self.db.table('users')
            self.ticketTable = self.db.table('tickets')
            self.organizationTable = self.db.table('organizations')
        else:
            self.db = TinyDB(currentDir + '/data/tinyDb.json')
            self.userTable = self.db.table('users')
            self.ticketTable = self.db.table('tickets')
            self.organizationTable = self.db.table('organizations')
            self.loadData()


    def loadData(self):
        currentDir = os.getcwd()
        with open(currentDir + '/data/users.json') as json_file:
            data = json.load(json_file)
            self.userTable.insert_multiple(data)

        with open(currentDir + '/data/tickets.json') as json_file:
            data = json.load(json_file)
            self.ticketTable.insert_multiple(data)

        with open(currentDir + '/data/organizations.json') as json_file:
            data = json.load(json_file)
            self.organizationTable.insert_multiple(data)

    def search(self, searchParams):
        targetData = [];

        if searchParams['searchOption'] == "Organizations":
            if searchParams['searchTerm'] in ['domain_names', 'tags']:
                targetOrgs = self.organizationTable.search(
                    where(searchParams['searchTerm'])[0] == searchParams['searchValue'])
            else:
                targetOrgs = self.organizationTable.search(
                where(searchParams['searchTerm']) == searchParams['searchValue'])
            for org in targetOrgs:
                result = dict()
                result['organisations'] = org
                result['users'] = self.userTable.search(where('organization_id') == org['_id'])
                result['tickets'] = self.ticketTable.search(where('organization_id') == org['_id'])
                targetData.append(result)

        elif searchParams['searchOption'] == "Users":
            if searchParams['searchTerm'] in ['tags']:
                targetUsers = self.userTable.search(
                    where(searchParams['searchTerm'])[0] == searchParams['searchValue'])
            else:
                targetUsers = self.userTable.search(where(searchParams['searchTerm']) == searchParams['searchValue'])
            for user in targetUsers:
                result = dict()
                result['users'] = user
                result['organisations'] = self.organizationTable.search(where('_id') == user['organization_id'])
                result['tickets'] = self.ticketTable.search(where('submitter_id') == user['_id'])
                targetData.append(result)

        elif searchParams['searchOption'] == "Tickets":
            if searchParams['searchTerm'] in ['tags']:
                targetTickets = self.userTable.search(
                    where(searchParams['searchTerm'])[0] == searchParams['searchValue'])
            else:
                targetTickets = self.ticketTable.search(where(searchParams['searchTerm']) == searchParams['searchValue'])
            for ticket in targetTickets:
                result = dict()
                result['tickets'] = ticket
                result['organisations'] = self.organizationTable.search(where('_id') == ticket['organization_id'])
                result['users'] = self.userTable.search(where('_id') == ticket['submitter_id'])
                targetData.append(result)

        return targetData
