import os
import sys
paths = [sys.argv[1]]
paths1 = []
paths2 = []
while paths:
    path = paths.pop()
    for filename in os.listdir(path):
<<<<<<< HEAD
        fullname = os.path.join(path,filename)    
=======
        fullname = os.path.join(path, filename)
>>>>>>> upstream/master
        if os.path.isdir(fullname):
            paths.append(fullname)
        else:
            extension = filename.split('.')[-1]
<<<<<<< HEAD
            if extension.lower() in ('png','gif','jpg','jpeg','js','css'):
                paths1.append((filename,fullname))
            if extension.lower() in ('css','js','py','html'):
                paths2.append(fullname)
for filename,fullname in paths1:
    for otherfullname in paths2:
        if open(otherfullname).read().find(filename)>=0:
=======
            if extension.lower() in ('png', 'gif', 'jpg', 'jpeg', 'js', 'css'):
                paths1.append((filename, fullname))
            if extension.lower() in ('css', 'js', 'py', 'html'):
                paths2.append(fullname)
for filename, fullname in paths1:
    for otherfullname in paths2:
        if open(otherfullname).read().find(filename) >= 0:
>>>>>>> upstream/master
            break
    else:
        print fullname
        # os.system('hg rm '+fullname)
        # os.system('rm '+fullname)
