import sys, os, paramiko
c = paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('84.200.33.70', username=os.environ.get('SSH_USER','root'), password=os.environ['SSH_PASS'], timeout=15)
i,o,e = c.exec_command(sys.argv[1], timeout=60)
sys.stdout.write(o.read().decode('utf-8','replace')); sys.stderr.write(e.read().decode('utf-8','replace'))
