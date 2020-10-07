from tkinter import *
from tkinter import ttk

class UserInterface(object):
	def __init__(self):
		super(UserInterface, self).__init__()
		# Default sign in message
		self.sign_in_message = "Please Sign In"
		# Sign in window
		self.sign_in_window = None
		# The main window instance
		self.instance = Tk()
		self.root_frame = Frame(self.instance, width=80, height=60)
		self.root_frame.grid(column=0, row=0)
		self.user_info_frame = Frame(self.root_frame, width=20, height=60, bd=5)
		self.user_info_frame.grid(column=0, row=0)
		ttk.Separator(self.root_frame, orient=VERTICAL).grid(column=1, row=0, sticky=N+S)
		# The main window title
		self.instance.title("Stock Trading Game")
		# The main window size
		self.instance.geometry('800x600')
		# A holder for the current logged in user name
		self.user_name = StringVar()
		self.user_name.set(self.sign_in_message)
		# A holder for the current logged in user password
		self.user_password = StringVar()
		self.user_password.set("")

		# Create a Menu Bar
		self.menu = Menu(self.instance)
		# Add a File tab
		self.file_tab = Menu(self.menu, tearoff=0)
		self.file_tab.add_command(label="Sign In", command=self.open_sign_in_window)	
		self.file_tab.add_command(label="Sign Out", command=self.open_sign_out_window)		
		self.file_tab.add_command(label="Exit", command=self.exit)
		self.menu.add_cascade(label="File", menu=self.file_tab)

		# Create a user info panel
		Label(self.user_info_frame, text="My Profile", font=("Courier", 22)).grid(column=0, row=0)
		ttk.Separator(self.user_info_frame, orient=HORIZONTAL).grid(column=0, row=1, sticky=E+W)
		Label(self.user_info_frame, textvariable=self.user_name, font=("Veranda", 16)).grid(column=0, row=2)
		Label(self.user_info_frame, text="My Stocks", font=("Courier", 22)).grid(column=0, row=3)
		ttk.Separator(self.user_info_frame, orient=HORIZONTAL).grid(column=0, row=4, sticky=E+W)
		# Start the gui
		self.instance.config(menu=self.menu)
		self.instance.mainloop()

	def open_sign_in_window(self):
		if self.sign_in_window is None:
			self.sign_in_window = Toplevel(self.instance)
			self.sign_in_window.title("Sign In")
			self.sign_in_window.geometry("300x90")
			Label(self.sign_in_window, text="Name").grid(column=0, row=0)
			self.user_name.set("")
			Entry(self.sign_in_window, textvariable=self.user_name, bd=5, width=30).grid(column=1, row=0, sticky=E)
			Label(self.sign_in_window, text="Password").grid(column=0, row=1)
			Entry(self.sign_in_window, textvariable=self.user_password, bd=5, width=30).grid(column=1, row=1, sticky=E)
			Button(self.sign_in_window, text="Submit", width=15, bd=5, command=self.submit_user).grid(column=1, row=2, pady=5, sticky=N+E+S+W)
		return
	
	def open_sign_out_window(self):
		self.user_name.set(self.sign_in_message)
		self.user_password.set("")
		self.sign_in_window = None	
		return

	def exit(self):
		self.instance.destroy()
		return

	def buy_stocks(self):
		return

	def sell_stocks(self):
		return

	def open_settings(self):
		return

	def submit_user(self):
		# ADD LOGIN HERE
		self.sign_in_window.destroy()

if __name__ == '__main__':
	ui = UserInterface()