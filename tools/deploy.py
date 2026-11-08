import os, sys, paramiko, posixpath
c = paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('84.200.33.70', username='root', password=os.environ['SSH_PASS'], timeout=15)
def run(cmd):
    i,o,e = c.exec_command(cmd, timeout=60); r=o.read().decode(); er=e.read().decode(); print(r+er); return r
run('mkdir -p /var/www/lera')
sf = c.open_sftp(); base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site'); n=0
for d, _, fs in os.walk(base):
    rel = os.path.relpath(d, base).replace(os.sep,'/'); rd = '/var/www/lera' + ('' if rel=='.' else '/'+rel)
    try: sf.mkdir(rd)
    except IOError: pass
    for f in fs: sf.put(os.path.join(d,f), rd+'/'+f); n+=1
print('uploaded', n)
run('chmod -R a+rX /var/www/lera')
