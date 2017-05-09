import re
import datetime
import csv
from time import sleep


def clear_screen():
    print("\033c", end="")


def get_current_datetime():
    now = datetime.datetime.now()
    fmt = '%Y/%m/%d %H:%M:%S'
    now_fmt = now.strftime(fmt)
    return now_fmt


def display_menu():
    print('-----------------------------------------------------------------')
    print('Work Log')
    print()
    print('Would you like to [s]earch a work log, [a]dd a new\n'
          'entry, or [q]uit? ')
    print('-----------------------------------------------------------------')
    return input('> ').lower()[0]


####################
# ADDING WORK LOGS #
####################

def get_work_log():
    msg = ('Must contain 3 fields: name, amount of time (in minutes),\n'
           'and notes.\n'
           'Separate values with a SPACE and a COMMA.\n'
           '> ')
    work_log = input(msg).split(', ')
    return check_work_log(work_log)


def check_work_log(work_log):
    if len(work_log) != 3:
        print('Please supply the correct number of field entries.\n'
              'You entered {}. There should be 3\n'.format(len(work_log)))
        return get_work_log()
    try:
        int(work_log[1])
    except ValueError:
        print('Time value must be an integer.\n')
        return get_work_log()
    return work_log


def add_work_log():
    with open('work_logs.csv', 'a') as csv_file:
        field_names = [
            'name',
            'time',
            'notes',
            'date'
        ]
        work_log_writer = csv.DictWriter(csv_file, delimiter=',',
                                         fieldnames=field_names)
        work_log = get_work_log()
        work_log_writer.writeheader()
        try:
            work_log_writer.writerow({
                'name': work_log[0],
                'time': work_log[1],
                'notes': work_log[2],
                'date': get_current_datetime()
            })
        except IndexError:
            print()


#######################
# SEARCHING WORK LOGS #
#######################

def get_search():
    msg = ('You can either search by [n]ame, [d]ate, [e]xact search,\n'
           'or by [p]attern\n'
           '> ')
    search = input(msg).lower()[0]
    if search == 'n':
        return 'name'
    elif search == 'd':
        return 'date'
    elif search == 'e':
        return 'exact search'
    elif search == 'p':
        return 'pattern'
    else:
        print('ERROR: Please enter your search parameter again.')
        return get_search()


def display_search_list(search):
    with open('work_logs.csv', newline='') as csv_file:
        work_log_reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(work_log_reader)
        i = 0
        if search == 'name' or search == 'date':
            for row in rows:
                print('{}. {}'.format(i + 1, row[search]))
                i += 1
            search_item = input('Which number work log would you like to view?\n'
                                '> ')
            try:
                search_item = int(search_item)
            except ValueError:
                print('ERROR: Please enter a number.')
                display_search_list(search)
            try:
                print(rows[search_item - 1]['name'], end=', ')
                print(rows[search_item - 1]['time'], end=', ')
                print(rows[search_item - 1]['notes'], end=', ')
                print(rows[search_item - 1]['date'])
            except TypeError:
                pass
        elif search == 'exact search':
            exact_search = input('What string do you wan to search for?\n> ')\
                                 .lower()
            for i in range(len(rows)):
                row = (rows[i]['name'] + ', ' + rows[i]['time'] + ', '
                      + rows[i]['notes'])
                if exact_search in row:
                    print('{}. {}'.format(i + 1, row) + ', ' + rows[i]['date'])
                    i += 1
        elif search == 'pattern':
            pattern = input('What pattern fo you want to search for?\n> ')\
                            .lower()
            for i in range(len(rows)):
                row = (rows[i]['name'] + ', ' + rows[i]['time'] + ', '
                      + rows[i]['notes'])
                if re.search(pattern, row) != None:
                    print(str(i + 1) + '. ' + row + ', ' + rows[i]['date'])
                    i += 1


# Run the program
if __name__ == '__main__':
    while True:
        clear_screen()
        menu = display_menu()

        # Exit
        if menu.lower()[0] == 'q':
            print('Exiting...')
            break

        # Search
        elif menu == 's':
            while True:
                clear_screen()
                search = get_search()
                display_search_list(search)
                if input('Search for another work log (Y/n)? ')\
                        .lower()[0] != 'y':
                    break

        # Add Work Log
        elif menu == 'a':
            while True:
                clear_screen()
                add_work_log()
                if input('Add another work log (Y/n)? ').lower()[0] != 'y':
                    break

        else:
            input('Incorrect input')
            sleep(1)
