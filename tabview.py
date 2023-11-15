from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cal_creator import MplCalendar
import customtkinter
from datetime import date ,datetime
from tkcalendar import Calendar
from db import DB

class Tabview(customtkinter.CTkTabview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.db = DB()
        

        # Create Tabs
        self.appTab = self.add("Set Appointment")
        self.calTab = self.add("Calendar")
        self.confTab = self.add("Configure")

        # Set default active tab
        self.set("Set Appointment")

        # Configure Columns of grid
        self.tab("Set Appointment").columnconfigure(0, weight=1)
        self.tab("Set Appointment").columnconfigure(1, weight=3)

        self.nameLabel = customtkinter.CTkLabel(self.appTab, text="Name:")
        self.nameLabel.grid(column=0, row=0)
        self.nameEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Name")
        self.nameEntry.grid(column=1, row=0)

        self.carLabel = customtkinter.CTkLabel(self.appTab, text="Car:")
        self.carLabel.grid(column=0, row=1)
        self.carEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Car")
        self.carEntry.grid(column=1, row=1)

        self.descLabel = customtkinter.CTkLabel(self.appTab, text="Description:")
        self.descLabel.grid(column=0, row=2)
        self.descEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Description")
        self.descEntry.grid(column=1, row=2)

        self.mechLabel = customtkinter.CTkLabel(self.appTab, text="Mechanic:")
        self.mechLabel.grid(column=0, row=3)
        self.mechChoice = customtkinter.CTkComboBox(master=self.appTab, values=["John", "Mike", "Dibbs", "Greg"])
        self.mechChoice.grid(column=1,row=3)
        
        today = date.today()
        self.daySelect = Calendar(
            master = self.appTab, 
            selectmode = 'day',
            date_pattern = "y-m-d")
            # year = today.year, 
            # month = today.month, 
            # day = today.day)
        self.daySelect.grid(
                column=0, 
                row=4, 
                columnspan=2)
        
        self.msg = customtkinter.CTkTextbox(master=self.appTab, state="disabled")
        self.msg.grid(column=0, columnspan=2, row=6)

        self.submitBtn = customtkinter.CTkButton(self.appTab, command=self.set_apt)
        self.submitBtn.grid(column=0, columnspan=2, row=7)
        
    def set_apt(self):
        if (self.validate()):
            query = "INSERT INTO apmts (name, car, description, apt_date, mechanic_id) VALUES (%s,%s,%s,%s,%s)"
            values = (self.nameEntry.get(), self.carEntry.get(), self.descEntry.get(), self.daySelect.get_date(), self.mechChoice.get())
            result = self.db.queryDB(query,values)
            print(result)

    def validate(self) -> bool:
        status = ""

        if (self.nameEntry.get() == ""):
            status += "Name cannot be blank \n"
        if (self.carEntry.get() == ""):
            status += "Car cannot be blank \n" 
        if (self.descEntry.get() == ""):
            status += "Description cannot be blank \n"
        if (date.fromisoformat(self.daySelect.get_date()) <= date.today()):
            status += "Date chosen cannot be in the past \n"

        if (status == ""):
            return True
        else:
            self.msg.configure(state="normal")
            self.msg.delete("0.0", "end")
            self.msg.insert("0.0", status)
            self.msg.configure(state="disabled")
            return False

        

        
        

        #Configure Rows of Grid
        # self.tab("Create Post").rowconfigure(0, weight=2)
        # self.tab("Create Post").rowconfigure(1, weight=2)
        # self.tab("Create Post").rowconfigure(2, weight=2)

        # self.cal = MplCalendar(date.today().year, date.today().month)
        # self.f = self.cal.getF()
        # self.canvas = FigureCanvasTkAgg(self.f, master=calTab)
        # self.canvas.get_tk_widget().pack()
        # self.canvas.draw()
    
    