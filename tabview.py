from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cal_creator import MplCalendar
import customtkinter
from datetime import date

class Tabview(customtkinter.CTkTabview):
    def __init__(self, *args):
        super().__init__(*args)

        # Create Tabs
        self.appTab = self.add("Set Appointment")
        self.calTab = self.add("Calendar")
        self.confTab = self.add("Configure")

        # Set default active tab
        self.set("Set Appointment")

        # Configure Columns of grid
        self.tab("Set Appointment").columnconfigure(0, weight=1)
        self.tab("Set Appointment").columnconfigure(1, weight=3)

        self.nameLabel = customtkinter.CTkLabel(self.appTab, text="Name:").grid(column=0, row=0)
        self.nameEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Name").grid(column=1, row=0)

        self.carLabel = customtkinter.CTkLabel(self.appTab, text="Car:")
        self.carLabel.grid(column=0, row=1)
        self.carEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Car")
        self.carEntry.grid(column=1, row=1)

        self.descLabel = customtkinter.CTkLabel(self.appTab, text="Description:")
        self.descLabel.grid(column=0, row=2)
        self.descEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Description")
        self.descEntry.grid(column=1, row=2)

        #Configure Rows of Grid
        # self.tab("Create Post").rowconfigure(0, weight=2)
        # self.tab("Create Post").rowconfigure(1, weight=2)
        # self.tab("Create Post").rowconfigure(2, weight=2)

        # self.cal = MplCalendar(date.today().year, date.today().month)
        # self.f = self.cal.getF()
        # self.canvas = FigureCanvasTkAgg(self.f, master=calTab)
        # self.canvas.get_tk_widget().pack()
        # self.canvas.draw()