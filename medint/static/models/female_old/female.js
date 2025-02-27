MODELS['FemaleHumanAnatomy.obj'] = {
  materials: {
      "material__female_body_innereyes": { "map_Kd": "Female_eye_diffuse.jpg" },
      "material__body_outer_eyes": { "Kd": [0, 0, 0] },
      "material__female_hair": { "map_Kd": "Female_hair_diffuse.jpg" },
      "material__body_female": { "map_Kd": "Female_body_diffuse.jpg" },
      "material__femalebreasts": { "map_Kd": "Breasts_diffuse.jpg" },
      "material__circular_heart_lower": { "map_Kd": "Heart_diffuse.jpg" },
      "material__circular_heart_upper": { "map_Kd": "Heart2_diffuse.jpg" },
      "explorer_default": { "Kd": [191, 191, 191] },
      "material__circulatory_veins": { "Kd": [48, 112, 189] },
      "material__circulatory_arteries": { "Kd": [180, 32, 41] },
      "material__digestive_system": { "map_Kd": "DigestiveSystem_diffuse.jpg" },
      "material__lymphatic_system": { "map_Kd": "LymphaticSystem_diffuse.jpg" },
      "material__nervous_nerves": { "Kd": [255, 226, 68] },
      "material__nervous_cerebrum_mult": { "Kd": [239, 203, 114] },
      "material__nervous_cerebrum_mult0": { "Kd": [240, 167, 154] },
      "material__nervous_cerebrum_mult1": { "Kd": [114, 181, 237] },
      "material__nervous_cerebrum_mult2": { "Kd": [163, 191, 135] },
      "material__nervous_cerebellum": { "Kd": [161, 102, 77] },
      "material__nervous_cerebrum": { "Kd": [240, 207, 182] },
      "material__female_reproductive_s": { "map_Kd": "FemaleReproductiveSystem_diffuse.jpg" },
      "material__respiratory_system": { "map_Kd": "RespiratorySystem_diffuse.jpg" },
      "material__skeletal_skeleton": { "map_Kd": "Skeleton_diffuse.jpg" },
      "material__skeletal_skull": { "map_Kd": "Skull_diffuse.jpg" },
      "material__reproductive_system": { "map_Kd": "ReproductiveSystem_diffuse.jpg" },
      "material__urinary_system": { "map_Kd": "UrinarySystem_diffuse.jpg" },
      "material__muscular_system": { "map_Kd": "MuscularSystem_diffuse.jpg" }
  },
  decodeParams: {
    "decodeOffsets": [-25873,12,-2207,0,0,-511,-511,-511],
    "decodeScales": [0.011080,0.011080,0.011080,0.000978,0.000978,0.001957,0.001957,0.001957]
  },  urls: {
    'dbf7eec4.famale.utf8': [
      { material: 'material__body_female',
        attribRange: [0, 13934],
        indexRange: [111472, 26068],
        bboxes: 189676,
        names: ['model__female_body_skin' ],
        lengths: [78204 ]
      }
    ],
    '1a9f193b.famale.utf8': [
      { material: 'material__body_outer_eyes',
        attribRange: [0, 2432],
        indexRange: [19456, 1216],
        bboxes: 23104,
        names: ['model__female_body_r_eye_sclera', 'model__female_body_l_eye_sclera' ],
        lengths: [1824, 1824 ]
      }
    ],
    'fcd7b5ce.famale.utf8': [
      { material: 'material__circular_heart_lower',
        attribRange: [0, 274],
        indexRange: [2192, 434],
        bboxes: 3494,
        names: ['model__female_circulatory_heart' ],
        lengths: [1302 ]
      }
    ],
    'da470f80.famale.utf8': [
      { material: 'material__circular_heart_upper',
        attribRange: [0, 1056],
        indexRange: [8448, 1175],
        bboxes: 11973,
        names: ['model__female_circulatory_heart' ],
        lengths: [3525 ]
      }
    ],
    '7714bc72.famale.utf8': [
      { material: 'material__circulatory_arteries',
        attribRange: [0, 55295],
        indexRange: [442360, 27647],
        bboxes: 1042266,
        names: ['model__female_circulatory_arteries' ],
        lengths: [82941 ]
      },
      { material: 'material__circulatory_arteries',
        attribRange: [525301, 54415],
        indexRange: [960621, 27215],
        bboxes: 1042272,
        names: ['model__female_circulatory_arteries' ],
        lengths: [81645 ]
      }
    ],
    '017f0062.famale.utf8': [
      { material: 'material__circulatory_veins',
        attribRange: [0, 55295],
        indexRange: [442360, 27637],
        bboxes: 1465016,
        names: ['model__female_circulatory_veins' ],
        lengths: [82911 ]
      },
      { material: 'material__circulatory_veins',
        attribRange: [525271, 55294],
        indexRange: [967623, 27646],
        bboxes: 1465022,
        names: ['model__female_circulatory_veins' ],
        lengths: [82938 ]
      },
      { material: 'material__circulatory_veins',
        attribRange: [1050561, 43627],
        indexRange: [1399577, 21813],
        bboxes: 1465028,
        names: ['model__female_circulatory_veins' ],
        lengths: [65439 ]
      }
    ],
    'c0542429.famale.utf8': [
      { material: 'material__digestive_system',
        attribRange: [0, 15741],
        indexRange: [125928, 27040],
        bboxes: 207048,
        names: ['model__female_digestivesystem' ],
        lengths: [81120 ]
      }
    ],
    '663071d2.famale.utf8': [
      { material: 'material__female_body_innereyes',
        attribRange: [0, 2944],
        indexRange: [23552, 1472],
        bboxes: 27968,
        names: ['model__female_body_l_eye', 'model__female_body_r_eye' ],
        lengths: [2208, 2208 ]
      }
    ],
    '1a159973.famale.utf8': [
      { material: 'material__female_hair',
        attribRange: [0, 11152],
        indexRange: [89216, 5576],
        bboxes: 105944,
        names: ['model__female_body_longhair', 'model__female_body_shorthair', 'model__female_body_eyelashes' ],
        lengths: [4152, 11808, 768 ]
      }
    ],
    'd59404cc.famale.utf8': [
      { material: 'material__female_reproductive_s',
        attribRange: [0, 18620],
        indexRange: [148960, 34048],
        bboxes: 251104,
        names: ['model__female_reproductivesystem' ],
        lengths: [102144 ]
      }
    ],
    '6926444d.famale.utf8': [
      { material: 'material__femalebreasts',
        attribRange: [0, 14098],
        indexRange: [112784, 24736],
        bboxes: 186992,
        names: ['model__female_breasts_fattytissue', 'model__female_breasts_milklobules' ],
        lengths: [5760, 68448 ]
      }
    ],
    '791e3dfb.famale.utf8': [
      { material: 'material__lymphatic_system',
        attribRange: [0, 55295],
        indexRange: [442360, 27639],
        bboxes: 13400188,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82917 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [525277, 55294],
        indexRange: [967629, 27646],
        bboxes: 13400194,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [1050567, 55294],
        indexRange: [1492919, 27646],
        bboxes: 13400200,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [1575857, 55294],
        indexRange: [2018209, 27646],
        bboxes: 13400206,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [2101147, 55294],
        indexRange: [2543499, 27646],
        bboxes: 13400212,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [2626437, 55294],
        indexRange: [3068789, 27646],
        bboxes: 13400218,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [3151727, 55294],
        indexRange: [3594079, 27646],
        bboxes: 13400224,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [3677017, 55294],
        indexRange: [4119369, 27646],
        bboxes: 13400230,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [4202307, 55294],
        indexRange: [4644659, 27646],
        bboxes: 13400236,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [4727597, 55294],
        indexRange: [5169949, 27646],
        bboxes: 13400242,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [5252887, 55294],
        indexRange: [5695239, 27646],
        bboxes: 13400248,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [5778177, 55294],
        indexRange: [6220529, 27646],
        bboxes: 13400254,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [6303467, 55294],
        indexRange: [6745819, 27646],
        bboxes: 13400260,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [6828757, 55294],
        indexRange: [7271109, 27646],
        bboxes: 13400266,
        names: ['model__female_lymphaticsystem' ],
        lengths: [82938 ]
      },
      { material: 'material__lymphatic_system',
        attribRange: [7354047, 55294],
        indexRange: [7796399, 27646],
        bboxes: 13400272,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [7879337, 55294],
        indexRange: [8321689, 27646],
        bboxes: 13400278,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [8404627, 55294],
        indexRange: [8846979, 27646],
        bboxes: 13400284,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [8929917, 55294],
        indexRange: [9372269, 27646],
        bboxes: 13400290,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [9455207, 55294],
        indexRange: [9897559, 27646],
        bboxes: 13400296,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [9980497, 55294],
        indexRange: [10422849, 27646],
        bboxes: 13400302,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [10505787, 55294],
        indexRange: [10948139, 27646],
        bboxes: 13400308,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [11031077, 55294],
        indexRange: [11473429, 27646],
        bboxes: 13400314,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [11556367, 55294],
        indexRange: [11998719, 27646],
        bboxes: 13400320,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [12081657, 55294],
        indexRange: [12524009, 27646],
        bboxes: 13400326,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [12606947, 55294],
        indexRange: [13049299, 27646],
        bboxes: 13400332,
        names: ['model__female_lymphaticsystem'],
        lengths: [82938]
      },
      { material: 'material__lymphatic_system',
        attribRange: [13132237, 28197],
        indexRange: [13357813, 14125],
        bboxes: 13400338,
        names: ['model__female_lymphaticsystem'],
        lengths: [42375]
      }
    ],
    '876e1564.famale.utf8': [
      { material: 'material__muscular_system',
        attribRange: [0, 55294],
        indexRange: [442352, 93918],
        bboxes: 1306296,
        names: ['model__female_muscular_plantar_lumbricales', 'model__female_muscular_pectoralis_major', 'model__female_muscular_obliquus_externus', 'model__female_muscular_biceps_brachii', 'model__female_muscular_triceps_brachiii', 'model__female_muscular_anterior_deltoideus', 'model__female_muscular_medial_deltoideus', 'model__female_muscular_orbicularis_oculi', 'model__female_muscular_sternocleidomastoideus', 'model__female_muscular_orbicularis_oris', 'model__female_muscular_frontalis', 'model__female_muscular_auricularis', 'model__female_muscular_occipitalis', 'model__female_muscular_trapezius', 'model__female_muscular_levator_labii_superioris_alaeque_nasi', 'model__female_muscular_nasalis', 'model__female_muscular_dilator_naris', 'model__female_muscular_procerus', 'model__female_muscular_corrugator', 'model__female_muscular_zygomaticus_minor', 'model__female_muscular_zygomaticus_major', 'model__female_muscular_masseter', 'model__female_muscular_rectus_femoris', 'model__female_muscular_sartorius', 'model__female_muscular_vastus_medialis', 'model__female_muscular_vastus_lateralis', 'model__female_muscular_gastrocnemius', 'model__female_muscular_semitendinosus', 'model__female_muscular_soleus', 'model__female_muscular_tibialis_anterior', 'model__female_muscular_tensor_fascia_latae', 'model__female_muscular_peroneus_longus', 'model__female_muscular_biceps_femoris', 'model__female_muscular_plantaris', 'model__female_muscular_semimembranosus', 'model__female_muscular_gracilis', 'model__female_muscular_adductor_magnus', 'model__female_muscular_gluteus_maximus', 'model__female_muscular_gluteus_medius', 'model__female_muscular_latissimus_dorsi', 'model__female_muscular_obliquus_internus', 'model__female_muscular_infraspinatus', 'model__female_muscular_posterior_deltoideus', 'model__female_muscular_rectus_abdominus', 'model__female_muscular_transverse_abdominus', 'model__female_muscular_temporalis', 'model__female_muscular_levator_labii_superioris', 'model__female_muscular_depressor_anguli_oris', 'model__female_muscular_depressor_labii_inferioris', 'model__female_muscular_mylohyoideus', 'model__female_muscular_mentalis', 'model__female_muscular_longus_capitus', 'model__female_muscular_auricularis_posterior', 'model__female_muscular_splenius_capitis', 'model__female_muscular_caninus', 'model__female_muscular_buccinator', 'model__female_muscular_rectus_capitis_posterior_minor', 'model__female_muscular_digastricus', 'model__female_muscular_stylohyoideus', 'model__female_muscular_longus_colli', 'model__female_muscular_longissimus_capitis', 'model__female_muscular_obliquus_capitis_inferior', 'model__female_muscular_obliquus_capitis_superior', 'model__female_muscular_rectus_capitis_posterior_major', 'model__female_muscular_levator_scapulae', 'model__female_muscular_semispinalis_capitis', 'model__female_muscular_rhomboideus', 'model__female_muscular_spinalis_dorsi', 'model__female_muscular_illiocostalis_lumborum', 'model__female_muscular_serratus_posterior_superior', 'model__female_muscular_sternohyoideus', 'model__female_muscular_sternothyroideus', 'model__female_muscular_omohyoideus', 'model__female_muscular_scalenus_anterior', 'model__female_muscular_scalenus_posterior', 'model__female_muscular_thyrohyoideus', 'model__female_muscular_splenius_cervicis', 'model__female_muscular_interspinales', 'model__female_muscular_serratus_posterior_inferior', 'model__female_muscular_psoas_minor', 'model__female_muscular_psoas_major', 'model__female_muscular_quadratus_lumborum', 'model__female_muscular_transversospinales', 'model__female_muscular_levator_costarum', 'model__female_muscular_subscapularis', 'model__female_muscular_supraspinatis', 'model__female_muscular_pectoralis_minor', 'model__female_muscular_serratus_anterior'],
        lengths: [7680, 4584, 14808, 5232, 6720, 1236, 1944, 4032, 2592, 1380, 3264, 2736, 1440, 4512, 1728, 1176, 1452, 1248, 1056, 1056, 1056, 2784, 7800, 2592, 5760, 1728, 8736, 8832, 2208, 2592, 3168, 4512, 5760, 2592, 7296, 2208, 3984, 2304, 3072, 2568, 2832, 1248, 1236, 1164, 2760, 3744, 1056, 1056, 768, 2304, 528, 1056, 768, 552, 1344, 576, 672, 2208, 1056, 1440, 1824, 672, 1056, 1056, 1440, 9888, 600, 1824, 7008, 5760, 1056, 1056, 2592, 1056, 2280, 1344, 1824, 4320, 8832, 2592, 5760, 2208, 15936, 8064, 1320, 1824, 3888, 4878]
      },
      { material: 'material__muscular_system',
        attribRange: [724106, 44708],
        indexRange: [1081770, 74842],
        bboxes: 1306824,
        names: ['model__female_muscular_serratus_anterior', 'model__female_muscular_brachialis', 'model__female_muscular_teres_minor', 'model__female_muscular_teres_major', 'model__female_muscular_coracobrachialis', 'model__female_muscular_brachioradialis', 'model__female_muscular_anconeus', 'model__female_muscular_flexor_carpi_ulnaris', 'model__female_muscular_extensor_carpi_ulnaris', 'model__female_muscular_extensor_digitorum', 'model__female_muscular_flexor_digitorum_superficialis', 'model__female_muscular_extensor_carpi_radialis_longus', 'model__female_muscular_pronator_teres', 'model__female_muscular_extensor_carpi_radialis_brevis', 'model__female_muscular_palmaris_longus', 'model__female_muscular_flexor_carpi_radialis', 'model__female_muscular_flexor_pollicis_longus', 'model__female_muscular_abductor_pollicis_longus', 'model__female_muscular_extensor_pollicis_longus_and_brevis', 'model__female_muscular_pronator_quadratus', 'model__female_muscular_adductor_pollicis', 'model__female_muscular_first_dorsal_interosseus', 'model__female_muscular_opponens_pollicis', 'model__female_muscular_dorsal_intersosseus', 'model__female_muscular_hypothenar_eminence', 'model__female_muscular_lumbricales_palmares', 'model__female_muscular_interossei_palmares', 'model__female_muscular_iliacus', 'model__female_muscular_gluteus_minimus', 'model__female_muscular_adductor_longus', 'model__female_muscular_adductor_brevis', 'model__female_muscular_piriformis', 'model__female_muscular_obturator_externus', 'model__female_muscular_obturator_internus', 'model__female_muscular_quadratus_femoris', 'model__female_muscular_popliteus', 'model__female_muscular_flexor_digitorum_longus', 'model__female_muscular_tibialis_posterior', 'model__female_muscular_extensor_digitorum_longus', 'model__female_muscular_extensor_hallucis_longus', 'model__female_muscular_flexor_hallucis_longus', 'model__female_muscular_peroneus_brevis', 'model__female_muscular_peroneus_tertius', 'model__female_muscular_extensor_digitorum_brevis', 'model__female_muscular_abductor_hallucis', 'model__female_muscular_flexor_digitorum_brevis', 'model__female_muscular_quadratus_plantae', 'model__female_muscular_abductor_digiti_minimi', 'model__female_muscular_dorsal_plantar_interossei', 'model__female_muscular_flexor_digiti', 'model__female_muscular_plantar_interossei', 'model__female_muscular_flexor_hallucis_brevis', 'model__female_muscular_adductor_hallucis', 'model__female_muscular_pectineus'],
        lengths: [3570, 1824, 1248, 1248, 1824, 2016, 1056, 1824, 2976, 13392, 20568, 2592, 1824, 2208, 4224, 2208, 3744, 2208, 4968, 168, 1632, 1824, 1440, 10944, 3264, 7296, 12768, 2112, 3840, 1056, 1056, 1056, 4224, 2928, 672, 1440, 11640, 2976, 9336, 2976, 4512, 2592, 1824, 8184, 1824, 16920, 2592, 2208, 7296, 1248, 4320, 3648, 6144, 1044]
      }
    ],
    '0ad76020.famale.utf8': [
      { material: 'material__nervous_cerebellum',
        attribRange: [0, 55294],
        indexRange: [442352, 109446],
        bboxes: 1048160,
        names: ['model__female_nervous_cerebellum_dont_subdivide'],
        lengths: [328338]
      },
      { material: 'material__nervous_cerebellum',
        attribRange: [770690, 20052],
        indexRange: [931106, 39018],
        bboxes: 1048166,
        names: ['model__female_nervous_cerebellum_dont_subdivide'],
        lengths: [117054]
      }
    ],
    'e65f9dfa.famale.utf8': [
      { material: 'material__nervous_cerebrum',
        attribRange: [0, 21506],
        indexRange: [172048, 43008],
        bboxes: 301072,
        names: ['model__female_nervous_cerebrum'],
        lengths: [129024]
      }
    ],
    '340f14bb.famale.utf8': [
      { material: 'material__nervous_cerebrum_mult',
        attribRange: [0, 6378],
        indexRange: [51024, 12216],
        bboxes: 87672,
        names: ['model__female_nervous_cerebrum_multicolor'],
        lengths: [36648]
      }
    ],
    '726010e8.famale.utf8': [
      { material: 'material__nervous_cerebrum_mult0',
        attribRange: [0, 8240],
        indexRange: [65920, 15912],
        bboxes: 113656,
        names: ['model__female_nervous_cerebrum_multicolor'],
        lengths: [47736]
      }
    ],
    '869f583e.famale.utf8': [
      { material: 'material__nervous_cerebrum_mult1',
        attribRange: [0, 5399],
        indexRange: [43192, 10200],
        bboxes: 73792,
        names: ['model__female_nervous_cerebrum_multicolor'],
        lengths: [30600]
      }
    ],
    '23d1a67c.famale.utf8': [
      { material: 'material__nervous_cerebrum_mult2',
        attribRange: [0, 2551],
        indexRange: [20408, 4680],
        bboxes: 34448,
        names: ['model__female_nervous_cerebrum_multicolor'],
        lengths: [14040]
      }
    ],
    'c054655d.famale.utf8': [
      { material: 'material__nervous_nerves',
        attribRange: [0, 24827],
        indexRange: [198616, 44730],
        bboxes: 332806,
        names: ['model__female_nervous_nerves', 'model__female_nervous_medulla_caudate_nucleus', 'model__female_nervous_amygdala'],
        lengths: [112440, 8598, 13152]
      }
    ],
    'adb873be.famale.utf8': [
      { material: 'material__reproductive_system',
        attribRange: [0, 155],
        indexRange: [1240, 232],
        bboxes: 1936,
        names: ['model__female_urinary_bladder'],
        lengths: [696]
      }
    ],
    '1dd6f429.famale.utf8': [
      { material: 'material__respiratory_system',
        attribRange: [0, 12852],
        indexRange: [102816, 22288],
        bboxes: 169680,
        names: ['model__female_respiratory_lungs', 'model__female_respiratory_epiglotis', 'model__female_respiratory_larynx_trachea_bronchus', 'model__female_respiratory_diaphragm'],
        lengths: [13056, 5424, 45240, 3144]
      }
    ],
    '6c9109bc.famale.utf8': [
      { material: 'material__skeletal_skeleton',
        attribRange: [0, 47124],
        indexRange: [376992, 80474],
        bboxes: 618414,
        names: ['model__female_skeletal_tarsal', 'model__female_skeletal_cervical_vertebra', 'model__female_skeletal_humerus', 'model__female_skeletal_radius', 'model__female_skeletal_ulna', 'model__female_skeletal_phalanges_hand', 'model__female_skeletal_metacarpal', 'model__female_skeletal_carpal', 'model__female_skeletal_femur', 'model__female_skeletal_patella', 'model__female_skeletal_tibia', 'model__female_skeletal_fibula', 'model__female_skeletal_pelvis', 'model__female_skeletal_pubis', 'model__female_skeletal_sacrum', 'model__female_skeletal_vertebral_column', 'model__female_skeletal_sternum', 'model__female_skeletal_clavicle', 'model__female_skeletal_scapula', 'model__female_skeletal_ribs', 'model__female_skeletal_malleolus', 'model__female_skeletal_calcaneus', 'model__female_skeletal_phalanges_foot', 'model__female_skeletal_metatarsal'],
        lengths: [5592, 17982, 5808, 3384, 2880, 10536, 4992, 4224, 7632, 1176, 6576, 2376, 18660, 300, 4092, 83028, 8856, 2688, 10572, 16968, 3528, 3432, 8184, 7956]
      }
    ],
    '05447aa5.famale.utf8': [
      { material: 'material__skeletal_skull',
        attribRange: [0, 16264],
        indexRange: [130112, 27928],
        bboxes: 213896,
        names: ['model__female_skeletal_teeth_lower', 'model__female_skeletal_cranium', 'model__female_skeletal_mandible', 'model__female_skeletal_teeth_upper'],
        lengths: [27024, 24144, 10536, 22080]
      }
    ],
    'bdeec8e8.famale.utf8': [
      { material: 'material__urinary_system',
        attribRange: [0, 1942],
        indexRange: [15536, 3520],
        bboxes: 26096,
        names: ['model__female_urinary_kidneys'],
        lengths: [10560]
      }
    ]
  }
};
