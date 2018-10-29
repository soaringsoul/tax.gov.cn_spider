from sc_tax_gov_spider.MainTaxSpider import MainTaxSpider

# 指定查询的工商注册名称和纳税人识别号或社会信用代码excel文件路径
file_path = r".\example_companies.xlsx"
# 指定excel文件中表示企业名和纳税人识别号或社会信用代码的列名
excel_columns_settings = {
    "excel文件中企业名对应的列名": 'companyName',
    "excel文件中企业工商注册号码或纳税人识别号对应的列名": 'creditCode',
    # 默认不使用纳税人识别号
    'use_tax_credit_code': False
}
obj = MainTaxSpider(file_path, excel_columns_settings)
obj.crawl_main()
