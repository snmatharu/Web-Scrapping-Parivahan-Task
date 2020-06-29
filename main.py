import requests
from lxml import html
import json
#sample function for captcha
def getcaptcha():      
    captcha='samplecaptcha'
    return captcha

#Inserting the data in form
with requests.Session() as c:
    url='https://parivahan.gov.in/rcdlstatus/?pur_cd=101'      
    dlNO='DL-0420110149646'                                    
    dob='09-02-1976'                                           
    captcha=getcaptcha()
    c.get(url)
    login_data=dict(tf_dlNO=dlNO,tf_dob_input=dob,j_idt32=captcha)
    c.post(url,data=login_data)                                 
    page=c.get('https://parivahan.gov.in')
    print(page.content)

#Getting Required Fields
pageContent=requests.get('https://parivahan.gov.in/rcdlstatus/?pur_cd=101')
tree = html.fromstring(pageContent.content)
name=tree.xpath('//*[@id="form_rcdl:j_idt124"]/table[1]/tbody/tr[2]/td[2]')
issue=tree.xpath('//*[@id="form_rcdl:j_idt124"]/table[2]/tbody/tr[1]/td[2]/text()')
expiry=tree.xpath('//*[@id="form_rcdl:j_idt124"]/table[2]/tbody/tr[1]/td[3]/text()')
vname=tree.xpath('//*[@id="form_rcdl:j_idt187_data"]/tr/td[2]')

#Input in Json
requireddata=name +issue +expiry +vname                    
with open("data.json", "r+") as file:
    data = json.load(file)
    data.update(requireddata)
    file.seek(0)
    json.dump(data, file)

