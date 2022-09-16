import cgi

forms= cgi.FieldStorage()
item =  form.getvalue('name')
email =  form.getvalue('email')
message =  form.getvalue('message')

print (item)
print(email)
print(message)