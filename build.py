#!/usr/bin/env python
"""Static site generator for Prokoolitus (RU at /, ET at /et/). Run: python build.py"""
import json, re, html, os, shutil
from cook import COOK, cook_page
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'site')
SRC = json.load(open(os.path.join(ROOT, 'source', 'pages.json'), encoding='utf-8'))
BY_ID = {p['id']: p for p in SRC}

PHONE, PHONE_HREF = '+372 5554 9216', '+37255549216'
EMAIL = 'info@prokoolitus.net'
ADDRESS = 'Iva 12, Tallinn'
COMPANY = 'SVETLO OÜ'
REG = '16844319'
MTR = '261507'

IMG = {  # semantic name -> file prefix
    'hero': '0b6a959378', 'cook': '518c95f835', 'clean': '916360d086', 'care': 'd57194bcbf',
    'about': '6a77d434b7', 'contact': 'e62da5b7ae', 'booking': '9e3be78a2a', 'cook2': '5ee50217ef',
}
def img(name):
    for f in os.listdir(os.path.join(OUT, 'img')):
        if f.startswith(IMG[name]): return 'img/' + f
    raise KeyError(name)

# ---------- html sanitising ----------
KEEP = {'h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'strong', 'b', 'em', 'i', 'br', 'table', 'thead', 'tbody', 'tr', 'td', 'th', 'a'}
class Clean(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.o = []; self.skip = 0
    def handle_starttag(self, t, a):
        if t in ('style', 'script', 'form', 'button', 'svg', 'figure', 'img', 'iframe'): self.skip += 1; return
        if self.skip: return
        if t == 'h1': t = 'h2'
        if t in KEEP:
            if t == 'a':
                h = dict(a).get('href', '')
                self.o.append(f'<a href="{html.escape(h)}">')
            elif t == 'br': self.o.append('<br>')
            else: self.o.append(f'<{t}>')
    def handle_endtag(self, t):
        if t in ('style', 'script', 'form', 'button', 'svg', 'figure', 'iframe'): self.skip = max(0, self.skip - 1); return
        if self.skip: return
        if t == 'h1': t = 'h2'
        if t in KEEP and t != 'br': self.o.append(f'</{t}>')
    def handle_data(self, d):
        if not self.skip: self.o.append(html.escape(d))
def clean(raw):
    c = Clean(); c.feed(raw); s = ''.join(c.o)
    s = re.sub(r'<(p|h[1-4]|li|strong|b|em|i|td|th)>\s*</\1>', '', s)
    s = re.sub(r'\s*\n\s*', '\n', s)
    return s.strip()
def body(pid): return clean(BY_ID[pid]['content']['rendered'])

# ---------- i18n ----------
T = {
 'ru': dict(lang='ru', prefix='', other='et', other_label='Eesti', site='Prokoolitus',
   tagline='Учебный центр для взрослых в Таллине',
   nav=[('index.html', 'Главная'), ('kursy.html', 'Курсы'), ('o-nas.html', 'О нас'), ('usloviya.html', 'Условия обучения'), ('bronirovanie.html', 'Запись'), ('kontakt.html', 'Контакты')],
   cta='Записаться', more='Подробнее', start='Старт', format='Очно в Таллине / онлайн (Zoom)', price='Стоимость', hours='Объём',
   footer_contact='Контакты', footer_reg='Регистрационный код', footer_mtr='Номер экономической деятельности', addr='Адрес', phone='Телефон', mail='E-mail'),
 'et': dict(lang='et', prefix='et/', other='ru', other_label='Русский', site='Prokoolitus',
   tagline='Täiskasvanute koolituskeskus Tallinnas',
   nav=[('index.html', 'Avaleht'), ('kursused.html', 'Kursused'), ('meist.html', 'Meist'), ('koolitustingimused.html', 'Koolitustingimused'), ('registreerimine.html', 'Registreerimine'), ('kontakt.html', 'Kontakt')],
   cta='Registreeru', more='Loe edasi', start='Algus', format='Kohapeal Tallinnas / veebis (Zoom)', price='Hind', hours='Maht',
   footer_contact='Kontakt', footer_reg='Registrikood', footer_mtr='Majandustegevusteate number', addr='Aadress', phone='Telefon', mail='E-post'),
}
# page-name pairs between languages
PAIR = {'index.html': 'index.html', 'kursy.html': 'kursused.html', 'o-nas.html': 'meist.html', 'usloviya.html': 'koolitustingimused.html',
        'bronirovanie.html': 'registreerimine.html', 'kontakt.html': 'kontakt.html',
        'uborka.html': 'puhastusteenindaja.html', 'uhod.html': 'hooldustootaja.html', 'povar.html': 'kokaabi.html'}
PAIR_REV = {v: k for k, v in PAIR.items()}

CSS = open(os.path.join(ROOT, 'style.css'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, 'style.css')) else ''

def page(lang, fname, title, inner, hero=None, desc='', hero_extra=''):
    t = T[lang]
    depth = '../' if lang == 'et' else ''
    other_file = (PAIR.get(fname) if lang == 'ru' else PAIR_REV.get(fname)) or 'index.html'
    other_url = ('/et/' + other_file) if lang == 'ru' else ('/' + other_file)
    other_url = other_url.replace('index.html', '')
    nav = ''.join(f'<a href="{"/" + t["prefix"] + f if f != "index.html" else "/" + t["prefix"]}"{" class=on" if f == fname else ""}>{n}</a>' for f, n in t['nav'])
    hero_html = ''
    if hero:
        hero_html = f'<section class="hero" style="background-image:linear-gradient(rgba(20,40,60,.62),rgba(20,40,60,.62)),url(/{img(hero)})"><div class="wrap"><h1>{title}</h1>{hero_extra}</div></section>'
    else:
        inner = f'<div class="wrap narrow"><h1>{title}</h1></div>' + inner
    return f'''<!doctype html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(re.sub('<[^>]+>', '', title))} — Prokoolitus</title>
<meta name="description" content="{html.escape(desc or t['tagline'])}">
<link rel="alternate" hreflang="{t['other']}" href="{other_url}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"><link rel="stylesheet" href="/style.css"></head><body>
<header><div class="wrap bar"><a class="logo" href="/{t['prefix']}">Prokoolitus<small>{t['tagline']}</small></a>
<input type="checkbox" id="m"><label for="m" class="burger">☰</label>
<nav>{nav}<a class="lang" href="{other_url}">{t['other_label']}</a></nav></div></header>
{hero_html}
<main>{inner}</main>
<footer><div class="wrap cols"><div><b>Prokoolitus</b><br>{COMPANY}<br>{t['footer_reg']}: {REG}<br>{t['footer_mtr']}: {MTR}</div>
<div><b>{t['footer_contact']}</b><br>{t['addr']}: {ADDRESS}<br>{t['phone']}: <a href="tel:{PHONE_HREF}">{PHONE}</a><br>{t['mail']}: <a href="mailto:{EMAIL}">{EMAIL}</a></div></div></footer>
<a class="fab" href="tel:{PHONE_HREF}" aria-label="{PHONE}">📞 <span>{PHONE}</span></a>
</body></html>'''

def write(lang, fname, html_s):
    d = os.path.join(OUT, 'et') if lang == 'et' else OUT
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, fname), 'w', encoding='utf-8').write(html_s)

