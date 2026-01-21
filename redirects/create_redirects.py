import os
import re

files = [
    'hu_ol_64', 'hu_ol_65', 'hu_ol_66', 'hu_ol_67', 'hu_ol_68', 'hu_ol_69', 'hu_ol_610',
    'hu_ol_70', 'hu_ol_71', 'hu_ol_72', 'hu_ol_73', 'hu_ol_74', 'hu_ol_75', 'hu_ol_76', 'hu_ol_77', 'hu_ol_78', 'hu_ol_79',
    'hu_centos_64', 'hu_centos_65', 'hu_centos_66', 'hu_centos_67', 'hu_centos_68', 'hu_centos_69', 'hu_centos_610',
    'hu_centos_70', 'hu_centos_71', 'hu_centos_72', 'hu_centos_73', 'hu_centos_74', 'hu_centos_75', 'hu_centos_76', 'hu_centos_77', 'hu_centos_78', 'hu_centos_79',
    'hu_rhel_64', 'hu_rhel_65', 'hu_rhel_66', 'hu_rhel_67', 'hu_rhel_68', 'hu_rhel_69', 'hu_rhel_610',
    'hu_rhel_70', 'hu_rhel_71', 'hu_rhel_72', 'hu_rhel_73', 'hu_rhel_74', 'hu_rhel_75', 'hu_rhel_76', 'hu_rhel_77', 'hu_rhel_78', 'hu_rhel_79',
    'hu_sles_12', 'hu_sles_12SP1', 'hu_sles_12SP2', 'hu_sles_12SP3', 'hu_sles_12SP4'
]

for filename in files:
    filepath = f'{filename}.adoc'
    if os.path.exists(filepath):
        content = f'''---
permalink: {filename}.html
redirect: ontap-sanhost/index.html
---'''
        with open(filepath, 'w') as f:
            f.write(content)
        print(f'Updated: {filepath}')
    else:
        print(f'Not found: {filepath}')
