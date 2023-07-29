from demoqa_tests.pages.registration_page import RegistrationPage


def test_form_filling(browser_actions):
    registration_page = RegistrationPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Nikolai')
        .fill_last_name('Danilov')
        .fill_email('Danilov@gmail.com')
        .select_gender('Male')
        .fill_mobile('9270535555')
        .fill_date_of_birth('25', '06', '1991')
        .select_subjects(['Chemistry', 'Arts'])
        .select_hobby('Music')
        .upload_picture('test_photo.jpg')
        .fill_address('Saratov')
        .select_state('NCR')
        .select_city('Delhi')
        .submit_data()
    )
    registration_page.should_have_title('Thanks for submitting the form')
    registration_page.modal_should_have_registered_user_info('Nikolai Danilov', 'Danilov@gmail.com', 'Male', '9270535555',
                                                       '25 June,1991', 'Chemistry, Arts', 'Music', 'test_photo.jpg',
                                                       'Saratov', 'NCR Delhi')
    registration_page.close_modal()
