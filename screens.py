# screens.py

import customtkinter as ctk
import os
import sys
from theme import (
    BACKGROUND,
    BLUE,
    LIGHT_BLUE,
    GREEN,
    MINT,
    TEXT,
    ERROR,
    WHITE
)

from animations import fade_labels
from PIL import Image


def resource_path(relative_path):
    """
    Works both while developing and inside the final .exe
    """

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# ===================================================
# SPLASH SCREEN
# ===================================================

def show_splash(app):

    app.clear_screen()

    peanut = ctk.CTkLabel(
        app,
        text="Para mi Peanut",
        font=("Arial", 46, "bold"),
        text_color=MINT
    )

    peanut.pack(
        pady=(120, 15)
    )

    loading = ctk.CTkLabel(
        app,
        text="Tengo una cosita para ti...",
        font=("Arial", 20),
        text_color=TEXT
    )

    loading.pack(
        pady=10
    )
    image_path = resource_path(
        "assets/intro.png"
    )

    intro_image = ctk.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(320, 380)
    )

    intro_photo = ctk.CTkLabel(
        app,
        text="",
        image=intro_image
    )

    intro_photo.pack(
        pady=5
    )
    app.intro_image = intro_image
    app.after(
        4500,
        lambda: show_intro(app)
    )
# ===================================================
# INTRO SCREEN
# ===================================================

def show_intro(app):

    app.clear_screen()

    title = ctk.CTkLabel(
        app,
        text="¡Feliz cumpleaños mi amorcito guapo!",
        font=("Arial", 42, "bold"),
        text_color=MINT
    )

    title.pack(
        pady=(60, 20)
    )
    subtitle = ctk.CTkLabel(
        app,
        text="Como es tu cumpleaños, te mereces algo especial...",
        font=("Arial", 22),
        text_color=TEXT
    )

    subtitle.pack(
        pady=10
    )
    image_path = resource_path(
        "assets/us.jpg"
    )

    couple_image = ctk.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(300, 400)
    )

    couple_photo = ctk.CTkLabel(
        app,
        text="",
        image=couple_image
    )

    couple_photo.pack(
        pady=10
    )

    app.couple_image = couple_image
    app.after(
        5550,
        lambda: show_pre_clues(app)
    )

# ===================================================
# PRE-CLUES SCREEN
# ===================================================

def show_pre_clues(app):

    app.clear_screen()

    title = ctk.CTkLabel(
        app,
        text="¿Listo?",
        font=("Arial", 38, "bold"),
        text_color=MINT
    )

    title.pack(
        pady=(150, 20)
    )

    subtitle = ctk.CTkLabel(
        app,
        text=(
            "Tu regalo no cabe dentro de una caja... \n Tienes que seguir unas pistas🕵️‍♂️"
        ),
        font=("Arial", 22),
        text_color=TEXT
    )

    subtitle.pack(
        pady=(40, 20)
    )

    start_button = ctk.CTkButton(
        app,
        text="VER REGALO ✨",
        font=("Arial", 18, "bold"),
        width=240,
        height=50,
        fg_color=BLUE,
        hover_color=GREEN,
        text_color=WHITE,
        corner_radius=25,
        command=lambda: show_first_clue(app)
    )

    start_button.pack(
        pady=30
    )


# ===================================================
# CLUE 1
# ===================================================

