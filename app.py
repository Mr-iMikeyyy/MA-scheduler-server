from cal_creator import MplCalendar
import customtkinter
import matplotlib
from db import DB
from frame import Frame


matplotlib.use('TkAgg')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        self.db = DB()

        self.geometry("800x500")


        
        # cursor = conn.cursor()

        # query = "SELECT id, name FROM mechanics"

        # # cursor.execute(query)
        # # cursor.close()
        # # conn.close()
        # results = self.db.queryDB(query)
        # for (id, name) in results:
        #     print("ID= " + str(id) + ", Name= " + name + "\n")

        self.title('Mark\'s Auto Schedule')
        self.frame = Frame(self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

app= App()
app.mainloop()

# feb = MplCalendar(2017, 1) #year, month
# feb.add_event(1, '1st day of February')
# feb.add_event(5, '         1         2         3         4         5         6')
# feb.add_event(5, '123456789012345678901234567890123456789012345678901234567890')
# feb.add_event(18, 'OSLL Field Maintenance Day')
# feb.add_event(18, 'OSLL Umpire Mechanics Clinic')
# feb.add_event(20, 'Presidents day')
# feb.add_event(25, 'OSLL Opening Day')
# feb.add_event(28, 'T-Ball Angels vs Dirtbags at OSLL')
# feb.show()