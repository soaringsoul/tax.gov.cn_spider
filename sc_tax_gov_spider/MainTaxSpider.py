import os
import re

import pandas as pd

from sc_tax_gov_spider.SingleTaxSpider import TaxSpider


class MainTaxSpider(object):
    def __init__(self, filepath, columns_settings):
        self.filepath = filepath
        self.ent_colname = columns_settings['excel文件中企业名对应的列名']
        self.ent_credit_colname = columns_settings['excel文件中企业工商注册号码或纳税人识别号对应的列名']
        self.use_ent_credit = columns_settings['use_tax_credit_code']
        self.write_excel_file_path = self.get_write_excel_file_path()

    def crawl_main(self):
        raw_df = pd.read_excel(r"%s" % self.filepath)
        print('采集开始！当前共有%s个企业需要采集' % raw_df.shape[0])
        print("*" * 50)
        # 读取的excel文件列名
        raw_df_columns = list(raw_df.columns)
        # 获取税务数据列名
        tax_record_columns = TaxSpider().record_lst_colname
        new_row_lst = []
        for index, row in raw_df.iterrows():
            raw_record_lst = list(row)
            ent_name = row[self.ent_colname]
            print('正在采集【%s】的涉税数据' % ent_name)
            # 设置是否使用纳税人识别号，默认不使用
            if self.use_ent_credit == False:
                ent_creditcode = ''
            else:
                ent_creditcode = row[self.ent_credit_colname]
            # 传入参数，并获取指定企业名的税务基本信息，以列表形式返回
            tax_record_lst = TaxSpider().get_tax_record(ent_name, ent_creditcode)
            print('【{ent_name}】涉税信息采集结果:\n {tax_info}'.format(ent_name=ent_name, tax_info=tax_record_lst))
            new_row_lst.append(raw_record_lst + tax_record_lst)

        new_df = pd.DataFrame(new_row_lst, columns=raw_df_columns + tax_record_columns)
        new_df.to_excel(self.write_excel_file_path, index=False)
        print("*" * 50)
        print('【采集完毕】，结果文件见\n【%s】' % self.write_excel_file_path)

    def get_write_excel_file_path(self):
        dir_path = os.path.dirname(self.filepath)
        file_name = os.path.basename(self.filepath)
        file_name = re.sub(r'.xlsx|.xls', '', file_name)
        result_file_path = os.path.join(dir_path, '%s_with_tax_info.xlsx' % file_name)

        return result_file_path


if __name__ == "__main__":
    # 指定查询的工商注册名称和纳税人识别号或社会信用代码excel文件路径
    file_path = r"../example_companies.xlsx"
    # 指定excel文件中表示企业名和纳税人识别号或社会信用代码的列名
    excel_columns_settings = {
        "excel文件中企业名对应的列名": 'companyName',
        "excel文件中企业工商注册号码或纳税人识别号对应的列名": 'creditCode',
        'use_tax_credit_code': False
    }
    obj = MainTaxSpider(file_path, excel_columns_settings)
    obj.crawl_main()
