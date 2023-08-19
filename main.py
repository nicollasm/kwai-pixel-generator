import tkinter as tk
from tkinter import ttk, messagebox
import interface

def generate_and_display():
    pixel_id = pixel_id_entry.get().strip()
    if not pixel_id:
        messagebox.showerror("Erro", "Por favor, insira o ID do Pixel.")
        return

    selected_events = [event for event, var in event_vars.items() if var.get()]
    interface.show_popup(pixel_id, selected_events)

app = tk.Tk()
app.title("Gerador de Scripts do Pixel do Kwai Ads")
app.geometry("600x600")

frame = ttk.Frame(app)
frame.pack(pady=20, padx=20)

ttk.Label(frame, text="Digite o ID do Pixel do Kwai Ads:").grid(row=0, column=0, sticky=tk.W, pady=5)
pixel_id_entry = ttk.Entry(frame, width=40)
pixel_id_entry.grid(row=0, column=1, pady=5, padx=5)

events = ['addPaymentInfo', 'addToCart', 'buttonClick', 'purchase', 'contentView', 'download', 'formSubmit',
          'initiatedCheckout', 'contact', 'placeOrder', 'search', 'completeRegistration', 'addToWishlist', 'subscribe']

event_vars = {event: tk.BooleanVar() for event in events}

for idx, event in enumerate(events, start=1):
    checkbox = ttk.Checkbutton(frame, text=event, variable=event_vars[event])
    checkbox.grid(row=idx, column=0, sticky=tk.W, pady=2)

generate_button = ttk.Button(frame, text="Gerar Scripts", command=generate_and_display)
generate_button.grid(row=len(events) + 1, column=0, columnspan=2, pady=10)

app.mainloop()
