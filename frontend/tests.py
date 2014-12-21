# Copyright (C) 2014 Vsevolod Ivanov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

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

