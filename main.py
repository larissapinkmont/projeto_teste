import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sistema Teste")
app.geometry("400x200")

label = ctk.CTkLabel(app, text="Bem vindo ao sistema teste", font=("Arial", 20))
label.pack(pady=40)

app.mainloop()
