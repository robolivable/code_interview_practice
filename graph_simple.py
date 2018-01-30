
import collections

def is_drawable(x=None, y=None):
    is_drawable = True
    if x is not None:
        is_drawable &= 100 <= x <= 200
    if y is not None:
        is_drawable &= 100 <= y <= 200
    is_drawable &= x is not None or y is not None
    return is_drawable

# "local bound"
#def is_edge(coord_a, node_b):
#    if not (0 <= node_b[0][0] - coord_a[0] <= 1) \
#       or not (0 <= node_b[0][1] - coord_a[1] <= 1):
#        return False
#    if node_b[1]['edges'][0] and coord_a == (node_b[0][0], node_b[0][1] - 1):
#        return True
#    if node_b[1]['edges'][1] and coord_a == (node_b[0][0] - 1, node_b[0][1]):
#        return True
#    if node_b[1]['edges'][2] and coord_a == (node_b[0][0] + 1, node_b[0][1]):
#        return True
#    if node_b[1]['edges'][3] and coord_a == (node_b[0][0], node_b[0][1] + 1):
#        return True
#    return False

def paint(canvas, bound):
    proc_stack = collections.deque([(0,0)])
    #proc_stack = [(0,0)]
    paintable = []
    while proc_stack:
        n = proc_stack.popleft()
        #n = proc_stack.pop()
        if is_drawable(*n):
            canvas[n[1]][n[0]]['value'] = 1
        canvas[n[1]][n[0]]['visited'] = True
        # check edges
        c1 = (canvas[n[1]][n[0]]['edges'][0] and (n[0], n[1] - 1)) or None
        c2 = (canvas[n[1]][n[0]]['edges'][1] and (n[0] - 1, n[1])) or None
        c3 = (canvas[n[1]][n[0]]['edges'][2] and (n[0] + 1, n[1])) or None
        c4 = (canvas[n[1]][n[0]]['edges'][3] and (n[0], n[1] + 1)) or None
        if c1 is not None \
           and 0 <= c1[0] < bound[0] \
           and 0 <= c1[1] < bound[1] \
           and not canvas[c1[1]][c1[0]]['visited']:
            proc_stack.append(c1)
            canvas[c1[1]][c1[0]]['visited'] = True
        if c2 is not None \
           and 0 <= c2[0] < bound[0] \
           and 0 <= c2[1] < bound[1] \
           and not canvas[c2[1]][c2[0]]['visited']:
            proc_stack.append(c2)
            canvas[c2[1]][c2[0]]['visited'] = True
        if c3 is not None \
           and 0 <= c3[0] < bound[0] \
           and 0 <= c3[1] < bound[1] \
           and not canvas[c3[1]][c3[0]]['visited']:
            proc_stack.append(c3)
            canvas[c3[1]][c3[0]]['visited'] = True
        if c4 is not None \
           and 0 <= c4[0] < bound[0] \
           and 0 <= c4[1] < bound[1] \
           and not canvas[c4[1]][c4[0]]['visited']:
            proc_stack.append(c4)
            canvas[c4[1]][c4[0]]['visited'] = True
    return canvas

DIM = (300, 300)

canvas = []
for _ in range(DIM[1]):
    n = []
    for __ in range(DIM[0]):
        if _ == 0:
            n.append({'visited':False, 'value':0, 'edges':[True, True, True, True]})
            continue
        n.append({'visited':False, 'value':0, 'edges':[True, False, False, True]})
    canvas.append(n)

print "painting %s canvas" % str(DIM)
import time
t = time.time()
paint(canvas, DIM)
print "painted canvas in %.5f sec" % (time.time() - t)

for r in canvas:
    s = ''
    for c in r:
        s += str(c['value'])
    print s

