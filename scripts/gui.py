import customtkinter
import psycopg
import sys

print("Python version: ", sys.version)
print("Customtkinter version: ", customtkinter.__version__)
print("psycopg version: ", psycopg.__version__)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Tapu Müdürlüğü Bilgi Sistemi")
app.geometry("800x800+200+200")

frame_size_width = 800
frame_size_height = 800

# Frames
panel = customtkinter.CTkFrame(master=app, width=frame_size_width, height=frame_size_height)
panel.grid(row=0, column=0, sticky='news')

home = customtkinter.CTkFrame(master=app, width=frame_size_width, height=frame_size_height)
home.grid(row=0, column=0, sticky='news')

insert_frame = customtkinter.CTkFrame(master=app, width=frame_size_width, height=frame_size_height)
insert_frame.grid(row=0, column=0, sticky='news')

update_frame = customtkinter.CTkFrame(master=app, width=frame_size_width, height=frame_size_height)
update_frame.grid(row=0, column=0, sticky='news')

delete_frame = customtkinter.CTkFrame(master=app, width=frame_size_width, height=frame_size_height)
delete_frame.grid(row=0, column=0, sticky='news')

def clear_widgets(frame):
	for widget in frame.winfo_children():
		widget.destroy()

def check_results(a,b,c):
	database_input = (a.get())
	username_input = (b.get())
	password_input = (c.get())
	if(str(database_input) == "tapu_db" and str(username_input) == "postgres" and str(password_input) == "15246868"):
		load_home()
		return
	else:
		label = customtkinter.CTkLabel(master=panel, text="Database Name or Username or Password is wrong!", text_font=("Roboto", 24),text_color="Red")
		label.pack(pady=12, padx=10)

def load_panel():

	panel.tkraise()

	panel.pack_propagate(False)

	db_name = customtkinter.StringVar()
	username = customtkinter.StringVar()
	password = customtkinter.StringVar()

	label = customtkinter.CTkLabel(master=panel, text="Tapu Müdürlüğü Bilgi  Sistemi", text_font=("Roboto", 28),text_color="Orange")
	label.pack(pady=12, padx=10)

	entry0 = customtkinter.CTkEntry(master=panel, placeholder_text="Enter Database Name", textvariable=db_name, width=200)
	entry0.pack(pady=12, padx=10)

	entry1 = customtkinter.CTkEntry(master=panel, placeholder_text="Username", textvariable=username, width=200)
	entry1.pack(pady=12, padx=10)

	entry2 = customtkinter.CTkEntry(master=panel, placeholder_text="Password", show="*", textvariable=password, width=200)
	entry2.pack(pady=12, padx=10)

	button = customtkinter.CTkButton(master=panel, text="LOGIN", command=lambda:check_results(db_name, username, password))
	button.pack(pady=12, padx=10)

def load_home():
	clear_widgets(panel)

	home.tkraise()

	label = customtkinter.CTkLabel(master=home, text="Lütfen yapmak istediginiz islemi giriniz:", text_font=("Roboto", 28),text_color="Orange")
	label.pack(pady=12, padx=10)

	insert_button = customtkinter.CTkButton(master=home, text="Veri ekleme", command=lambda:insert_handle())
	insert_button.pack(pady=12, padx=10)

	update_button = customtkinter.CTkButton(master=home, text="Veri guncellleme", command=lambda:update_handle())
	update_button.pack(pady=12, padx=10)

	delete_button = customtkinter.CTkButton(master=home, text="Veri silme", command=lambda:delete_handle())
	delete_button.pack(pady=12, padx=10)

def insert_handle():
	clear_widgets(home)

	insert_frame.tkraise()

	property_type = customtkinter.StringVar()
	property_owner_name = customtkinter.StringVar()
	property_owner_surname = customtkinter.StringVar()
	property_owner_id = customtkinter.StringVar()
	property_price = customtkinter.StringVar()
	property_room_number = customtkinter.StringVar()
	property_survey = customtkinter.StringVar()
	property_address = customtkinter.StringVar()
	property_estate_id = customtkinter.StringVar()

	insert_label = customtkinter.CTkLabel(master=insert_frame, text="Lütfen eklemeleri yapiniz", text_font=("Roboto", 28),text_color="Orange")
	insert_label.pack(pady=12, padx=10)

	p_type = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet turu", textvariable=property_type, width=200)
	p_type.pack(pady=12, padx=10)

	p_owner_name = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet sahibi ismi", textvariable=property_owner_name, width=200)
	p_owner_name.pack(pady=12, padx=10)

	p_owner_surname = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet sahibi soyismi", textvariable=property_owner_surname, width=200)
	p_owner_surname.pack(pady=12, padx=10)

	p_owner_id = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet sahibi id", textvariable=property_owner_id, width=200)
	p_owner_id.pack(pady=12, padx=10)

	p_price = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet fiyati", textvariable=property_price, width=200)
	p_price.pack(pady=12, padx=10)

	p_room_number = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet oda sayisi", textvariable=property_room_number, width=200)
	p_room_number.pack(pady=12, padx=10)

	p_survey = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet boyutu", textvariable=property_survey, width=200)
	p_survey.pack(pady=12, padx=10)

	p_address = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet adresi", textvariable=property_address, width=200)
	p_address.pack(pady=12, padx=10)

	p_estate_id = customtkinter.CTkEntry(master=insert_frame, placeholder_text="Mulkiyet id", textvariable=property_estate_id, width=200)
	p_estate_id.pack(pady=12, padx=10)

	main_insert_button = customtkinter.CTkButton(master=insert_frame, text="Veri ekle", command=lambda:insert_db(property_type, 
																										property_owner_name, 
																										property_owner_surname,
																										property_owner_id,
																										property_price,
																										property_room_number,
																										property_survey,
																										property_address,
																										property_estate_id))
	main_insert_button.pack(pady=12, padx=10)

	back_button = customtkinter.CTkButton(master=insert_frame, text="Geri don", command=lambda:load_home())
	back_button.pack(pady=12, padx=10)

