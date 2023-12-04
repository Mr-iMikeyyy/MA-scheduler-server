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
        self.tab("Set Appointment").columnconfigure(1, weight=1)
        self.tab("Set Appointment").columnconfigure(2, weight=1)

        self.nameLabel = customtkinter.CTkLabel(self.appTab, text="Name:")
        self.nameLabel.grid(column=0, row=0)
        self.nameEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Name")
        self.nameEntry.grid(column=1, row=0, sticky="EW")

        self.carLabel = customtkinter.CTkLabel(self.appTab, text="Car:")
        self.carLabel.grid(column=0, row=1)
        self.carEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Car")
        self.carEntry.grid(column=1, row=1, sticky="EW")

        self.descLabel = customtkinter.CTkLabel(self.appTab, text="Description:")
        self.descLabel.grid(column=0, row=2)
        self.descEntry = customtkinter.CTkEntry(self.appTab, placeholder_text="Description")
        self.descEntry.grid(column=1, row=2, sticky="EW")

        self.mechLabel = customtkinter.CTkLabel(self.appTab, text="Mechanic:")
        self.mechLabel.grid(column=0, row=3)
        self.mechChoice = customtkinter.CTkComboBox(master=self.appTab, values=["John", "Mike", "Dibbs", "Greg", "Garet"])
        self.mechChoice.grid(column=1,row=3, sticky="EW")

        self.hourLabel = customtkinter.CTkLabel(self.appTab, text="Hours:")
        self.hourLabel.grid(column=0, row=4)
        self.hourChoice = customtkinter.CTkComboBox(master=self.appTab, values=["1", "2", "3", "4", "5", "6", "7", "8"])
        self.hourChoice.grid(column=1, row=4, sticky="EW")
        
        self.daySelect = Calendar(
            master = self.appTab, 
            selectmode = 'day',
            date_pattern = "y-m-d")
        self.daySelect.grid(
                column=2, 
                row=0, 
                rowspan=5)
        
        self.msg = customtkinter.CTkTextbox(master=self.appTab, state="disabled", height= 150)
        self.msg.grid(column=0, columnspan=3, row=5, sticky="ew", pady=10)

        self.submitBtn = customtkinter.CTkButton(self.appTab, command=self.set_apt, text="Set Appt.")
        self.submitBtn.grid(column=0, columnspan=3, row=6)

        ######

        #Calendar Tab

        ######

        self.cal = MplCalendar(date.today().year, date.today().month, self.db)
        self.f = self.cal.getF()
        self.canvas = FigureCanvasTkAgg(self.f, master=self.calTab)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        
    def set_apt(self):
        if (self.validate()):
            query = "INSERT INTO apmts (name, car, description, apt_date, mechanic_id, hours) VALUES (%s,%s,%s,%s,%s,%s)"
            mechanicID = int
            match self.mechChoice.get():
                case "John": mechanicID = 1
                case "Greg": mechanicID = 2
                case "Mike": mechanicID = 3
                case "Dibbs": mechanicID = 4
                case "Garet": mechanicID = 5
                case _: mechanicID = None
            aptDate = self.daySelect.get_date()
            if (len(aptDate) < 10):
                aptDate = aptDate[:8] + "0" + aptDate[8:]
            values = (self.nameEntry.get(), self.carEntry.get(), self.descEntry.get(), aptDate, mechanicID, int(self.hourChoice.get()))
            print(values)
            self.db.insertDB(query,values)

    def validate(self) -> bool:
        status = ""

        if (self.nameEntry.get() == ""):
            status += "Name cannot be blank \n"
        if (self.carEntry.get() == ""):
            status += "Car cannot be blank \n" 
        if (self.descEntry.get() == ""):
            status += "Description cannot be blank \n"
        aptDate = self.daySelect.get_date()
        if (len(aptDate) < 10):
            aptDate = aptDate[:8] + "0" + aptDate[8:]
        if (date.fromisoformat(aptDate) <= date.today()):
            status += "Date chosen cannot be in the past \n"
        if (self.hourChoice.get() == "0"):
            status += "Hours cannot be 0 \n"

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

        
    
    