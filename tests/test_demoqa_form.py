import datetime

from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User, UserHobby, UserGender


def test_form_filling(browser_actions):
    registration_page = RegistrationPage()
    tested_user = User(first_name='Nikolai', last_name='Danilov', email='Danilov@gmail.com', gender=UserGender.Male.name,
                       mobile='9270535555', date_of_birth=datetime.date(1991, 6, 25), subjects=['Chemistry', 'Arts'],
                       hobby=UserHobby.Music.name, picture='test_photo.jpg', address='Saratov',
                       state='NCR', city='Delhi')
    registration_page.open()
    registration_page.register(tested_user)
    registration_page.should_have_registered(tested_user)
