

class AlarmClock:
    def __init__(self):
        self.current_time = '00:00'
        self.is_clock_on = False

    def clock_power(self):
        self.is_clock_on = True
        print('your clock is now on lets set the time')

    def change_time(self):
        self.current_time = input('please enter the time')
        print(f'the current time is now {self.current_time}')

    


