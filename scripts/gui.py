import customtkinter
from functools import partial
import psycopg

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Tapu Operations Program")
app.geometry("800x500+400+200")

panel = customtkinter.CTkFrame(master=app, width=800, height=500)
home = customtkinter.CTkFrame(master=app, width=800, height=500)

def clear_widgets(frame):
	for widget in frame.winfo_children():
		widget.destroy()

for frame in (panel, home):
    frame.grid(row=0, column=0, sticky='news')

def check_results(a,b,c):
	database_input = (a.get())
	username_input = (b.get())
	password_input = (c.get())
	if(str(database_input) == "tapu_db" and str(username_input) == "postgres" and str(password_input) == "15246868"):
	#if(True):
		load_home()
		return
	else:
		label = customtkinter.CTkLabel(master=panel, text="Database Name or Username or Password is wrong!", text_font=("Roboto", 24),text_color="Red")
		label.pack(pady=12, padx=10)

def load_panel():
	clear_widgets(home)

	panel.tkraise()

	panel.pack_propagate(False)

	db_name = customtkinter.StringVar()
	username = customtkinter.StringVar()
	password = customtkinter.StringVar()

	label = customtkinter.CTkLabel(master=panel, text="Tapu Müdürlüğü Bilgi  Sistemi", text_font=("Roboto", 28))
	label.pack(pady=12, padx=10)

	entry0 = customtkinter.CTkEntry(master=panel, placeholder_text="Enter Database Name", textvariable=db_name, width=200)
	entry0.pack(pady=12, padx=10)

	entry1 = customtkinter.CTkEntry(master=panel, placeholder_text="Username", textvariable=username, width=200)
	entry1.pack(pady=12, padx=10)

	entry2 = customtkinter.CTkEntry(master=panel, placeholder_text="Password", show="*", textvariable=password, width=200)
	entry2.pack(pady=12, padx=10)

	# check_results = partial(check_results, db_name, username, password)
	
	button = customtkinter.CTkButton(master=panel, text="LOGIN", command=lambda:check_results(db_name, username, password))
	#button = customtkinter.CTkButton(master=panel, text="LOGIN", command=lambda:load_home())
	button.pack(pady=12, padx=10)

def load_home():
	clear_widgets(panel)

	home.tkraise()

	query = customtkinter.StringVar()

	label = customtkinter.CTkLabel(master=home, text="Lütfen sorguyu giriniz:", text_font=("Roboto", 28),text_color="Green")
	label.pack(pady=12, padx=10)

	entry_home = customtkinter.CTkEntry(master=home, placeholder_text="Write The Query",textvariable=query, width=700, height=80)
	entry_home.pack(pady=12, padx=10)

	#home_button = customtkinter.CTkButton(master=home, text="Send Query", command=lambda:load_panel())
	home_button = customtkinter.CTkButton(master=home, text="Send Query", command=lambda:connect_database(query))
	home_button.pack(pady=12, padx=10)
	# home_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

def tuple_parser(tuple):
    word = ""
    for item in tuple:
        word = word + str(item) + "---"
    return word

def connect_database(query_input):
	try:
		q = (query_input.get())
		q = str(q)
		db_connection = psycopg.connect(dbname="tapu_db", user="postgres", host="localhost", password="15246868")
		cur = db_connection.cursor()
		cur.execute(q)
		query_result = cur.fetchone()

		print(query_result)

		res = tuple_parser(query_result)
		print(res)

		res_label = customtkinter.CTkLabel(master=home, text=res, text_font=("Roboto", 12))
		res_label.pack(pady=12, padx=10)

		cur.close()
	except:
		print("Cannot execute query!")
	finally:
		if db_connection is not None:
			db_connection.close()
			print("Connection closed!")

def main():
	load_panel()
	app.mainloop()

if __name__ == "__main__":
	try:
		main()
	except:
		print("program error")