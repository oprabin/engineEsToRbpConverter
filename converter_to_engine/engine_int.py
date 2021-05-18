# created by oprabin on 18/05/2021.

import datetime
import json
from datetime import time

output_file = open('../output/engine_init.csv', "w+")

with open('../input/input_data.json') as input_file:
    data = json.load(input_file)
    for each_data in data:
        required_fields = [
            'claimNumber',
            'reservedField26_medical',
            'memberZipId',
            'procedureCode6',
            'procedureCode1',
            'modifier',
            'modifierCode2',
            'svcDischargeCode',
            'serviceDate',
            'endDateOfService',
            'placeOfService',
            'billedAmount',
            'procedureCode7',
            'procedureCodeDescription7',
            'memberCityId',
            'mbrStateId',
            'providerZip',
            'providerCity',
            'providerState',
            'serviceQty',
            'DiagnosisCode1',
            'DiagnosisCode2',
            'DiagnosisCode3',
            'DiagnosisCode4',
            'DiagnosisCode5',
            'DiagnosisCode6',
            'DiagnosisCode7',
            'DiagnosisCode8',
            'DiagnosisCode9',
            'DiagnosisCode10',
            'DiagnosisCode11',
            'DiagnosisCode12',
            'DiagnosisCode13',
            'DiagnosisCode14',
            'DiagnosisCode15',
            'DiagnosisCode16',
            'DiagnosisCode17',
            'DiagnosisCode18',
            'DiagnosisCode19',
            'DiagnosisCode20',
            'DiagnosisCode21',
            'DiagnosisCode22',
            'DiagnosisCode23',
            'DiagnosisCode24',
            'DiagnosisCode25',
            'memberDOB',
            'procedureCode2',
            'claimTypeId',
            'revBillTypeCode',
            'HIPPSCode',
            'procedureCode3',
            'procedureCode4',
            'memberGenderId'
        ]

        epoch_date_field = [
            'serviceDate',
            'endDateOfService',
            'memberDOB',
        ]

        data_dictionary = each_data['_source']

        for each_field in required_fields:
            if each_field in data_dictionary.keys():
                value = data_dictionary[each_field]

                if each_field in epoch_date_field:
                    value = datetime.datetime.fromtimestamp(long(data_dictionary[each_field]) / 1000).strftime(
                        '%Y-%m-%d')


            else:
                value = ''

            output_file.write("{}|".format(value))
