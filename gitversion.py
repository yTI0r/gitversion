import subprocess
import os

def shell_data(command):
    return subprocess.run(command,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    text=True).stdout.strip("\n")
def replace(line:str, new_vals:list):
    for vals in new_vals:
        old, new = vals
        line = line.replace(old, new)

    return line
with open('version.h.inc') as fi, open('version.h','w') as fo:
    os.chdir('..')
    data=[
        ('{git_tag}',shell_data(['git','describe','--tags'])),
        ('{git_count}',shell_data(['git','rev-list','--all','--count'])),
        ('{git_hash}',shell_data(["git", "rev-parse", "--short", "HEAD"]))
    ]
    lines = fi.read()
    fo.write(replace(lines,data))
    