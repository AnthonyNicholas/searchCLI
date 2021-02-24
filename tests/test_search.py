import pytest
from tests.testUtils import *
import unittest
from unittest.mock import MagicMock
from model.TinyDbDAO import TinyDbDAO

from model.Search import Search


# from model.TinyDbInteraction import TinyDbInteraction

#
# There aren’t many things that will mean an automatic “no thanks” but lack of tests or extremely sparse or poorly implemented tests are one of them. Reliable code is made so in part by an intelligently-implemented test suite. If you don’t provide one I have to conclude you write code that isn’t that reliable.
#
# Make sure your test makes it easy to identify where the problem in your code is. A simple way to do this is to make only one assertion per test block.
# Unit test where necessary, e.g. complex methods, code we might find obscure or crucial functions. Just to be sure you know what we mean by unit testing: “a unit [is] the smallest testable part of an application” and should mock out interactions with any adjacent classes.
# Integration tests for our coding exercise are optional, but whether to include them or not will depend on the type of test you are doing. If you’re not sure, put them in anyway. So far we haven’t rejected anyone for putting in too many tests.
# Test everything. TDD, BDD, unit, integration - there are different schools of thought on how to best approach testing and most of them have merit. At the end of the day the important thing is that any breaking changes to your code break your tests and clearly identify where the problem is.

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




