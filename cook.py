"""Cook assistant (Abikokk / Помощник повара) course pages. Source: Abikokk.pdf from the client."""

def li(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def olist(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'

COOK = {
 'ru': dict(title='Помощник повара', cta='Записаться', rows=[
  ('Группа учебной программы', 'Питание'),
  ('Объём программы', '200 ак. часов (80 ак. ч. теории, 100 ак. ч. практики, 20 ак. ч. самостоятельной работы, не входят в общие часы курса)'),
  ('Даты начала курсов', '16.11.2026 – 28.01.2027'), ('С возможностью трудоустройства', ''),
  ('Место проведения', 'Iva 12, Tallinn / Online Zoom'), ('Стоимость курса', '2400 €'), ('Язык обучения', 'Русский'),
  ('Основа составления программы', 'Профессиональные компетенции помощника повара 3-го уровня B.2.1 – B.2.5 и B.2.6 (сквозные компетенции). Обозначение профессионального стандарта в реестре: 04-18052017-3.7.1/3k')],
  sections=[
   ('Учебная среда', 'Учебный центр организует курсы в учебных помещениях, отвечающих требованиям гигиены и безопасности труда в соответствии с «Законом о гигиене и безопасности труда». Помещения оснащены современной презентационной техникой, а также столами и стульями, подходящими для взрослых. В учебном центре есть необходимая техника для обучения. Выдаются рабочие инструменты, аппаратура и специальная одежда. Для каждого курса изготавливается раздаточный материал, выдаётся в бумажном виде, у каждого учащегося есть доступ в интернет. Вне зависимости от длительности учебного дня каждому участнику обеспечен перерыв на чай или кофе.'),
   ('Целевая группа', 'Обучение подходит тем, кто хочет получить знания и навыки для работы помощником повара.'),
   ('Цель обучения', 'Дать учащимся возможность приобрести знания, навыки и подходы к работе в организациях и компаниях, предоставляющих услуги размещения и питания, а также создать условия для продолжения обучения в течение всей жизни. Обучение включает продуманную теоретическую программу и значительное количество практических занятий.')],
  prog_h='Программа курса',
  prog=['Пищевая гигиена — 6 ак.ч.', 'Оборудование и инвентарь кухни — 6 ак.ч.', 'Техника безопасности при работе на кухне — 6 ак.ч.',
        'Организация безопасной и эффективной работы помощника повара на кухне — 4 ак.ч.', 'Большая кухня и специфика работы на большой кухне — 4 ак.ч.',
        'Кухня ресторана и специфика работы — 4 ак.ч.', 'Здоровое питание, сбалансированность пищи. Качество питания — 4 ак.ч.',
        'Пища как товар: упаковка, срок реализации, хранение. Классификация — 5 ак.ч.', 'Уборка и чистка — 8 ак.ч.',
        'Сырьё, продукты, полуфабрикаты и особенности их использования — 6 ак.ч.', 'Приёмы тепловой обработки — 5 ак.ч.',
        'Методы и приёмы приготовления и подачи блюд и гигиена пищи — 6 ак.ч.', 'Особенности национального меню Эстонии и работы в команде большой кухни — 4 ак.ч.',
        'Понятие технологических карт, умение ими пользоваться — 6 ак.ч.', 'Первичная обработка овощей и грибов — 2 ак.ч.', 'Виды и правила нарезки — 2 ак.ч.',
        'Первичная обработка рыбы — 2 ак.ч.', 'Первичная обработка мяса и птицы — 2 ак.ч.', 'Соусы — 4 ак.ч.', 'Практическая работа помощника повара в ресторане — 100 ак.ч.'],
  total='Всего часов: 180', res_h='В результате обучения учащийся',
  res=['обслуживает предприятия общественного питания, придерживается принципов обслуживания клиентов и специфики большой кухни или ресторана;',
       'соответствует требованиям охраны труда, экологической безопасности и гигиены;',
       'работает самостоятельно, качественно, безопасно и ресурсоэффективно на большой кухне или в ресторане, исходя из этики кулинарии;',
       'рационально организует свою работу, анализирует, оценивает и улучшает свою работу и работу в команде;',
       'ценит своё профессиональное развитие и дальнейшее обучение в сфере обслуживания.'],
  tail=[
   ('Практика', 'Практика направлена на развитие, расширение и применение знаний и навыков, полученных в ходе теоретического обучения, в практической рабочей среде, а также на развитие социальных навыков, личностных качеств и установок, повышающих готовность к будущей работе. Предоставляем каждому ученику практику в лучших ресторанах Таллина.'),
   ('Учебные материалы', 'Конспекты преподавателей, презентационные слайды, учебные пособия, видеоматериалы, кулинарные телепрограммы.'),
   ('Требования к началу обучения', li(['Заявление', 'Документ, удостоверяющий личность'])),
   ('Требования к окончанию и выдаваемые документы', 'Если ученик выполняет учебную программу на 75% и сдаёт зачёт по теории и практике на 75%, выдаётся свидетельство об окончании курса, в противном случае — справка. Справка выдаётся в соответствии с количеством часов участия в занятиях.'),
   ('Квалификация преподавателей', '<p><b>Наталья Бондаренко</b> — андрагог 6 категории; Таллиннский торговый техникум с отличием (1986), специальность «Технология приготовления пищи»; Таллиннский технический университет (1993), «Пищевые технологии», специальная педагогика IV категории; Таллиннский университет (2012). Общий стаж 30 лет, преподавательский — 20 лет.</p><p><b>Роман Сокальский</b> — повар, окончил Teko в 2007; бренд-шеф в группе Meriton: Mademoiselle Café, Trofe restoran, Enzo restoran; открыл 22 Resto, Horg gastro peatus; шеф-повар и совладелец Kalamaja Gastro; 3 место в Эстонии в конкурсе «Aasta kokk»; с 2014 года в ассоциации шеф-поваров Эстонии; 2015 — гран-при конкурса «Балтийская звезда».</p>')]),
 'et': dict(title='Abikokk', cta='Registreeru', rows=[
  ('Õppekava rühm', 'Toitumine'),
  ('Õppekava maht', '200 ak. tundi (80 ak. tundi teooria, 100 ak. tundi praktika, 20 ak. tundi iseseisvat tööd, ei kuulu kursuse kogu tundide hulka)'),
  ('Koolituse toimumise ajad', '16.11.2026 – 28.01.2027'), ('Töölevõtuvõimalusega', ''),
  ('Läbiviimise asukoht', 'Iva 12, Tallinn / Online Zoom'), ('Kursuse maksumus', '2400 €'), ('Õppekeel', 'Vene keel'),
  ('Õppekava koostamise alus', '3. taseme abikoka kutsekompetentsid B.2.1 – B.2.5 ja B.2.6 (läbivad kompetentsid). Kutsestandardi tähis kutseregistris: 04-18052017-3.7.1/3k')],
  sections=[
   ('Õppekeskkond', 'Koolituskeskus korraldab kursusi klassiruumides, mis vastavad töötervishoiu ja tööohutuse nõuetele vastavalt töötervishoiu ja tööohutuse seadusele. Klassiruumid on varustatud kaasaegse esitlustehnikaga, samuti täiskasvanutele sobivate laudade ja toolidega. Koolituskeskuses on olemas koolituseks vajalik varustus. Töövahendid, seadmed ja eririided on olemas. Iga kursuse jaoks on ette valmistatud paberkandjal jaotusmaterjalid ning igal õpilasel on internetiühendus. Olenemata koolipäeva pikkusest pakub koolituskeskus igale kursusel osalejale tee- või kohvipausi.'),
   ('Sihtgrupp', 'Abikoka koolitus sobib neile, kes soovivad omandada koka abilise tööks vajalikud teadmised ja oskused.'),
   ('Koolituse eesmärk', 'Võimaldada õppijatel omandada teadmisi, oskusi ja lähenemisviise töötamiseks majutus- ja toitlustusteenuseid pakkuvates organisatsioonides ja ettevõtetes ning luua tingimused täiendõppeks ja elukestvaks õppeks. Koolitus hõlmab läbimõeldud teoreetilist programmi ja märkimisväärsel hulgal praktilist koolitust.')],
  prog_h='Kursuse programm',
  prog=['Toiduhügieen — 6 akadeemilist tundi', 'Köögiseadmed ja -tarbed — 6 akadeemilist tundi', 'Köögiohutus — 6 akadeemilist tundi',
        'Köögiabilise ohutu ja tõhusa töö korraldamine — 4 akadeemilist tundi', 'Suurköögid ja suurköökides töötamise eripärad — 4 akadeemilist tundi',
        'Restoraniköögid ja nende töö eripärad — 4 akadeemilist tundi', 'Tervislik toitumine, tasakaalustatud toit. Toitumisalane kvaliteet — 4 akadeemilist tundi',
        'Toit kui kaup: pakendamine, säilivusaeg, ladustamine. Klassifikatsioon — 5 akadeemilist tundi', 'Puhastamine ja sanitaartingimused — 8 akadeemilist tundi',
        'Toorained, tooted, pooltooted ja nende kasutamine — 6 akadeemilist tundi', 'Kuumtöötlustehnikad — 5 akadeemilist tundi',
        'Toidu valmistamise ja serveerimise meetodid ja võtted ning toiduhügieen — 6 akadeemilist tundi',
        'Eesti rahvamenüü tunnused ja töötamine suurköögimeeskonnas — 4 akadeemilist tundi', 'Protsessiskeemide mõiste ja nende kasutamine — 6 akadeemilist tundi',
        'Esmane töötlemine: köögiviljad ja seened — 2 akadeemilist tundi', 'Viilutamise liigid ja reeglid — 2 akadeemilist tundi', 'Kala esmane töötlemine — 2 akadeemilist tundi',
        'Liha ja linnuliha esmane töötlemine — 2 akadeemilist tundi', 'Kastmed — 4 akadeemilist tundi', 'Praktiline töö restoranis abikokana — 100 akadeemilist tundi'],
  total='Kokku tunde: 180', res_h='Koolituse tulemusena õppija',
  res=['teenindab toitlustusasutusi, järgib klienditeeninduse põhimõtteid ja suurköögi või restorani eripärasid;',
       'järgib töötervishoiu ja tööohutuse, keskkonnaohutuse ja hügieeninõudeid;',
       'töötab iseseisvalt, tõhusalt, ohutult ja ressursitõhusalt suurköögis või restoranis, lähtudes kulinaarsest eetikast;',
       'organiseerib ratsionaalselt oma tööd, analüüsib, hindab ja täiustab oma tööd ja meeskonnatööd suurköögis või restoranis;',
       'väärtustab professionaalset arengut ja täiendõpet teenindussektoris.'],
  tail=[
   ('Praktika', 'Praktika eesmärk on arendada, laiendada ja rakendada teoreetilise koolituse käigus omandatud teadmisi ja oskusi praktilises töökeskkonnas, samuti arendada sotsiaalseid oskusi, isikuomadusi ja hoiakuid, mis parandavad õpilaste valmisolekut tulevaseks tööks. Pakume igale õppijale praktikavõimalusi Tallinna parimates restoranides.'),
   ('Õppematerjalid', 'Õpetaja märkmed, esitlusslaidid, õppevahendid, videod, telesaated kokandusest.'),
   ('Koolituse alustusnõuded', li(['Avaldus', 'Isikut tõendav dokument'])),
   ('Koolituse läbimise ja väljastatavate dokumentide nõuded', 'Kui õppija läbib õppekava 75% ulatuses ja sooritab testi, väljastatakse tunnistus (kui teooria ja praktilised testid on sooritatud 75% ulatuses); vastasel juhul väljastatakse tõend. Tõend väljastatakse vastavalt tundides osalemise arvule.'),
   ('Õpetaja kvalifikatsioon', '<p><b>Natalja Bondarenko</b> — 6. kategooria andragoog; lõpetas 1986. aastal kiitusega Tallinna Kutseülikooli Tehnikakooli, eriala „Toiduainete tehnoloogia“. 1993. aastal lõpetas Tallinna Tehnikaülikooli, eriala „Toiduainete tehnoloogia“, eripedagoogika IV kategooria. 2012. aastal lõpetas Tallinna Ülikooli. Kogukogemus 30 aastat, õpetamiskogemus 20 aastat.</p><p><b>Roman Sokalsky</b> — eriala kokk, lõpetas Teko 2007; bränd-šeff Meritoni grupis: Mademoiselle Café, Trofe restoran, Enzo restoran; avas 22 Resto, Horg gastro peatus; peakokk ja kaasomanik Kalamaja Gastro; 3. koht Eestis „Aasta kokk“; 2014 liitumine Eesti peakokkade seltsiga; 2015 grand prix konkursil „Baltika täht“.</p>')]),
}

def cook_page(lang):
    d = COOK[lang]; pre = '/et/' if lang == 'et' else '/'
    rows = ''.join((f'<p><strong>{a.upper()}:</strong> {b}</p>' if b else f'<p><strong>{a.upper()}</strong></p>') for a, b in d['rows'])
    secs = ''.join(f'<h3>{a}</h3><p>{b}</p>' for a, b in d['sections'])
    tail = ''.join(f'<h3>{a}</h3>' + (b if b.startswith('<') else f'<p>{b}</p>') for a, b in d['tail'])
    return (f'<div class="wrap narrow article">{rows}{secs}<h3>{d["prog_h"]}</h3>{olist(d["prog"])}<p><strong>{d["total"]}</strong></p>'
            f'<h3>{d["res_h"]}</h3>{li(d["res"])}{tail}<p><a class="btn" href="{pre}kontakt.html">{d["cta"]}</a></p></div>')
