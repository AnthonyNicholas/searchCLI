from model.Search import Search
from tests.TestResources.MockDb import MockDb


# from model.TinyDbInteraction import TinyDbInteraction

#
# There aren’t many things that will mean an automatic “no thanks” but lack of tests or extremely sparse or poorly implemented tests are one of them. Reliable code is made so in part by an intelligently-implemented test suite. If you don’t provide one I have to conclude you write code that isn’t that reliable.
#
# Make sure your test makes it easy to identify where the problem in your code is. A simple way to do this is to make only one assertion per test block.
# Unit test where necessary, e.g. complex methods, code we might find obscure or crucial functions. Just to be sure you know what we mean by unit testing: “a unit [is] the smallest testable part of an application” and should mock out interactions with any adjacent classes.
# Integration tests for our coding exercise are optional, but whether to include them or not will depend on the type of test you are doing. If you’re not sure, put them in anyway. So far we haven’t rejected anyone for putting in too many tests.
# Test everything. TDD, BDD, unit, integration - there are different schools of thought on how to best approach testing and most of them have merit. At the end of the day the important thing is that any breaking changes to your code break your tests and clearly identify where the problem is.


def test_get_search_result():
    searchOptions = {}
    searchOptions['searchOption'] = 'Users'
    searchOptions['searchTerm'] = 'external_id'
    searchOptions['searchValue'] = '74341f74-9c79-49d5-9611-87ef9b6eb75f'

    mockDb = MockDb()
    search = Search(mockDb)
    searchResult = search.getSearchResult(searchOptions)

    assert searchResult == [(0, "fake row", 0.0)]


def test_parse_search_inputs():

    searchOptions = {}
    searchOptions['searchOption'] = 'Users'
    searchOptions['searchTerm'] = '_id'
    searchOptions['searchValue'] = '1'

    search = Search()

    parsedSearchOptions = search.parseSearchInputs(searchOptions)

    assert isinstance(parsedSearchOptions['searchValue'], int)
