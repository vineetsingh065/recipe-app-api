from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

	def test_create_user_with_email_sucessful(self):
		"""Test creating new user with email"""
		email = "test@gmail.com"
		password = "Testpass123"
		user = get_user_model().objects.create_user(
			email=email,
			password=password
			)
		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))


	def test_new_user_email_normalized(self):
		"""test new user normalized"""
		email = "test@GMAIL.COM"
		user = get_user_model().objects.create_user(email, 'test123')

		self.assertEqual(user.email, email.lower())


	def test_new_user_invalid_email(self):
		"""test creating user with no email"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'test123')



	def test_create_new_super_user(self):
		"""test create new su"""
		user = get_user_model().objects.create_superuser(
			'testsuper@gmail.com',
			'test123@'
			)
		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)
