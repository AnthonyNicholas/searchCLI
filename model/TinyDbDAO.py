from tinydb import TinyDB, Query, where
import json
import os
import sys


class TinyDbDAO:
    def __init__(self, dbPath="/data/tinyDb.json"):
        currentDir = os.getcwd()

        if os.path.isfile(currentDir + dbPath):
            self.db = TinyDB(currentDir + dbPath)
            self.userTable = self.db.table("users")
            self.ticketTable = self.db.table("tickets")
            self.organizationTable = self.db.table("organizations")
        else:
            self.db = TinyDB(currentDir + dbPath)
            self.userTable = self.db.table("users")
            self.ticketTable = self.db.table("tickets")
            self.organizationTable = self.db.table("organizations")
            try:
                self.loadData()
            except:
                print(
                    "Sorry, unable to load data for search application.  Please ensure tickets, users and organizations files are present and valid."
                )
                print("\n** Thankyou for using Zendesk Search **\n")
                sys.exit()

    def loadData(self):
        currentDir = os.getcwd()
        with open(currentDir + "/data/users.json") as json_file:
            data = json.load(json_file)
            self.userTable.insert_multiple(data)

        with open(currentDir + "/data/tickets.json") as json_file:
            data = json.load(json_file)
            self.ticketTable.insert_multiple(data)

        with open(currentDir + "/data/organizations.json") as json_file:
            data = json.load(json_file)
            self.organizationTable.insert_multiple(data)

    def search(self, searchOptions):
        targetData = []

        if searchOptions["searchOption"] == "Organizations":
            if searchOptions["searchTerm"] in ["domain_names", "tags"]:
                targetOrgs = self.organizationTable.search(
                    where(searchOptions["searchTerm"]).any(searchOptions["searchValue"])
                )
            else:
                targetOrgs = self.organizationTable.search(
                    where(searchOptions["searchTerm"]) == searchOptions["searchValue"]
                )
            for org in targetOrgs:
                result = dict()
                result["organizations"] = org
                result["users"] = self.userTable.search(
                    where("organization_id") == org.get("_id")
                )
                result["tickets"] = self.ticketTable.search(
                    where("organization_id") == org.get("_id")
                )
                targetData.append(result)

        elif searchOptions["searchOption"] == "Users":
            if searchOptions["searchTerm"] in ["tags"]:
                targetUsers = self.userTable.search(
                    where(searchOptions["searchTerm"]).any(searchOptions["searchValue"])
                )
            else:
                targetUsers = self.userTable.search(
                    where(searchOptions["searchTerm"]) == searchOptions["searchValue"]
                )
            for user in targetUsers:
                result = dict()
                result["users"] = user
                result["organizations"] = self.organizationTable.search(
                    where("_id") == user.get("organization_id")
                )
                result["tickets"] = self.ticketTable.search(
                    where("submitter_id") == user.get("_id")
                )
                targetData.append(result)

        elif searchOptions["searchOption"] == "Tickets":
            if searchOptions["searchTerm"] in ["tags"]:
                targetTickets = self.ticketTable.search(
                    where(searchOptions["searchTerm"]).any(searchOptions["searchValue"])
                )
            else:
                targetTickets = self.ticketTable.search(
                    where(searchOptions["searchTerm"]) == searchOptions["searchValue"]
                )
            for ticket in targetTickets:
                result = dict()
                result["tickets"] = ticket
                result["organizations"] = self.organizationTable.search(
                    where("_id") == ticket.get("organization_id")
                )
                result["users"] = self.userTable.search(
                    where("_id") == ticket.get("submitter_id")
                )
                targetData.append(result)

        return targetData
