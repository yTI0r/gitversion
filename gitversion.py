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
    last_git_tag=shell_data(['git','describe','--tags','--abbrev=0','--always'])     
    data=[
        ('{git_tag}',last_git_tag),
        ('{git_count}',shell_data(['git','rev-list',f'{last_git_tag}..HEAD','--count'])),
        ('{git_hash}',shell_data(["git", "rev-parse", "--short", "HEAD"]))
    ]
    lines = fi.read()
    fo.write(replace(lines,data))
    