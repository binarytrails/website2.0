from django.test import TestCase
from frontend.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            nick="foobar-founder",
            name="Foo",
            lastname="Bar",
            email="foobar@email.com"
        )

    def test_user_was_created(self):
        user = User.objects.get(nick="foobar-founder")
        
        self.assertEqual(user.nick, "foobar-founder")
        self.assertEqual(user.name, "Foo")
        self.assertEqual(user.lastname, "Bar")
        self.assertEqual(user.email, "foobar@email.com")

