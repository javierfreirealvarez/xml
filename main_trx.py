import xml.etree.ElementTree as ET

import yaml

with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

input_filename = data['transaction_input_filename']
output_filename = data['transaction_generated_filename']

tree = ET.parse(input_filename)



root = tree.getroot()
trxs = root.findall('./trx')
with open(output_filename, 'w') as f:
    for trx in trxs:
        attributes = trx.attrib
        trx_type_NL = attributes['trx_type_NL']
        if trx_type_NL == 'Increase':
            #add value to the line
            line = ET.tostring(trx, encoding='unicode').replace(trx.tail, '')
            line = line.strip()

            f.write(line)
            print(trx)


