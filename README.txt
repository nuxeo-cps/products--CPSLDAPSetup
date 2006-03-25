$Id$

=======================
CPSLDAPSetup
=======================

This package provides a sample LDAP configuration in the form of an
extension profile for CPS 3.4

The main goal of this product is to provide an example of such a
configuration and ease the setup.

This configuration defines an LDAP server as the main user
sources. Groups and roles are stored within the ZODB.

You may start from this to setup your own configuration.

/!\ WARNING /!\
---------------

By importing the profile on an existing CPS Site running with
the (default) ZODB members directory, **you will lose all existing user
data**. This is because the members directory in its whole has to be
replaced by a different one.


Configuration :
----------------

 - edit the members_ldap.xml file from profiles/default/directories/
 and adjust to parameters according to your own LDAP server
 configuration.

 - Please consult other xml files in profiles/default to get the
   details on how the directories will be setup.

Installation :
--------------

 - Install the `python-ldap` module in the PYTHONPATH of your Zope instance. You
   can check if it's correctly installed by typing `import ldap` in a python
   shell.
 - Extract this product within your Products directory.
 - Restart Zope
 - Create a CPS Site. *Do not check* the CPS LDAP Setup profile at this point.
 - If you're trying this on an existing CPS Site, make a backup copy
   of the members directory.
 - Go to portal_setup tool, select the CPS LDAP Setup profile and
   import it.
 - you'll need to give each member the Member role for her CPS
   login to succeed.

The ldap_utils/ subfolder provides sample configuration files to setup a test
OpenLDAP server. The default setup works out of the box with
these. If you use it, don't forget to change the passwords.

Tuning:
-------

 - the members_ldap directory is associated to the standard RAM Cache
   Manager sitting at the top of portal_directories.
 - CPSUserFolder comes with it's own built in cache set to 1s by the
   CPSDefault base profile.

Dependencies :
---------------

 - CPS >= 3.4.0
   http://www.cps-project.org/
 - python-ldap
   http://python-ldap.sf.net
