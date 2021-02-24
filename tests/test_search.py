import pytest
from tests.testUtils import *
import unittest
from unittest.mock import MagicMock
from model.TinyDbDAO import TinyDbDAO

from model.Search import Search

class TestSearch(unittest.TestCase):

    def test_parse_search_inputs_converts_to_int_for_users(self):
        searchOptions = createSearchOptions('Users', '_id', '1')
        search = Search()
        parsedSearchOptions = search.parseSearchInputs(searchOptions)
        assert isinstance(parsedSearchOptions['searchValue'], int)

    def test_parse_search_inputs_converts_to_bool_for_users(self):
        searchOptions = createSearchOptions('Users', 'active', 'true')
        search = Search()
        parsedSearchOptions = search.parseSearchInputs(searchOptions)
        assert isinstance(parsedSearchOptions['searchValue'], bool)

    def test_parse_search_inputs_converts_to_int_for_tickets(self):
        searchOptions = createSearchOptions('Tickets', 'assignee_id', '1')
        search = Search()
        parsedSearchOptions = search.parseSearchInputs(searchOptions)
        assert isinstance(parsedSearchOptions['searchValue'], int)

    def test_parse_search_inputs_converts_to_int_for_organization(self):
        searchOptions = createSearchOptions('Organizations', '_id', '1')
        search = Search()
        parsedSearchOptions = search.parseSearchInputs(searchOptions)
        assert isinstance(parsedSearchOptions['searchValue'], int)

    def test_parse_search_inputs_throws_exception_if_input_cannot_be_cast_to_int(self):
        searchOptions = createSearchOptions('Organizations', '_id', 'abc')
        search = Search()
        with self.assertRaises(Exception):
            search.parseSearchInputs(searchOptions)

    def test_parse_search_inputs_throws_exception_if_input_cannot_be_cast_to_bool(self):
        searchOptions = createSearchOptions('Users', 'active', 'abc')
        search = Search()
        with self.assertRaises(Exception):
            search.parseSearchInputs(searchOptions)

    def test_get_search_result(self):
        searchOptions = createSearchOptions('Users', 'external_id', '74341f74-9c79-49d5-9611-87ef9b6eb75f')
        mockDb = TinyDbDAO()
        mockDb.search = MagicMock(return_value=[(0, "fake row", 0.0)])
        search = Search(mockDb)
        searchResult = search.getSearchResult(searchOptions)

        assert searchResult == [(0, "fake row", 0.0)]

    def test_list_search_fields(self):
        db = TinyDbDAO()
        db.organizationTable.all = MagicMock(return_value=[{"hi": "there"}])
        db.userTable.all = MagicMock(return_value=[{"hi": "there"}])
        db.ticketTable.all = MagicMock(return_value=[{"hi": "there"}])
        search = Search(db)
        fieldDict = search.listSearchFields()

        assert fieldDict["organization"] == ["hi"]

    def test_get_deduplicated_list_from_contents_dedupes(self):
        search = Search()
        contents = [{"hi": "there"}, {"hi": "back"}]
        dedupedList = search.getDeduplicatedListFromContents(contents)
        assert len(dedupedList) == 1

    def test_get_deduplicated_list_from_contents_holds_correct_key(self):
        search = Search()
        contents = [{"hi": "there"}, {"hi": "back"}]
        dedupedList = search.getDeduplicatedListFromContents(contents)
        assert "hi" in dedupedList




