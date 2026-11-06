# -*- coding: utf-8 -*-
"""Contingut de les subpàgines (text original de parroquiasarria.net).

Cada entrada: slug -> dict(title, section, body)
  - section: 'parroquia' | 'sagraments' | 'grups' | None
  - body: HTML del contingut principal ('' = la pàgina original no té contingut)
"""

IMG = "https://www.parroquiasarria.net/wp-content/uploads"
NEWSLETTER = ("https://17dd61f7.sibforms.com/serve/MUIFAOMnYilmelZp8FaTNO_YAMkaSoM9nCrZDlMoe1QdyevJKSJYn6ssjYKRhnGmCRH5QIsGBI2ZAi-2va6qEdONZjyFUqxFXfK7f7F9CcpB5NRujF_ddRRKNd1-C-xd7p-Ccndc6rzDCYqcEhExdJenceyLcKoLGrfZJpakMhZZRFAPf7jPNU-WJxNgOPGBY2zEGerdLk2TDH4v")

PAGES = {}

# ------------------------------------------------------------------ PARRÒQUIA
PAGES["parroquia"] = dict(title="Parròquia", section=None, index="parroquia", body="")

PAGES["benvingut"] = dict(title="Benvingut", section="parroquia", body=f"""
<figure class="wide"><img src="{IMG}/2016/06/header.jpg" alt="parròquia de Sant Vicenç de Sarrià"></figure>
<p class="lead">Amic que ens visites:</p>
<p><strong>Siguis qui siguis, estem contents d’acollir­te.</strong><br>
Et trobes a la Parròquia de Sant Vicenç de Sarrià. Aquesta església és el testimoni que les generacions precedents ens han deixat. Testimoni de la seva fe en Déu, aquí elles han ofert les seves joies i les seves penes, aquí elles han celebrat la presència de Jesucrist. Respecta­la!</p>
<p>Aquesta església continua essent el lloc de recolliment, el lloc de pregària, el lloc en el qual s’aplega per a l’Eucaristia i els altres sagraments la comunitat cristiana d’avui.</p>
<blockquote><p>No destorbis el silenci. No alteris el seu sentit. No pertorbis el seu ordre!</p></blockquote>
<p>Amb els teus ulls i el teu cor, esguarda la bellesa del treball dels homes, cerca la presència discreta de Déu i deixa que Crist et parli.</p>
<hr>
<div class="center"><img src="{IMG}/2016/06/logo-sat-vicens-sarria.jpg" alt="logo-sat-vicens-sarria" style="max-width:220px"></div>
""")

PAGES["historia-i-art"] = dict(title="Història i Art", section="parroquia", body=f"""
<p class="lead">La <strong>Parròquia de Sant Vicenç de Sarrià</strong> és molt antiga.</p>
<p>El primer testimoni escrit on apareix el nom de Sarrià (<strong><em>Sirriano</em></strong>) és de l’<strong>any 987</strong>. Es tracta d’un testament sacramental d’un tal Muç, que tenia una peça de terra a Sarrià, al costat de Sant Vicenç. Cal recordar que l’any 975 Almansor va fer una gran ràtzia per Catalunya i els testimonis escrits anteriors es van perdre o es van cremar. Així, doncs, Sant Vicenç de Sarrià és parròquia mil·lenària. Ho vàrem celebrar tot al llarg de 1987, amb actes diversos.</p>
<figure class="wide"><img src="{IMG}/2016/06/INTERIOR.jpg" alt="Interior del temple, vist des del cor."><figcaption>Interior del temple, vist des del cor.</figcaption></figure>
<p>Sarrià com a enclavament era una de les moltes <strong>torres de guaita</strong> i de defensa que hi havia pel Barcelonès. Era lloc de pas per anar de Barcelona al Llobregat (Santa Creu d’Olorde, Molins e Rei).</p>
<p>Ens impressiona que al poble de Sarrià, en el mateix lloc on ara s’alça el temple neoclàssic, hi hagués una església romànica, que ja existia al segle X i es va consagrar l’any 1147. Més endavant aquesta petita església romànica dóna lloc a <strong>una edificació més gran, d’estil gòtic</strong>; som a mitjan segle XIV i el monestir de Pedralbes té jurisdicció sobre l’església i el poble de Sarrià.</p>
<p>A l’inici del segle XV l’església ja estava construïda. Aquesta església, per ornar-la interiorment, els sarrianencs varen contractar Jaume Huguet per fer un retaule de Sant Vicenç per a l’altar major. Ha passat molt de temps, però se’n conserven diverses taules que, com a dipòsit de la comunitat parroquial, es conserven al Museu Nacional d’Art de Catalunya (MNAC).</p>
<figure class="float-r"><img src="{IMG}/2016/06/LLOSA.jpg" alt="LLOSA"><figcaption>Llosa commemorativa dels 1000 anys, a la façana de la parròquia.</figcaption></figure>
<p>Al final del segle XVIII els sarrianencs, amb el seu rector al capdavant, convingueren edificar un nou temple i, una vegada demanat el permís, varen procedir a l’execució de l’obra segons el pla , pressupost i condicions de l’<strong>arquitecte Mas.</strong> La consagració del nou temple va tenir lloc el 1789. És d’estil neoclàssic. La façana, de gran simplicitat, presenta al dintell de la porta central l’escut amb la petxina i una fornícula que allotja la imatge del sant patró. A l’interior d’aquest nou temple es va col·locar a l’altar major un retaule barroc, fet exprés per l’artista Nicolau Travé. El foc de l’any 1936 el consumí.<br>
Si fem un recorregut per l’interior del temple veurem, entrant a mà esquerra, la pica baptismal.</p>
<p>El baptisteri conté pintures de Fornells Pla. A un costat hi ha una petita placa per recordar que entre tants i tants sarrianencs batejats aquí, hi rebé el baptisme Dom Gabriel Brasó Tulla (1912-1978), monjo benedictí de Montserrat, d’on fou prior i abat coadjutor, i abat president de Subiaco.</p>
<figure class="float-l"><img src="{IMG}/2016/06/MONTSERRAT.png" alt="MONTSERRAT"><figcaption>Altar de la Mare de Déu de Montserrat.</figcaption></figure>
<p>En aquest mateix costat esquerre, al creuer, hi ha el <strong>retaule del Roser</strong>, obra de l’artista terrassenc Agustí Pujol, que el va finalitzar el 1619. Durant la guerra civil va quedar molt afectat i el 1914 el van reconstruir.</p>
<p>Arribem a l’altar de la Puríssima, obra barroca molt semblant a l’<strong>altar de la Puríssima</strong> de l’església parroquial de Sitges. Les pintures de les parets també són de Fornells Pla. Passem a l’altar major, amb les pintures al fresc de Josep Obiols, fill de Sarrià, que envolten sant Vicenç. Al centre hi ha un baix relleu, obra de l’escultor Rafel Solanic, que representa l’escena dels deixebles d’Emaús. L’altar del Santíssim, a l’altre costat de l’altar major, es va poder conservar.</p>
<p>Al creuer destaca el <strong>retaule de l’antic convent de Santa Clara</strong>, situat on ara hi ha el Parc de la Ciutadella. És obra de l’escultor Andreu Sala. Aquest retaule, abans d’arribar l’any 1961 a la Parròquia de Sant Vicenç de Sarrià, va estar col·locat al Tinell del Palau Reial Major i després va presidir l’altar major de l’església de Sant Jaume, al carrer Ferran.</p>
<p>Seguint avall, trobem l’<strong>altar de la Mare de Déu de Montserrat</strong>, amb pintures d’Adrià Gual, acabades per Lluís Pallarés, deixeble seu.</p>
<figure class="float-r"><img src="{IMG}/2016/06/MURAL.png" alt="MURAL"><figcaption>Altar de la Puríssima.</figcaption></figure>
<p>A continuació reposen, des de fa més de 25 anys, les despulles del beat Pere Tarrés (1905-1950), metge i sacerdot que va morir en olor de santedat l’agost de 1950. El seu apostolat el va fer especialment entre els pobres i la joventut d’aquesta parròquia. Va ser beatificat per Joan Pau II el dia 5 de setembre de 2004 a Loreto.</p>
<p>Finalment trobem l’<strong>altar de Sant Josep.</strong> La imatge d’aquest sant prové del monestir de Pedralbes.</p>
<p>Dos sants han deixat una gran empremta a Sarrià: <strong>sant Vicenç i santa Eulàlia.</strong></p>
<p>El campanar que ens aixopluga a tots, des que és parroquia mil·lenària al vespre resta il·luminat com si fos un far. De fet, és el punt de referència de tots els sarrianencs, orgullosos del nostre poble i de la nostra Parròquia de Sant Vicenç.</p>
<div class="gallery">
  <figure><img src="{IMG}/2016/06/ROSER-179x300.png" alt="Retaule del Roser."><figcaption>Retaule del Roser.</figcaption></figure>
  <figure><img src="{IMG}/2016/06/VICENS-224x300.jpg" alt="Taula del retaule de sant Vicenç, de Jaume Huguet."><figcaption>Taula del retaule de sant Vicenç, de Jaume Huguet.</figcaption></figure>
  <figure><img src="{IMG}/2016/06/PURISSIMA-198x300.png" alt="Mural de Fornells-Pla al baptisteri."><figcaption>Mural de Fornells-Pla al baptisteri.</figcaption></figure>
</div>
<div class="callout"><p><strong>Carmen Sobrevila Masvidal</strong><br><em>Historiadora</em></p></div>
""")

