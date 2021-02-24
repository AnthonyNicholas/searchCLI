import click
import sys
from pprint import pprint

from model.Search import Search

optionDict = {}
search = Search()

def runMenu():
    print("Welcome to Zendesk Search")
    continueOption = input("Type 'quit' to exit at any time, Press 'Enter' to continue:  ")

    if continueOption.lower() == "quit":
        exitProgram()

    print("Select search options:")
    print("Press 1 to search Zendesk")
    print("Press 2 to view a list of searchable fields")
    print("Type 'quit' to exit")
    mainMenu()

@click.command()
@click.option('--menu_option', prompt='Please enter your search option', default="1", help='menu_option.')
def mainMenu(menu_option):
    if menu_option == "1":
        getSearchOption()
    elif menu_option == "2":
        viewSearchOptions()
    elif menu_option.lower() == "quit":
        exitProgram()
    else:
        print("\nYour selection was invalid. Please try again.\n")
        mainMenu()


@click.command()
@click.option('--search_option', prompt='Select 1) Users or 2) Tickets or 3) Organizations ', default="1", help='search_option.')
def getSearchOption(search_option):
    if search_option == "1":
        print("You selected Users")
        optionDict['searchOption'] = "Users"
        getSearchParameters()
    elif search_option == "2":
        print("You selected Tickets")
        optionDict['searchOption'] = "Tickets"
        getSearchParameters()
    elif search_option == "3":
        print("You selected Organizations")
        optionDict['searchOption'] = "Organizations"
        getSearchParameters()
    elif search_option.lower() == "quit":
        exitProgram()
    else:
        print("\nYour selection was invalid. Please try again.\n")
        mainMenu()

@click.command()
@click.option('--search_term', prompt='Enter search term ', help='searchOption.')
@click.option('--search_value', prompt='Enter search value ', default="", help='searchOption.')
def getSearchParameters(search_term, search_value):

    if (search_term.lower() == "quit" or search_value.lower() == "quit"):
        exitProgram()

    optionDict['searchTerm'] = search_term
    optionDict['searchValue'] = search_value
    try:
        targetData = search.getSearchResult(optionDict)
    except Exception as ex:
        print(ex)
        getSearchParameters()

    displaySearchResult(optionDict, targetData)

def displaySearchResult(searchOptions, targetData):

    print('\n\n ** Search Results for Search of {} with SearchTerm = {} and SearchValue = {} **\n'.format(optionDict['searchOption'], optionDict['searchTerm'], optionDict['searchValue']))

    if searchOptions['searchOption'] == "Organizations":
        for result in targetData:
            print("\nOrganization Result: \n")
            pprint(result['organizations'])
            print("\nAssociated Users: \n")
            pprint(result['users'])
            print("\nAssociated Tickets: \n")
            pprint(result['tickets'])

    elif searchOptions['searchOption'] == "Users":
        for result in targetData:
            print("\nUser Result: \n")
            pprint(result['users'])
            print("\nAssociated Organizations: \n")
            pprint(result['organizations'])
            print("\nAssociated Tickets: \n")
            pprint(result['tickets'])

    elif searchOptions['searchOption'] == "Tickets":
        for result in targetData:
            print("\nTicket Result: \n")
            pprint(result['tickets'])
            print("\nAssoicated Organizations: \n")
            pprint(result['organizations'])
            print("\nAssociated Users: \n")
            pprint(result['users'])

    reRunMainMenu()

def viewSearchOptions():
    fieldDict = search.listSearchFields()

    print("\nSearch Organization with:\n")
    pprint(fieldDict['organization'])

    print("\nSearch User with:\n")
    pprint(fieldDict['user'])

    print("\nSearch Ticket with:\n")
    pprint(fieldDict['ticket'])

    reRunMainMenu()

def reRunMainMenu():

    print("\nWould you like to continue searching?\n")
    continueOption = input("Type 'quit' to exit at any time, Press 'Enter' to continue:  ")

    if continueOption.lower() == "quit":
        exitProgram()

    print("Select search options:")
    print("Press 1 to search Zendesk")
    print("Press 2 to view a list of searchable fields")
    print("Type 'quit' to exit")

    mainMenu()

def exitProgram():
    print("\n** Thankyou for using Zendesk Search **\n")
    sys.exit()
