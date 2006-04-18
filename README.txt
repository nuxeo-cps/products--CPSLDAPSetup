============
CPSLDAPSetup
============

:Revision: $Id$

This package provides a sample LDAP configuration in the form of an extension
profile for CPS 3.4.1

The main goal of this product is to provide an example of such a configuration
and ease the setup.

This configuration defines an LDAP server as the main user sources. Groups and
roles are stored within the ZODB. All users registered in the members directory
automatically get the 'Member' role (thanks to a read_process_expr in the
members schema).

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


Installation
------------

 - Install the ``python-ldap``_ module in the PYTHONPATH of your Zope instance.
   You can check if it's correctly installed by typing `import ldap` in a
   python shell.
 - Extract this product within your Products directory.
 - Restart Zope
 - Create a CPS Site. *Do not check* the CPS LDAP Setup profile at this point.
 - If you're trying this on an existing CPS Site, make a backup copy
   of the members directory.
 - Go to portal_setup tool, select the CPS LDAP Setup profile and
   import it.
 - If your LDAP server is read only, may also want to additionally import the
   CPS LDAP Setup Readonly profile (see below for more details on the readonly
   setup).

The ldap_utils/ subfolder provides sample configuration files to setup a test
OpenLDAP server. The default setup works out of the box with these. If you use
it, don't forget to change the passwords.


Structure
---------

The default profile included in this setup changes the default ``members`` ZODB
directory installed by the CPSDefault base profile by the following new compound
structure of directories::

                                members
                                - type:   MetaDirectory
                                - schema: members

                                   |
                 ------------------------------------------
                 |                                        |

         members_stack                            members_cps_fields
         - type:   StackingDirectory              - type:   ZODBDirectory
         - schema: members_ldap                   - schema: members_cps_fields

                 |
       ----------------------------------------------------
       |                                                  |
  members_ldap                                    members_zodb
  - type:   LDAPBackingDirectory                  - type:   ZODBDirectory
  - schema: members_ldap                          - schema: members_ldap

The toplevel meta directory is used to aggregate attributes that are defined in
the inetOrgPerson schema that is used by the left hand side branch whereas the
right hand side branch (a single ZODB directory) is used to store CPS specific
attributes such as ``homeless``, ``last_login_time`` and any user defined fields
that do not fit in the inetOrgPerson branch.

The stacking directory is necessary to plug the LDAPBackingDirectory since the
toplevel directory is not able to perform primary key (uid <-> dn) translation.
The stacking is also useful to define members in the ZODB that are not defined
in the LDAP server.

The groups and roles are not affected by this setup. They remain stored in the 
``groups`` and ``roles`` ZODB directories as defined in the CPSDefault base
profiles.

Cross references between the members / groups and members / roles directories
are implemented as computed fields in the members schema.


Read-only LDAP mode
-------------------

If you want to plug CPS on a readonly LDAP server you should furthermore import
the CPSLDAPSetup "readonly_ldap" extension profile (after having first applied
the CPSLDAPSetup "default" extension profile).

This extension add a dynamic readonly protection to the fields that are stored
in the LDAP server to make it explicit to users they cannot change those values.
CPS specific fields (groups, roles and homeless) can still get changed (by a
Manager) since they do not require LDAP write access.

Furthermore, new members created from CPS are stored in the "members_zodb"
backing instead of "members_ldap".

Tuning
------

 - the members_ldap and the ZODB directories are associated to the
   standard RAM Cache Manager sitting at the top of portal_directories.
 - CPSUserFolder comes with it's own built in cache set to 1s by the
   CPSDefault base profile.

Dependencies
------------

 - CPS >= 3.4.1
   http://www.cps-project.org/
 - _``python-ldap``: http://python-ldap.sf.net