def show_first_clue(app):

    app.clear_screen()

    clue = ctk.CTkLabel(
        app,
        text="PISTA #1",
        font=("Arial", 34, "bold"),
        text_color=MINT
    )

    clue.pack(
        pady=(170, 15)
    )

    question = ctk.CTkLabel(
        app,
        text="Vas a necesitar uno de estos... además de tu maleta",
        font=("Arial", 22, "bold"),
        text_color=LIGHT_BLUE
    )

    question.pack(
        pady=(20, 25)
    )

    button_frame = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    button_frame.pack(
        pady=10
    )

    # --------------------
    # Hiking boots
    # --------------------

    hiking_button = ctk.CTkButton(
        button_frame,
        text="🥾 Botas de hiking",
        font=("Arial", 17),
        width=190,
        height=50,
        corner_radius=20,
        fg_color=BLUE,
        hover_color=GREEN,
        command=lambda: check_answer(app, True, show_PRE_second_clue)
    )

    hiking_button.grid(
        row=0,
        column=0,
        padx=10
    )

    # --------------------
    # Goggles
    # --------------------

    swimming_button = ctk.CTkButton(
        button_frame,
        text="🥽 Goggles",
        font=("Arial", 17),
        width=190,
        height=50,
        corner_radius=20,
        fg_color=BLUE,
        hover_color=GREEN,
        command=lambda: check_answer(app, False, show_PRE_second_clue)
    )

    swimming_button.grid(
        row=0,
        column=1,
        padx=10
    )

    # --------------------
    # Tuxedo
    # --------------------

    tuxedo_button = ctk.CTkButton(
        button_frame,
        text="👨🏽‍💼 Tuxedo",
        font=("Arial", 17),
        width=190,
        height=50,
        corner_radius=20,
        fg_color=BLUE,
        hover_color=GREEN,
        command=lambda: check_answer(app, False, show_PRE_second_clue)
    )

    tuxedo_button.grid(
        row=0,
        column=2,
        padx=10
    )


# ===================================================
# CHECK ANSWER
# ===================================================
def check_answer(app, correct, next_screen):

    if correct:

        # Cancel error timer if there is one
        if hasattr(app, "feedback_after_id"):

            if app.feedback_after_id is not None:

                try:
                    app.after_cancel(
                        app.feedback_after_id
                    )

                except Exception:
                    pass

                app.feedback_after_id = None

        show_correct_screen(
            app,
            next_screen
        )

    else:

        # Remove previous error
        if hasattr(app, "feedback_label"):

            if app.feedback_label is not None:

                if app.feedback_label.winfo_exists():

                    app.feedback_label.destroy()

        # Cancel previous timer
        if hasattr(app, "feedback_after_id"):

            if app.feedback_after_id is not None:

                try:
                    app.after_cancel(
                        app.feedback_after_id
                    )

                except Exception:
                    pass

        app.feedback_label = ctk.CTkLabel(
            app,
            text="Mmm... nop 😏\nIntenta otra vez",
            font=("Arial", 20, "bold"),
            text_color=ERROR
        )

        app.feedback_label.pack(
            pady=25
        )

        app.feedback_after_id = app.after(
            5000,
            lambda: remove_feedback(app)
        )

# ===================================================
# REMOVE WRONG ANSWER MESSAGE
# ===================================================

def remove_feedback(app):

    if hasattr(app, "feedback_label"):

        if app.feedback_label is not None:

            if app.feedback_label.winfo_exists():

                app.feedback_label.destroy()

    app.feedback_label = None
    app.feedback_after_id = None


# ===================================================
# CORRECT ANSWER TRANSITION
# ===================================================

def show_correct_screen(app, next_screen):

    app.clear_screen()

    correct_text = ctk.CTkLabel(
        app,
        text="Correcto 💚",
        font=("Arial", 42, "bold"),
        text_color=BACKGROUND
    )

    correct_text.pack(
        pady=(200, 20)
    )

    message = ctk.CTkLabel(
        app,
        text="SIII MI AMOR",
        font=("Arial", 24),
        text_color=BACKGROUND
    )

    message.pack(
        pady=10
    )

    def wait_before_fade_out():

        app.after(
            1500,
            fade_out
        )

    def fade_out():

        fade_labels(
            app=app,

            labels=[
                correct_text,
                message
            ],

            start_colors=[
                MINT,
                TEXT
            ],

            end_colors=[
                BACKGROUND,
                BACKGROUND
            ],

            steps=20,
            speed=40,

            on_complete=lambda: next_screen(app)
        )

    fade_labels(
        app=app,

        labels=[
            correct_text,
            message
        ],

        start_colors=[
            BACKGROUND,
            BACKGROUND
        ],

        end_colors=[
            MINT,
            TEXT
        ],

        steps=20,
        speed=40,

        on_complete=wait_before_fade_out
    )
