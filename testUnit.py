import unittest
from sched import forms
from sched import filters
from sched import app
from jinja2 import Environment
from datetime import datetime, date, timedelta
from datetime import timedelta
from sched import models
import json


class Form(unittest.TestCase):

        # 1
    def testform(self):
        form = forms.AppointmentForm()
        self.assertEqual(
            '<input id="title" name="title" type="text" value="">',
            str(form.title))
        self.assertEqual(
            '<input id="start" name="start" type="text" value="">',
            str(form.start))
        self.assertEqual(
            '<input id="end" name="end" type="text" value="">',
            str(form.end))
        self.assertEqual(
            '<input id="allday" name="allday" type="checkbox" value="y">',
            str(form.allday))
        self.assertEqual(
            '<input id="location" name="location" type="text" value="">',
            str(form.location))
        self.assertEqual(
            '<textarea id="description" name="description"></textarea>',
            str(form.description))
    # 2

    def testLogin(self):
        form = forms.LoginForm()
        self.assertEqual(
            '<input id="username" name="username" type="text" value="">',
            str(form.username))
        self.assertEqual(
            '<input id="password" name="password" type="password" value="">',
            str(form.password))


class filter(unittest.TestCase):
        # 3

    def testdatetime(self):
        now = date(2010, 11, 11)
        fecha = filters.do_datetime(now)
        self.assertNotEqual(fecha, "2010-11-11 - Thursday")
    # 4

    def testdatetime2(self):
        now = datetime(2010, 11, 11, 13, 00, 00)
        fecha = filters.do_datetime(now)
        self.assertEqual(fecha, '2010-11-11 - Thursday at 1:00pm')
    # 5

    def testdatetimeNull(self):
        fecha = filters.do_datetime(None)
        self.assertNotEqual(fecha, "Today")
        self.assertEqual(fecha, '')
    # 6

    def testdatetimeNullFormat(self):
        now = datetime(2010, 11, 11, 14, 00, 00)
        fecha = filters.do_datetime(now, None)
        self.assertEqual(fecha, '2010-11-11 - Thursday at 2:00pm')
    # 7

    def testDatetimeFormat(self):
        a = '%Y-%m-%d - %A'
        now = datetime(2010, 11, 11, 14, 00, 00)
        fecha = filters.do_datetime(now, a)
        self.assertNotEqual(fecha, '2010-11-11 - Thursday at 2:00pm')
    # 8

    def testdateNullOne(self):
        fechadate = filters.do_date(None)
        self.assertEqual(fechadate, '')
    # 9

    def testdateNull(self):
        now = datetime(2010, 11, 11, 13, 00, 00)
        fechadate = filters.do_date(now)
        self.assertNotEqual(fechadate, '2010-11-11 - Thursday at 1:00pm')
        self.assertEqual(fechadate, '2010-11-11 - Thursday')
    # 10

    def testdurationhour(self):
        time = filters.do_duration(3600)
        self.assertNotEqual(time, "1 day")
        self.assertEqual(time, "0 day, 1 hour, 0 minute, 0 second")
    # 11

    def testDurationdays(self):
        time = filters.do_duration(258732)
        self.assertEqual(time, "2 days, 23 hours, 52 minutes, 12 seconds")
    # 12

    def testdo_nl2br(self):
        tEnv = Environment(
            autoescape=False,
            extensions=['jinja2.ext.i18n',
                        'jinja2.ext.autoescape'])
        text = "Texto con '\n' saltos '\n' juntos"
        changes = filters.do_nl2br(tEnv, text)
        self.assertNotEqual(changes, "")
        self.assertEqual(
            changes,
            "Texto con &#39;<br />&#39; saltos &#39;<br />&#39; juntos")
    # 13

    def test_do_nl2br_with_Markup(self):
        tEnv = Environment(
            autoescape=True,
            extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape'])
        text = "Texto con '\n' saltos '\n' <script>juntos</script>"
        changes = filters.do_nl2br(tEnv, text)
        self.assertNotEqual(
            changes, "Texto con &#39;<br />&#39; saltos &#39;<br />&#39; juntos")
        self.assertEqual(
            changes,
            "Texto con &#39;<br />&#39; saltos &#39;<br />&#39; &lt;script&gt;juntos&lt;/script&gt;")


class testModelUser(unittest.TestCase):
        # 14

    def testUserpass(self):
        user = models.User(name="mayra", email="moon.prinsses@hotmail.com")
        user._set_password("mayra")
        assert "sha1" in user._get_password()
        self.assertNotEqual(user._get_password(), "123456")
        self.assertEqual(True, user.check_password("mayra"))
    # 15

    def testStatusUser(self):
        user = models.User(name="Nuevo", email="nuevo@gmail.com")
        user._set_password("123456")
        self.assertNotEqual(user.get_id(), 0)
        self.assertNotEqual(user.is_active(), False)
    # 16

    def testAuthenticateUser(self):
        user, authenticate = models.User.authenticate(
            app.db.session.query, "nuevo@gmail.com", "123456")
        self.assertEqual(authenticate, False)
        self.assertNotEqual(user, "None")
    # 17

    def testNullPasswordUser(self):
        user = models.User(name="Nuevo", email="nuevo@gmail.com")
        self.assertEqual(False, user.check_password("123456"))
    # 18

    def testActiveUser(self):
        user, authenticate = models.User.authenticate(
            app.db.session.query, "moon.prinsses@hotmail.com", "mayra")
        self.assertNotEqual(authenticate, False)
        self.assertEqual(user.name, "mayra")
    # 19

    def testNotExistUser(self):
        user, authenticate = models.User.authenticate(
            app.db.session.query, "cosa@hotmail.com", "mayra")
        self.assertEqual(authenticate, False)
        self.assertEqual(user, None)


class testModelApponintment(unittest.TestCase):
        # 20

    def test_appointment_duration(self):
        now = datetime.now()
        appt = models.Appointment(
            title='Prueba Unitaria', start=now,
            end=now + timedelta(seconds=1800),
            allday=False)
        self.assertEqual(1800, appt.duration)
        self.assertNotEqual(1801, appt.duration)
    # 21

    def testAppointmentR(self):
        now = datetime.now()
        appt = models.Appointment(
            title='Prueba Unitaria Repre', start=now,
            end=now + timedelta(seconds=1800),
            allday=False)
        self.assertNotEqual('<Appointment: 4>', appt.__repr__())


class testApp(unittest.TestCase):
        # 22

    def setUp(self):
        self.appt = app.app.test_client()
    # 23

    def testAppointmentList(self):
        r = self.appt.get("/appointments")
        self.assertEquals(r.status_code, 301)
        assert 'Redirecting' in r.data
    # 24

    def testlogin(self):
        r = self.appt.get("/login/")
        self.assertEquals(r.status_code, 200)
        assert 'Log user' in r.data
        UserAct = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'),
            follow_redirects=True)
        self.assertEquals(UserAct.status_code, 200)
    # 25

    def testFailedLogin(self):
        r = self.appt.post('/login/', data=dict(
            username='nuevo@gmail.com',
            password='123456'), follow_redirects=True)
        self.assertEquals(r.status_code, 200)
    # 26

    def testLogout(self):
        r = self.appt.get("/logout/")
        self.assertEquals(r.status_code, 302)
        assert 'Redirecting' in r.data
    # 27

    def testApptDetail(self):
        r = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'), follow_redirects=True)
        r = self.appt.get('/appointments/6/')
        self.assertEquals(r.status_code, 200)
        assert "cita" in r.data
    # 28

    def testApptNotExistdetail(self):
        r = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'), follow_redirects=True)
        print("hola")
        r = self.appt.get('/appointments/0/')
        self.assertEquals(r.status_code, 404)
        assert "Not Found" in r.data

    def testEditappoitnment(self):
        r = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'), follow_redirects=True)
        r = self.appt.get('/appointments/6/edit/')
        self.assertEquals(r.status_code, 200)
        assert "Edit Appointment" in r.data
        assert "Add Appointment" not in r.data
        r = self.appt.post('/appointments/6/edit/', data=dict(
            title="cita",
            start="2014-10-09 02:46:56.000000",
            end="2014-10-10 02:46:56.000000",
            location="la oficina",
            description="junta importante"
        ), follow_redirects=True)
        self.assertEquals(r.status_code, 200)
        assert "cita" in r.data
        assert "Evento" not in r.data

    def testEditAppoitnmentNotExist(self):
        r = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'), follow_redirects=True)
        r = self.appt.get('/appointments/0/edit/')
        self.assertEquals(r.status_code, 404)
        assert "Not Found" in r.data

    def testCreateAppoitnment(self):
        r = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'), follow_redirects=True)
        r = self.appt.get('/appointments/create/')
        self.assertEquals(r.status_code, 200)
        assert "Add Appointment" in r.data
        assert "Edit Appointment" not in r.data
        r = self.appt.post('/appointments/create/', data=dict(
            title="Nuevo",
            start="2014-10-11 03:32:40",
            end="2014-10-12 14:30:27",
            location="lugar",
            description="alguna cosa"
        ), follow_redirects=True)
        self.assertEquals(r.status_code, 200)
        assert "Nuevo" in r.data

    def test_appoitnment_delete(self):
        response = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'), follow_redirects=True)
        response = self.appt.get('/appointments/6/delete/')
        self.assertEquals(response.status_code, 405)
        assert "Not Allowed" in response.data

    def test_index(self):
        response = self.appt.post('/login/', data=dict(
            username='moon.prinsses@hotmail.com',
            password='mayra'), follow_redirects=True)

        response = self.appt.get('/')
        self.assertEquals(response.status_code, 200)
        assert " " in response.data


if __name__ == '__main__':
    unittest.main()
