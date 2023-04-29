import unittest

from unittest.loader import makeSuite

#from test_cases.fill_in_a_form import TestFillInaForm
from test_cases.framework import Test
from test_cases.add_new_player import TestAddAPlayer
from test_cases.set_language_polish import TestSetLanguage
from test_cases.to_player_form import TestAddAPlayer
from test_cases.open_players_list import TestOpenPlayersList
from test_cases.log_out import TestLogOut
from test_cases.login_to_the_system import TestLoginPage
from test_cases.find_player import TestFindPlayer

def full_suite():
   test_suite = unittest.TestSuite()
   #test_suite.addTest(makeSuite(TestName))
   test_suite.addTest(makeSuite(TestAddAPlayer))
   test_suite.addTest(makeSuite(TestSetLanguage))
   test_suite.addTest(makeSuite(TestAddAPlayer))
   test_suite.addTest(makeSuite(TestOpenPlayersList))
   test_suite.addTest(makeSuite(TestLogOut))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestFindPlayer))
   test_suite.addTest(makeSuite(Test))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())


