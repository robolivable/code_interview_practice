
import collections

def drawable(x=None, y=None):
    is_drawable = True
    if x is not None:
        is_drawable &= 100 <= x <= 200
    if y is not None:
        is_drawable &= 100 <= y <= 200
    is_drawable &= x is not None or y is not None
    return is_drawable

def paint(canvas, bound):
    proc_stack = collections.deque([(0,0)])
    #proc_stack = [(0,0)]
    paintable = []
    while proc_stack:
        n = proc_stack.popleft()
        #n = proc_stack.pop()
        if drawable(*n):
            canvas[n[1]][n[0]]['value'] = 1
        canvas[n[1]][n[0]]['visited'] = True
        c1 = (n[0], n[1] - 1)
        c2 = (n[0] - 1, n[1])
        c3 = (n[0] + 1, n[1])
        c4 = (n[0], n[1] + 1)
        if 0 <= c1[0] < bound[0] \
           and 0 <= c1[1] < bound[1] \
           and not canvas[c1[1]][c1[0]]['visited']:
            proc_stack.append(c1)
            canvas[c1[1]][c1[0]]['visited'] = True
        if 0 <= c2[0] < bound[0] \
           and 0 <= c2[1] < bound[1] \
           and not canvas[c2[1]][c2[0]]['visited']:
            proc_stack.append(c2)
            canvas[c2[1]][c2[0]]['visited'] = True
        if 0 <= c3[0] < bound[0] \
           and 0 <= c3[1] < bound[1] \
           and not canvas[c3[1]][c3[0]]['visited']:
            proc_stack.append(c3)
            canvas[c3[1]][c3[0]]['visited'] = True
        if 0 <= c4[0] < bound[0] \
           and 0 <= c4[1] < bound[1] \
           and not canvas[c4[1]][c4[0]]['visited']:
            proc_stack.append(c4)
            canvas[c4[1]][c4[0]]['visited'] = True
    return canvas

DIM = (1900, 1450)

canvas = []
for _ in range(DIM[1]):
    n = []
    for __ in range(DIM[0]):
        n.append({'visited':False, 'value':0})
    canvas.append(n)

print "painting %s canvas" % str(DIM)
import time
t = time.time()
paint(canvas, DIM)
print "painted canvas in %.5f sec" % (time.time() - t)

exit()

for r in canvas:
    s = ''
    for c in r:
        s += str(c['value'])
    print s

