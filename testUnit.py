import unittest
from sched import forms
from sched import filters
from sched.app import app
from jinja2 import Environment
from datetime import datetime, date, timedelta
from datetime import timedelta


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


class filter(unittest.TestCase):


	def testdatetime(self):
		now = date(2010, 11, 11)
		fecha = filters.do_datetime(now)
		self.assertNotEqual(fecha, "2010-11-11 - Thursday")


	def testdatetime2(self):
		now = datetime(2010, 11, 11, 13, 00, 00)
		fecha = filters.do_datetime(now)
		self.assertEqual(fecha, '2010-11-11 - Thursday at 1:00pm')


	def testdatetimeNull(self):
		fecha = filters.do_datetime(None)
		self.assertNotEqual(fecha, "Today")
		self.assertEqual(fecha, '')


	def testdatetimeNullFormat(self):
		now = datetime(2010, 11, 11, 14, 00, 00)
		fecha = filters.do_datetime(now, None)
		self.assertEqual(fecha, '2010-11-11 - Thursday at 2:00pm')


	def testdatetimeFormat(self):
		a = '%Y-%m-%d - %A'
		now = datetime(2010, 11, 11, 14, 00, 00)
		fecha = filters.do_datetime(now, a)
		self.assertNotEqual(fecha, '2010-11-11 - Thursday at 2:00pm')


	def testdateNull(self):
		fechadate = filters.do_date(None)
		self.assertEqual(fechadate, '')


	def testdateNull(self):
		now = datetime(2010, 11, 11, 13, 00, 00)
		fechadate = filters.do_date(now)
		self.assertNotEqual(fechadate, '2010-11-11 - Thursday at 1:00pm')
		self.assertEqual(fechadate, '2010-11-11 - Thursday')


	def testdurationhour(self):
		time = filters.do_duration(3600)
		self.assertNotEqual(time, "1 day")
		self.assertEqual(time, "0 day, 1 hour, 0 minute, 0 second")


	def testdurationdays(self):
		time = filters.do_duration(258732)
		self.assertEqual(time, "2 days, 23 hours, 52 minutes, 12 seconds")


	def testdo_nl2br(self):
		template_env = Environment(
    	autoescape=False,
    	extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape'])
		text = "Texto con '\n' saltos '\n' juntos"
		changes = filters.do_nl2br(template_env, text)
		self.assertNotEqual(changes, "")
		self.assertEqual(changes, "Texto con &#39;<br />&#39; saltos &#39;<br />&#39; juntos")


	def test_do_nl2br_with_Markup(self):
		template_env = Environment(
    	autoescape=True,
    	extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape'])
		text = "Texto con '\n' saltos '\n' <script>juntos</script>"
		changes = filters.do_nl2br(template_env, text)
		self.assertNotEqual(changes, "Texto con &#39;<br />&#39; saltos &#39;<br />&#39; juntos")
		self.assertEqual(changes, "Texto con &#39;<br />&#39; saltos &#39;<br />&#39; &lt;script&gt;juntos&lt;/script&gt;")


if __name__ == '__main__':
    unittest.main()
