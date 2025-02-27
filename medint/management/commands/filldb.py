# - coding: utf-8  -
from django.core.management import BaseCommand
import urllib2
from medint.models import Disease


rows  = '''Intestinal infectious diseases (001-009)
001	Cholera
002	Typhoid and paratyphoid fevers
003	Other salmonella infections
004	Shigellosis
005	Other food poisoning (bacterial)
006	Amebiasis
007	Other protozoal intestinal diseases
008	Intestinal infections due to other organisms
009	Ill-defined intestinal infections
Tuberculosis (010-018)
010	Primary tuberculous infection
011	Pulmonary tuberculosis
012	Other respiratory tuberculosis
013	Tuberculosis of meninges and central nervous system
014	Tuberculosis of intestines, peritoneum, and mesenteric glands
015	Tuberculosis of bones and joints
016	Tuberculosis of genitourinary system
017	Tuberculosis of other organs
018	Miliary tuberculosis
Zoonotic bacterial diseases (020-027)
020	Plague
021	Tularemia
022	Anthrax
023	Brucellosis
024	Glanders
025	Melioidosis
026	Rat-bite fever
027	Other zoonotic bacterial diseases
Other bacterial diseases (030-041)
030	Leprosy
031	Diseases due to other mycobacteria
032	Diphtheria
033	Whooping cough
034	Streptococcal sore throat and scarlet fever
035	Erysipelas
036	Meningococcal infection
037	Tetanus
038	Septicemia
039	Actinomycotic infections
040	Other bacterial diseases
041	Bacterial infection in conditions classified elsewhere and of unspecified site
Human immunodeficiency virus (042)
042 Human immunodeficiency virus [HIV] disease
Poliomyelitis and other non-arthropod-borne viral diseases of central nervous system (045-049)
045	Acute poliomyelitis
046	Slow virus infection of central nervous system
047	Meningitis due to enterovirus
048	Other enterovirus diseases of central nervous system
049	Other non-arthropod-borne viral diseases of central nervous system
Viral diseases accompanied by exanthem (050-059)
050	Smallpox
051	Cowpox and paravaccinia
052	Chickenpox
053	Herpes zoster
054	Herpes simplex
055	Measles
056	Rubella
057	Other viral exanthemata
058	Other human herpesvirus
059	Other poxvirus infections
Arthropod-borne viral diseases (060-066)
060	Yellow fever
061	Dengue
062	Mosquito-borne viral encephalitis
063	Tick-borne viral encephalitis
064	Viral encephalitis transmitted by other and unspecified arthropods
065	Arthropod-borne hemorrhagic fever
066	Other arthropod-borne viral diseases
Other diseases due to viruses and Chlamydiae (070-079)
070	Viral hepatitis
071	Rabies
072	Mumps
073	Ornithosis
074	Specific diseases due to Coxsackie virus
075	Infectious mononucleosis
076	Trachoma
077	Other diseases of conjunctiva due to viruses and Chlamydiae
078	Other diseases due to viruses and Chlamydiae
079	Viral infection in conditions classified elsewhere and of unspecified site
Rickettsioses and other arthropod-borne diseases (080-088)
080	Louse-borne [epidemic] typhus
081	Other typhus
082	Tick-borne rickettsioses
083	Other rickettsioses
084	Malaria
085	Leishmaniasis
086	Trypanosomiasis
087	Relapsing fever
088	Other arthropod-borne diseases
Syphilis and other venereal diseases (090-099)
090	Congenital syphilis
091	Early syphilis, symptomatic
092	Early syphilis, latent
093	Cardiovascular syphilis
094	Neurosyphilis
095	Other forms of late syphilis, with symptoms
096	Late syphilis, latent
097	Other and unspecified syphilis
098	Gonococcal infections
099	Other venereal diseases
Other	spirochetal diseases (100-104)
100	Leptospirosis
101	Vincent's angina
102	Yaws
103	Pinta
104	Other spirochetal infection
Mycoses (110-118)
110	Dermatophytosis
111	Dermatomycosis, other and unspecified
112	Candidiasis
114	Coccidioidomycosis
115	Histoplasmosis
116	Blastomycotic infection
117	Other mycoses
118	Opportunistic mycoses
Helminthiases (120-129)
120	Schistosomiasis [bilharziasis]
121	Other trematode infections
122	Echinococcosis
123	Other cestode infection
124	Trichinosis
125	Filarial infection and dracontiasis
126	Ancylostomiasis and necatoriasis
127	Other intestinal helminthiases
128	Other and unspecified helminthiases
129	Intestinal parasitism, unspecified
Other infectious and parasitic diseases (130-136)
130	Toxoplasmosis
131	Trichomoniasis
132	Pediculosis and phthirus infestation
133	Acariasis
134	Other infestation
135	Sarcoidosis
136	Other and unspecified infectious and parasitic diseases
Late effects of infectious and parasitic diseases (137-139)
137	Late effects of tuberculosis
138	Late effects of acute poliomyelitis
139	Late effects of other infectious and parasitic diseases
2.	NEOPLASMS
Malignant neoplasm of lip, oral cavity, and pharynx (140-149)
140	Malignant neoplasm of lip
141	Malignant neoplasm of tongue
142	Malignant neoplasm of major salivary glands
143	Malignant neoplasm of gum
144	Malignant neoplasm of floor of mouth
145	Malignant neoplasm of other and unspecified parts of mouth
146	Malignant neoplasm of oropharynx
147	Malignant neoplasm of nasopharynx
148	Malignant neoplasm of hypopharynx
149	Malignant neoplasm of other and ill-defined sites within the lip, oral cavity, and pharynx
Malignant neoplasm of digestive organs and peritoneum (150-159)
150	Malignant neoplasm of esophagus
151	Malignant neoplasm of stomach
152	Malignant neoplasm of small intestine, including duodenum
153	Malignant neoplasm of colon
154	Malignant neoplasm of rectum, rectosigmoid junction, and anus
155	Malignant neoplasm of liver and intrahepatic bile ducts
156	Malignant neoplasm of gallbladder and extrahepatic bile ducts
157	Malignant neoplasm of pancreas
158	Malignant neoplasm of retroperitoneum and peritoneum
159	Malignant neoplasm of other and ill-defined sites within the digestive organs and peritoneum
Malignant neoplasm of respiratory and intrathoracic organs (160-165)
160	Malignant neoplasm of nasal cavities, middle ear, and accessory sinuses
161	Malignant neoplasm of larynx
162	Malignant neoplasm of trachea, bronchus, and lung
163	Malignant neoplasm of pleura
164	Malignant neoplasm of thymus, heart, and mediastinum
165	Malignant neoplasm of other and ill-defined sites within the respiratory system and intrathoracic organs
Malignant neoplasm of bone, connective tissue, skin, and breast (170-176)
170	Malignant neoplasm of bone and articular cartilage
171	Malignant neoplasm of connective and other soft tissue
172	Malignant melanoma of skin
173	Other malignant neoplasm of skin
174	Malignant neoplasm of female breast
175	Malignant neoplasm of male breast
Kaposi's sarcoma (176)
176	Kaposi's sarcoma
Malignant neoplasm of genitourinary organs (179-189)
179	Malignant neoplasm of uterus, part unspecified
180	Malignant neoplasm of cervix uteri
181	Malignant neoplasm of placenta
182	Malignant neoplasm of body of uterus
183	Malignant neoplasm of ovary and other uterine adnexa
184	Malignant neoplasm of other and unspecified female genital organs
185	Malignant neoplasm of prostate
186	Malignant neoplasm of testis
187	Malignant neoplasm of penis and other male genital organs
188	Malignant neoplasm of bladder
189	Malignant neoplasm of kidney and other and unspecified urinary organs
Malignant neoplasm of other and unspecified sites (190-199)
190	Malignant neoplasm of eye
191	Malignant neoplasm of brain
192	Malignant neoplasm of other and unspecified parts of nervous system
193	Malignant neoplasm of thyroid gland
194	Malignant neoplasm of other endocrine glands and related structures
195	Malignant neoplasm of other and ill-defined sites
196	Secondary and unspecified malignant neoplasm of lymph nodes
197	Secondary malignant neoplasm of respiratory and digestive systems
198	Secondary malignant neoplasm of other specified sites
199	Malignant neoplasm without specification of site
Malignant neoplasm of lymphatic and hematopoietic tissue (200-208)
200	Lymphosarcoma and reticulosarcoma
201	Hodgkin's disease
202	Other malignant neoplasm of lymphoid and histiocytic tissue
203	Multiple myeloma and immunoproliferative neoplasms
204	Lymphoid leukemia
205	Myeloid leukemia
206	Monocytic leukemia
207	Other specified leukemia
208	Leukemia of unspecified cell type
Neuroendocrine tumors (209)
209	Neuroendocrine tumors
Benign neoplasms (210-229)
210	Benign neoplasm of lip, oral cavity, and pharynx
211	Benign neoplasm of other parts of digestive system
212	Benign neoplasm of respiratory and intrathoracic organs
213	Benign neoplasm of bone and articular cartilage
214	Lipoma
215	Other benign neoplasm of connective and other soft tissue
216	Benign neoplasm of skin
217	Benign neoplasm of breast
218	Uterine leiomyoma
219	Other benign neoplasm of uterus
220	Benign neoplasm of ovary
221	Benign neoplasm of other female genital organs
222	Benign neoplasm of male genital organs
223	Benign neoplasm of kidney and other urinary organs
224	Benign neoplasm of eye
225	Benign neoplasm of brain and other parts of nervous system
226	Benign neoplasm of thyroid gland
227	Benign neoplasm of other endocrine glands and related structures
228	Hemangioma and lymphangioma, any site
229	Benign neoplasm of other and unspecified sites
Carcinoma in situ (230-234)
230	Carcinoma in situ of digestive organs
231	Carcinoma in situ of respiratory system
232	Carcinoma in situ of skin
233	Carcinoma in situ of breast and genitourinary system
234	Carcinoma in situ of other and unspecified sites
Neoplasms of uncertain behavior (235-238)
235	Neoplasm of uncertain behavior of digestive and respiratory systems
236	Neoplasm of uncertain behavior of genitourinary organs
237	Neoplasm of uncertain behavior of endocrine glands and nervous system
238	Neoplasm of uncertain behavior of other and unspecified sites and tissues
Neoplasms of unspecified nature (239)
239	Neoplasm of unspecified nature
3.	ENDOCRINE, NUTRITIONAL AND METABOLIC DISEASES, AND IMMUNITY DISORDERS
Disorders of thyroid gland (240-246)
240	Simple and unspecified goiter
241	Nontoxic nodular goiter
242	Thyrotoxicosis with or without goiter
243	Congenital hypothyroidism
244	Acquired hypothyroidism
245	Thyroiditis
246	Other disorders of thyroid
Diseases of other endocrine glands (249-259)
249	Secondary diabetes mellitus
250	Diabetes mellitus
251	Other disorders of pancreatic internal secretion
252	Disorders of parathyroid gland
253	Disorders of the pituitary gland and its hypothalamic control
254	Diseases of thymus gland
255	Disorders of adrenal glands
256	Ovarian dysfunction
257	Testicular dysfunction
258	Polyglandular dysfunction and related disorders
259	Other endocrine disorders
Nutritional deficiencies (260-269)
260	Kwashiorkor
261	Nutritional marasmus
262	Other severe protein-calorie malnutrition
263	Other and unspecified protein-calorie malnutrition
264	Vitamin A deficiency
265	Thiamine and niacin deficiency states
266	Deficiency of B-complex components
267	Ascorbic acid deficiency
268	Vitamin D deficiency
269	Other nutritional deficiencies
Other metabolic disorders and immunity disorders (270-279)
270	Disorders of amino-acid transport and metabolism
271	Disorders of carbohydrate transport and metabolism
272	Disorders of lipoid metabolism
273	Disorders of plasma protein metabolism
274	Gout
275	Disorders of mineral metabolism
276	Disorders of fluid, electrolyte, and acid-base balance
277	Other and unspecified disorders of metabolism
278	Obesity and other hyperalimentation
279	Disorders involving the immune mechanism
4.	DISEASES OF BLOOD AND BLOOD-FORMING ORGANS
Diseases of the blood and blood-forming organs (280-289)
280	Iron deficiency anemias
281	Other deficiency anemias
282	Hereditary hemolytic anemias
283	Acquired hemolytic anemias
284	Aplastic anemia
285	Other and unspecified anemias
286	Coagulation defects
287	Purpura and other hemorrhagic conditions
288	Diseases of white blood cells
289	Other diseases of blood and blood-forming organs
5.	MENTAL DISORDERS
Organic psychotic conditions (290-294)
290	Senile and presenile organic psychotic conditions
291	Alcoholic psychoses
292	Drug psychoses
293	Transient organic psychotic conditions
294	Other organic psychotic conditions (chronic)
Other psychoses (295-299)
295	Schizophrenic psychoses
296	Affective psychoses
297	Paranoid states
298	Other nonorganic psychoses
299	Psychoses with origin specific to childhood
Neurotic disorders, personality disorders, and other nonpsychotic mental disorders (300-316)
300	Neurotic disorders
301	Personality disorders
302	Sexual deviations and disorders
303	Alcohol dependence syndrome
304	Drug dependence
305	Nondependent abuse of drugs
306	Physiological malfunction arising from mental factors
307	Special symptoms or syndromes, not elsewhere classified
308	Acute reaction to stress
309	Adjustment reaction
310	Specific nonpsychotic mental disorders following organic brain damage
311	Depressive disorder, not elsewhere classified
312	Disturbance of conduct, not elsewhere classified
313	Disturbance of emotions specific to childhood and adolescence
314	Hyperkinetic syndrome of childhood
315	Specific delays in development
316	Psychic factors associated with diseases classified elsewhere
Intellectual Disabilities (317-319)
317	Mild intellectual disabilities
318	Other specified intellectual disabilities
319	Unspecified intellectual disabilities
6.	DISEASES OF THE NERVOUS SYSTEM AND SENSE ORGANS
Inflammatory diseases of the central nervous system (320-326)
320	Bacterial meningitis
321	Meningitis due to other organisms
322	Meningitis of unspecified cause
323	Encephalitis, myelitis, and encephalomyelitis
324	Intracranial and intraspinal abscess
325	Phlebitis and thrombophlebitis of intracranial venous sinuses
326	Late effects of intracranial abscess or pyogenic infection
327	Organic sleep disorders
Hereditary and degenerative diseases of the central nervous system (330-337)
330	Cerebral degenerations usually manifest in childhood
331	Other cerebral degenerations
332	Parkinson's disease
333	Other extrapyramidal disease and abnormal movement disorders
334	Spinocerebellar disease
335	Anterior horn cell disease
336	Other diseases of spinal cord
337	Disorders of the autonomic nervous system
Pain (338)
338	Pain, not elsewhere classified
Other headache syndromes (339)
339	Other headache syndromes
Other disorders of the central nervous system (340-349)
340	Multiple sclerosis
341	Other demyelinating diseases of central nervous system
342	Hemiplegia and hemiparesis
343	Infantile cerebral palsy
344	Other paralytic syndromes
345	Epilepsy
346	Migraine
347	Cataplexy and narcolepsy
348	Other conditions of brain
349	Other and unspecified disorders of the nervous system
Disorders of the peripheral nervous system (350-359)
350	Trigeminal nerve disorders
351	Facial nerve disorders
352	Disorders of other cranial nerves
353	Nerve root and plexus disorders
354	Mononeuritis of upper limb and mononeuritis multiplex
355	Mononeuritis of lower limb
356	Hereditary and idiopathic peripheral neuropathy
357	Inflammatory and toxic neuropathy
358	Myoneural disorders
359	Muscular dystrophies and other myopathies
Disorders of the eye and adnexa (360-379)
360	Disorders of the globe
361	Retinal detachments and defects
362	Other retinal disorders
363	Chorioretinal inflammations and scars and other disorders of choroid
364	Disorders of iris and ciliary body
365	Glaucoma
366	Cataract
367	Disorders of refraction and accommodation
368	Visual disturbances
369	Blindness and low vision
370	Keratitis
371	Corneal opacity and other disorders of cornea
372	Disorders of conjunctiva
373	Inflammation of eyelids
374	Other disorders of eyelids
375	Disorders of lacrimal system
376	Disorders of the orbit
377	Disorders of optic nerve and visual pathways
378	Strabismus and other disorders of binocular eye movements
379	Other disorders of eye
Diseases of the ear and mastoid process (380-389)
380	Disorders of external ear
381	Nonsuppurative otitis media and Eustachian tube disorders
382	Suppurative and unspecified otitis media
383	Mastoiditis and related conditions
384	Other disorders of tympanic membrane
385	Other disorders of middle ear and mastoid
386	Vertiginous syndromes and other disorders of vestibular system
387	Otosclerosis
388	Other disorders of ear
389	Hearing loss
7.	DISEASES OF THE CIRCULATORY SYSTEM
Acute rheumatic fever (390-392)
390	Rheumatic fever without mention of heart involvement
391	Rheumatic fever with heart involvement
392	Rheumatic chorea
Chronic rheumatic heart disease (393-398)
393	Chronic rheumatic pericarditis
394	Diseases of mitral valve
395	Diseases of aortic valve
396	Diseases of mitral and aortic valves
397	Diseases of other endocardial structures
398	Other rheumatic heart disease
Hypertensive disease (401-405)
401	Essential hypertension
402	Hypertensive heart disease
403	Hypertensive renal disease
404	Hypertensive heart and renal disease
405	Secondary hypertension
Ischemic heart disease (410-414)
410	Acute myocardial infarction
411	Other acute and subacute form of ischemic heart disease
412	Old myocardial infarction
413	Angina pectoris
414	Other forms of chronic ischemic heart disease
Diseases of pulmonary circulation (415-417)
415	Acute pulmonary heart disease
416	Chronic pulmonary heart disease
417	Other diseases of pulmonary circulation
Other forms of heart disease (420-429)
420	Acute pericarditis
421	Acute and subacute endocarditis
422	Acute myocarditis
423	Other diseases of pericardium
424	Other diseases of endocardium
425	Cardiomyopathy
426	Conduction disorders
427	Cardiac dysrhythmias
428	Heart failure
429	Ill-defined descriptions and complications of heart disease
Cerebrovascular disease (430-438)
430	Subarachnoid hemorrhage
431	Intracerebral hemorrhage
432	Other and unspecified intracranial hemorrhage
433	Occlusion and stenosis of precerebral arteries
434	Occlusion of cerebral arteries
435	Transcient cerebral ischemia
436	Acute but ill-defined cerebrovascular disease
437	Other and ill-defined cerebrovascular disease
438	Late effects of cerebrovascular disease
Diseases of arteries, arterioles, and capillaries (440-448)
440	Atherosclerosis
441	Aortic aneurysm and dissection
442	Other aneurysm
443	Other peripheral vascular disease
444	Arterial embolism and thrombosis
445	Atheroembolism
446	Polyarteritis nodosa and allied conditions
447	Other disorders of arteries and arterioles
448	Diseases of capillaries
Diseases of veins and lymphatics, and other diseases of circulatory system (451-459)
451	Phlebitis and thrombophlebitis
452	Portal vein thrombosis
453	Other venous embolism and thrombosis
454	Varicose veins of lower extremities
455	Hemorrhoids
456	Varicose veins of other sites
457	Noninfective disorders of lymphatic channels
458	Hypotension
459	Other disorders of circulatory system
8.	DISEASES OF THE RESPIRATORY SYSTEM
Acute respiratory infections (460-466)
460	Acute nasopharyngitis [common cold]
461	Acute sinusitis
462	Acute pharyngitis
463	Acute tonsillitis
464	Acute laryngitis and tracheitis
465	Acute upper respiratory infections of multiple or unspecified sites
466	Acute bronchitis and bronchiolitis
Other	diseases of upper respiratory tract (470-478)
470	Deviated nasal septum
471	Nasal polyps
472	Chronic pharyngitis and nasopharyngitis
473	Chronic sinusitis
474	Chronic disease of tonsils and adenoids
475	Peritonsillar abscess
476	Chronic laryngitis and laryngotracheitis
477	Allergic rhinitis
478	Other diseases of upper respiratory tract
Pneumonia and influenza (480-488)
480	Viral pneumonia
481	Pneumococcal pneumonia [Streptococcus pneumoniae pneumonia]
482	Other bacterial pneumonia
483	Pneumonia due to other specified organism
484	Pneumonia in infectious diseases classified elsewhere
485	Bronchopneumonia, organism unspecified
486	Pneumonia, organism unspecified
487	Influenza
488	Influenza due to identified avian influenza virus
Chronic obstructive pulmonary disease and allied conditions (490-496)
490	Bronchitis, not specified as acute or chronic
491	Chronic bronchitis
492	Emphysema
493	Asthma
494	Bronchiectasis
495	Extrinsic allergic alveolitis
496	Chronic airways obstruction, not elsewhere classified
Pneumoconioses and other lung diseases due to external agents (500-508)
500	Coalworkers' pneumoconiosis
501	Asbestosis
502	Pneumoconiosis due to other silica or silicates
503	Pneumoconiosis due to other inorganic dust
504	Pneumopathy due to inhalation of other dust
505	Pneumoconiosis, unspecified
506	Respiratory conditions due to chemical fumes and vapors
507	Pneumonitis due to solids and liquids
508	Respiratory conditions due to other and unspecified external agents
Other diseases of respiratory system (510-519)
510	Empyema
511	Pleurisy
512	Pneumothorax
513	Abscess of lung and mediastinum
514	Pulmonary congestion and hypostasis
515	Postinflammatory pulmonary fibrosis
516	Other alveolar and parietoalveolar pneumopathy
517	Lung involvement in conditions classified elsewhere
518	Other diseases of lung
519	Other diseases of respiratory system
9.	DISEASES OF THE DIGESTIVE SYSTEM
Diseases of oral cavity, salivary glands, and jaws (520-529)
520	Disorders of tooth development and eruption
521	Diseases of hard tissues of teeth
522	Diseases of pulp and periapical tissues
523	Gingival and periodontal diseases
524	Dentofacial anomalies, including malocclusion
525	Other diseases and conditions of the teeth and supporting structures
526	Diseases of the jaws
527	Diseases of the salivary glands
528	Diseases of the oral soft tissues, excluding lesions specific for gingiva and tongue
529	Diseases and other conditions of the tongue
Diseases of esophagus, stomach, and duodenum (530-539)
530	Diseases of esophagus
531	Gastric ulcer
532	Duodenal ulcer
533	Peptic ulcer, site unspecified
534	Gastrojejunal ulcer
535	Gastritis and duodenitis
536	Disorders of function of stomach
537	Other disorders of stomach and duodenum
538 	Gastrointestinal mucositis (ulcerative)
539	Complications of bariatric procedures
Appendicitis (540-543)
540	Acute appendicitis
541	Appendicitis, unqualified
542	Other appendicitis
543	Other diseases of appendix
Hernia of abdominal cavity (550-553)
550	Inguinal hernia
551	Other hernia of abdominal cavity, with gangrene
552	Other hernia of abdominal cavity, with obstruction, but without mention of gangrene
553	Other hernia of abdominal cavity without mention of obstruction or gangrene
Noninfective enteritis and colitis (555-558)
555	Regional enteritis
556	Ulcerative colitis
557	Vascular insufficiency of intestine
558	Other noninfective gastroenteritis and colitis
Other diseases of intestines and peritoneum (560-569)
560	Intestinal obstruction without mention of hernia
562	Diverticula of intestine
564	Functional digestive disorders, not elsewhere classified
565	Anal fissure and fistula
566	Abscess of anal and rectal regions
567	Peritonitis
568	Other disorders of peritoneum
569	Other disorders of intestine
Other diseases of digestive system (570-579)
570	Acute and subacute necrosis of liver
571	Chronic liver disease and cirrhosis
572	Liver abscess and sequelae of chronic liver disease
573	Other disorders of liver
574	Cholelithiasis
575	Other disorders of gallbladder
576	Other disorders of biliary tract
577	Diseases of pancreas
578	Gastrointestinal hemorrhage
579	Intestinal malabsorption
10.	DISEASES OF THE GENITOURINARY SYSTEM
Nephritis, nephrotic syndrome, and nephrosis (580-589)
580	Acute glomerulonephritis
581	Nephrotic syndrome
582	Chronic glomerulonephritis
583	Nephritis and nephropathy, not specified as acute or chronic
584	Acute renal failure
585	Chronic renal failure
586	Renal failure, unspecified
587	Renal sclerosis, unspecified
588	Disorders resulting from impaired renal function
589	Small kidney of unknown cause
Other diseases of urinary system (590-599)
590	Infections of kidney
591	Hydronephrosis
592	Calculus of kidney and ureter
593	Other disorders of kidney and ureter
594	Calculus of lower urinary tract
595	Cystitis
596	Other disorders of bladder
597	Urethritis, not sexually transmitted, and urethral syndrome
598	Urethral stricture
599	Other disorders of urethra and urinary tract
Diseases of male genital organs (600-608)
600	Hyperplasia of prostate
601	Inflammatory diseases of prostate
602	Other disorders of prostate
603	Hydrocele
604	Orchitis and epididymitis
605	Redundant prepuce and phimosis
606	Infertility, male
607	Disorders of penis
608	Other disorders of male genital organs
Disorders of breast (610-611)
610	Benign mammary dysplasias
611	Other disorders of breast
612	Deformity and disproportion of reconstructed breast
Inflammatory disease of female pelvic organs (614-616)
614	Inflammatory disease of ovary, fallopian tube, pelvic cellular tissue, and peritoneum
615	Inflammatory diseases of uterus, except cervix
616	Inflammatory disease of cervix, vagina, and vulva
Other disorders of female genital tract (617-629)
617	Endometriosis
618	Genital prolapse
619	Fistula involving female genital tract
620	Noninflammatory disorders of ovary, fallopian tube, and broad ligament
621	Disorders of uterus, not elsewhere classified
622	Noninflammatory disorders of cervix
623	Noninflammatory disorders of vagina
624	Noninflammatory disorders of vulva and perineum
625	Pain and other symptoms associated with female genital organs
626	Disorders of menstruation and other abnormal bleeding from female genital tract
627	Menopausal and postmenopausal disorders
628	Infertility, female
629	Other disorders of female genital organs
11.	COMPLICATIONS OF PREGNANCY, CHILDBIRTH, AND THE PUERPERIUM
Ectopic and molar pregnancy and other pregnancy with abortive outcome (630-639)
630	Hydatidiform mole
631	Other abnormal product of conception
632	Missed abortion
633	Ectopic pregnancy
634	Spontaneous abortion
635	Legally induced abortion
636	Illegally induced abortion
637	Unspecified abortion
638	Failed attempted abortion
639	Complications following abortion and ectopic and molar pregnancies
Complications mainly related to pregnancy (640-649)
640	Hemorrhage in early pregnancy
641	Antepartum hemorrhage, abruptio placentae, and placenta previa
642	Hypertension complicating pregnancy, childbirth, and the puerperium
643	Excessive vomiting in pregnancy
644	Early or threatened labor
645	Prolonged pregnancy
646	Other complications of pregnancy, not elsewhere classified
647	Infective and parasitic conditions in the mother classifiable elsewhere but complicating pregnancy, childbirth, and the puerperium
648	Other current conditions in the mother classifiable elsewhere but complicating pregnancy, childbirth, and the puerperium
649	Other conditions or status of the mother complicating pregnancy, childbirth, or the puerperium
Normal delivery, and other indications for care in pregnancy, labor, and delivery (650-659)
650	Normal delivery
651	Multiple gestation
652	Malposition and malpresentation of fetus
653	Disproportion
654	Abnormality of organs and soft tissues of pelvis
655	Known or suspected fetal abnormality affecting management of mother
656	Other fetal and placental problems affecting management of mother
657	Polyhydramnios
658	Other problems associated with amniotic cavity and membranes
659	Other indications for care or intervention related to labor and delivery and not elsewhere classified
Complications occurring mainly in the course of labor and delivery (660-669)
660	Obstructed labor
661	Abnormality of forces of labor
662	Long labor
663	Umbilical cord complications
664	Trauma to perineum and vulva during delivery
665	Other obstetrical trauma
666	Postpartum hemorrhage
667	Retained placenta or membranes, without hemorrhage
668	Complications of the administration of anesthetic or other sedation in labor and delivery
669	Other complications of labor and delivery, not elsewhere classified
Complications of the puerperium (670-677)
670	Major puerperal infection
671	Venous complications in pregnancy and the puerperium
672	Pyrexia of unknown origin during the puerperium
673	Obstetrical pulmonary embolism
674	Other and unspecified complications of the puerperium, not elsewhere classified
675	Infections of the breast and nipple associated with childbirth
676	Other disorders of the breast associated with childbirth, and disorders of lactation
677	Late effect of complication of pregnancy, childbirth, and the puerperium
Other Maternal and Fetal Complications (678-679)
678	Other fetal conditions
679	Complications of in utero procedures
12.	DISEASES OF THE SKIN AND SUBCUTANEOUS TISSUE
Infections of skin and subcutaneous tissue (680-686)
680	Carbuncle and furuncle
681	Cellulitis and abscess of finger and toe
682	Other cellulitis and abscess
683	Acute lymphadenitis
684	Impetigo
685	Pilonidal cyst
686	Other local infections of skin and subcutaneous tissue
Other inflammatory conditions of skin and subcutaneous tissue (690-698)
690	Erythematosquamous dermatosis
691	Atopic dermatitis and related conditions
692	Contact dermatitis and other eczema
693	Dermatitis due to substances taken internally
694	Bullous dermatoses
695	Erythematous conditions
696	Psoriasis and similar disorders
697	Lichen
698	Pruritus and related conditions
Other diseases of skin and subcutaneous tissue (700-709)
700	Corns and callosities
701	Other hypertrophic and atrophic conditions of skin
702	Other dermatoses
703	Diseases of nail
704	Diseases of hair and hair follicles
705	Disorders of sweat glands
706	Diseases of sebaceous glands
707	Chronic ulcer of skin
708	Urticaria
709	Other disorders of skin and subcutaneous tissue
13.	DISEASES OF THE MUSCULOSKELETAL SYSTEM AND CONNECTIVE TISSUE
Arthropathies and related disorders (710-719)
710	Diffuse diseases of connective tissue
711	Arthropathy associated with infections
712	Crystal arthropathies
713	Arthropathy associated with other disorders classified elsewhere
714	Rheumatoid arthritis and other inflammatory polyarthropathies
715	Osteoarthrosis and allied disorders
716	Other and unspecified arthropathies
717	Internal derangement of knee
718	Other derangement of joint
719	Other and unspecified disorder of joint
Dorsopathies (720-724)
720	Ankylosing spondylitis and other inflammatory spondylopathies
721	Spondylosis and allied disorders
722	Intervertebral disc disorders
723	Other disorders of cervical region
724	Other and unspecified disorders of back
Rheumatism, excluding the back (725-729)
725	Polymyalgia rheumatica
726	Peripheral enthesopathies and allied syndromes
727	Other disorders of synovium, tendon, and bursa
728	Disorders of muscle, ligament, and fascia
729	Other disorders of soft tissues
Osteopathies, chondropathies, and acquired musculoskeletal deformities (730-739)
730	Osteomyelitis, periostitis, and other infections involving bone
731	Osteitis deformans and osteopathies associated with other disorders classified elsewhere
732	Osteochondropathies
733	Other disorders of bone and cartilage
734	Flat foot
735	Acquired deformities of toe
736	Other acquired deformities of limbs
737	Curvature of spine
738	Other acquired deformity
739	Nonallopathic lesions, not elsewhere classified
14.	CONGENITAL ANOMALIES
Congenital anomalies (740-759)
740	Anencephalus and similar anomalies
741	Spina bifida
742	Other congenital anomalies of nervous system
743	Congenital anomalies of eye
744	Congenital anomalies of ear, face, and neck
745	Bulbus cordis anomalies and anomalies of cardiac septal closure
746	Other congenital anomalies of heart
747	Other congenital anomalies of circulatory system
748	Congenital anomalies of respiratory system
749	Cleft palate and cleft lip
750	Other congenital anomalies of upper alimentary tract
751	Other congenital anomalies of digestive system
752	Congenital anomalies of genital organs
753	Congenital anomalies of urinary system
754	Certain congenital musculoskeletal deformities
755	Other congenital anomalies of limbs
756	Other congenital musculoskeletal anomalies
757	Congenital anomalies of the integument
758	Chromosomal anomalies
759	Other and unspecified congenital anomalies
15.	CERTAIN CONDITIONS ORIGINATING IN THE PERINATAL PERIOD
Maternal causes of perinatal morbidity and mortality (760-763)
760	Fetus or newborn affected by maternal conditions which may be unrelated to present pregnancy
761	Fetus or newborn affected by maternal complications of pregnancy
762	Fetus or newborn affected by complications of placenta, cord, and membranes
763	Fetus or newborn affected by other complications of labor and delivery
Other conditions originating in the perinatal period (764-779)
764	Slow fetal growth and fetal malnutrition
765	Disorders relating to short gestation and unspecified low birthweight
766	Disorders relating to long gestation and high birthweight
767	Birth trauma
768	Intrauterine hypoxia and birth asphyxia
769	Respiratory distress syndrome
770	Other respiratory conditions of fetus and newborn
771	Infections specific to the perinatal period
772	Fetal and neonatal hemorrhage
773	Hemolytic disease of fetus or newborn, due to isoimmunization
774	Other perinatal jaundice
775	Endocrine and metabolic disturbances specific to the fetus and newborn
776	Hematological disorders of fetus and newborn
777	Perinatal disorders of digestive system
778	Conditions involving the integument and temperature regulation of fetus and newborn
779	Other and ill-defined conditions originating in the perinatal period
16.	SYMPTOMS, SIGNS, AND ILL-DEFINED CONDITIONS
Symptoms (780-789)
780	General symptoms
781	Symptoms involving nervous and musculoskeletal systems
782	Symptoms involving skin and other integumentary tissue
783	Symptoms concerning nutrition, metabolism, and development
784	Symptoms involving head and neck
785	Symptoms involving cardiovascular system
786	Symptoms involving respiratory system and other chest symptoms
787	Symptoms involving digestive system
788	Symptoms involving urinary system
789	Other symptoms involving abdomen and pelvis
Nonspecific abnormal findings (790-796)
790	Nonspecific findings on examination of blood
791	Nonspecific findings on examination of urine
792	Nonspecific abnormal findings in other body substances
793	Nonspecific abnormal findings on radiological and other examination of body structure
794	Nonspecific abnormal results of function studies
795	Nonspecific abnormal histological and immunological findings
796	Other nonspecific abnormal findings
Ill-defined and unknown causes of morbidity and mortality (797-799)
797	Senility without mention of psychosis
798	Sudden death, cause unknown
799	Other ill-defined and unknown causes of morbidity and mortality
17.	INJURY AND POISONING
Fracture of skull (800-804)
800	Fracture of vault of skull
801	Fracture of base of skull
802	Fracture of face bones
803	Other and unqualified skull fractures
804	Multiple fractures involving skull or face with other bones
Fracture of spine and trunk (805-809)
805	Fracture of vertebral column without mention of spinal cord lesion
806	Fracture of vertebral column with spinal cord lesion
807	Fracture of rib(s), sternum, larynx, and trachea
808	Fracture of pelvis
809	Ill-defined fractures of bones of trunk
Fracture of upper limb (810-819)
810	Fracture of clavicle
811	Fracture of scapula
812	Fracture of humerus
813	Fracture of radius and ulna
814	Fracture of carpal bone(s)
815	Fracture of metacarpal bone(s)
816	Fracture of one or more phalanges of hand
817	Multiple fractures of hand bones
818	Ill-defined fractures of upper limb
819	Multiple fractures involving both upper limbs, and upper limb with rib(s) and sternum
Fracture of lower limb (820-829)
820	Fracture of neck of femur
821	Fracture of other and unspecified parts of femur
822	Fracture of patella
823	Fracture of tibia and fibula
824	Fracture of ankle
825	Fracture of one or more tarsal and metatarsal bones
826	Fracture of one or more phalanges of foot
827	Other, multiple, and ill-defined fractures of lower limb
828	Multiple fractures involving both lower limbs, lower with upper limb, and lower limb(s) with rib(s) and sternum
829	Fracture of unspecified bones
Dislocation (830-839)
830	Dislocation of jaw
831	Dislocation of shoulder
832	Dislocation of elbow
833	Dislocation of wrist
834	Dislocation of finger
835	Dislocation of hip
836	Dislocation of knee
837	Dislocation of ankle
838	Dislocation of foot
839	Other, multiple, and ill-defined dislocations
Sprains and strains of joints and adjacent muscles (840-848)
840	Sprains and strains of shoulder and upper arm
841	Sprains and strains of elbow and forearm
842	Sprains and strains of wrist and hand
843	Sprains and strains of hip and thigh
844	Sprains and strains of knee and leg
845	Sprains and strains of ankle and foot
846	Sprains and strains of sacroiliac region
847	Sprains and strains of other and unspecified parts of back
848	Other and ill-defined sprains and strains
Intracranial injury, excluding those with skull fracture (850-854)
850	Concussion
851	Cerebral laceration and contusion
852	Subarachnoid, subdural, and extradural hemorrhage, following injury
853	Other and unspecified intracranial hemorrhage following injury
854	Intracranial injury of other and unspecified nature
Internal injury of chest, abdomen, and pelvis (860-869)
860	Traumatic pneumothorax and hemothorax
861	Injury to heart and lung
862	Injury to other and unspecified intrathoracic organs
863	Injury to gastrointestinal tract
864	Injury to liver
865	Injury to spleen
866	Injury to kidney
867	Injury to pelvic organs
868	Injury to other intra-abdominal organs
869	Internal injury to unspecified or ill-defined organs
Open wound of head, neck, and trunk (870-879)
870	Open wound of ocular adnexa
871	Open wound of eyeball
872	Open wound of ear
873	Other open wound of head
874	Open wound of neck
875	Open wound of chest (wall)
876	Open wound of back
877	Open wound of buttock
878	Open wound of genital organs (external), including traumatic amputation
879	Open wound of other and unspecified sites, except limbs
Open wound of upper limb (880-887)
880	Open wound of shoulder and upper arm
881	Open wound of elbow, forearm, and wrist
882	Open wound of hand except finger(s) alone
883	Open wound of finger(s)
884	Multiple and unspecified open wound of upper limb
885	Traumatic amputation of thumb (complete) (partial)
886	Traumatic amputation of other finger(s) (complete) (partial)
887	Traumatic amputation of arm and hand (complete) (partial)
Open wound of lower limb (890-897)
890	Open wound of hip and thigh
891	Open wound of knee, leg [except thigh], and ankle
892	Open wound of foot except toe(s) alone
893	Open wound of toe(s)
894	Multiple and unspecified open wound of lower limb
895	Traumatic amputation of toe(s) (complete) (partial)
896	Traumatic amputation of foot (complete) (partial)
897	Traumatic amputation of leg(s) (complete) (partial)
Injury to blood vessels (900-904)
900	Injury to blood vessels of head and neck
901	Injury to blood vessels of thorax
902	Injury to blood vessels of abdomen and pelvis
903	Injury to blood vessels of upper extremity
904	Injury to blood vessels of lower extremity and unspecified sites
Late effects of injuries, poisonings, toxic effects, and other external causes (905-909)
905	Late effects of musculoskeletal and connective tissue injuries
906	Late effects of injuries to skin and subcutaneous tissues
907	Late effects of injuries to the nervous system
908	Late effects of other and unspecified injuries
909	Late effects of other and unspecified external causes
Superficial injury (910-919)
910	Superficial injury of face, neck, and scalp except eye
911	Superficial injury of trunk
912	Superficial injury of shoulder and upper arm
913	Superficial injury of elbow, forearm, and wrist
914	Superficial injury of hand(s) except finger(s) alone
915	Superficial injury of finger(s)
916	Superficial injury of hip, thigh, leg, and ankle
917	Superficial injury of foot and toe(s)
918	Superficial injury of eye and adnexa
919	Superficial injury of other, multiple, and unspecified sites
Contusion with intact skin surface (920-924)
920	Contusion of face, scalp, and neck except eye(s)
921	Contusion of eye and adnexa
922	Contusion of trunk
923	Contusion of upper limb
924	Contusion of lower limb and of other and unspecified sites
Crushing injury (925-929)
925	Crushing injury of face, scalp, and neck
926	Crushing injury of trunk
927	Crushing injury of upper limb
928	Crushing injury of lower limb
929	Crushing injury of multiple and unspecified sites
Effects of foreign body entering through orifice (930-939)
930	Foreign body on external eye
931	Foreign body in ear
932	Foreign body in nose
933	Foreign body in pharynx and larynx
934	Foreign body in trachea, bronchus, and lung
935	Foreign body in mouth, esophagus, and stomach
936	Foreign body in intestine and colon
937	Foreign body in anus and rectum
938	Foreign body in digestive system, unspecified
939	Foreign body in genitourinary tract
Burns (940-949)
940	Burn confined to eye and adnexa
941	Burn of face, head, and neck
942	Burn of trunk
943	Burn of upper limb, except wrist and hand
944	Burn of wrist(s) and hand(s)
945	Burn of lower limb(s)
946	Burns of multiple specified sites
947	Burn of internal organs
948	Burns classified according to extent of body surface involved
949	Burn, unspecified
Injury to nerves and spinal cord (950-957)
950	Injury to optic nerve and pathways
951	Injury to other cranial nerve(s)
952	Spinal cord injury without evidence of spinal bone injury
953	Injury to nerve roots and spinal plexus
954	Injury to other nerve(s) of trunk excluding shoulder and pelvic girdles
955	Injury to peripheral nerve(s) of shoulder girdle and upper limb
956	Injury to peripheral nerve(s) of pelvic girdle and lower limb
957	Injury to other and unspecified nerves
Certain traumatic complications and unspecified injuries (958-959)
958	Certain early complications of trauma
959	Injury, other and unspecified
Poisoning by drugs, medicinals and biological substances (960-979)
960	Poisoning by antibiotics
961	Poisoning by other anti-infectives
962	Poisoning by hormones and synthetic substitutes
963	Poisoning by primarily systemic agents
964	Poisoning by agents primarily affecting blood constituents
965	Poisoning by analgesics, antipyretics, and antirheumatics
966	Poisoning by anticonvulsants and anti-Parkinsonism drugs
967	Poisoning by sedatives and hypnotics
968	Poisoning by other central nervous system depressants and anesthetics
969	Poisoning by psychotropic agents
970	Poisoning by central nervous system stimulants
971	Poisoning by drugs primarily affecting the autonomic nervous system
972	Poisoning by agents primarily affecting the cardiovascular system
973	Poisoning by agents primarily affecting the gastrointestinal system
974	Poisoning by water, mineral, and uric acid metabolism drugs
975	Poisoning by agents primarily acting on the smooth and skeletal muscles and respiratory system
976	Poisoning by agents primarily affecting skin and mucous membrane, ophthalmological, otorhinolaryngological, and dental drugs
977	Poisoning by other and unspecified drugs and medicinals
978	Poisoning by bacterial vaccines
979	Poisoning by other vaccines and biological substances
Toxic effects of substances chiefly nonmedicinal as to source (980-989)
980	Toxic effect of alcohol
981	Toxic effect of petroleum products
982	Toxic effect of solvents other than petroleum-based
983	Toxic effect of corrosive aromatics, acids, and caustic alkalis
984	Toxic effect of lead and its compounds (including fumes)
985	Toxic effect of other metals
986	Toxic effect of carbon monoxide
987	Toxic effect of other gases, fumes, or vapors
988	Toxic effect of noxious substances eaten as food
989	Toxic effect of other substances, chiefly nonmedicinal as to source
Other and unspecified effects of external causes (990-995)
990	Effects of radiation, unspecified
991	Effects of reduced temperature
992	Effects of heat and light
993	Effects of air pressure
994	Effects of other external causes
995	Certain adverse effects, not elsewhere classified
Complications of surgical and medical care, not elsewhere classified (996-999)
996	Complications peculiar to certain specified procedures
997	Complications affecting specified body systems, not elsewhere classified
998	Other complications of procedures, not elsewhere classified
999	Complications of medical care, not elsewhere classified
'''
from xml.dom.minidom import parseString
class Command(BaseCommand):
    def handle(self, *args, **options):
		for r in rows.split('\n'):
			c = r[:3]
			if c.isdigit():
				u = 'http://apps.nlm.nih.gov/medlineplus/services/mpconnect_service.cfm?mainSearchCriteria.v.c=%s' % c
				print u
				f = urllib2.urlopen(u)
				res = '\n'.join(f)
				d = parseString(res)
				e = d.getElementsByTagName('entry')




				if e:
					t = e[0].getElementsByTagName('title')[0].childNodes[0].data
					s = e[0].getElementsByTagName('summary')[0].childNodes[0].data
					l = d.getElementsByTagName('link')[0].getAttribute('href') if d.getElementsByTagName('link') else ''
					print t
					print l
					print c
					Disease.objects.create(name=t, description=s, link=l, icd9=c)
				else:
					print 'NO INFO FOR CODE ', c