import re
import csv


class SearchWorkLog:
    def get_search(self):
        msg = ('You can either search by:\n'
               '[t]itle,\n'
               '[d]ate,\n'
               '[e]xact search,\n'
               '[p]attern\n'
               '> ')
        search = input(msg).lower()[0]
        if search == 't':
            return 'title'
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
            count = 0
            if search == 'title' or search == 'date':
                for row in rows:
                    print('{}. {}'.format(count + 1, row[search]))
                    count += 1
                search_item = input('Which number work log would you '
                                    'like to view?\n'
                                    '> ')
                # check if search_item is an int
                try:
                    search_item = int(search_item)
                except ValueError:
                    print('ERROR: Please enter a number.')
                    return self.search_work_logs(search)
                # Check if the number entered is within the range of the list
                # of work logs
                if search_item <= 0:
                    print('ERROR: The number entered was out of range')
                    return self.search_work_logs(search)
                try:
                    # Print all of these on the same line
                    title = 'Title: ' + rows[search_item - 1]['title']
                    time_spent = 'Time Spent: '\
                                 + rows[search_item - 1]['time'] + ' minutes'
                    notes = 'Notes: ' + rows[search_item - 1]['notes']
                    date = 'Date: ' + rows[search_item - 1]['date']
                    print(title + ' | ' + time_spent + ' | ' + notes + ' | ' +
                          date)
                except IndexError:
                    print('ERROR: The number entered was out of range')
                    return self.search_work_logs(search)
            elif search == 'exact search':
                exact_search = input('What string do you wan to search for?\n'
                                     '> ').lower()
                for i in range(len(rows)):
                    row = ('Title: ' + rows[i]['title'] + ' | ' +
                           'Time spent: ' + rows[i]['time'] + ' minutes' +
                           ' | ' + 'Notes: ' + rows[i]['notes'])
                    if exact_search in row:
                        print('{}. {}'.format(count + 1, row) + ' | ' +
                              'Date: ' + rows[i]['date'])
                        count += 1
            elif search == 'pattern':
                pattern = input('What pattern fo you want to search for?\n'
                                '> ').lower()
                for i in range(len(rows)):
                    row = ('Title: ' + rows[i]['title'] + ' | ' +
                           'Time spent: ' + rows[i]['time'] + ' minutes' +
                           ' | ' + 'Notes: ' + rows[i]['notes'])
                    if re.search(pattern, row) is not None:
                        print('{}. {}'.format(count + 1, row) + ' | ' +
                              'Date: ' + rows[i]['date'])
                        count += 1
