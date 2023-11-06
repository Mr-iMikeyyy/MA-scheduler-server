from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cal_creator import MplCalendar
import customtkinter
from datetime import date

class Tabview(customtkinter.CTkTabview):
    def __init__(self, *args):
        super().__init__(*args)

        # Create Tabs
        appTab = self.add("Set Appointment")
        calTab = self.add("Calendar")
        confTab = self.add("Configure")

        # Set default active tab
        self.set("Set Appointment")

        # Configure Columns of grid
        # self.tab("Create Post").columnconfigure(0, weight=2)
        # self.tab("Create Post").columnconfigure(1, weight=2)
        # self.tab("Create Post").columnconfigure(2, weight=2)

        #Configure Rows of Grid
        # self.tab("Create Post").rowconfigure(0, weight=2)
        # self.tab("Create Post").rowconfigure(1, weight=2)
        # self.tab("Create Post").rowconfigure(2, weight=2)

        self.cal = MplCalendar(date.today().year, date.today().month)
        self.f = self.cal.getF()
        self.canvas = FigureCanvasTkAgg(self.f, master=calTab)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()