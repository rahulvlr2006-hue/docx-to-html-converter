import customtkinter as ctk
from tkinter import filedialog
from converter import convert_docx_to_html
from tkinterweb import HtmlFrame
import os


# -----------------------
# VARIABLES
# -----------------------

selected_file = ""


# -----------------------
# FUNCTIONS
# -----------------------
def show_about():

    about_window = ctk.CTkToplevel(app)

    about_window.title("About")
    about_window.geometry("400x300")

    # Make it stay on top
    about_window.transient(app)

    # Focus the window
    about_window.focus()

    # Grab all input until closed
    about_window.grab_set()

    title = ctk.CTkLabel(
        about_window,
        text="DOCX TO HTML Converter",
        font=("Arial", 20, "bold")
    )
    title.pack(pady=15)

    version = ctk.CTkLabel(
        about_window,
        text="Version 1.0"
    )
    version.pack(pady=5)

    developer = ctk.CTkLabel(
        about_window,
        text="Developed by Rahul"
    )
    developer.pack(pady=5)

    close_button = ctk.CTkButton(
        about_window,
        text="Close",
        command=about_window.destroy
    )
    close_button.pack(pady=15)
def preview_html():

    global selected_file

    if not selected_file:

        status_label.configure(
            text="Status: Please select a DOCX file"
        )
        return

    html = convert_docx_to_html(selected_file)

    preview_window = ctk.CTkToplevel(app)
    preview_window.title("HTML Preview")
    preview_window.geometry("1000x700")

    browser = HtmlFrame(preview_window)
    browser.pack(fill="both", expand=True)

    browser.load_html(html)
def change_theme(choice):
    if choice == "Dark":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


def browse_file():
    global selected_file

    file_path = filedialog.askopenfilename(
        filetypes=[("Word Documents", "*.docx")]
    )

    if file_path:

        selected_file = file_path

        file_box.configure(state="normal")
        file_box.delete("1.0", "end")
        file_box.insert("1.0", file_path)
        file_box.configure(state="disabled")

        status_label.configure(
            text="Status: DOCX Selected"
        )


def clear_selection():
    global selected_file

    selected_file = ""

    file_box.configure(state="normal")
    file_box.delete("1.0", "end")
    file_box.insert("1.0", "No file selected")
    file_box.configure(state="disabled")
    progress_bar.set(0)

    status_label.configure(
        text="Status: File Removed"
    )


def refresh_file():
    global selected_file

    selected_file = ""

    file_box.configure(state="normal")
    file_box.delete("1.0", "end")
    file_box.insert("1.0", "No file selected")
    file_box.configure(state="disabled")
    progress_bar.set(0)

    status_label.configure(
        text="Status: Ready"
    )


def convert_file():

    global selected_file

    if not selected_file:

        status_label.configure(
            text="Status: Please select a DOCX file"
        )
        return

    progress_bar.set(0.2)
    app.update()

    html = convert_docx_to_html(selected_file)

    progress_bar.set(0.6)
    app.update()

    save_path = filedialog.asksaveasfilename(
        defaultextension=".html",
        filetypes=[("HTML Files", "*.html")]
    )

    if not save_path:
        progress_bar.set(0)
        return

    with open(save_path, "w", encoding="utf-8") as file:
        file.write(html)

    progress_bar.set(1)

    status_label.configure(
        text="Status: Conversion Successful ✅"
    )


def open_html():

    html_file = filedialog.askopenfilename(
        filetypes=[("HTML Files", "*.html")]
    )

    if html_file:
        os.startfile(html_file)


# -----------------------
# APP SETTINGS
# -----------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

try:
    app.iconbitmap("assets/icon.ico")
except:
    pass

app.title("DOCX TO HTML Converter")
app.geometry("900x650")
app.resizable(False, False)


# -----------------------
# TITLE
# -----------------------

title_label = ctk.CTkLabel(
    app,
    text="DOCX TO HTML CONVERTER",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)


# -----------------------
# STATUS LABEL
# -----------------------

status_label = ctk.CTkLabel(
    app,
    text="Status: Ready"
)
status_label.pack(pady=10)


# -----------------------
# FILE SECTION
# -----------------------

file_title = ctk.CTkLabel(
    app,
    text="Selected DOCX File"
)
file_title.pack()

file_box = ctk.CTkTextbox(
    app,
    width=750,
    height=60
)
file_box.pack(pady=10)

file_box.insert("1.0", "No file selected")
file_box.configure(state="disabled")


# -----------------------
# BUTTON FRAME
# -----------------------

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

browse_button = ctk.CTkButton(
    button_frame,
    text="📂 Browse DOCX",
    command=browse_file
)
browse_button.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

refresh_button = ctk.CTkButton(
    button_frame,
    text="🔄",
    width=50,
    command=refresh_file
)
refresh_button.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

delete_button = ctk.CTkButton(
    button_frame,
    text="🗑",
    width=50,
    command=clear_selection
)
delete_button.grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


# -----------------------
# ACTION BUTTONS
# -----------------------

action_frame = ctk.CTkFrame(app)
action_frame.pack(pady=20)

convert_button = ctk.CTkButton(
    action_frame,
    text="⚡ Convert",
    command=convert_file
)
convert_button.grid(
    row=0,
    column=0,
    padx=10
)

open_button = ctk.CTkButton(
    action_frame,
    text="🌐 Open HTML",
    command=open_html
)
open_button.grid(
    row=0,
    column=1,
    padx=10
)
preview_button = ctk.CTkButton(
    action_frame,
    text="👁 Preview",
    command=preview_html
)

preview_button.grid(
    row=0,
    column=2,
    padx=10
)


# -----------------------
# THEME SWITCHER
# -----------------------

theme_label = ctk.CTkLabel(
    app,
    text="Theme"
)
theme_label.pack(pady=(20, 5))

theme_menu = ctk.CTkOptionMenu(
    app,
    values=["Dark", "Light"],
    command=change_theme
)
theme_menu.pack()

theme_menu.set("Dark")


# -----------------------
# FOOTER
# -----------------------

footer = ctk.CTkLabel(
    app,
    text="Version 1.0"
)
footer.pack(pady=20)
about_button = ctk.CTkButton(
    app,
    text="ℹ About",
    command=show_about
)

about_button.pack(pady=10)


# -----------------------
# RUN APP
# -----------------------

progress_bar = ctk.CTkProgressBar(
    app,
    width=400
)

progress_bar.pack(pady=10)

progress_bar.set(0)
app.mainloop()