import json
import csv

fn1 = 'preview.json'
with open(fn1) as fnObj:
    dict = json.load(fnObj)
    

dictList = [{'站號代號':dict[0]['sno'],'場站名稱':dict[0]['sna'],'場站總停車格':dict[0]['tot']},
            {'站號代號':dict[1]['sno'],'場站名稱':dict[1]['sna'],'場站總停車格':dict[1]['tot']},
            {'站號代號':dict[2]['sno'],'場站名稱':dict[2]['sna'],'場站總停車格':dict[2]['tot']},
            {'站號代號':dict[3]['sno'],'場站名稱':dict[3]['sna'],'場站總停車格':dict[3]['tot']},
            {'站號代號':dict[4]['sno'],'場站名稱':dict[4]['sna'],'場站總停車格':dict[4]['tot']},
            {'站號代號':dict[5]['sno'],'場站名稱':dict[5]['sna'],'場站總停車格':dict[5]['tot']},
            {'站號代號':dict[6]['sno'],'場站名稱':dict[6]['sna'],'場站總停車格':dict[6]['tot']},
            {'站號代號':dict[7]['sno'],'場站名稱':dict[7]['sna'],'場站總停車格':dict[7]['tot']},
            {'站號代號':dict[8]['sno'],'場站名稱':dict[8]['sna'],'場站總停車格':dict[8]['tot']},
            {'站號代號':dict[9]['sno'],'場站名稱':dict[9]['sna'],'場站總停車格':dict[9]['tot']},
            {'站號代號':dict[10]['sno'],'場站名稱':dict[10]['sna'],'場站總停車格':dict[10]['tot']},
            {'站號代號':dict[11]['sno'],'場站名稱':dict[11]['sna'],'場站總停車格':dict[11]['tot']},
            {'站號代號':dict[12]['sno'],'場站名稱':dict[12]['sna'],'場站總停車格':dict[12]['tot']},
            {'站號代號':dict[13]['sno'],'場站名稱':dict[13]['sna'],'場站總停車格':dict[13]['tot']},
            {'站號代號':dict[14]['sno'],'場站名稱':dict[14]['sna'],'場站總停車格':dict[14]['tot']},
            {'站號代號':dict[15]['sno'],'場站名稱':dict[15]['sna'],'場站總停車格':dict[15]['tot']},
            {'站號代號':dict[16]['sno'],'場站名稱':dict[16]['sna'],'場站總停車格':dict[16]['tot']},
            {'站號代號':dict[17]['sno'],'場站名稱':dict[17]['sna'],'場站總停車格':dict[17]['tot']},
            {'站號代號':dict[18]['sno'],'場站名稱':dict[18]['sna'],'場站總停車格':dict[18]['tot']},
            {'站號代號':dict[19]['sno'],'場站名稱':dict[19]['sna'],'場站總停車格':dict[19]['tot']},
            {'站號代號':dict[20]['sno'],'場站名稱':dict[20]['sna'],'場站總停車格':dict[20]['tot']},
            {'站號代號':dict[21]['sno'],'場站名稱':dict[21]['sna'],'場站總停車格':dict[21]['tot']},
            {'站號代號':dict[22]['sno'],'場站名稱':dict[22]['sna'],'場站總停車格':dict[22]['tot']},
            {'站號代號':dict[23]['sno'],'場站名稱':dict[23]['sna'],'場站總停車格':dict[23]['tot']},
            {'站號代號':dict[24]['sno'],'場站名稱':dict[24]['sna'],'場站總停車格':dict[24]['tot']},
            {'站號代號':dict[25]['sno'],'場站名稱':dict[25]['sna'],'場站總停車格':dict[25]['tot']},
            {'站號代號':dict[26]['sno'],'場站名稱':dict[26]['sna'],'場站總停車格':dict[26]['tot']},
            {'站號代號':dict[27]['sno'],'場站名稱':dict[27]['sna'],'場站總停車格':dict[27]['tot']},
            {'站號代號':dict[28]['sno'],'場站名稱':dict[28]['sna'],'場站總停車格':dict[28]['tot']},
            {'站號代號':dict[29]['sno'],'場站名稱':dict[29]['sna'],'場站總停車格':dict[29]['tot']}]

fn2 = 'preview.csv'

with open(fn2, 'w', newline = '') as csvFile:
    fields = ['站號代號', '場站名稱', '場站總停車格']
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)

    dictWriter.writeheader()
    for row in dictList:
        dictWriter.writerow(row)
