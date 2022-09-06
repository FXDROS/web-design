# from django.test import TestCase
# from django.test import TestCase, Client
# from django.apps import apps
# from django.urls import resolve
# from .views import loginUsr, signUp, logoutFunc
# from .apps import AuthenticateConfig

# # Create your tests here.

# class TestingApp(TestCase):
#     def test_app_is_exist(self):
#         self.assertEqual(AuthenticateConfig.name, 'authenticate')
#         self.assertEqual(apps.get_app_config('authenticate').name, 'authenticate')

# class TestRouting(TestCase):
#     def test_authenticate_url_is_exist(self):
#         response = Client().get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_login_url_is_exist(self):
#         response = Client().get('/login/')
#         self.assertEqual(response.status_code, 200)

#     def test_signup_url_is_exist(self):
# 	    response = Client().get('/signup/')
# 	    self.assertEqual(response.status_code, 200)