# ---------- course data ----------
COURSES = {
 'ru': [
  dict(slug='povar.html', name='Помощник повара', img='cook', text='Основы кулинарного дела и работы на профессиональной кухне под руководством опытных поваров.', start='16.11.2026 – 28.01.2027', price='2400 €', hours='200 ак. часов', page=True),
  dict(slug='uborka.html', name='Специалист по уборке', img='clean', text='Современные методы клининга, профессиональная химия и стандарты чистоты для коммерческих и жилых объектов.', start='16.11.2026 – 20.01.2027', price='2300 €', hours='140 ак. часов', page=True),
  dict(slug='uhod.html', name='Работник по уходу', img='care', text='Знания и навыки для профессиональной заботы о пожилых людях и людях с особыми потребностями.', start='16.11.2026 – 09.03.2027', price='2499 €', hours='310 ак. часов', page=True),
 ],
 'et': [
  dict(slug='kokaabi.html', name='Abikokk', img='cook', text='Kokanduse alused ja töö professionaalses köögis kogenud kokkade juhendamisel.', start='16.11.2026 – 28.01.2027', price='2400 €', hours='200 ak. tundi', page=True),
  dict(slug='puhastusteenindaja.html', name='Puhastusteenindaja', img='clean', text='Kaasaegsed koristusmeetodid, professionaalsed puhastusvahendid ja puhtusstandardid.', start='16.11.2026 – 20.01.2027', price='2300 €', hours='140 ak. tundi', page=True),
  dict(slug='hooldustootaja.html', name='Hooldustöötaja', img='care', text='Teadmised ja oskused eakate ja puudega inimeste professionaalseks hooldamiseks.', start='16.11.2026 – 09.03.2027', price='2490 €', hours='355 ak. tundi', page=True),
 ]}

