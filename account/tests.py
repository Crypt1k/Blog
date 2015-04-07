from django.test import TestCase
from account.forms import RegisterForm


class AccountTests(TestCase):
    def test_blank_register_form(self):
        """
        If form empty, an appropriate message should be displayed.
        """
        form = RegisterForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['This field is required.'],
            'password1': ['This field is required.'],
            'password2': ['This field is required.']
            })

    def test_create_user(self):
        """ User creation test """
        form = RegisterForm({'username': 'Admin',
                             'email': 'admin@gmail.com',
                             'password1': '12345',
                             'password2': '12345'})
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'Admin')
        self.assertEqual(user.email, 'admin@gmail.com')
