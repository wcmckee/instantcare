import ic

#ic.createdbtext('newtable')
#ic.createdatabase('default')
#ic.createmsgdatabase('default')
#ic.createtext('testthis', 'imfriend', 'thisdruggo', 'you will live again!')
#ic.pushbutton('newtable', 'william', 15)

#print(ic.readata('newtable'))
#ic.createtext('default', 'william', 'joe', 'this for joesz')
print('button push')
inusr = input('username: ')
holdwn = input('button push: ')

ic.pushbutton('default', inusr, holdwn)


print(ic.readata('default'))

print('leave message')


friendname = input('friend name: ')
inuser = input('username: ')
message = input('message: ')

ic.createtext('default', friendname, inusr, message )

print(ic.readtext())
#ic.pushbutton('default', 'william', 30)
#print(ic.readtext())