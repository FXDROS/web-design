from django.test import TestCase, Client
from django.apps import apps
from django.urls import resolve
from .views import events, apply
from .models import Events, EventsParticipants, Schedule
from .apps import StoryOneConfig


# Create your tests here.class TestIndex(TestCase):

class TestingApp(TestCase):
    def test_app_is_exist(self):
        self.assertEqual(StoryOneConfig.name, 'story_one')
        self.assertEqual(apps.get_app_config('story_one').name, 'story_one')

class TestRouting(TestCase):
	def test_index_url_is_exist(self):
		response = Client().get('/')
		self.assertEqual(response.status_code, 200)

	def test_profile_url_is_exist(self):
		response = Client().get('/profile/')
		self.assertEqual(response.status_code, 200)

	def test_gallery_url_is_exist(self):
		response = Client().get('/gallery/')
		self.assertEqual(response.status_code, 200)

	def test_index_using_template(self):
		response = Client().get('/')
		self.assertTemplateUsed(response, 'profile.html')

	def test_search_is_exist(self):
		response = Client().get('/books/')
		self.assertEqual(response.status_code, 200)

	def test_data_is_exist(self):
		response = Client().get('/data/?q=anime')
		self.assertEqual(response.status_code, 200)

class TestSchedule(TestCase):
	def test_schedule_using_template(self):
		response = Client().get('/schedule/')
		self.assertEqual(response.status_code, 200)
		
	def setUp(self):
		jadwal = Schedule(subject ="abc")
		jadwal.save()

	def test_add_schedule_url_is_exist(self):
		response = Client().post('/schedule/1/detail', data={'subject':'abc'})
		self.assertEqual(response.status_code, 200)

class TestAddEvent(TestCase):
	def test_add_Event_url_is_exist(self):
		response = Client().get('/events/')
		self.assertEqual(response.status_code, 200)

	def test_add_Event_index_func(self):
		found = resolve('/events/')
		self.assertEqual(found.func, events)

	def test_add_Event_using_template(self):
		response = Client().get('/events/')
		self.assertTemplateUsed(response, 'events.html')

	def test_Event_model_create_new_object(self):
		acara = Events(event ="abc")
		acara.save()
		self.assertEqual(Events.objects.all().count(), 1)

	def test_add_Kegiatanpost(self):
		response = Client().post('/events', {'events' : 'abcd', 'day' : 'abcd','date' : 'abcd','time' : 'abcd','place' : 'abcd'})
		self.assertEqual(response.status_code, 301)

class TestAddMember(TestCase):
	def setUp(self):
		acara = Events(event ="abc")
		acara.save()

	def test_add_Member_url_is_exist(self):
		response = Client().post('/events/apply/1', data={'event':'bambang'})
		self.assertEqual(response.status_code, 302)

	def test_add_Person_POST(self):
		response = Client().post('/events/apply/1', {'name':'abcd', 'email' : 'abcd'})
		self.assertEqual(response.status_code, 302)

class TestModel(TestCase):
	def test_str_model_event(self):
		event = Events.objects.create(event='OHFasilkom', day='Monday', date='07 September 2020', time='08.00', place='Gedung B Fasilkom')
		self.assertEqual(event.__str__(), 'OHFasilkom')

	def test_str_model_member(self):
		event = Events.objects.create(event='OHFasilkom', day='Monday', date='07 September 2020', time='08.00', place='Gedung B Fasilkom')
		member = EventsParticipants.objects.create(name='Bambang', eventName=event)
		self.assertEqual(member.__str__(), 'Bambang')