def cards(lang):
    t = T[lang]; out = ['<div class="cards">']
    for c in COURSES[lang]:
        pr = f'<div class="meta"><span>{t["start"]}: {c["start"]}</span>' + (f'<span>{t["price"]}: {c["price"]}</span>' if c['price'] else '') + '</div>'
        link = f'<a class="btn ghost" href="/{t["prefix"]}{c["slug"]}">{t["more"]}</a>' if c['page'] else f'<a class="btn ghost" href="/{t["prefix"]}kontakt.html">{t["cta"]}</a>'
        out.append(f'<article class="card"><img src="/{img(c["img"])}" alt="{c["name"]}" loading="lazy"><div class="pad"><h3>{c["name"]}</h3><p>{c["text"]}</p>{pr}{link}</div></article>')
    out.append('</div>'); return ''.join(out)

def contact_block(lang):
    t = T[lang]
    return f'<ul class="contact"><li><b>{t["addr"]}:</b> {ADDRESS}</li><li><b>{t["phone"]}:</b> <a href="tel:{PHONE_HREF}">{PHONE}</a></li><li><b>{t["mail"]}:</b> <a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>'

# ---------- page texts that were authored by hand ----------
RU = {
 'index': dict(title='Профессиональные курсы для взрослых в Эстонии', hero_text='Получите востребованную профессию и уверенное будущее. Учебный центр Prokoolitus предлагает практическое обучение для взрослых: помощник повара, специалист по уборке, работник по уходу.',
   faq=[('Кто может поступить на курсы?', 'Обучение доступно всем взрослым, желающим получить новую профессию.'), ('Как проходит запись на обучение?', 'Свяжитесь с нами по телефону или e-mail, и мы подтвердим место в группе.'), ('Нужен ли опыт работы?', 'Опыт не требуется — мы обучаем с нуля.'), ('Выдаются ли документы об окончании?', 'Да, по итогам обучения выдаётся официальный документ.'), ('Где проходят занятия?', 'В Таллине, по адресу Iva 12, а также онлайн в Zoom.')],
   steps=[('Выбор курса', 'Ознакомьтесь с нашими направлениями и выберите подходящую программу.'), ('Заявка', 'Свяжитесь с нами, чтобы забронировать место в учебной группе.'), ('Начало занятий', 'Приступайте к обучению под руководством опытных преподавателей.')],
   why='Почему Prokoolitus', whyt='Практика на каждом курсе, преподаватели-практики, помощь в поиске работы. Курсы подходят и людям с особыми потребностями.', stepsh='Как проходит обучение', faqh='Частые вопросы', coursesh='Наши курсы'),
 'o-nas': ('О нас', 'Учебный центр Prokoolitus организует обучение для взрослых и предлагает профессиональные курсы на территории Эстонии. Мы стремимся давать качественное образование по направлениям: помощник повара, специалист по уборке, работник по уходу, няня и опорное лицо — помогая нашим студентам успешно реализоваться в профессии.',
   ['Особое внимание уделяем практической части занятий: в классах преподают только практики.', 'Программы курсов соответствуют стандартам системы образования.', 'Курсы подходят и людям с особыми потребностями.', 'Помогаем с поиском работы после обучения.']),
 'kursy': ('Курсы', 'Профессиональные курсы для взрослых в Эстонии — упор на практические навыки и трудоустройство.'),
 'bronirovanie': ('Запись на курсы', 'Как записаться на профессиональные курсы в Эстонии? Здесь вы найдёте основные сведения о бронировании мест и порядке подачи заявки.',
   [('Какие документы необходимы?', 'Документ, удостоверяющий личность, и заполненная заявка.'), ('Можно ли оплатить обучение частями?', 'Да, мы предлагаем гибкие условия оплаты. Уточняйте у администратора.'), ('Как узнать расписание?', 'Актуальное расписание публикуется на странице каждого курса. Старт ближайших групп — 16.11.2026.'), ('На каком языке проходят курсы?', 'Русский язык обучения.'), ('Выдаётся ли сертификат?', 'Да, по завершении программы выпускники получают документ об освоении профессии.'), ('Помогаете ли вы с трудоустройством?', 'Да, помогаем в поиске работы и готовим к успешному началу карьеры.')]),
 'kontakt': ('Контакты', 'Свяжитесь с учебным центром Prokoolitus для консультации по профессиональным курсам в Эстонии. Напишите или позвоните — мы ответим на все вопросы.'),
}
ET = {
 'index': dict(title='Tere tulemast Prokoolituse kodulehele!', hero_text='Prokoolitus pakub praktilisi ja kvaliteetseid täienduskoolitusi täiskasvanutele. Meie eesmärk on anda õppijatele vajalikud teadmised ja oskused edukaks töötamiseks ning professionaalseks arenguks.',
   faq=[('Kes saab kursustele tulla?', 'Koolitus on avatud kõigile täiskasvanutele, kes soovivad uut elukutset.'), ('Kuidas registreerumine käib?', 'Võta meiega ühendust telefoni või e-posti teel ja kinnitame sulle koha rühmas.'), ('Kas töökogemust on vaja?', 'Ei ole, õpetame algusest peale.'), ('Kas väljastatakse lõpudokument?', 'Jah, koolituse lõpus väljastatakse ametlik dokument.'), ('Kus toimuvad tunnid?', 'Tallinnas, aadressil Iva 12, ning veebis Zoomis.')],
   steps=[('Vali kursus', 'Tutvu meie suundadega ja vali sobiv õppekava.'), ('Registreeru', 'Võta meiega ühendust, et broneerida koht õpperühmas.'), ('Alusta õpinguid', 'Alusta õpinguid kogenud õppejõudude juhendamisel.')],
   why='Miks Prokoolitus', whyt='Praktiline osa igal kursusel, ainult praktikud õpetajad, abi töö leidmisel. Kursused sobivad ka puuetega inimestele.', stepsh='Kuidas õpe toimub', faqh='Korduma kippuvad küsimused', coursesh='Meie kursused'),
 'meist': ('Meist', 'Prokoolituse koolituskeskus korraldab täiskasvanute koolitusi ja pakub kutsekursusi Eestis. Meie eesmärk on anda kvaliteetset haridust kokaabi, puhastusteenindaja, hooldustöötaja, lapsehoidja ja tugiisiku erialadel ning aidata õppijatel oma erialal edukalt toime tulla.',
   ['Pöörame suurt tähelepanu tundide praktilisele osale: klassides õpetavad ainult praktikud.', 'Meie kursuste programmid vastavad haridussüsteemi standarditele.', 'Kursused sobivad ka puuetega inimestele.', 'Aitame pärast koolitust töö leidmisel.']),
 'kursused': ('Kursused', 'Täiskasvanute kutsekursused Eestis — rõhk praktilistel oskustel ja töölesaamisel.'),
 'registreerimine': ('Registreerimine', 'Kuidas kursustele registreeruda? Siin on põhiteave kohtade broneerimise ja avalduse esitamise kohta.',
   [('Milliseid dokumente on vaja?', 'Isikut tõendav dokument ja täidetud avaldus.'), ('Kas õppemaksu saab osade kaupa tasuda?', 'Jah, pakume paindlikke maksetingimusi. Täpsustage administraatorilt.'), ('Kust leian tunniplaani?', 'Ajakava on avaldatud iga kursuse lehel. Lähimate rühmade algus on 16.11.2026.'), ('Mis keeles kursused toimuvad?', 'Õppekeel on vene keel.'), ('Kas väljastatakse tunnistus?', 'Jah, programmi lõpetanud saavad dokumendi eriala omandamise kohta.'), ('Kas aitate töö leidmisel?', 'Jah, aitame tööd leida ja valmistame ette edukaks karjääristardiks.')]),
 'kontakt': ('Kontakt', 'Kas soovid rohkem teada meie koolituste kohta või vajad abi sobiva kursuse valimisel? Võta meiega ühendust — vastame hea meelega kõigile küsimustele!'),
}

