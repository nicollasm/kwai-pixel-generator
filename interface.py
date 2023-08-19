import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from logic import generate_kwai_pixel_script


def show_popup(pixel_id, selected_events):
    popup = tk.Toplevel()
    popup.title("Scripts Gerados")
    popup.geometry("700x500")

    for idx, event in enumerate(selected_events, start=1):
        script = generate_kwai_pixel_script(pixel_id, event)

        label = ttk.Label(popup, text=f"Script para {event}:")
        label.grid(row=idx, column=0, sticky=tk.W, pady=5)

        text_widget = tk.Text(popup, height=5, width=50)
        text_widget.grid(row=idx, column=1, pady=5, padx=5)
        text_widget.insert(tk.END, script)

        copy_button = ttk.Button(popup, text="Copiar", command=lambda e=script: copy_to_clipboard(e))
        copy_button.grid(row=idx, column=2, pady=5, padx=5)


def copy_to_clipboard(script):
    pyperclip.copy(script)
    messagebox.showinfo("Copiado", "Script copiado para a área de transferência!")
