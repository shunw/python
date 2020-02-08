import requests
import json

# reference link: 
# http://cuihuan.net/wuhan/nCoV.html

def get_json_file(output_file): 
    '''
    output_file: the file name will be saved. 
    this is to get and save the json file for later usage
    '''
    response = requests.get('https://lab.isaaclin.cn/nCoV/api/area?latest=0')

    response.encoding = 'utf-8'

    json_data = json.loads(response.text)

    with open(output_file, 'w') as write_file: 
        json.dump(json_data, write_file)
class Deal_nCoV_data(object): 
    def __init__(self, input_name): 
        self.input_name = input_name

    def prepare_df(self): 
        with open(self.input_name, 'r') as read_file: 
            raw_data = json.load(read_file)

        # print (raw_data['results'][0]['provinceName'])
        print (len(raw_data['results']))
        # res_dict = todos['results']
        # print (len(res_dict[0]))

        # suc_dict = todos['success']
        # print (suc_dict)


        # print (res_dict['confirmedCount'])

    def final_run(self): 
        self.prepare_df()

if __name__ == '__main__': 
    raw_data_fl = 'nCoV_data.json'

    # # get data
    # get_json_file(raw_data_fl)

    # ana data
    nCov_stat = Deal_nCoV_data(raw_data_fl)
    nCov_stat.final_run()

    