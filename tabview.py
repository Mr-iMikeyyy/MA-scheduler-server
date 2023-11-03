from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cal_creator import MplCalendar
import customtkinter
from datetime import date

class Tabview(customtkinter.CTkTabview):
    def __init__(self, *args):
        super().__init__(*args)

        # Create Tabs
        self.add("Set Appointment")
        self.add("Calendar")
        self.add("Configure")

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

        ###########

        # Column 0

        ###########
        self.cal = MplCalendar(date.today().year, date.today().month)
        self.f = self.cal.getF()
        self.canvas = FigureCanvasTkAgg(self.f, master=self.tab("Calendar"))
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()