import os, paramiko
c = paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('84.200.33.70', username='root', password=os.environ['SSH_PASS'], timeout=15)
f = '/etc/nginx/sites-enabled/memstroy'
def run(cmd):
    i, o, e = c.exec_command(cmd, timeout=60); r = o.read().decode(); er = e.read().decode(); print(r + er); return r
run(f'cp {f} /root/memstroy.nginx.bak_before_lera')
sf = c.open_sftp(); old = sf.open(f).read().decode()
start = old.index('    location / {'); end = old.index('    listen 443 ssl;')
new = old[:start] + '''    root /var/www/lera;
    index index.html;
    charset utf-8;
    location / {
        try_files $uri $uri/ $uri.html =404;
    }
    location /img/ { expires 30d; }

''' + old[end:]
sf.open(f, 'w').write(new.encode())
run('nginx -t && systemctl reload nginx && echo RELOADED || (cp /root/memstroy.nginx.bak_before_lera ' + f + ' && echo ROLLED_BACK)')
