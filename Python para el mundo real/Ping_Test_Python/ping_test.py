# Python for Engineers - Ping Test Application

# We use subprocess Library to run external commands in Python
import subprocess

alive_ping = []
dead_ping = []

# Let's read the original file
my_file = open('ip_add.txt', 'r')
read_file = my_file.read().split('\n')
print(read_file)
# print(read_file)

# Using subprocess + call method to perform a ping test
for i in read_file:
    ping_ip = subprocess.call('ping {} -n 5'.format(i))

    if (ping_ip == 0):
        alive_ping.append(i)

    else:
        dead_ping.append(i)

print(alive_ping)
print(dead_ping)

# Generating text files with the information
alive_file = open('alive.txt', 'w')
for item in alive_ping:
    alive_file.write(item + '\n')

dead_file = open('dead.txt', 'w')
for j in dead_ping:
    dead_file.write(j + '\n')

my_file.close()
alive_file.close()
dead_file.close()
