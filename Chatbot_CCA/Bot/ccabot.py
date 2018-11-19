from pyxlsb import open_workbook
import re
import json

text="Please provide me the details for amex for tech associate"
file = 'D:\\Python\\CCA\\QA2QE Transform India - Weekly Progress Report.xlsb'
wb = open_workbook(file)
count=0
kbasum=float(0)
sbasum=float(0)
lc_cc=float(0)
t1adata1=0
LCCC=float(0)
KBA=float(0)
SBA=float(0)
values=int(0)
accountname=[]

for s in text.split():
    s.lower()
    y=s.isdigit()
    #print(y)
    Greetings = ['hi','hello','good morning','good evening','hey','bye','good bye','wassup']
    if text.lower() in Greetings:
        with open('D:\\Python\\Django\\Chatbot_CCA\\Bot\\Greetings.json', 'r') as db:
            greet = json.load(db)
            question_id = question_id.lower()
            print(greet[question_id])
            #return HttpResponse(greet[question_id])
    elif"amex" in s:
        #-----------S2-FS----------------#
        if "amex" in text and "tech" in text:
            project = 'AMERICAN EXPRESS'
            track = 'S2-FS QE'
            with wb.get_sheet(4) as sheet:

                for row in sheet.rows():

                    values = [r.v for r in row]
                    t1adata1=values[15]
                    if values[16]== project and values[31]== track:

                        count = count +1
                        kbasum = kbasum+float(values[52]*100)
                        sbasum = sbasum+float(values[53]*100)
                        lc_cc=lc_cc+float(values[25]*100)
            print("From T1A Tech Avg of completed KBA=",round(kbasum/count))
            print("From T1A Tech Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))

        #-------------T1B Auto--------------#
        elif "amex" in text and "automation" in text:
            track = 'T1b-Automation'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[32]== project and values[14]== track:
                        count = count +1
                        kbasum = kbasum+float(values[136]*100)
                        sbasum = sbasum+float(values[138]*100)
                        lc_cc=lc_cc+float(values[167]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))

          #-------------S1-DA Ready--------------#
        elif "amex" in text and "s1da" in text:
            track = 'S1-DA Ready'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[32]== project and values[14]== track:
                        count = count +1
                        kbasum = kbasum+float(values[136]*100)
                        sbasum = sbasum+float(values[138]*100)
                        lc_cc=lc_cc+float(values[167]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
          #-------------Dev Ops--------------#
        elif "amex" in text and "devops" in text:
            track = 'T1c-WS & DevOps'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[32]== project and values[14]== track:
                        count = count +1
                        kbasum = kbasum+float(values[136]*100)
                        sbasum = sbasum+float(values[138]*100)
                        lc_cc=lc_cc+float(values[167]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))


           #-------------Associate ID--------------#
        elif"amex" in text and y is True:
            rsp=text.lower()
            assocaiteid=int(re.search(r'\d+', rsp).group())
            print(assocaiteid)
            file = 'D:\\Python\\CCA\\QA2QE Transform India - Weekly Progress Report.xlsb'
            wb = open_workbook(file)
            if assocaiteid is not None:
                c=0
                sheet=wb.get_sheet(4)
                for row in sheet.rows():
                    values = [r.v for r in row]
                    count = count+1
                    if(count>2):
                        t1adata1=values[0]
                        if(t1adata1==assocaiteid):
                            LCCC=LCCC+round(values[167]*100)
                            KBA=KBA+round(values[136]*100)
                            SBA=SBA+round(values[138]*100)
                            name=values[1]
                            c+=1
                            print("LC and CC",int(LCCC),"%")
                            print("KBA",int(KBA),"%")
                            print("SBA",int(SBA),"%")
                            print("Name",name)
                            break
                if(c==0):
                    print("Associate ID is not available please re-check the ID")
        elif"Tech" not in text or "Automation" not in text or "DevOps" not in text or "Digital Automation" not in text or "Full Stack" not in text or "Overall" not in text or "all clusters" not in text :
            print("Please re-check the cluster name")