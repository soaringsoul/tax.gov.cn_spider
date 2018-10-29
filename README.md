# 12366纳税服务平台-涉税基本信息采集程序说明

## 概述

此项目是2018年1月应公司某个项目需求查询一批四川省内企业的涉税信息，使用`python`编写的采集程序。

今天整理之前的文档，顺便测试了下，截止到今天（2018年10月29日）仍然是可以使用，所以顺便就完善下说明文档，并重新上传到github,供有需要的人后续使用。

## 采集源

[12366纳税服务平台-国家税务总局四川省税务局-涉税基本信息查询](https://12366.sc-n-tax.gov.cn/jsp/sst/menu/index.html?jbxx)

采集页面和单条企业基本信息查询结果页面示例：

![12366_tax_base_info_search_index](/screenshots/12366_tax_base_info_search_index.jpg)



## 采集程序使用说明

本程序未使用任何爬虫框架，直接使用`requests`的方法完成，使用方法：

* 安装以下依赖库

   > requests
   > pandas 
   > openpyxl
   > xlrd

* 打开`run.py`,填写你需要批量获取的企业信息的excel文件路径，并指定excel文件中：企业名和纳税人识别号的列名：

    from sc_tax_gov_spider.MainTaxSpider import MainTaxSpider
    ​	​	
    ​		# 指定查询的工商注册名称和纳税人识别号或社会信用代码excel文件路径
    ​		file_path = r"example_companies.xlsx"
    ​		# 指定excel文件中表示企业名和纳税人识别号或社会信用代码的列名
    ​		excel_columns_settings = {
    ​		    "excel文件中企业名对应的列名": 'companyName',
    ​		    "excel文件中企业工商注册号码或纳税人识别号对应的列名": 'creditCode',
    ​		    # 默认不使用纳税人识别号
    ​		    'use_tax_credit_code': False
    ​		}
    ​		obj = MainTaxSpider(file_path, excel_columns_settings)
    ​		obj.crawl_main()


* 执行 `python run.py`，即会自动采集， 

  ![running](/screenshots/running.jpg)



* 采集完成后，会将采集完成的结果写入到一个`你原始文件名_with_tax_info.xlsx`的excel文件
  直接打开即可查看

![result](/screenshots/result.jpg)



## 其他说明

本采集程序开始编写时，该网站只能使用`requests.post`方式获取数据，今天 看了下已经支持使用`requests.get`方式获取数据了。如果有需要需要批量采集从此网站采集数据，建议采用此方式。

`requests_url= https://12366.sc-n-tax.gov.cn/service/jbxxcx/getjbxxByNsrsbh?nsrsbh=&nsrmc=成都数喆数据科技有限公司`



![request.get](/screenshots/request.get.jpg)



