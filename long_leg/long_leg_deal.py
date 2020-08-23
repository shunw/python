import pandas as pd
from functools import partial 
import re
import os
import glob

'''
purpose is to make the total score temperately. 
current this format is no need
'''

class basic_deal(object): 
    def __init__(self, apply_doc_folder, peop_info_doc, previous_2_score = None):
        self.apply_doc_folder = apply_doc_folder
        self.peop_info_doc = peop_info_doc
        self.previous_2_score = previous_2_score
        
        # self.apply_df = pd.read_csv(self.apply_doc)
        self.chld_age = 'ChildrenAge'
        self.chld_age_new = 'ChildrenAge_new'
        self.day_rep= 'DaysToReply'
        self.day_rep_new= 'DaysToReply_new'
        self.q_age_range = '孩子年龄段'
        self.q_mail_back_per = '回信周期'
        self.support = '支持人'

        self.name = 'name'
        self.name_new = 'name_new'
        self.score = 'object_score'
        self.time = 'TimeSubmitted'
        
        # 以下三项for 孩子类型得分col
        self.g = 'TargetAudience_NongCun'
        self.h = 'TargetAudience_Beijing'
        self.i = 'TargetAudience_PuTong'

        # 回信方式得分
        self.j = 'AnswerMethod'

        # 项目目标得分
        self.k = 'Mission'

        # 通信重点得分
        self.l = 'NeedToDo_JieNa'
        self.m = 'NeedToDo_JianYi'
        self.n = 'NeedToDo_LiaoJie'
        self.o = 'NeedToDo_RenGe'
        self.p = 'NeedToDo_ChengXian'

        # 烦恼的内心需求得分
        self.q = 'Needs_ShengLi'
        self.r = 'Needs_AnQuan' 
        self.s = 'Needs_GuiShu'
        self.t = 'Needs_ZunZhong'
        self.u = 'Needs_ZiWo'

        # 送物品选项得分
        self.v = 'ThingsToProvide'

        self.chld_age_min = 5
        self.chld_age_max = 14
        self.min_period = 5
        self.max_period = 7
        self.remove_word = '民大'

    def _judge_chd_age(self, row): 
        cnt = 0
        min_age = 0
        min_age_2 = 0
        max_age = 100
        age_qty = len(row[self.chld_age_new])
        if age_qty < 2: 
            
            print ('Please check the age range cell, there is only one age available!')
            print ('the name is {}'.format(row[self.name]))
            print ('the name is {}'.format(row['id']))

        for num in row[self.chld_age_new].split(','):
            if min_age == 0: 
                min_age = int(num)
                min_age_2 = int(num)
            elif int(num) < min_age: 
                min_age_2 = min_age
                min_age = int(num)
            
            if max_age == 100: 
                max_age = int(num)
                
            elif int(num) > max_age: 
                max_age = int(num)
        
        if min_age == max_age: 
            print ('Min age is same as max age, please check the age range cell!')

        if (min_age < self.chld_age_min and min_age_2 < self.chld_age_min) or max_age > self.chld_age_max: 
            return '错'
        else: 
            return '对'

    def _reply_range(self, row): 
        
        max_p = 1000
        if len(row[self.day_rep_new]) == 1:
            if int(row[self.day_rep_new]) <= self.max_period and int(row[self.day_rep_new]) >= self.min_period: 
                return '对'
            else: 
                return '错'
        elif len(row[self.day_rep_new]) == 0:
            print ('There is no number here, please check')
            print ('The row num is {}'.format(row['id']))
        else: 
            for num in row[self.day_rep_new].split(','):
                if max_p == 1000: 
                    max_p = int(num)
                elif max_p < int(num): 
                    max_p = int(num)

            if max_p <= self.max_period and max_p >= self.min_period: 
                return '对'
            else: 
                return '错'

    def _name_refine(self, row): 
        # only keep the name
        name_update = row[self.name].replace('ー', ' ')
        name_list = re.findall(r"[\w']+", str(name_update))
        if len(name_list) == 1: 
            n = name_list[0]
            if self.remove_word in n: 
                if n.replace(self.remove_word, '') in self.people_df['name_new'].unique(): 
                    return n.replace(self.remove_word, '').strip()
                else: 
                    return n.strip()
            
            else: 
                return n.strip()

        else: 
            for i in name_list: 
                if i.strip() == self.remove_word: continue
                else: 
                    return i.strip()
    
    def _name_refine_people_inf(self, row): 
        # only keep the name
        name_update = row[self.name].replace('ー', ' ')
        name_list = re.findall(r"[\w']+", str(name_update))
        if len(name_list) == 1: 
            n = name_list[0]
            return n.strip()
        else: 
            n = "".join(string for string in name_list)
            return n.strip()

    def ready_through_csv_folder(self): 
        # read through all the csv folder, and union all the data till now
        # to make the self.apply_df ready
        self.top = os.getcwd()
        folder = os.path.join(self.top, self.apply_doc_folder)
        all_files = glob.glob(folder + "/*.csv")
        li = list()
        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)

        self.apply_df = pd.concat(li, axis=0, ignore_index=True)
        
            

    def get_num_from_age(self):
        '''根据 children Age unique的结果，决定按照如下流程
        1. 去掉括号里的字
        2. 将中英文数字提取出来
        '''
        
        # 去掉括号里的字，生成新的一栏
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age].apply(lambda x: re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", str(x)))
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].apply(lambda x: re.sub(u"\\（.*?\\）|\\{.*?}|\\[.*?]", "", str(x)))


        # 提取其中的数字，转化中文，jul/ jun等为数字        
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('Apr', '4')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('Aug', '8')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('六', '6')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('Jun', '6')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('七', '7')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('Jul', '7')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('十二', '12')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('十', '10')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('十一', '11')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('十三', '13')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('十四', '14')
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].str.replace('小学', '6, 12')
        
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].apply(lambda x: re.sub('[^a-zA-Z0-9\n\.]', " ", str(x)))
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].apply(lambda x: x.split(' '))
        self.apply_df[self.chld_age_new] =  self.apply_df[self.chld_age_new].apply(lambda x: ",".join(string for string in x if len(string) > 0))

        # print (self.apply_df[self.chld_age_new].unique())
        # 选出最大数字和最小数字，看是否在 5-14 之内，如果不在，则判错，如果在，则判对
        self.apply_df[self.q_age_range] = self.apply_df.apply(self._judge_chd_age, axis = 1)
        
    def get_num_from_day_reply(self):
        '''根据 children Age unique的结果，决定按照如下流程
        1. 去掉括号里的字
        2. 将中英文数字提取出来
        '''
        
        # 去掉括号里的字，生成新的一栏
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep].apply(lambda x: re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", str(x)))
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].apply(lambda x: re.sub(u"\\（.*?\\）|\\{.*?}|\\[.*?]", "", str(x)))

        

        # 提取其中的数字，转化中文，jul/ jun等为数字        
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('一周', '7,')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('1周', '7')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('一个星期', '7,')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('一星期', '7')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('七', '7')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('三天', '3')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('两星期', '14')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('两天', '2')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('五天', '5')
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].str.replace('月', '30')
        
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].apply(lambda x: re.sub('[^a-zA-Z0-9\n\.]', " ", str(x)))
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].apply(lambda x: x.split(' '))
        self.apply_df[self.day_rep_new] =  self.apply_df[self.day_rep_new].apply(lambda x: ",".join(string for string in x if len(string) > 0))

        # 选出最大数字和最小数字，看是否在 5-7 之内，如果不在，则判错，如果在，则判对
        # print (self.apply_df[self.day_rep_new].unique())
        self.apply_df[self.q_mail_back_per] = self.apply_df.apply(self._reply_range, axis = 1)
    
    def clear_name(self): 
        # this is to clean the name, remove 民大, clear the name with 少数民族
        self.apply_df[self.name_new] =  self.apply_df.apply(self._name_refine, axis = 1)

    def _object_score(self, row): 
        # 辅助计算客观题总分
        score = 0
        if row[self.q_age_range] == '对': 
            score += 3
        if row[self.q_mail_back_per] == '对': 
            score += 3
        
        # 孩子类型得分
        if row[self.g] == 1 and row[self.h] == 1 and row[self.i] == 0: 
            score += 3
        
        # 回信方式得分
        if row[self.j] == 3:
            score += 3

        # 项目目标得分
        if row[self.k] == 2: 
            score += 10
        elif row[self.k] == 1: 
            score += 4
        elif row[self.k] == 3: 
            score += 2

        # 通信重点得分
        if row[self.l] == 1:
            score += 2
        if row[self.m] == 0:
            score += 2
        if row[self.n] == 1:
            score += 2
        if row[self.o] == 1:
            score += 2
        if row[self.p] == 1:
            score += 2

        # 烦恼的内心需求得分
        if row[self.q] == 0:
            score += 1
        if row[self.r] == 1:
            score += 1
        if row[self.s] == 1:
            score += 1
        if row[self.t] == 1:
            score += 1
        if row[self.u] == 0:
            score += 1
        
        # 送物品选项得分
        if row[self.v] == 4: 
            score += 3

        return score

    def object_test_score(self): 
        # 计算客观题的总分，按照最下面的积分规则
        self.apply_df[self.score] =  self.apply_df.apply(self._object_score, axis = 1)
    def remove_duplicate(self): 
        # 消除名字是一样的人，规则：分数取高分， 如果分数相同，取时间点为后的行
        self.apply_df = self.apply_df.sort_values(by = [self.name_new, self.score, self.time])
        self.apply_df = self.apply_df.drop_duplicates([self.name_new], keep = 'last')
    def refine_peop_doc(self):         
        # 将报名表整理成一个df，以便之后进行left join
        # 只留id/ name + 一列为民大
        self.people_df = pd.read_csv(self.peop_info_doc)
        self.people_df = self.people_df[['id', 'name', 'phone', 'email']]
        self.people_df[self.name_new] =  self.people_df.apply(self._name_refine_people_inf, axis = 1)
        self.people_df['group'] = '民大'
        
        self.people_df = self.people_df.sort_values(by = [self.name_new, 'phone', 'email'])
        self.people_df = self.people_df.drop_duplicates([self.name_new, 'phone', 'email'], keep = 'last')

        self.people_df.to_csv('people_info_update.csv', encoding = 'utf-8-sig', index = False)
        
        total_name = self.people_df[self.name_new].count()
        unique_name = len(self.people_df[self.name_new].unique())
        
        value_ind = 0
        name_counts_ls = list()
        name_counts_ind = self.people_df[self.name_new].value_counts().index
        for i in self.people_df[self.name_new].value_counts(): 
            if i > 1: 
                name_counts_ls.append(name_counts_ind[value_ind])
            value_ind += 1
        
        dup_name_df = pd.DataFrame(data = {'name_new': name_counts_ls})

        if name_counts_ls: 
            combine_df = pd.merge(dup_name_df, self.people_df, how = 'left', on = [self.name_new])
            combine_df.to_csv('diff_peop_duplicate_name.csv', encoding = 'utf-8-sig', index = False)

        if total_name != unique_name: 
            print ()
            print ('**********************')
            
            print ('There is different people with duplicate name!')
            print ('Please check the doc name is: diff_peop_duplicate_name.csv')
            print ('**********************')
            print ()

    def previous_scored(self): 
        # 将之前打过分的整理一个dataframe出来
        self.previous_score_record = pd.read_csv(self.previous_2_score)
        self.previous_score_record = self.previous_score_record[[self.name, self.support]]
        self.previous_score_record[self.name_new] = self.previous_score_record.apply(self._name_refine, axis = 1)
        self.previous_score_record.to_csv('name&support.csv', encoding = 'utf-8-sig', index = False)

    def people_group(self): 
        # this is to define which person is 民大, add a new col for it
        self.result = pd.merge(self.apply_df, self.people_df, how = 'left', on = [self.name_new])
        self.result = pd.merge(self.result, self.previous_score_record, how = 'left', on = [self.name_new])
        
    def final_run(self):
        # 将某个文件夹下的csv 文件全部导入, make self.apply_df ready
        self.ready_through_csv_folder()

        # 整理 申请人 的信息
        self.refine_peop_doc()
        
        # 整理之前分配过的人员的信息
        if self.previous_2_score: 
            self.previous_scored()

        # 整理 测试结果 的信息
        self.get_num_from_age()
        self.get_num_from_day_reply()
        self.clear_name()
        self.object_test_score()
        self.remove_duplicate()

        # 将 申请人 信息整合到 测试结果的表格中
        self.people_group()

        # 最后的result输出
        self.result.to_csv('people_test_result_refine.csv',encoding='utf-8-sig', index = False)    



