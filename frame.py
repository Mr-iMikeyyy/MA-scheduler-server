import customtkinter
from tabview import Tabview

class Frame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bigJohnTitle = customtkinter.CTkFont(family="Big John", size=24)

        self.title = customtkinter.CTkLabel(master=self, text="Mark's Auto Schedule", font=self.bigJohnTitle)
        self.title.pack(pady=20, padx=10)

        self.tabview = Tabview(self)
        self.tabview.pack(padx=20,pady=10)