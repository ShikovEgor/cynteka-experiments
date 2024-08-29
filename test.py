import numpy as np
true = {
    "1_(12).pdf": 
    {'buyer': {'account_number': '40702810702300004449', 'taxpayer_number': '7716708608'}, 
                   'seller': {'account_number': '40702810214000000054', 'taxpayer_number': '5027096299'}},
    "Счет_на_оплату_№_МС000005503_от_17_07_2024_2_xls.pdf": 
    {'buyer': {'account_number': '7719897463', 'taxpayer_number': '30101810400000000225'},'seller': {'account_number': None, 'taxpayer_number': '9731123974'}},
    "Счет_фактура_и_УПД_06_07_24_№_4318_29_460_00_в_т_ч.pdf":
    {'buyer': {'account_number': None, 'taxpayer_number': '7805655443'},'seller': {'account_number': None, 'taxpayer_number': '5027216461'}},
    "Счет_на_оплату_№_ЦБ-7718_от_17.07.2024.pdf": 
    {'buyer': {'account_number': '40702810400000326167','taxpayer_number': '5009133727'}, 'seller': {'account_number': '30101810400000000555','taxpayer_number': '5027216461'}}}
