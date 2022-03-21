import hashlib, os, sys
import time





# os.lisdir
# basically --dir
#
# os.stat
#
# os.walk
# generate the filenames in a tree from top down


import hashlib, os, sys

#skip /dev /proc /run  /sys /tmp  /var/lib  /var/run

for root, dirs,files in os.walk("/", topdown=True):
    if (dirs=="/dev" or dirs=="/proc" or dirs=="/run" or dirs=="/sys" or dirs=="/tmp" or dirs=="/var/lib" or dirs=="/var/run"):
        continue

    else:
        with open("Hashes.txt", "w") as f:
            for name in files:
                try:
                    print(os.path.join(root, name))
                    f.write(os.path.join(root, name) + " : ")
                    FileName = (os.path.join(root, name))

                    hasher = hashlib.sha256()
                    with open(str(FileName), 'rb') as afile:
                        buf = afile.read()
                        hasher.update(buf)
                    print(hasher.hexdigest())
                    f.write(hasher.hexdigest() +"\n")
                    f.write(str(time.strftime('%a %H:%M:%S')) + "\n")
                except Exception as e:
                    print(e)


#Sources
#https://stackoverflow.com/questions/42324235/md5-hashing-all-files-in-a-directory
