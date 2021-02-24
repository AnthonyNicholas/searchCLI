from tests.testUtils import *
import unittest
from unittest.mock import MagicMock
from model.TinyDbDAO import TinyDbDAO
import os


class TestTinyDbDAO:

    def test_search_users(self):
        searchOptions = createSearchOptions('Users', '_id', '1')
        db = TinyDbDAO()
        db.userTable.search = MagicMock(return_value=[{"hi": "there"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['users'] == {"hi": "there"}

    def test_search_users_with_organization(self):
        searchOptions = createSearchOptions('Users', '_id', '1')
        db = TinyDbDAO()
        db.userTable.search = MagicMock(return_value=[{"hi": "there"}])
        db.organizationTable.search = MagicMock(return_value=[{"name": "abc"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['organizations'] == [{"name": "abc"}]

    def test_search_users_with_tickets(self):
        searchOptions = createSearchOptions('Users', '_id', '1')
        db = TinyDbDAO()
        db.userTable.search = MagicMock(return_value=[{"hi": "there"}])
        db.ticketTable.search = MagicMock(return_value=[{"name": "abc"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['tickets'] == [{"name": "abc"}]

    def test_search_organizations(self):
        searchOptions = createSearchOptions('Organizations', '_id', '1')
        db = TinyDbDAO()
        db.organizationTable.search = MagicMock(return_value=[{"hi": "there"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['organizations'] == {"hi": "there"}

    def test_search_organizations_with_users(self):
        searchOptions = createSearchOptions('Organizations', '_id', '1')
        db = TinyDbDAO()
        db.organizationTable.search = MagicMock(return_value=[{"hi": "there"}])
        db.userTable.search = MagicMock(return_value=[{"name": "abc"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['users'] == [{"name": "abc"}]

    def test_search_organizations_with_tickets(self):
        searchOptions = createSearchOptions('Organizations', '_id', '1')
        db = TinyDbDAO()
        db.organizationTable.search = MagicMock(return_value=[{"hi": "there"}])
        db.ticketTable.search = MagicMock(return_value=[{"name": "abc"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['tickets'] == [{"name": "abc"}]

    def test_search_tickets(self):
        searchOptions = createSearchOptions('Tickets', '_id', '1')
        db = TinyDbDAO()
        db.ticketTable.search = MagicMock(return_value=[{"hi": "there"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['tickets'] == {"hi": "there"}

    def test_search_tickets_with_users(self):
        searchOptions = createSearchOptions('Tickets', '_id', '1')
        db = TinyDbDAO()
        db.ticketTable.search = MagicMock(return_value=[{"hi": "there"}])
        db.userTable.search = MagicMock(return_value=[{"name": "abc"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['users'] == [{"name": "abc"}]

    def test_search_tickets_with_organizations(self):
        searchOptions = createSearchOptions('Tickets', '_id', '1')
        db = TinyDbDAO()
        db.ticketTable.search = MagicMock(return_value=[{"hi": "there"}])
        db.organizationTable.search = MagicMock(return_value=[{"name": "abc"}])
        targetData = db.search(searchOptions)
        assert targetData[0]['organizations'] == [{"name": "abc"}]

    def test_load_data(self):
        searchOptions = createSearchOptions('Organizations', '_id', '101')
        db = TinyDbDAO("/tests/testTinyDb.json")
        db.loadData()
        targetData = db.search(searchOptions)
        assert targetData is not None
        currentDir = os.getcwd()
        os.remove(currentDir + "/tests/testTinyDb.json")