# ===================================================
# pre CLUE 2
# ===================================================

def show_PRE_second_clue(app):

    app.clear_screen()

    clue_text = ctk.CTkLabel(
        app,
        text="...👀 pero en Países Bajos no hay montañas para hacer hike...",
        font=("Arial", 24),
        text_color=TEXT
    )

    clue_text.pack(
        pady=(300,20)
    )
    
    app.after(
            3550,
            lambda: showsecond_clue(app)
        )
    

   

# ===================================================
# CLUE 2
# ===================================================
def showsecond_clue(app): 
    
    app.clear_screen()
      
    clue = ctk.CTkLabel(
            app,
            text="PISTA #2",
            font=("Arial", 34, "bold"),
            text_color=MINT
    )
    
    clue.pack(
        pady=(180, 20)
    )
    question = ctk.CTkLabel(
            app,
            text="Vamos a llegar en uno de estos...",
            font=("Arial", 22, "bold"),
            text_color=LIGHT_BLUE
     )
    
    question.pack(
        pady=(20, 25)
    )
    
    button_frame = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )
    
    button_frame.pack(
        pady=10
    )
    # --------------------
    # Bote
    # --------------------

    boat_button = ctk.CTkButton(
        button_frame,
        text="🚢 Barco",
        font=("Arial", 17),
        width=190,
        height=50,
        corner_radius=20,
        fg_color=BLUE,
        hover_color=GREEN,
        command=lambda: check_answer(app, False,show_third_clue)
    )

    boat_button.grid(
        row=0,
        column=0,
        padx=10
    )

    # --------------------
    # Goggles
    # --------------------

    plane_button = ctk.CTkButton(
        button_frame,
        text="✈️ Avión",
        font=("Arial", 17),
        width=190,
        height=50,
        corner_radius=20,
        fg_color=BLUE,
        hover_color=GREEN,
        command=lambda: check_answer(app, False, show_third_clue)
    )

    plane_button.grid(
        row=0,
        column=1,
        padx=10
    )

    # --------------------
    # Tuxedo
    # --------------------

    train_button = ctk.CTkButton(
        button_frame,
        text="🚅 Tren",
        font=("Arial", 17),
        width=190,
        height=50,
        corner_radius=20,
        fg_color=BLUE,
        hover_color=GREEN,
        command=lambda: check_answer(app, True, show_third_clue)
    )

    train_button.grid(
        row=0,
        column=2,
        padx=10
    )
    
# ===================================================
# CLUE 3 - IMAGE CHOICE
# ===================================================

def show_third_clue(app):

    app.clear_screen()

    clue = ctk.CTkLabel(
        app,
        text="PISTA #3",
        font=("Arial", 34, "bold"),
        text_color=MINT
    )

    clue.pack(
        pady=(80, 10)
    )

    question = ctk.CTkLabel(
        app,
        text="¿A qué tipo de lugar crees que iremos?",
        font=("Arial", 22, "bold"),
        text_color=LIGHT_BLUE
    )

    question.pack(
        pady=(5, 25)
    )

    castle_image = ctk.CTkImage(
        light_image=Image.open("assets/cochem.png"),
        dark_image=Image.open("assets/cochem.png"),
        size=(230, 170)
    )

    beach_image = ctk.CTkImage(
        light_image=Image.open("assets/playa.png"),
        dark_image=Image.open("assets/playa.png"),
        size=(230, 170)
    )

    city_image = ctk.CTkImage(
        light_image=Image.open("assets/city.png"),
        dark_image=Image.open("assets/city.png"),
        size=(230, 170)
    )

    image_frame = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    image_frame.pack(
        pady=10
    )

    # --------------------------------
    # CASTLE / NATURE - CORRECT
    # --------------------------------

    castle_button = ctk.CTkButton(
        image_frame,
        text="",
        image=castle_image,
        width=240,
        height=180,
        fg_color=BLUE,
        hover_color=GREEN,
        corner_radius=15,
        command=lambda: check_answer(
            app,
            True,
            show_password_screen
        )
    )

    castle_button.grid(
        row=0,
        column=0,
        padx=12
    )

    # --------------------------------
    # BEACH
    # --------------------------------

    beach_button = ctk.CTkButton(
        image_frame,
        text="",
        image=beach_image,
        width=240,
        height=180,
        fg_color=BLUE,
        hover_color=GREEN,
        corner_radius=15,
        command=lambda: check_answer(
            app,
            False,
            show_password_screen
        )
    )

    beach_button.grid(
        row=0,
        column=1,
        padx=12
    )

    # --------------------------------
    # MODERN CITY
    # --------------------------------

    city_button = ctk.CTkButton(
        image_frame,
        text="",
        image=city_image,
        width=240,
        height=180,
        fg_color=BLUE,
        hover_color=GREEN,
        corner_radius=15,
        command=lambda: check_answer(
            app,
            False,
            show_password_screen
        )
    )

    city_button.grid(
        row=0,
        column=2,
        padx=12
    )
    
