import requests


class TaxSpider(object):
    def __init__(self):

        self.record_lst_colname = ['纳税人识别号', '纳税人名称', '纳税人状态', '法定代表人', '税务登记日期', '纳税人脱敏电话', '经营地址', '主营税务机关', '主营内容']

    def get_tax_record(self, entName, entCreditCode):
        res_json = self.get_res_json(entName, entCreditCode)
        tax_record_lst = self.paras_res_json(res_json)
        return tax_record_lst

    def get_res_json(self, entName, entCreditCode):
        url = "http://wsbs.sc-n-tax.gov.cn/sscx/nsrjbxx/getnsrjbxx.json"
        body_data = {
            'nsrmc': '%s' % entName,  # 企业名
            'nsrsbh': '%s' % entCreditCode,  # 企业统一社会信用代码或者纳税人识别号

        }
        headers = {
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
            'Origin': 'http',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Length': '104',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http',
            'Host': 'wsbs.sc-n-tax.gov.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'Hm_lvt_44d8b00f6bb77695a5955a28338fb3ea=1516851820; wsbs_city_code=510100; last_update_city_time=Thu%20Jan%2025%202018%2011%3A43%3A41%20GMT%2B0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4); emergency_notice_id=undefined; Hm_lpvt_44d8b00f6bb77695a5955a28338fb3ea=1516860834; sid=c74d1d1c-0bcc-4b9c-899b-8d67c17aa47c',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}

        res = requests.post(
            url=url,
            data=body_data,
            headers=headers, timeout=60)
        try:
            return res.json()
        except Exception as e:
            return {'error': e, 'code': 2018}

    def paras_res_json(self, res_json):

        raw_k_lst = ['nsrsbh', 'nsrmc', 'nsrztmc', 'fddbrxm', 'djrq', 'scjydlxdh', 'scjydz', 'swjgmc', 'jyfw']

        if res_json.get('code') == '100':
            data = res_json['data']
            tax_record_lst = [data[k] for k in raw_k_lst]
            return tax_record_lst
        else:
            try:
                message = res_json['message'][0].get('msg')
            except:
                message = res_json.get('error')
            return [message for i in range(9)]


if __name__ == "__main__":
    # 指定查询的工商注册名称和工商注册号码
    entName = ''  # 工商注册名称
    creditCode = '91510100MA61X9CU5A'  # 统一社会信用代码或者纳税人识别号
    obj = TaxSpider()
    # 税务基本信息：列表
    r_lst = obj.get_tax_record(entName=entName, entCreditCode=creditCode)
    # 税务字段名：列表
    r_col_lst = obj.record_lst_colname
    print(r_col_lst)
    print(r_lst)
