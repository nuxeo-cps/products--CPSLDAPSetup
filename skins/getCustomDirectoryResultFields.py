##parameters=directory_id, default_field=None
"""
Get the list of fields to be displayed in the directory search result list.
"""
#$Id: getCustomDirectoryResultFields.py 13481 2005-04-20 21:54:16Z fguillaume $

if directory_id == 'members':
    fields = [{'id': 'uid', 'title': 'Uid'},
              {'id': 'fullname', 'title': 'label_user_fullname'},
              {'id': 'email', 'title': 'label_email'},
              ]
elif directory_id == 'roles':
    fields = [{'id': 'role', 'title': 'Role'},
              {'id': 'title', 'title': 'label_title'},
              ]
elif directory_id == 'groups':
    fields = [{'id': 'group', 'title': 'label_group'},
              {'id': 'title', 'title': 'label_title'},
              ]
else:
    fields = []

return fields
