import re
import csv


class SearchWorkLog:
    def get_search(self):
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
            return self.get_search()

    def search_work_logs(self, search):
        with open('work_logs.csv', newline='') as csv_file:
            work_log_reader = csv.DictReader(csv_file, delimiter=',')
            rows = list(work_log_reader)
            i = 0  # counting variable
            if search == 'name' or search == 'date':
                for row in rows:
                    print('{}. {}'.format(i + 1, row[search]))
                    i += 1
                search_item = input('Which number work log would you '
                                    'like to view?\n'
                                    '> ')
                # check if search_item is an int
                try:
                    search_item = int(search_item)
                except ValueError:
                    print('ERROR: Please enter a number.')
                    return self.search_work_logs(search)
                # Fixes glitch where the script crashes after correctly
                # displaying the row
                try:
                    print(rows[search_item - 1]['name'], end=', ')
                    print(rows[search_item - 1]['time'], end=', ')
                    print(rows[search_item - 1]['notes'], end=', ')
                    print(rows[search_item - 1]['date'])
                except IndexError:
                    print('ERROR: The number entered was out of range')
                    return self.search_work_logs(search)
            elif search == 'exact search':
                exact_search = input('What string do you wan to search for?\n'
                                     '> ').lower()
                for i in range(len(rows)):
                    row = (rows[i]['name'] + ', ' + rows[i]['time'] + ', '
                           + rows[i]['notes'])
                    if exact_search in row:
                        print('{}. {}'.format(i + 1, row) + ', '
                              + rows[i]['date'])
                        i += 1
            elif search == 'pattern':
                pattern = input('What pattern fo you want to search for?\n'
                                '> ').lower()
                for i in range(len(rows)):
                    row = (rows[i]['name'] + ', ' + rows[i]['time'] + ', '
                           + rows[i]['notes'])
                    if re.search(pattern, row) != None:
                        print(str(i + 1) + '. ' + row + ', ' + rows[i]['date'])
