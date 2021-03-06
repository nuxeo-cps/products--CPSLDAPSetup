# (C) Copyright 2005-2007 Nuxeo SAS <http://nuxeo.com>
# Authors:
# Julien Anguenot <ja@nuxeo.com>
# Olivier Grisel <og@nuxeo.com>
# M.-A. Darche <madarche@nuxeo.com>
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
"""Helper for LDAP configuration using CPSUserFolder.
"""

from logging import getLogger

from Products.CMFCore.DirectoryView import registerDirectory
from Products.GenericSetup import profile_registry
from Products.GenericSetup import EXTENSION

from Products.CPSCore.interfaces import ICPSSite

logger = getLogger('CPSLDAPSetup')

imports_ok = True
try:
    import ldap
except ImportError, err:
    logger.info(
        "The python-ldap library isn't installed or has problems %s"
        "The CPSLDAPSetup profiles won't be available." % str(err))
    imports_ok = False

if imports_ok:
    registerDirectory('skins', globals())

    def initialize(registrar):
        """CPSLDAPSetup registrations. """

        # Extension profile registration
        profile_registry.registerProfile(
            'default',
            'CPS LDAP Setup (members in LDAP, groups and roles in ZODB)',
            "Sample LDAP Setup for Nuxeo CPS",
            'profiles/default',
            'CPSLDAPSetup',
            EXTENSION,
            for_=ICPSSite)

        profile_registry.registerProfile(
            'readonly_ldap',
            'CPS LDAP Setup (extension to use LDAP in read only mode)',
            "Extension to default to use LDAP in read only mode",
            'profiles/readonly_ldap',
            'CPSLDAPSetup',
            EXTENSION,
            for_=ICPSSite)

        profile_registry.registerProfile(
            'classical',
            "CPS LDAP Setup (members and groups in LDAP, roles in ZODB)",
            "Extension to plug to classical LDAP directories",
            'profiles/classical',
            'CPSLDAPSetup',
            EXTENSION,
            for_=ICPSSite)


