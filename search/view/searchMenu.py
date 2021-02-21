from search.model.Search import *

optionDict = {}

def runMenu():
    print("Hello to Zendesk Search")
    print("Type 'quit' to exit at any time, Press 'Enter' to continue")
    # if click.confirm('Do you want to continue?'):
    print("Select search options:")
    print("Press 1 to search Zendesk")
    print("Press 2 to view a list of searchable fields")
    print("Type 'quit' to exit")
    mainMenu()

    # else:
    #     click.echo('\nThankyou for using Zendesk Search!')
    #     sys.exit()

@click.command()
@click.option('--menu_option', prompt='Please enter your search option', default=1, help='menu_option.')
def mainMenu(menu_option):
    if menu_option == 1:
        getSearchOption()
    elif menu_option == 2:
        print("You selected View")
    else:
        print("Your selection was invalid.")

@click.command()
@click.option('--search_option', prompt='Select 1) Users or 2) Tickets or 3) Organizations ', default=1, help='search_option.')
def getSearchOption(search_option):
    if search_option == 1:
        print("You selected Users")
        optionDict['searchOption'] = "Users"
        getSearchParameters()

    elif search_option == 2:
        print("You selected Tickets")
        optionDict['searchOption'] = "Tickets"
        getSearchParameters()

    elif search_option == 3:
        print("You selected Organizations")
        optionDict['searchOption'] = "Organizations"
        getSearchParameters()

    else:
        print("Your selection was invalid.")

@click.command()
@click.option('--search_term', prompt='Enter search term ', help='searchOption.')
@click.option('--search_value', prompt='Enter search value ',  help='searchOption.')
def getSearchParameters(search_term, search_value):
    optionDict['searchTerm'] = search_term
    optionDict['searchValue'] = search_value

    searcher = Search()

    targetData = searcher.getResult(optionDict)
    pprint(targetData)
