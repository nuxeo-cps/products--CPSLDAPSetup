# -*- coding: iso-8859-15 -*-
# (C) Copyright 2005 Nuxeo SARL <http://nuxeo.com>
# Authors: Julien Anguenot <ja@nuxeo.com>
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
"""Helper for LDAP configuration using CPSUserFolder
"""

from Products.CMFCore.DirectoryView import registerDirectory
from Products.GenericSetup import profile_registry
from Products.GenericSetup import EXTENSION

from Products.CPSCore.interfaces import ICPSSite


registerDirectory('skins', globals())

def initialize(registrar):
    """CPSUserFolderLDAPSetup registrations. """

    # Extension profile registration
    profile_registry.registerProfile(
        'default',
        'CPS LDAP Setup',
        "Sample LDAP Setup for Nuxeo CPS", 
        'profiles/default',
        'CPSUserFolderLDAPSetup',
        EXTENSION,
        for_=ICPSSite)
