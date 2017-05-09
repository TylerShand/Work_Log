from add_work_log import AddWorkLog
from search_work_log import SearchWorkLog
from time import sleep


add = AddWorkLog()
search = SearchWorkLog()


def clear_screen():
    print("\033c", end="")


def display_menu():
    print('-----------------------------------------------------------------')
    print('Work Log')
    print()
    print('Would you like to [s]earch a work log, [a]dd a new\n'
          'entry, or [q]uit? ')
    print('-----------------------------------------------------------------')
    return input('> ').lower()[0]


# Run the program
if __name__ == '__main__':
    while True:
        clear_screen()
        menu = display_menu()
        # Exit Script
        if menu == 'q':
            print('Exiting...')
            break
        # Search
        elif menu == 's':
            while True:
                clear_screen()
                search_input = search.get_search()
                search.search_work_logs(search_input)
                if input('Search for another work log (Y/n)? ')\
                        .lower()[0] != 'y':
                    break
        # Add Work Log
        elif menu == 'a':
            while True:
                clear_screen()
                add.add_work_log()
                if input('Add another work log (Y/n)? ').lower()[0] != 'y':
                    break
        else:
            print('Incorrect input')
            sleep(1)
