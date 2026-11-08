import os, paramiko
c = paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect('84.200.33.70', username='root', password=os.environ['SSH_PASS'], timeout=15)
def run(cmd, t=180):
    i, o, e = c.exec_command(cmd, timeout=t); r = o.read().decode(); er = e.read().decode(); print(r + er); return r
conf = '''server {
    listen 80;
    server_name prokoolitus.net www.prokoolitus.net;
    root /var/www/lera;
    index index.html;
    charset utf-8;
    location / { try_files $uri $uri/ $uri.html =404; }
    location /img/ { expires 30d; }
}
'''
sf = c.open_sftp(); sf.open('/etc/nginx/sites-available/prokoolitus', 'w').write(conf.encode())
run('ln -sf /etc/nginx/sites-available/prokoolitus /etc/nginx/sites-enabled/prokoolitus && nginx -t 2>&1 | tail -2 && systemctl reload nginx && echo RELOADED')
run('certbot --nginx -d prokoolitus.net -d www.prokoolitus.net --non-interactive --agree-tos --register-unsafely-without-email --redirect 2>&1 | tail -12')
run('nginx -t 2>&1 | tail -1')
