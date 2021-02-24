from model.TinyDbDAO import TinyDbDAO

class Search:

    def __init__(self, dbDAO = TinyDbDAO()):
        self.databaseDAO = dbDAO

    def parseSearchInputs(self, searchOptions):

        table = searchOptions['searchOption']
        searchTerm = searchOptions['searchTerm']
        searchValue = searchOptions['searchValue']

        if searchOptions['searchOption'] == "Organizations":
            if searchTerm in ['_id', 'organization_id']:
                searchOptions['searchValue'] = int(searchValue)
        elif searchOptions['searchOption'] == "Users":
            if searchTerm in ['_id', 'organization_id']:
                searchOptions['searchValue'] = int(searchValue)
            elif searchTerm in ['active', 'verified', 'shared', 'suspended']:
                searchOptions['searchValue'] = searchTerm.lower() == 'true'
        elif searchOptions['searchOption'] == "Tickets":
            if searchTerm in ['submitter_id', 'assignee_id', 'organization_id', ]:
                searchOptions['searchValue'] = int(searchValue)

        return searchOptions

    def getSearchResult(self, searchOptions):

        searchOptions = self.parseSearchInputs(searchOptions)

        targetData = self.databaseDAO.search(searchOptions)

        return targetData

    def listSearchFields(self):

        fieldDict = {}

        organizationContents = self.databaseDAO.organizationTable.all()
        fieldDict['organization'] = self.getDeduplicatedListFromContents(organizationContents)

        userContents = self.databaseDAO.userTable.all()
        fieldDict['user'] = self.getDeduplicatedListFromContents(userContents)

        ticketContents = self.databaseDAO.userTable.all()
        fieldDict['ticket'] = self.getDeduplicatedListFromContents(ticketContents)

        return fieldDict

    def getDeduplicatedListFromContents(self, contents):

        fieldList = list()

        for doc in contents:
            for key in doc.keys():
                fieldList.append(key)

        dedupedList = list(dict.fromkeys(fieldList))

        return dedupedList



if __name__ == '__main__':
    search = Search()
    search.loadData()
