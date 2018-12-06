import time

state = int(time.time())
def rand():
    global state
    state = (1103515245 * state + 12345) & 0xffffFFFF
    return (state >> 16) & 0x7FFF

print state
print "gen = [",
for i in range(10):
    print str(rand() % 100) + ",",
print "]"