PAGES["sant-vicenc"] = dict(title="Sant Vicenç", section="parroquia", body=f"""
<p class="lead">Sant Vicenç (que vol dir invencible, invicte…) és un màrtir del segle IV. En un temps de persecució religiosa ell no va voler abdicar de la seva fe, no es va deixar “vèncer” per les dificultats i va voler seguir la fe cristiana fins a les darreres conseqüències.</p>
<figure class="float-r"><img src="{IMG}/2016/09/PINTURA-180x300.png" alt="Pintura a l'Altar Major"><figcaption>Pintura a l'Altar Major</figcaption></figure>
<p>La seva mort i de fet la seva vida, encara que no se’n coneix força, són un testimoniatge heroic i un estímul engrescant de servei, comprimís i fidelitat, entrega y generositat.</p>
<p>Sant Vicenç ja apareix als primers martirologis i fins i tot és citat per sants posteriors com Sant Agustí:</p>
<blockquote><p>“Sant Vicenç, vencedor en tot. Va vèncer en les paraules i va vèncer en els turments, va vèncer en la confessió i va vèncer en la tribulació, va vèncer abrasat pel foc i va vèncer a l’ésser llençat a les ones, va vèncer finalment, a l’ésser turmentat i va vèncer al morir per la fe*”.</p></blockquote>
<p>Sant Vicenç neix a Osca, pels volts de final del segle III. De família romana benestant, fins i tot participants en l’alta vida política de la regió, i cristians decidits.</p>
<p>Els cristians en aquell temps eren tolerats, fins i tot alguns ocupaven alts càrrecs, però amb la persecució de Dioclecià (303-311 dC.) tot va acabar.</p>
<p>Abans de la persecució Vicenç va anar a estudiar a Saragosa, allà va conèixer el bisbe sant Valeri, i va destacar en la pietat així com també era un bon estudiant. Dins aquesta vida virtuosa va ser ordenat diaca per mans del bisbe Valeri al seu servei: s’encarregava del més pobres i desafavorits. També va destacar en la predicació: fins i tot el bisbe, que era tartamut, li encomanava que el substituís en el ministeri de la paraula.</p>
<figure class="float-l"><img src="{IMG}/2016/09/LLESA-300x218.png" alt="Detall del frontal de Sant Vicenç a Liesa, Osca."><figcaption>Detall del frontal de Sant Vicenç a Liesa, Osca.</figcaption></figure>
<p>Va arribar, però, la persecució, cada vegada més cruel fins que el bisbe Sant Valeri i el seu diaca Sant Vicenç van ser forçats a abdicar de la seva fe.</p>
<p>En cap moment, però, no es van fer enrere i van haver de patir moltes tortures. Primer de tot es diu que van ser empresonats, i després desterrats cap a València, en un viatge molt dur per tots dos. Arriben d’allò més fatigats; a Sant Valeri, però, se l’enduran cap a França.</p>
<p>Sant Vicenç haurà de patir molts turments fins morir el 22 de gener de l’any 304dC. A les imatges del retaule de la parròquia de Sant Vicenç (al MNAC hi són els originals, a la parròquia unes rèpliques) es pot veure els diferents capítols de la seva tortura, com ara: lligat, azotat, esquinçat per ferros, exposat al foc de la graella…</p>
<p>També, la grossa pedra circular amb la que apareix sovint (com ara a la imatge de la fornícula de l’entrada de l’església; a la imatge de dalt de l’altar major…) té la seva explicació: com que Sant Vicenç no va renegar de la seva fe, al contrari, la podria fer créixer inclús pels voltants, un cop mort i per evitar-ho, els perseguidors van voler que el seu cos fos menjat per les bèsties, però aquestes no hi gosarien; aleshores va ser lligat a una gran pedra (circular com les de molí) i tirat a l’aigua perquè els peixos del fons de l’abisme se’l mengessin. Però la pedra no s’enfonsava i va anar surant fins a una altra vora on d’altres cristians el van trobar i donar sepultura.</p>
<p>Sant Vicenç va despertar una profunda devoció i popularitat, no sols amb les seves referències per escrit sinó també amb les seves relíquies que es van estendre per tot el món cristià conegut d’aleshores.</p>
<p>Sant Vicenç es un fort testimoniatge que perdura fins als nostres dies i, des de la situació que sigui, per moltes dificultats que comporti, ens esperona a seguir ben decidits el Senyor, tal com ell en el seu moment va fer.</p>
<div class="gallery">
  <figure><img src="{IMG}/2016/09/FONICULA-184x300.png" alt="Fonícula de Sant Vicenç a l’atri de la parròquia"><figcaption>Fonícula de Sant Vicenç a l’atri de la parròquia</figcaption></figure>
  <figure><img src="{IMG}/2016/09/DIBUIX-164x300.png" alt="Dibuix del sant (Martí Nuet)"><figcaption>Dibuix del sant (Martí Nuet)</figcaption></figure>
  <figure><img src="{IMG}/2016/09/ALTAR-236x300.png" alt="Escultura del Sant a la parròquia"><figcaption>Escultura del Sant a la parròquia</figcaption></figure>
</div>
<p><small>(* Del llibret “<em>Sant Vicenç, màrtir, el color de la fe</em>”.)</small></p>
""")

