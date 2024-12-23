import os
import shutil

def copy_static_files(source, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(dest, item)
        print(f"Copying {s} to {d}")
        if os.path.isfile(s):
            shutil.copy(s, d)
        else:
            copy_static_files(s, d)