def faq_html(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'

def contact_form(lang):
    labels = dict(ru=('Имя', 'E-mail', 'Телефон', 'Сообщение', 'Отправить'), et=('Nimi', 'E-post', 'Telefon', 'Sõnum', 'Saada'))[lang]
    return f'''<form class="form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
<label>{labels[0]}*<input name="name" required></label><label>{labels[1]}*<input type="email" name="email" required></label>
<label>{labels[2]}<input name="phone"></label><label>{labels[3]}*<textarea name="message" rows="5" required></textarea></label>
<button class="btn" type="submit">{labels[4]}</button></form>'''

def build():
    for lang, X in (('ru', RU), ('et', ET)):
        t = T[lang]; pre = '/' + t['prefix']
        k = lambda n: X[n] if n in X else None
        ix = X['index']
        kl = "kursy.html" if lang == "ru" else "kursused.html"
        facts = dict(ru=[('16.11', 'старт ближайших групп'), ('140–310', 'академических часов практики и теории'), ('Таллин + Zoom', 'очно и онлайн'), ('0', 'опыт не нужен — учим с нуля')],
                     et=[('16.11', 'lähimate rühmade algus'), ('140–355', 'akadeemilist tundi teooriat ja praktikat'), ('Tallinn + Zoom', 'kohapeal ja veebis'), ('0', 'kogemust pole vaja — õpetame algusest')])[lang]
        hero_x = f'<p class="herotext">{ix["hero_text"]}</p><p class="herobtn"><a class="btn" href="{pre}{kl}">{ix["coursesh"]}</a> <a class="btn light" href="{pre}kontakt.html">{t["cta"]}</a></p>'
        hp = '<section class="facts"><div class="wrap grid4">' + ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in facts) + '</div></section>'              f'<section class="wrap"><h2>{ix["coursesh"]}</h2>{cards(lang)}</section>'              f'<section class="why"><div class="wrap narrow"><h2>{ix["why"]}</h2><p class="lead">{ix["whyt"]}</p></div></section>'              f'<section class="steps wrap"><h2>{ix["stepsh"]}</h2><div class="grid3">' + ''.join(f'<div><span>{i + 1}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(ix['steps'])) + '</div></section>'              f'<section class="wrap narrow"><h2>{ix["faqh"]}</h2>{faq_html(ix["faq"])}</section>'              f'<section class="cta"><div class="wrap"><h2>{t["cta"]}</h2><p>{PHONE} · {EMAIL}</p><a class="btn" href="{pre}kontakt.html">{t["cta"]}</a></div></section>'
        write(lang, 'index.html', page(lang, 'index.html', ix['title'], hp, hero='hero', desc=ix['hero_text'], hero_extra=hero_x))

        kn = 'kursy' if lang == 'ru' else 'kursused'
        title, lead = X[kn]
        write(lang, f'{kn}.html', page(lang, f'{kn}.html', title, f'<section class="wrap"><p class="lead narrow">{lead}</p>{cards(lang)}</section>', hero='cook', desc=lead))

        an = 'o-nas' if lang == 'ru' else 'meist'
        title, lead, bullets = X[an]
        write(lang, f'{an}.html', page(lang, f'{an}.html', title, f'<section class="wrap narrow"><p class="lead">{lead}</p><ul class="ticks">' + ''.join(f'<li>{b}</li>' for b in bullets) + '</ul></section>', hero='about', desc=lead))

        bn = 'bronirovanie' if lang == 'ru' else 'registreerimine'
        title, lead, faq = X[bn]
        write(lang, f'{bn}.html', page(lang, f'{bn}.html', title, f'<section class="wrap narrow"><p class="lead">{lead}</p>{faq_html(faq)}<h2>{t["cta"]}</h2>{contact_form(lang)}</section>', hero='booking', desc=lead))

        title, lead = X['kontakt']
        write(lang, 'kontakt.html', page(lang, 'kontakt.html', title, f'<section class="wrap narrow"><p class="lead">{lead}</p>{contact_block(lang)}{contact_form(lang)}</section>', hero='contact', desc=lead))

    # pages converted straight from the WordPress content
    write('ru', 'uborka.html', page('ru', 'uborka.html', 'Специалист по уборке', f'<div class="wrap narrow article">{body(152)}<p><a class="btn" href="/kontakt.html">Записаться</a></p></div>', hero='clean'))
    write('ru', 'uhod.html', page('ru', 'uhod.html', 'Работник по уходу', f'<div class="wrap narrow article">{body(122)}<p><a class="btn" href="/kontakt.html">Записаться</a></p></div>', hero='care'))
    write('ru', 'usloviya.html', page('ru', 'usloviya.html', 'Условия обучения', f'<div class="wrap narrow article">{body(21)}</div>'))
    write('et', 'puhastusteenindaja.html', page('et', 'puhastusteenindaja.html', 'Puhastusteenindaja', f'<div class="wrap narrow article">{body(160)}<p><a class="btn" href="/et/kontakt.html">Registreeru</a></p></div>', hero='clean'))
    write('et', 'hooldustootaja.html', page('et', 'hooldustootaja.html', 'Hooldustöötaja', f'<div class="wrap narrow article">{body(173)}<p><a class="btn" href="/et/kontakt.html">Registreeru</a></p></div>', hero='care'))
    write('et', 'koolitustingimused.html', page('et', 'koolitustingimused.html', 'Koolitustingimused', f'<div class="wrap narrow article">{body(182)}</div>'))
    write('ru', 'povar.html', page('ru', 'povar.html', COOK['ru']['title'], cook_page('ru'), hero='cook'))
    write('et', 'kokaabi.html', page('et', 'kokaabi.html', COOK['et']['title'], cook_page('et'), hero='cook'))
    open(os.path.join(OUT, 'style.css'), 'w', encoding='utf-8').write(CSS)
    print('built', sum(len(f) for _, _, f in os.walk(OUT)), 'files')

if __name__ == '__main__':
    build()