PAGES["santa-eulalia"] = dict(title="Santa Eulàlia", section="parroquia", body=f"""
<p class="lead">Santa Eulàlia (<em>que vol dir “de bon parlar”, “que parla bé”</em>) va ser una adolescent que va morir màrtir a començaments del segle IV. Una noia que va deixar petxada en la història del cristianisme.</p>
<figure class="float-r"><img src="{IMG}/2016/06/BREVIARI.png" alt="Miniatura del breviari de Martí d'Aragó - sg.XV"><figcaption>Miniatura del breviari de Martí d'Aragó - sg.XV</figcaption></figure>
<p>En una de les pitjors persecucions cristianes, la del 304dC., decretada per l’emperador romà Dioclecià a tot l’imperi i executada a la península pel jutge Dacià, la reacció de la jove, enlloc de fugir i deixar Barcelona a la seva sort, el que ens deixarà per sempre serà un llegat d’entusiasme i d’entrega a l’amor a Crist i als germans.</p>
<p>Val a dir que aquesta persecució és la mateixa en la que Sant Vicenç va deixar la seva vida, i tants i tants d’altres sants.</p>
<p>Santa Eulàlia era de bona família, vivien a la ciutat de Barcelona d’aleshores. Doncs bé, quan comença la persecució, els pares agafen la noia i fugen cap a les afores, concretament a una vil·la que tenien a Sarrià, i quedar així protegits. Quan les notícies del patiment dels cristians arriben a la zona i ella se n’adona, una nit, innocentment, fuig de casa i s’adreça cap a la ciutat decidida a enfrontar-se amb el jutge per retreure-li el que estava fent.</p>
<p>El jutge romà es resisteix davant la poca edat de la jove, però donada la seva actitud ferma en la defensa del cristianisme acabarà per aplicar-li els càstigs i la mort. Amb tot de tortures i xantatges per què abdiqués de la seva fe, ella, resistint ferma i continuant increpant al jutge, va haver de patir assots, estiraments, ferides fetes amb ferros, desgarraments, cremades… Però mai es va fer enrere sinó ben al contrari, ben alegre de poder sofrir per Jesucrist i compartir la seva Passió.</p>
<p>Santa Eulàlia finalment va morir penjada en una creu en forma d’X (<em>aquesta creu surt en moltes representacions de la santa</em>). La intenció dels botxins és que el seu cos exposat se’l mengessin les aus de presa, per escarment dels cristians, però una forta nevada li va cobrir, i així protegir, el seu cos.</p>
<p>La seva persona és avui dia encara un estímul de fe, esperança i engrescament en el seguiment de Jesús. A destacar, potser, del seu testimoniatge:</p>
<ul>
  <li>la seva solidaritat, que no pot suportar la crueltat desencadenada contra els seus amics cristians i va a fer-los costat</li>
  <li>la seva valentia, tot encarant-se amb el jutge malgrat el destí que això li comportaria</li>
  <li>la seva generositat, perquè no es va estalviar la seva vida tot fugint</li>
  <li>la seva justícia, per reivindicar i defensar la vida i la llibertat de tots</li>
  <li>la seva perseverança, sense fer-se enrere en cap moment tot i els patiments</li>
  <li>la seva esperança, que no dubtà en cap moment en què la victòria sempre acabarà sent la de Crist</li>
  <li>la seva fe i adhesió total i incondicional de seguir a Jesucrist per damunt de totes les coses, inclús de la mateixa vida</li>
  <li>en definitiva, Santa Eulàlia és tot un testimoniatge del poder de la gràcia de Déu que resplendeix tant més fort, quant més feble pot arribar a ser la persona, en aquest cas una jove innocent</li>
</ul>
<p>Avui, les restes de la santa romanen a la Catedral de Barcelona, relíquies guardades en un sepulcre a la cripta sota l’altar major per a la veneració dels fidels.</p>
<p>Després de centenars d’anys, Santa Eulàlia encara desperta la veneració de tants i tants cristians, especialment dels barcelonins (<em>la ciutat dels quals ella n’és patrona</em>), i d’una manera també molt especial dels veïns de Sarrià (<em>la parròquia dels quals ella n’és copatrona juntament amb Sant Vicenç</em>).</p>
<div class="gallery">
  <figure><img src="{IMG}/2016/06/CAPELLA-226x300.png" alt="Sepulcre de Santa Eulàlia"><figcaption>Sepulcre de Santa Eulàlia</figcaption></figure>
  <figure><img src="{IMG}/2016/06/PINTURA-97x300.jpg" alt="Santa Eulàlia, per Martí Nuet."><figcaption>Santa Eulàlia, per Martí Nuet.</figcaption></figure>
  <figure><img src="{IMG}/2016/06/SARCOFAG-300x226.png" alt="Sarcòfag de la Santa a la Catedral de Barcelona"><figcaption>Sarcòfag de la Santa a la Catedral de Barcelona</figcaption></figure>
</div>
<p><small>Del llibret “<em>Santa Eulàlia, una fe jove</em>“.</small></p>
""")