def create_support_list(sup_qty, sup_name_list):
    # 按照需要支持的总数，除以人数，然后均分，生成一个csv文件用于copy paste
    sup_people_qty = len(sup_name_list)
    
    base = sup_qty // sup_people_qty
    remain = sup_qty % sup_people_qty
    
    sup_final_list = list()
    
    for v in sup_name_list:
        for i in range(base): 
            sup_final_list.append(v)

    sup_final_list.extend(sup_name_list[:remain])
    
    sup_final_list = sorted(sup_final_list)
    
    sup_final_dict = {'支持人': sup_final_list}
    df = pd.DataFrame(data = sup_final_dict)
    df.to_csv('support.csv', encoding = 'utf-8-sig', index = False)


def get_name_ls(fl_name): 
    handle = open(fl_name, encoding= 'UTF-8-SIG')
    fl_lines = handle.readlines()
    handle.close()
    res = list()
    for line in fl_lines: 
        res.append(line.strip().split('.')[1])
    return res
if __name__ == '__main__':
    '''
    -2. 确认 申请人表格 里是否有重名
    -1. 将之前分配过的志愿者的表格录入；

    0. 将之前有过的记录都整合在一张表格里（以防有的人在导入时间前后填了两遍问卷）

    1. 先整理 测试表格 里的年龄答案（提取数字，将中文替换），回信周期答案（提取数字，将中文替换），及测试人的名字（将民大字样去掉，忽略特殊字符），然后判断回答正确与否
    1-5. 将 测试表格 的重名去掉，取一个高的分数 （有可能有的人做了两份）
    2. 将 申请人表格 里的字符去掉
    
    然后将之前分配过的人名，在之后的表格中去掉

    3. 将两个表格进行left merge 按照名字col
    4. 看下有多少信需要支持，然后生成支持人csv，将名字贴进去
    '''

    # apply_doc = 'applicant_export20191214.csv'
    # apply_doc_folder = 'ready_to_score'
    # peop_doc = 'min_da_chu_xian_2019-12-14.csv'
    # previous_2_score = 'previous_assinged_2_score.csv'
    # long_leg = basic_deal(apply_doc_folder, peop_doc, previous_2_score)
    # long_leg.final_run()
    
    # sup_qty = 120
    # sup_name_fl = 'support.txt'
    # sup_name_list = get_name_ls(sup_name_fl)
    # for i in sup_name_list: 
    #     print (i.encode('utf-8-sig'))
    # create_support_list(sup_qty, sup_name_list)
    '''
    test_re
    '''
    fl = pd.read_csv('_till_1215.csv', encoding = 'utf-8-sig')
    # re_ch = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', re.UNICODE)
    
    fl['cldage_new'] = fl['ChildrenAge'].apply(lambda x: re.sub('[六]', '6', x))
    print (fl['cldage_new'].unique())
    #===============================================

    '''
    ******************************************************************
    客观题合计(满分40) 评分规则
    ******************************************************************
    [孩子年龄段] = '对', 3, 0 [5-14]
    [回信周期] = '对', 3, 0 [5-7]


    孩子类型得分
    =IF(AND(G2=1,H2=1,I2=0),Sheet2!$C$2,0)

    TRUE = 3/ FALSE = 0
    G2: TargetAudience_NongCun = 1
    H2: TargetAudience_Beijing = 1
    I2: TargetAudience_PuTong = 0 

    回信方式得分
    =IF(J2=3,Sheet2!$D$2,0)

    TRUE = 3/ FALSE = 0
    J2: AnswerMethod = 3

    项目目标得分
    =IF(K2=2,Sheet2!$E$2,IF(K2=1,Sheet2!$E$3,IF(K2=3,Sheet2!$E$4,0)))

    K2: Mission

    K2 = 2 => 10
    K2 = 1 => 4
    K2 = 3 => 2
    ELSE => 0

    通信重点得分
    =IF(L2=1,2,0)+IF(M2=0,2,0)+IF(N2=1,2,0)+IF(O2=1,2,0)+IF(P2=1,2,0)

    SUM FOLLOWING: 
    L2: NeedToDo_JieNa = 1, 2, 0
    M2: NeedToDo_JianYi = 0, 2, 0
    N2: NeedToDo_LiaoJie = 1, 2, 0
    O2: NeedToDo_RenGe = 1, 2, 0
    P2: NeedToDo_ChengXian = 1, 2, 0

    烦恼的内心需求得分
    =IF(Q2=0,1,0)+IF(R2=1,1,0)+IF(S2=1,1,0)+IF(T2=1,1,0)+IF(U2=0,1,0)

    Q2: Needs_ShengLi = 0, 1, 0
    R2: Needs_AnQuan = 1,1,0
    S2: Needs_GuiShu = 1,1,0
    T2: Needs_ZunZhong = 1,1,0
    U2: Needs_ZiWo = 0,1,0


    送物品选项得分
    =IF(V2=4,Sheet2!$H$2,0)

    V2: ThingsToProvide = 4, 3, 0

    '''