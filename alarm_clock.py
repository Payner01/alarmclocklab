

class AlarmClock:
    def __init__(self):
        self.current_time = '00:00'
        self.is_clock_on = False
        self.alarm_set = None

    def clock_power(self):
        self.is_clock_on = True
        print('your clock is now on lets set the time')

    def change_time(self):
        self.current_time = input('please enter the time')
        print(f'the current time is now {self.current_time}')

    def set_alarm(self):
        self.alarm_set = input('please set an alarm')
        print(f'the alarm you set is for {self.alarm_set}')