# ------------------------------------------------------------------ SAGRAMENTS
PAGES["sagraments"] = dict(title="Sagraments", section=None, index="sagraments", body="")

PAGES["catecumenat"] = dict(title="Catecumenat", section="sagraments", body="")

PAGES["catecumenat-adults"] = dict(title="Catecumenat Adults", section="sagraments", body="""
<p class="lead">Una persona major d’edat pot demanar la seva incorporació a l’Església i rebre els sagraments de la iniciació cristiana: baptisme, eucaristia i confirmació.</p>
<p>El catecumen (persona que fa aquest procés), això és qui demana fer aquest camí de trobada amb Crist, després d’una primera entrevista, iniciarà aquest itinerari amb diverses etapes formatives i ritus que l’església té previst des d’antic. Rebrà els tres sagraments, incorporant-se així plenament a l’Església, en una sola celebració en la Vetlla Pasqual, la nit en que els cristians celebrem la Resurrecció de Crist i la seva victòria sobre la mort i el pecat.</p>
<p>Si un adult encara no ha rebut el sagrament de la confirmació, tot i estar batejat i haver rebut la primera comunió, també pot integrar-se en un procés catecumenal per a poder ser confirmat.</p>
<div class="callout"><p>Qui desitgi rebre aquests sagraments, pot adreçar-se al despatx parroquial o parlar amb els mossens perquè l’informin del camí concret a seguir.</p></div>
""")

PAGES["baptisme"] = dict(title="Baptisme", section="sagraments", body=f"""
<figure class="float-r"><img src="{IMG}/2016/06/Bautiz4m.jpg" alt="Bautiz4m"></figure>
<p class="lead">Rebre el baptisme suposa néixer a una nova vida, la vida dels fills de Déu. A més de la vida biològica, la vida heretada per la nissaga humana, es neix a la vida divina, la vida heretada per la pasqua del Crist.</p>
<p>En efecte, en el baptisme hom es configura a la mort en la creu de Crist (immersió en l’aigua), i per tant també a la seva resurreció (sorgir d’entre les aigües de la mort). Una vida ara transformada, gloriosa, plena tota ella de l’amor de Déu.</p>
<p>El batejat entra a formar part d’aquesta vida guanyada pel Crist, i des d’ara la seva essència com a cristià serà estimar com Crist va estimar, i com Crist viu eternament en l’amor del Pare i de l’Esperit Sant..</p>
<p>El baptisme suposa l’abolició del pecat original, aquella realitat que ens feia estranys a Déu, que feia que ens mantinguéssim al marge, fora de Déu on som abocats inel·ludiblement a la mort.</p>
<p>Altrament, el baptisme ens dota d’aquella altra realitat que ens fa familiars a Déu, fills, en comunió amb ell. Ara som temples de l’Esperit, on l’Esperit de Déu hi habita amb propietat; cada vegada que estimem com Crist va estimar és l’Esperit que actua en nosaltres.</p>
<figure class="float-l"><img src="{IMG}/2016/06/Bautiz1m.jpg" alt="Bautiz1m"></figure>
<p>Tot i que la tendència a prescindir de Déu romàn, és per això que el batejat ha de vetllar per mantenir aquesta vida divina dins seu amb l’ajut de l’Església, dels seus sagraments i de tots els cristians d’entre els quals ell ara en forma part. En el baptisme es condensa tota la realitat de la salvació, però el nou cristià ha d’estendre a tot el llarg de la seva vida aquest amor de Déu del qual ara ja participa i frueix fins a la vida eterna. .</p>
<hr>
<h3>Dates:</h3>
<div class="callout">
  <p><strong>Tots els Diumenges (dia de la Resurrecció), a les 17’30h.</strong></p>
  <p>En temps <em>pasqual</em> també dins alguna de les misses dominicals</p>
  <p>En temps de <em>quaresma</em> s’exceptua tot bateig</p>
</div>
<h3>Sol·licitud del baptisme:</h3>
<p><strong>Requisits</strong></p>
<ul>
  <li>Omplir i lliurar la sol·licitud en despatx parroquial</li>
  <li>Pertànyer al veïnatge de la parròquia</li>
  <li>Compromís dels pares i padrins en l’educació cristiana del batejat</li>
</ul>
""")

