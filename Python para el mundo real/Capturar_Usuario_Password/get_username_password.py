# Extract username and password from a txt file
# format of data:
# ID:type:country:name:password:current_time

f = open("main_data.txt", 'r')
username = open('user.txt', 'w')
password = open('pass.txt', 'w')

for line in f:
    parts = line.split(':')
    name = parts[3]
    single_pass = parts[4]
    username.write(name)
    username.write('\n')
    password.write(single_pass)
    password.write('\n')

f.close()
username.close()
password.close()
