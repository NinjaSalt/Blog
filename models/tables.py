# coding: utf8
def get_user():
    if auth.user:
        return auth.user.username
    else:
        return 'None'

def get_id():
    user_ids = db().select(db.auth_user.ALL)
    for row in user_ids:
        if row.email == auth.user.email:
            return row.id
    return 'None'

db.define_table('post',
   Field('author', default=get_user()),
   Field('title'),
   Field('post_date', 'datetime', default = request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
   Field('post_content','text'))
