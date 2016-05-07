import subprocess

output = subprocess.check_output(["git", "log", "--name-only"])

print output
