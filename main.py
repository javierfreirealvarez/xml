import xml.etree.ElementTree as ET
import yaml

with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

input_filename = data['exchange_rates_input_filename']
output_filename = data['exchange_rates_generated_filename']
reporting_currency = data['exchange_rates_reporting_currency']


tree = ET.parse(input_filename)



root = tree.getroot()
ccys = root.findall('./ccy_xrt')
with open(output_filename, 'w') as f:
    f.write ('<?xml version="1.0" encoding="UTF-8"?>')
    f.write('<EA_data>')
    for ccy in ccys:
        attributes = ccy.attrib
        ccy_code = attributes['ccy_code']
        curr_2 = attributes['curr_2']
        ccy_xrt_type = attributes['ccy_xrt_type']

        # Adapt
        if ccy_code == reporting_currency or curr_2 == reporting_currency:
            line = ET.tostring(ccy, encoding='unicode').replace(ccy.tail, '')
            line = line.strip()

            f.write(line)
            print(ccy)
    f.write('</EA_data>')