PAGES["eucaristia"] = dict(title="Eucaristia", section="sagraments", body=f"""
<div class="gallery wide">
  <figure><img src="{IMG}/2016/06/EUCARISTIA_2.png" alt=""></figure>
  <figure><img src="{IMG}/2016/06/EUCARISTIA_1.png" alt=""></figure>
</div>
<h2>Horari de Misses</h2>
<p><em>Aquest horari està subjecte a qualsevol canvi oportú</em></p>
<div class="timeline">
  <div><strong>Feiners</strong>8 h (a l’agost és suprimeix), 10h i 20’15 h.</div>
  <div><strong>Dissabtes i Vigílies de festa</strong>19’15h. Dissabtes: amb atenció especial a les families</div>
  <div><strong>Diumenges</strong>8’30h (Capella Siervas de Maria, Clos de Sant Francesc) 10h, 11’30h, 13h i 20’15h.<br>Horari d’estiu: 10h, 11’30h, 13h i 20’15h (juliol – agost)</div>
  <div><strong>Festes</strong>Segons el calendari civil i litúrgic</div>
</div>
<hr>
<h3>Visites al sagrari</h3>
<p>Església oberta:</p>
<ul>
  <li>Laborables: 7’30h – 21h.</li>
  <li>Dissabtes: 7’30h – 14h / 17h – 21h.</li>
  <li>Festius: 8h – 14h / 17h – 21h.</li>
</ul>
<h3>Exposició del santísim</h3>
<p>Horari escolar dilluns a divendres de 8.30 a 20h</p>
<h3>Primeres comunions</h3>
<p><a href="catequesis-infants.html">Servei de catequesi d’infants</a></p>
<h3>Comunió als malalts / viàtic</h3>
<p>Contactar amb els responsables:<br>Mossens de la parròquia</p>
<h3>Misses funerals</h3>
<p>Segons el dia i l’hora.<br>Concretar al despatx parroquial.</p>
<h3>Intencions de les misses</h3>
<p>Segons el dia i l’hora.<br>Concretar al despatx parroquial.</p>
""")

PAGES["confirmacio"] = dict(title="Confirmació", section="sagraments", body=f"""
<div class="gallery wide" style="grid-template-columns:repeat(3,1fr)">
  <figure><img src="{IMG}/2016/06/conf12.jpg" alt=""></figure>
  <figure><img src="{IMG}/2016/06/conf10.jpg" alt=""></figure>
  <figure><img src="{IMG}/2016/06/conf08.jpg" alt=""></figure>
</div>
<h2>El sagrament</h2>
<p>La història de la salvació està tota ella amarada per la promesa de l’Esperit (“Abocaré el meu esperit damunt els teus fills, beneiré els teus plançons.” Is 32, 15. “No els giraré mai més l’esquena, perquè hauré infós el meu esperit al poble d’Israel. Ho dic jo, el Senyor, Déu sobirà.” Ez 39, 29.).</p>
<p>Jesús és el qui posseix en plenitud aquest Esperit (“Aquí teniu el meu servent, que jo sostinc, el meu elegit, en qui m’he complagut. He posat damunt d’ell el meu Esperit…” Is 42,1. “L’Esperit del Senyor, Déu sobirà, reposa sobre meu…” Is 61,1.).</p>
<p>I, per la seva pasqua, vessa sobre nosaltres el seu esperit (“ell ha rebut del Pare l’Esperit Sant promès, i ara l’ha donat amb abundància” Ac 2, 33.). Això esdevé en la Pentecosta (Ac 2, 1-11), i sempre que es celebra aquest sagrament.</p>
<p>El sagrament de la Confirmació suposa la plenitud de l’Esperit que ja és rebut en el Baptisme. És l’enfortiment i la confirmació dels dons de l’Esperit.</p>
<h2>Els dons de l’Esperit Sant</h2>
<div class="gifts">
  <div class="gift"><h3>Ciència</h3><p>L’Esperit Sant que el Pare enviarà en nom meu, us farà recordar tot el que jo us he dit, i us ho farà entendre.</p><cite>Jn 14, 26</cite></div>
  <div class="gift"><h3>Consell</h3><p>Escolta els consells, deixa’t instruir i arribaràs a ser un home assenyat.</p><cite>Pr 19,20</cite></div>
  <div class="gift"><h3>Enteniment</h3><p>Estic ben convençut que esteu plens de bondat, que posseïu un coneixement perfecte i que sou capaços d’instruir-vos els uns als altres.</p><cite>Rm 15, 14</cite></div>
  <div class="gift"><h3>Fortalesa</h3><p>Si tenim Déu amb nosaltres, qui tindrem en contra?</p><cite>Rm 8,31</cite></div>
  <div class="gift"><h3>Pietat</h3><p>Tots els qui són guiats per l’Esperit de Déu són fills de Déu.</p><cite>Rm 8,14</cite></div>
  <div class="gift"><h3>Saviesa</h3><p>Tota saviesa ve del Senyor i és amb ell per sempre.</p><cite>Sir 1,1</cite></div>
  <div class="gift"><h3>Temor de Déu</h3><p>Els ulls del Senyor vetllen els qui el veneren, els qui esperen en l’amor que els té.</p><cite>Sl 33,18</cite></div>
</div>
""")

