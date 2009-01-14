# Copyright (c) 2006 Nuxeo SAS <http://nuxeo.com>
# Author : Georges Racinet <gracinet@nuxeo.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#

# $Id$

from Testing import ZopeTestCase

from Products.CPSDefault.tests.CPSTestCase import ExtensionProfileLayerClass

# register profiles
ZopeTestCase.installProduct('CPSLDAPSetup')

class CPSLDAPSetupLayerClass(ExtensionProfileLayerClass):
    extension_ids = ('CPSLDAPSetup:default',)

CPSLDAPSetupLayer = CPSLDAPSetupLayerClass(__name__, 'CPSLDAPSetupLayer')

class CPSLDAPSetupGroupLayerClass(ExtensionProfileLayerClass):
    extension_ids = ('CPSLDAPSetup:classical',)

CPSLDAPSetupGroupLayer = CPSLDAPSetupGroupLayerClass(__name__,
                                                     'CPSLDAPSetupGroupLayer')

class CPSLDAPSetupReadonlyLayerClass(ExtensionProfileLayerClass):
    extension_ids = ('CPSLDAPSetup:default',
                     'CPSLDAPSetup:readonly_ldap',)

CPSLDAPSetupReadonlyLayer = CPSLDAPSetupReadonlyLayerClass(
    __name__, 'CPSLDAPSetupReadonlyLayer')
