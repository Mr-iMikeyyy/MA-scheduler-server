from cal_creator import MplCalendar
import tkinter
import matplotlib

matplotlib.use('TkAgg')

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mark\'s Auto Schedule')

feb = MplCalendar(2017, 1) #year, month
feb.add_event(1, '1st day of February')
feb.add_event(5, '         1         2         3         4         5         6')
feb.add_event(5, '123456789012345678901234567890123456789012345678901234567890')
feb.add_event(18, 'OSLL Field Maintenance Day')
feb.add_event(18, 'OSLL Umpire Mechanics Clinic')
feb.add_event(20, 'Presidents day')
feb.add_event(25, 'OSLL Opening Day')
feb.add_event(28, 'T-Ball Angels vs Dirtbags at OSLL')
feb.show()