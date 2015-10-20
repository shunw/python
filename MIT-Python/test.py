import time

start_time = time.time()
name = raw_input('what is your name: ')
end_time = time.time()
total_time = end_time-start_time

print total_time
print 'It took %0.2f to enter your name' % total_time