PAGES["matrimoni"] = dict(title="Matrimoni", section="sagraments", body=f"""
<div class="gallery wide">
  <figure><img src="{IMG}/2016/06/MATRIMONI_2.png" alt=""></figure>
  <figure><img src="{IMG}/2016/06/MATRIMONI_1.png" alt=""></figure>
</div>
<p class="lead">Pel sagrament del matrimoni la grandesa de l’amor entre un home i una dóna va molt més enllà d’un mer pacte, la seva unió esdevé aliança.</p>
<p>Tot amor és imatge de l’amor de Déu, però l’amor esponsal gaudeix d’una peculiaritat: la vocació matrimonial és la crida a fer de l’amor a l’espòs un amor sobrenatural, un amor com el de Déu al seu poble (Antiga Aliança) que mai no l’abandonarà, o com el de Crist a la seva Església (Nova Aliança) el qual sempre hi està present, i d’una manera especial en els sagraments.</p>
<p>Pel sagrament del matrimoni els esposos s’enriqueixen d’un tresor infinit, les capacitats d’estimar-se trenquen les barreres naturals, i s’omplen de la força i de la benedicció de Déu.</p>
<p>Els nuvis volen segellar la seva unió davant l’altar, on Crist es dóna tot ell a nosaltres, perquè volen que la seva entrega sigui imatge de l’entrega total de Crist, volen que la seva unió participi de la dinàmica divina, volen entrar dins el joc d’unió i d’entrega totals de Deú.</p>
<hr>
<h3>HORARI I NORMATIVA CASAMENTS</h3>
<p><a class="dl" href="{IMG}/2016/06/1.PSV_CASAMENTS_NORMATIVA_CATALA_2023.pdf" target="_blank" rel="noopener">1.PSV_CASAMENTS_NORMATIVA_CATALA_2023</a></p>
<ul>
  <li>Tots els dies excepte Diumenges.</li>
  <li>Cal tenir en compte l’horari habitual de les misses.</li>
  <li>Cal tenir en compte 1 hora 1/2 entre l’inici del casament i l’inici d’una altra celebració.</li>
  <li>Per concertar data i tramitar l’expedient matrimonial cal presentar-se al despatx parroquial.</li>
</ul>
<h3>INSCRIPCIONS CURS PREMATRIMONIAL</h3>
<p><a class="dl" href="https://forms.gle/vRdpK3AiFpuYqURs9" target="_blank" rel="noopener">https://forms.gle/vRdpK3AiFpuYqURs9</a></p>
<div class="callout">
  <p><strong>Horari de despatx:</strong> Dilluns, dimecres i divendres, de 17.30 a 20.00 h</p>
  <p><strong>Lloc:</strong> Carrer del Rector Voltà, 5</p>
  <p><strong>Més informació:</strong> <a href="tel:932030907">93 203 09 07</a></p>
</div>
""")

PAGES["uncio-de-malalts"] = dict(title="Unció de malalts", section="sagraments", body="""
<p class="lead">Els sacerdots de la parròquia poden atendre espiritualment als malalts a les seves cases o als hospitals de la zona. Truquin a la parròquia i explica’ns quin tipus d’atenció necessites: sagrada Comunió, Confessió, Unció de Malalts…</p>
<p>Hi ha voluntaris en la parròquia, Pastoral de la Salut,  que poden atendre altres necessitats dels malalts: companyia, realitzar compres o gestions per les quals es vegin impedits.</p>
""")

# ------------------------------------------------------------------ GRUPS
PAGES["grups"] = dict(title="Grups", section=None, index="grups", body="")

PAGES["catequesis-infants"] = dict(title="Catequesis Infants", section="grups", body=f"""
<h2>La Catequesi d’Infants</h2>
<p class="lead">La parròquia ofereix aquest Servei de Catequesi d’Infants per col·laborar amb els pares en la iniciació i la formació cristiana dels seus fills.</p>
<div class="timeline">
  <div><strong>1r any</strong>Curs d’iniciació. Primeres oracions. Coneixement de la persona de Jesús i del seu missatge. Iniciació al Sagrament de la Penitència.</div>
  <div><strong>2n any</strong>Aprofundiment en el coneixement de l’Evangeli, la pregària i la vivència cristiana. Iniciació al Sagrament de la Comunió o Eucaristia.</div>
</div>
<h3>CATEQUESI PARES I MARES</h3>
<p>Un dijous al mes tindrem la reunió catequètica pels pares i mares</p>
<h3>MISSA FAMILIAR</h3>
<p>Cada dissabte a les 19.15h tenim la missa familiar amb atenció amb infants, un cop per més serà amb atenció amb els nens de la catequesi.</p>
<hr>
<h2>El racó del catequista</h2>
<p><strong>El nou catecisme</strong></p>
<p>Ja està aplicant-se el nou Catecisme impulsat per la Conferència Episcopal Espanyola.</p>
<p><a class="dl" href="{IMG}/2016/06/PPT.ppt">PPT</a></p>
<p><strong>Secretariat Interdiocesà de Catequesi (SIC)</strong></p>
<p>Ofereix ajuts per al bon funcionament de la catequesi, com per exemple, les publicacions “<a href="http://www.sic-catequesi.cat/" target="_blank" rel="noopener">Catequesi</a>“, on rebem informació i material.</p>
""")

PAGES["catequesis-confirmacio"] = dict(title="Catequesis Confirmació", section="grups", body="")
PAGES["postconfirmacio"] = dict(title="Postconfirmació", section="grups", body="")

PAGES["cercle-estudis"] = dict(title="Cercle Estudis", section="grups", body=f"""
<h2>Els Cercles d’Estudi</h2>
<figure class="float-r"><img src="{IMG}/2016/06/CERCLE_1-300x250.jpg" alt="CERCLE_1"></figure>
<p class="lead">La formació seriosa i profunda, la lectura meditada de la Paraula de Déu, el compartir experiències de fe a nivell de grup, tot això alimentat per una vida de pregària constant, ens porten a conèixer millor l’Església, a estimar-la en els seus sagraments i a voler descobrir a través d’ella què és el que Déu vol de nosaltres.</p>
<p>Aprofundir en el misteri de la nostra fe és una tasca indispensable i necessària per avançar en el camí de Jesucrist, cap al Pare, en l’amor de l’Esperit Sant.</p>
<blockquote><p><strong><em>Animeu-vos a participar, des del compromís lliure.</em></strong></p></blockquote>
""")

