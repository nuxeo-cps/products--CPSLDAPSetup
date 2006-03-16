import unittest

from Products.CPSDefault.tests.CPSTestCase import CPSTestCase
from layer import CPSLDAPSetupLayer

class SetupTestCase(CPSTestCase):
    
    layer = CPSLDAPSetupLayer

    def test_layer(self):
        # test that the layer has been loaded
        self.assertEquals(self.portal.portal_directories.members.meta_type,
                          'CPS Meta Directory')

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SetupTestCase))
    return suite

if __name__ == '__main__':
    framework(descriptions=1, verbosity=2)
