"""Provides code for manipulating contact data in the database.

Also provides various methods for verification.
"""

import tkinter as tk
from tkinter import messagebox
from . import user, helper
import sqlite3


conn = sqlite3.connect('material.db')
c = conn.cursor()


class ContactsManagement:
	"""Provides contact management methods, like addition, deletion, view, modify, search.

	Attributes:-
	tablename: sanitized name of the currently active table
	window: parent or root phonebook window
	frame: currently active frame or screen
	clicked: indicates whether a buttton has been clicked. Useful for creating local loops
	status: returns status and occasionally data from the last method, if needed
	"""

	def __init__(self, window, frame, tablename):
		self.tablename = tablename
		self.window = window
		self.frame = frame
		self.clicked = tk.IntVar()
		self.clicked.set(0)
		self.status = None
		self.draw_contacts_menu()

	def _gen_new_frame(self):
		"""Destroys any existing frame and generates a new one."""
		if self.frame:
			self.frame.destroy()
		self.frame = tk.Frame(master=self.window, bg='#455A64')
		self.frame.pack(expand='True', fill='both')

	def draw_contacts_menu(self):
		"""Draws buttons for calling different methods on screen."""
		def return_to_user():
			"""Returns control to user management module."""
			self.frame.destroy()
			self.clicked.set(1)

		self.window.title('Contacts Management')
		self._gen_new_frame()
		self.clicked.set(0)
		btn_1 = helper.create_button(self.frame, text='Show All Contacts', command=self.show_all_contacts)
		helper.grid_button(btn_1)
		btn_2 = helper.create_button(self.frame, text='Add Contact', command=self.add_contact)
		helper.grid_button(btn_2)
		btn_3 = helper.create_button(self.frame, text='Remove Contact', command=self.remove_contact)
		helper.grid_button(btn_3)
		btn_4 = helper.create_button(self.frame, text='Modify Contact', command=self.modify_contact)
		helper.grid_button(btn_4)
		btn_5 = helper.create_button(self.frame, text='Search Contact', command=self.search_contact)
		helper.grid_button(btn_5)
		btn_user = helper.create_button(self.frame, text='Switch to User Management Menu', command=return_to_user, width=30)
		helper.grid_button(btn_user)
		btn_user.wait_variable(self.clicked)

	
