import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("db_project")
app.geometry("800x500")
# app.eval("tk::PlaceWindow . center")

panel = customtkinter.CTkFrame(master=app, width=800, height=500)
#panel.pack(pady=20, padx=60, fill="both", expand=True)

home = customtkinter.CTkFrame(master=app, width=800, height=500)
#home.pack(pady=20, padx=60, fill="both", expand=True)


def clear_widgets(frame):

	for widget in frame.winfo_children():
		widget.destroy()


def load_panel():
	clear_widgets(home)

	panel.tkraise()

	panel.pack_propagate(False)

	label = customtkinter.CTkLabel(master=panel, text="login", text_font=("Roboto", 24))
	label.pack(pady=12, padx=10)

	entry1 = customtkinter.CTkEntry(master=panel, placeholder_text="Username")
	entry1.pack(pady=12, padx=10)

	entry2 = customtkinter.CTkEntry(master=panel, placeholder_text="Password", show="*")
	entry2.pack(pady=12, padx=10)

	button = customtkinter.CTkButton(master=panel, text="login", command=lambda:load_home())
	button.pack(pady=12, padx=10)
	button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

	checkbox = customtkinter.CTkCheckBox(master=panel, text="Remember me")
	checkbox.pack(pady=12, padx=10)

def load_home():
	clear_widgets(panel)

	home.tkraise()

	entry_home = customtkinter.CTkEntry(master=home, placeholder_text="query")
	entry_home.pack(pady=12, padx=10)

	home_button = customtkinter.CTkButton(master=home, text="login 2", command=lambda:load_panel())
	home_button.pack(pady=12, padx=10)
	# home_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

for frame in (panel, home):
    frame.grid(row=0, column=0, sticky='news')

if __name__ == "__main__":
		load_panel()
		app.mainloop()
else:
	print("program error")
