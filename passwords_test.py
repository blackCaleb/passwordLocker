import unittest
from passwords import Password

class PasswordTest(unittest.TestCase):
    def tearDown(self):
        '''
        Specifies may array of password
        '''
        password.usr_password = []
    
    def setUp(self):
        '''
        this test runs before all the other tests
        '''
        self.new_password = Password('hero', 'maze23')

    def test_init(self):
        '''
        this checks if passwords are initiallized properly
        '''
        self.assertEqual(self.new_password.ppage, 'hero')
        self.assertEqual(self.new_password.ppage'maze23')

    def test_save_ppage(self):
        '''
        this checks if the object is saved properly
        '''
        self.new_password.save_ppage()
        self.asserEqual(len(self.new_passwords), 1)

    def test_save_multiple_passwords(self):
        '''
        This checks if the object is saved
        '''
         self.new_password.save_ppage()
         test_pass = Password('Hero', 'maze23')
         test_pass.save_ppage()
         self.assertEqual(len(Password.usr_password),2)

    def test_delete_passwords(self):
        '''
        this checks if account can be deleted
        '''
        self.new_password.save_ppage()
        test_pass = Password('Hero', 'maze23')
        test_pass.save_ppage()
        self.new_password.delete_ppage()
        self.assertEqual(len(Password.usr_password),1)

    def test_display_passwords(self):
        '''
        this checks if display function works properly
        '''
        self.new_password.save_ppage()
        test_pass = Password('Hero', 'maze23')
        test_pass.save_ppage()
        self.assertEqual(Password.display_ppage(), test_pass.display_ppage()
        Password.usr_password)

    def  test_find_password_(self):
        '''
        This finds a password that has been saved
        '''
        self.new_password.save_ppage()
        test_pass = Password('Hero', 'maze23')
        test_pass.save_ppage()
        found_password = Password.find_by_ppage('hero')
        self.assertEqual(found_password, test_pass.ppage)

    def test_password_exists(self):
        '''
        returns true/false if the password exists
        '''
        self.new_password.save_ppage()
        test_pass = Password('Hero', 'maze23')
        test_pass.save_ppage()
        password_exist = Password.password_exists('hero')
        self.assertTrue(password_exist)


if __name__ == '__main__':
    unittest.main()




