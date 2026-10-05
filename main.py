# main.py

import customtkinter as ctk

from theme import BACKGROUND
from screens import show_splash


ctk.set_appearance_mode("dark")


class BirthdayApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(
            "Para mi Peanut 💙"
        )

        self.geometry(
            "900x600"
        )

        self.resizable(
            False,
            False
        )

        self.configure(
            fg_color=BACKGROUND
        )

        # Variables used for temporary messages
        self.feedback_label = None
        self.feedback_after_id = None

        # Start the game
        show_splash(self)

    def clear_screen(self):

        for widget in self.winfo_children():

            widget.destroy()


# ------------------------------------
# RUN APP
# ------------------------------------

if __name__ == "__main__":

    app = BirthdayApp()

    app.mainloop()