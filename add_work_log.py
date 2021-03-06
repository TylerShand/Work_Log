import datetime
import csv
import pandas  # <-- This is why I love Python <3


class AddWorkLog:
    def clear_screen(self):
        print("\033c", end="")

    def get_current_datetime(self):
        now = datetime.datetime.now()
        fmt = '%Y/%m/%d %H:%M:%S'
        now_fmt = now.strftime(fmt)
        return now_fmt

    def get_work_log(self):
        msg = ('Must contain 3 fields:\n'
               '   - title,\n'
               '   - amount of time (in minutes),\n'
               '   - notes\n'
               'Seperate values with a pipe character: |\n'
               '> ')
        work_log = input(msg).split('|')
        return self.check_work_log(work_log)

    def check_work_log(self, work_log):
        title = work_log[0]
        time = work_log[1]
        if len(work_log) != 3:
            self.clear_screen()
            print('Please supply the correct number of field entries.\n'
                  'You entered {}. There should be 3\n'.format(len(work_log)))
            return self.get_work_log()
        # Check if work log title is present
        if title == '' or title.isspace():
            self.clear_screen()
            print('Work log title is a required field\n')
            return self.get_work_log()
        # Check if time value is an int
        try:
            int(time)
        except ValueError:
            # If not, restart get_work_log()
            self.clear_screen()
            print('Time value must be an integer.\n')
            return self.get_work_log()
        return work_log

    def add_work_log(self):
        with open('work_logs.csv', 'a') as csv_file:
            field_names = [
                'title',
                'time',
                'notes',
                'date'
            ]
            work_log_writer = csv.DictWriter(csv_file, delimiter=',',
                                             fieldnames=field_names)
            work_log = self.get_work_log()
            if pandas.read_csv('work_logs.csv').empty:
                work_log_writer.writeheader()
            work_log_writer.writerow({
                'title': work_log[0],
                'time': work_log[1],
                'notes': work_log[2],
                'date': self.get_current_datetime()
            })