PAGES["esplai"] = dict(title="Esplai", section="grups", body=f"""
<figure class="float-r"><img src="{IMG}/2016/06/vine-a-lesplai.jpg" alt="vine-a-lesplai"></figure>
<p><a class="dl" href="{IMG}/2016/06/2.-ESPLAI-SANT-VICENC%CC%A7-DE-SARRIA%CC%80-JPEG-PDF.pdf" target="_blank" rel="noopener">2. ESPLAI SANT VICENÇ DE SARRIÀ-JPEG-PDF</a></p>
<p class="lead"><strong>L’Esplai de la Parròquia</strong> està format per una trentena de nois i noies i els seus monitors que comparteixen les tardes de cada dissabte (<strong><em>de 17 a 19 h, al Centre Parroquial</em></strong>) amb els jocs i activitats diverses que fem per grups d’edats. És el lloc ideal per aprendre a conviure, conèixer nous amics i passar-ho molt bé!</p>
<p>Fem una excursió o més cada trimestre, activitats amb els pares i relacionades amb el barri, i molt més! L’Esplai està federat al MCEC i al llarg del curs es fan diverses activitats amb altres esplais.</p>
<p>A l’estiu el curs culmina amb els campaments, uns 10 o 12 intensos i divertits dies, cada any més divertits i especials.</p>
<div class="gallery wide">
  <figure><img src="{IMG}/2016/06/espla05-960x400_c.jpg" alt="espla05"></figure>
  <figure><img src="{IMG}/2016/06/project05-960x400_c.jpg" alt="project05"></figure>
  <figure><img src="{IMG}/2016/06/espla04-960x400_c.jpg" alt="espla04"></figure>
  <figure><img src="{IMG}/2016/06/espla03-960x400_c.jpg" alt="espla03"></figure>
  <figure><img src="{IMG}/2016/06/espla02-960x400_c.jpg" alt="espla02"></figure>
  <figure><img src="{IMG}/2016/06/espla01-960x400_c.jpg" alt="espla01"></figure>
</div>
<div class="callout">
  <p>Visita’ns al nostre bloc:</p>
  <p><a href="http://www.esplaistvicenc.blogspot.com/" target="_blank" rel="noopener"><strong>www.esplaistvicenc</strong>.blogspot.com/</a></p>
  <p>MAIL: <a href="mailto:esplaisantvicenc@gmail.com">esplaisantvicenc@gmail.com</a>.</p>
</div>
<h2>QUÈ ÉS EL MOVIMENT INFANTIL I JUVENIL DE LA PARRÒQUIA DE SANT VICENÇ DE SARRIÀ?</h2>
<h3>El Moviment Infantil i Juvenil</h3>
<p>És el <strong>grup educatiu de la Parròquia de Sant Vicenç de Sarrià</strong>, el qual neix de la Comunitat Parroquial com un instrument i mètode per la formació humana i cristiana dels infants, adolescents i joves en i durant el temps de lleure o esplai.</p>
<p>El subjecte educatiu darrerament responsable, doncs, no és altre que la Comunitat Parroquial, la qual és presidida pel Rector designat per l’Ordinari Diocesà i a la qual li és confiada la implantació de l’’Església en un territori que correspon en bona part a l’antiga Vila de Sarrià.</p>
<p>El Moviment Infantil i Juvenil no és un pàrquing ni un lloc d’entreteniment d’infants i adolescents. És un moviment educatiu que col·labora en la tasca educativa de les famílies i convida infants, adolescents i joves a participar activament en unes propostes educatives que parteixen dels seus interessos i necessitats més vitals i els orienta a trobar la resposta adequada en la persona de Jesucrist i el seu Evangeli.</p>
<p>El Moviment Infantil i Juvenil realitza aquesta tasca dissenyant una successió d’etapes educatives corresponents a les característiques de cada edat, etapes que han d’anar sempre orientades a la integració fe-vida dels infants, dels adolescents i els joves que hi participen.</p>
<figure class="wide"><a href="https://www.parroquiasarria.net/projecte-educatiu-de-lesplai-sant-vicenc/" target="_blank" rel="noopener"><img src="{IMG}/2016/06/banner-projecte-educatiu.jpg" alt="banner-projecte-educatiu"></a></figure>
<h2>Decàleg dels nois i noies de l’esplai:</h2>
<ol class="decaleg">
  <li><span>El noi/a de l’Esplai ha de ser <strong>respectuós amb els altres i amb la natura</strong>.</span></li>
  <li><span>El noi/a de l’Esplai és <strong>sincer i no diu mentides</strong>.</span></li>
  <li><span>El noi/a de l’Esplai <strong>obeeix bé</strong> i de seguida.</span></li>
  <li><span>El noi/a de l’Esplai <strong>és amable i educat</strong>.</span></li>
  <li><span>El noi/a de l’Esplai és <strong>alegre i somriu</strong>, és optimista.</span></li>
  <li><span>El noi/a de l’Esplai és <strong>net, polit i endreçat</strong>.</span></li>
  <li><span>El noi/a de l’Esplai <strong>s’esforça en l’estudi, el treball i el joc</strong>.</span></li>
  <li><span>El noi/a de l’Esplai és <strong>bon fill, bon germà i bon company</strong>.</span></li>
  <li><span>El noi/a de l’esplai <strong>és servicial i valent</strong>.</span></li>
  <li><span>El noi/a de l’Esplai <strong>vol estimar cada dia més Jesús</strong>.</span></li>
</ol>
""")

PAGES["caritas"] = dict(title="Càritas", section="grups", body=f"""
<h2>Assistència Social – Càritas Parroquial</h2>
<figure class="float-r"><img src="{IMG}/2016/06/caritas_parroquial.jpg" alt="caritas_parroquial"></figure>
<p class="lead">Entre els serveis que té organitzats la Parròquia figura el de l’Assistència Social.</p>
<p>Les voluntàries s’encarreguen d’aquest servei, que es presta tots els dimecres a la tarda, de 17.00h a 19.00h, en les dependències del carrer de Arquitecte Mas, 3.</p>
<p>S’atenen aquelles persones del barri que hi fan cap en busca d’una orientació o d’una ajuda per enfocar i resoldre problemes de tipus familiars, educatius, socials, econòmics, etc.</p>
<p>A través d’aquest servei es fa efectiva la comunicació de béns, expressió del compromís de la comunitat amb els més necessitats. Es treballa també amb immigrants.</p>
<div class="callout">
  <p><strong>Lloc:</strong> Dependències parroquials del carrer de l’Arquitecte Mas, 3</p>
  <p><strong>Horari:</strong> Tots els dimecres, de 17.00 a 19.00 h</p>
  <p><strong>Més informació:</strong> <a href="tel:932030339">93.203.03.39</a> (Secretariat d’Acció Social-Càritas)</p>
</div>
<h3>Enllaços d’interés</h3>
<ul>
  <li><a href="http://www.caritasbcn.org/ca/" target="_blank" rel="noopener">Càritas Diocesana de Barcelona</a></li>
  <li><a href="http://www.assis.cat/" target="_blank" rel="noopener">Centre Assís</a></li>
</ul>
<div class="center"><img src="{IMG}/2016/06/POSTER.png" alt="POSTER" style="max-width:420px;border-radius:12px"></div>
""")

