import cgi, cgitb
import sys

form = cgi.FieldStorage()
searchterm1 =  form.getvalue('Input1')
searchterm2=form.getValue('Input2')

print "hello"
