import click
import sys


@click.command()
@click.option('--option', prompt='Please enter your search option', default=1, help='searchOption.')
def search(option):
    if option is 1:
        print("You selected Search")
    elif option is 2:
        print("You selected View")
    else:
        print("Your selection was invalid.")

if __name__ == '__main__':
    print("Hello to Zendesk Search")
    print("Type 'quit' to exit at any time, Press 'Enter' to continue")
    # if click.confirm('Do you want to continue?'):
    #     print("Select search options:")
    #     print("Press 1 to search Zendesk")
    #     print("Press 2 to view a list of searchable fields")
    #     print("Type 'quit' to exit")

    search()

    # else:
    #     click.echo('\nThankyou for using Zendesk Search!')
    #     sys.exit()