# ------------------------------------------------------------------ ALTRES
PAGES["horaris"] = dict(title="Horaris", section=None, body="""
<h2>Horaris Missa d’Estiu:</h2>
<div class="timeline">
  <div><strong>Feiners:</strong>8h (a l’agost es suprimeix), 10h i 20:15h.</div>
  <div><strong>Dissabtes:</strong>10h i 19:15h (familiar). Solemnitat també.</div>
  <div><strong>Diumenges i solemnitats de precepte:</strong>10h, 11:30h i 20:15h (CAST)</div>
  <div><strong>Dies festius no de precepte:</strong>8:30h, 10h i 20:15h.</div>
</div>
<h3>Confessions:</h3>
<p>Dies feiners de 8.30 a 10h i de 19.45 a 20.15h, mitja hora abans de la missa dominical.</p>
<h2>Despatx parroquial:</h2>
<p>Només els dimecres de 17.30 a 20h.</p>
<h2>Càritas parroquial – Espai d’acollida:</h2>
<p>Dimecres, de 17.30 a 18.30h a la sala gran de la rectoria (no cal cita prèvia).</p>
<div class="callout"><p>Centre Parroquial Sant Vicenç: c/ Pare Miquel de Sarrià, 8 – 08034 Barcelona. T. <a href="tel:932039772">93.203.97.72</a></p></div>
<h2>Obertura del temple:</h2>
<p>A les 7:30 de dilluns a dissabte; els diumenges obre a les 9h. Tancament a les 21h. Es tanca dissabte de 14h a 16h i diumenge de 14h a 17h.</p>
""")

PAGES["donatius"] = dict(title="Donatius", section=None, body="""
<p class="lead">Els donatius son necessaris per al manteniment de la Parròquia i el desenvolupament de les seves activitats pastorals i socials . Us agraïm anticipadament el vostre donatiu.</p>
<p>Els donatius a l’Església es poden desgravar en la declaració de la renda. Si teniu voluntat de fer la desgravació, ens ho heu de comunicar en el moment de fer el donatiu i facilitar les dades de NOM, COGNOMS I DNI per tal que la Parròquia pugui notificar-ho a Hisenda.</p>
<h3>Hi ha diferents opcions per fer un donatiu :</h3>
<div class="gifts">
  <div class="gift"><h3>Transferència bancària puntual</h3><p>al nostre compte corrent <strong>ES15 2100 0808 1302 0037 7372</strong> indicant com a concepte NOM, COGNOMS I DNI.</p><p><em>Si voleu rebut de la vostra donació, heu d’enviar còpia de comprovant bancari de la transferència a la Parròquia. Ens la podeu facilitar tant per correu ordinari, per correu electrònic a <a href="mailto:santvicenc181@arqbcn.cat">santvicenc181@arqbcn.cat</a> ó entregar-lo personalment els dies de Despatx Parroquial ( dilluns –dimecres i divendres de 17.30h a 20 h ).</em></p></div>
  <div class="gift"><h3>BIZUM</h3><p><strong>BIZUM DONATIVO ONG: 00687</strong></p></div>
  <div class="gift"><h3>Transferència bancària periòdica.</h3><p>Heu d’emplenar el Formulari de Donació. Una vegada omplert i signat ens ho feu arribar el Formulari (tant per correu ordinari, per correu electrònic a <a href="mailto:psantvicencsarria@arq.cat">psantvicencsarria@arq.cat</a> ó en mà els dies de Despatx Parroquial ( dilluns –dimecres i divendres de 17.30h a 20 h ). Al omplir el Formulari de Donació ja tenim les dades necessàries per elaborar els rebuts.</p></div>
  <div class="gift"><h3>Xec bancari.</h3><p>Recordeu que el xec ha de ser nominatiu, indicant que el beneficiari es la PARROQUIA SANT VICENÇ DE SARRIA. Podeu enviar el xec per correu ordinari o entregar-lo personalment els dies de Despatx Parroquial ( dilluns –dimecres i divendres de 17.30h a 20 h ). Si voleu rebut de la vostra donació, juntament amb el xec ens heu de facilitar NOM, COGNOMS I DNI.</p></div>
  <div class="gift"><h3>Donatiu a través del portal</h3><p><a href="https://www.donoamiiglesia.es/san/Home#!/donar/2fb6d17c-ed3e-e611-80e8-005056b101e1" target="_blank" rel="noopener">donoamiiglesia.es</a> només cal entrar a l’apartat “donar a mi parroquia” i introduir el codi postal de la parròquia 08034 i seleccionar Sant Vicenç de Sarrià.</p></div>
</div>
<hr>
<p><strong>Descargar els documents necessaris:</strong></p>
<p><a class="dl" href="https://www.parroquiasarria.net/wp-content/uploads/2016/11/Formulari-de-Donaci%C3%B3.docx">Formulari de Donació</a></p>
""")

PAGES["contacte"] = dict(title="Contacte", section=None, body=f"""
<iframe class="map" loading="lazy" title="Mapa" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d610.9022345490649!2d2.120996103704187!3d41.39936745353153!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x167c6d0eadc05027!2sParroquia+San+Vicente+de+Sarri%C3%A1!5e0!3m2!1ses!2ses!4v1474192243713" allowfullscreen></iframe>
<div class="callout">
  <p>C/Rector Voltà 5, 08034 BARCELONA</p>
  <p><strong><a href="tel:932030907">TEL. 932 030 907</a></strong></p>
  <p><a href="mailto:santvicenc181@arqbcn.cat">santvicenc181@arqbcn.cat</a></p>
</div>
<p>Subcriu-te a la nostra newsletter i rebràs cada setmana totes les notícies, celebracions i activitats de la Parròquia de Sant Vicenç de Sarrià! <a href="{NEWSLETTER}" target="_blank" rel="noopener">Inscriu-t’hi fent clic aquí!</a></p>
""")