def insert_db(input1,input2,input3,input4,input5,input6,input7,input8,input9):
	try:
		a = str(input1.get())
		b = str(input2.get())
		c = str(input3.get())
		d = str(input4.get())
		e = str(input5.get())
		f = str(input6.get())
		g = str(input7.get())
		h = str(input8.get())
		l = str(input9.get())

		db_connection = psycopg.connect(dbname="tapu_db", user="postgres", host="localhost", password="15246868")
		cur = db_connection.cursor()

		query = """INSERT INTO property (pType,pOwnerName,pOwnerSurname,pOwnerID,pPrice,pRoomNumber,pSurvey,pAddress,pEstateID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		query_values = (a,b,c,d,e,f,g,h,l)

		print(query)

		cur.execute(query,query_values)
		db_connection.commit()
		query_result = cur.fetchone()

		cur.close()
	except:
		print("Cannot execute query!")
	finally:
		if db_connection is not None:
			db_connection.close()
			print("Connection closed!")

def update_handle():
	clear_widgets(home)
	clear_widgets(insert_frame)
	clear_widgets(update_frame)

	update_frame.tkraise()

	update_input = customtkinter.StringVar()

	update_label = customtkinter.CTkLabel(master=update_frame, text="Mulk tablosu update", text_font=("Roboto", 28),text_color="Orange")
	update_label.pack(pady=12, padx=10)

	update_option_menu = customtkinter.CTkOptionMenu(master=update_frame, values=["pType","pOwnerName","pOwnerSurname","pOwnerID,pPrice","pRoomNumber","pSurvey","pAddress","pEstateID"], command=lambda:option_handler())
	update_option_menu.pack(pady=12, padx=10)

	update_entry = customtkinter.CTkEntry(master=update_frame, placeholder_text="Update entry", textvariable=update_input, width=200)
	update_entry.pack(pady=12, padx=10)

	back_button = customtkinter.CTkButton(master=update_frame, text="Geri don", command=lambda:load_home())
	back_button.pack(pady=12, padx=10)

def option_handler():
	pass

def delete_handle():
	clear_widgets(home)
	clear_widgets(insert_frame)
	clear_widgets(update_frame)
	clear_widgets(delete_frame)

	delete_frame.tkraise()

	delete_input = customtkinter.StringVar()

	delete_label = customtkinter.CTkLabel(master=delete_frame, text="Mulk tablosu delete", text_font=("Roboto", 28),text_color="Orange")
	delete_label.pack(pady=12, padx=10)

	delete_entry = customtkinter.CTkEntry(master=delete_frame, placeholder_text="Estate ID to delete", textvariable=delete_input, width=200)
	delete_entry.pack(pady=12, padx=10)

	delete_button = customtkinter.CTkButton(master=delete_frame, text="Delete", command=lambda:delete_db(delete_input))
	delete_button.pack(pady=12, padx=10)

	back_button = customtkinter.CTkButton(master=delete_frame, text="Geri don", command=lambda:load_home())
	back_button.pack(pady=12, padx=10)

def delete_db(del_id):
	try:
		deletion = str(del_id.get())
		db_connection = psycopg.connect(dbname="tapu_db", user="postgres", host="localhost", password="15246868")
		cur = db_connection.cursor()

		cur.execute("DELETE FROM property WHERE pestateid = %s",(deletion,))
		db_connection.commit()
		query_result = cur.fetchone()

		cur.close()
	except:
		print("Cannot execute query!")
	finally:
		if db_connection is not None:
			db_connection.close()
			print("Connection closed!")

# def tuple_parser(tuple):
#     word = ""
#     for item in tuple:
#         word = word + str(item) + "\n"
#     return word

# def connect_database(query_input):
# 	try:
# 		q = (query_input.get())
# 		q = str(q)
# 		db_connection = psycopg.connect(dbname="tapu_db", user="postgres", host="localhost", password="15246868")
# 		cur = db_connection.cursor()
# 		cur.execute(q)
# 		query_result = cur.fetchone()

# 		print(query_result)

# 		res = tuple_parser(query_result)
# 		print(res)

# 		res_label = customtkinter.CTkLabel(master=home, text=res, text_font=("Roboto", 14), text_color="white")
# 		res_label.pack(pady=12, padx=10)

# 		cur.close()
# 	except:
# 		print("Cannot execute query!")
# 	finally:
# 		if db_connection is not None:
# 			db_connection.close()
# 			print("Connection closed!")

def main():
	load_panel()
	app.mainloop()

if __name__ == "__main__":
	try:
		main()
	except:
		print("program error")