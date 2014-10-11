import unittest
from sched import forms
from sched.app import app

class Form(unittest.TestCase):
	def testform(self):
		form = forms.AppointmentForm()
		self.assertEqual(
			'<input id="title" name="title" type="text" value="">', str(form.title))
		self.assertEqual(
			'<input id="start" name="start" type="text" value="">', str(form.start))
		self.assertEqual(
			'<input id="end" name="end" type="text" value="">', str(form.end))
		self.assertEqual(
			'<input id="allday" name="allday" type="checkbox" value="y">', str(form.allday))
		self.assertEqual(
			'<input id="location" name="location" type="text" value="">', str(form.location))
		self.assertEqual(
			'<textarea id="description" name="description"></textarea>', str(form.description))
	
	def testLogin(self):
		form = forms.LoginForm()
		self.assertEqual(
			'<input id="username" name="username" type="text" value="">', str(form.username))
		self.assertEqual(
			'<input id="password" name="password" type="password" value="">', str(form.password))


if __name__ == '__main__':
	unittest.main()

