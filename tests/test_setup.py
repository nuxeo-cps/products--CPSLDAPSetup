import unittest

from Products.CPSDefault.tests.CPSTestCase import CPSTestCase
from layer import CPSLDAPSetupLayer
from layer import CPSLDAPSetupGroupLayer
from layer import CPSLDAPSetupReadonlyLayer

class SetupTestCase(CPSTestCase):
    
    layer = CPSLDAPSetupLayer

    def test_layer(self):
        # test that the layer has been loaded
        self.assertEquals(self.portal.portal_directories.members.meta_type,
                          'CPS Meta Directory')

class SetupGroupTestCase(CPSTestCase):
    
    layer = CPSLDAPSetupGroupLayer

    def test_layer(self):
        # test that the layer has been loaded
        self.assertEquals(self.portal.portal_directories.members.meta_type,
                          'CPS Meta Directory')

class SetupGroupTestCase(CPSTestCase):
    
    layer = CPSLDAPSetupGroupLayer

    def test_layer(self):
        # test that the layer has been loaded
        self.assertEquals(self.portal.portal_directories.members.meta_type,
                          'CPS Meta Directory')

class SetupReadonlyTestCase(CPSTestCase):
    
    layer = CPSLDAPSetupReadonlyLayer

    def test_layer(self):
        # test that the layer has been loaded
        self.assertEquals(self.portal.portal_directories.members.meta_type,
                          'CPS Meta Directory')

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SetupTestCase))
    suite.addTest(unittest.makeSuite(SetupGroupTestCase))
    suite.addTest(unittest.makeSuite(SetupReadonlyTestCase))
    return suite

if __name__ == '__main__':
    framework(descriptions=1, verbosity=2)