# ===================================================
# PASSWORD SCREEN
# ===================================================

def show_password_screen(app):

    app.clear_screen()

    title = ctk.CTkLabel(
        app,
        text="UNA ÚLTIMA COSA...",
        font=("Arial", 34, "bold"),
        text_color=MINT
    )

    title.pack(
        pady=(110, 20)
    )

    instruction = ctk.CTkLabel(
        app,
        text=(
            "Escribe la contraseña para saber tu itinerario\n"
            "del 24 y 25 de octubre"
        ),
        font=("Arial", 24, "bold"),
        text_color=TEXT
    )

    instruction.pack(
        pady=15
    )

    hint = ctk.CTkLabel(
        app,
        text="Pista: es el país al que iremos.",
        font=("Arial", 14),
        text_color=LIGHT_BLUE
    )

    hint.pack(
        pady=(0, 25)
    )

    password_entry = ctk.CTkEntry(
        app,
        width=300,
        height=45,
        placeholder_text="Escribe la contraseña...🔐",
        font=("Arial", 18),
        justify="center"
    )

    password_entry.pack(
        pady=10
    )

    result_label = ctk.CTkLabel(
        app,
        text="",
        font=("Arial", 18, "bold")
    )

    result_label.pack(
        pady=10
    )

    def verify_password():

        answer = password_entry.get().strip().lower()

        if answer == "alemania" or answer == "Alemania":

            result_label.configure(
                text="Contraseña correcta 💚",
                text_color=MINT
            )

            password_entry.configure(
                state="disabled"
            )

            verify_button.configure(
                state="disabled"
            )
            app.after(
                1500,
                lambda: password_success(app)
            )

        else:

            result_label.configure(
                text="Esa no es 👀 intenta otra vez.",
                text_color=ERROR
            )

    verify_button = ctk.CTkButton(
        app,
        text="DESBLOQUEAR 🔓",
        font=("Arial", 18, "bold"),
        width=220,
        height=50,
        corner_radius=25,
        fg_color=BLUE,
        hover_color=GREEN,
        command=verify_password
    )

    verify_button.pack(
        pady=15
    )

    # Pressing ENTER also submits password
    password_entry.bind(
        "<Return>",
        lambda event: verify_password()
    )
def password_success(app):

    app.clear_screen()

    title = ctk.CTkLabel(
        app,
        text="DESBLOQUEADO 🔓💙",
        font=("Arial", 42, "bold"),
        text_color=MINT
    )

    title.pack(
        pady=(50, 20)
    )
    # --------------------------------
    # Ticket Image
    # --------------------------------

    image_path = resource_path(
        "assets/ticket.png"
    )

    ticket_image = ctk.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(870, 465)
    )

    ticket_photo = ctk.CTkLabel(
        app,
        text="",
        image=ticket_image
    )

    ticket_photo.pack(
        pady=6
    )

    app.ticket_image = ticket_image
 