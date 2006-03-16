Sample utilities for LDAP setup
===============================
$Id$

- sample-users.ldif:
  provides a bunch of ldap entries to test your LDAP setup

- slapd.conf:
  sample OpenLDAP server configuration files that fit the sample-user.ldif setup
  and the sample cps_ldap.conf file

Use the slapadd command line tool to load the ldif configuration to your
OpenLDAP server:

  $ sudo slapadd -d 256 -vc -l sample-users.ldif

You might need to restart your server to take the new tree into account.

To check/export what's in the OpenLDAP server:

  $ sudo slapcat

You can also use graphical LDAP client such luma or ldapbrowser to test the
config of your LDAP server.
