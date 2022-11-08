"""Provides code for user management.

Features functionality to add, select or remove user. Control moves to contacts module after successful
user selection.
"""

import tkinter as tk
from . import helper, contacts
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('material.db')
c = conn.cursor()

class UserManagement:

	def __init__(self, window):
		self.frame = None
		self.window = window
		self.username = None
		self.password = None
		self.clicked = tk.IntVar()
		self.clicked.set(0)
		self.status = False
		self.draw_user_menu()

	def _gen_new_frame(self):
		"""Destroys any existing frame and generates and configure a new frame."""
		if self.frame:
			self.frame.destroy()
		self.frame = tk.Frame(master=self.window, bg='#455A64')
		self.frame.pack(expand=True, fill='both')

	def draw_user_menu(self):
		"""Draws User Management menu with 3 options on the screen."""
		self.window.title('User Management')
		self._gen_new_frame()
		btn_add_user = helper.create_button(self.frame, 'Add User', self.add_user)
		helper.grid_button(btn_add_user)
		btn_remove_user = helper.create_button(self.frame, 'Remove User', self.remove_user)
		helper.grid_button(btn_remove_user)
		btn_select_user = helper.create_button(self.frame, 'Select User', self.select_user)
		helper.grid_button(btn_select_user)

