import unittest
import sched.app as app

class app(unittest.TestCase):
	def setUp(self):
		self.appt = app.app.user()

	def appointment_list(self):
		response = self.appointment_list("/appointments")
		self.assertEquals(response.status_code)
		assert 'Redirecting' in response.data

#se encuentra un evento establecido
	def appointment_detail(self):
		response = self.appt.post('/login/', data = dict(username = 'sun.prinsses@hotmail.com', password = 'mayra'), follow_redirects = true)
		response = self.appt.get('/appointments/1/')
		self.assertEquals(response.status_code)
		assert "titulo" in response.data
		assert "cita" not in response.data

	def appointment_detail(self):
		response = self.appt.post('/login/', data = dict(username = 'sun.prinsses@hotmail.com', password = 'mayra'), follow_redirects = true)
		response = self.appt.get('/appointments/0/')
		self.assertEquals(response.status_code)
		assert "Not Found" in response.data

