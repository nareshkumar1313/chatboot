from django.shortcuts import HttpResponse
from pyxlsb import open_workbook
import json
import re

def get_flightresults(request, question_id):
    print(question_id)
    text=question_id
    #text="Please provide me the details for Amex for Automation associate"
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
    c=0
    accountname=[]
    #text.lower()
    for s in text.split():
        y=s.isdigit()
        #print(y)

    Greetings = ['hi','hello','good morning','good evening','hey','bye','good bye','wassup']
    if text.lower() in Greetings:
        with open('D:\\Python\\Django\\Chatbot_CCA\\Bot\\Greetings.json', 'r') as db:
            greet = json.load(db)
            question_id = question_id.lower()
            print(greet[question_id])
            return HttpResponse(greet[question_id])
    elif"amex" in text:
        #-----------S2 FS----------------#
        if "amex" in text and "full stack" in text:
            project = 'AMERICAN EXPRESS'
            track = 'S2-FS QE'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():

                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1A Tech Avg of completed KBA=",round(kbasum/count))
            print("From T1A Tech Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From S2 Full Stack of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From S2 Full Stack of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From S2 Full Stack of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #-------------T1B Auto--------------#
        elif "amex" in text and "automation" in text:
            track = 'T1b-Automation'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From T1B Automation of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From T1B Automation of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From T1B Automation of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------S1 DA------------#
        elif "amex" in text and "digital" in text:
            track = 'S1-DA Ready'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From S1 Digital Automation of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From S1 Digital Automation of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From S1 Digital Automation of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------S1DA------------#
        elif "amex" in text and "devops" in text:
            track = 'T1c-WS & DevOps'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From DevOps of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From DevOps of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From DevOps of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------Overall Stats------------#
        elif "amex" in text and "overall" in text:
            #track = 'T1c-WS & DevOps'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project:
                        count = count +1
                        kbasum = kbasum+round((values[51]*100),1)
                        sbasum = sbasum+round((values[52]*100),1)
                        lc_cc=lc_cc+round((values[24]*100),1)
                        overall=(round((kbasum/count),1)+round((sbasum/count),1))/2
            print("Overall completed KBA=",overall)
            return HttpResponse("Overall AMERICAN EXPRESS Progress Avg="+str(round(overall))+"%")
        #------------CCA Role - Test Analyst------------#
        elif "amex" in text and "Test Analyst" in text:
            role = 'Test Analyst'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Analyst of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Analyst of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Analyst of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------CCA Role - Sr Test Analyst------------#
        elif "amex" in text and "Senior" in text:
            role = 'Sr. Test Analyst'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Sr. Test Analyst of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Sr. Test Analyst of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Sr. Test Analyst of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
         #------------CCA Role - Test Lead------------#
        elif "amex" in text and "Test Lead" in text:
            role = 'Test Lead'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Lead of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Lead of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Lead of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        elif "amex" in text and "Test Manager" in text:
            role = 'Test Manager'
            project = 'AMERICAN EXPRESS'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Manager of AMERICAN EXPRESS Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Manager of AMERICAN EXPRESS Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Manager of AMERICAN EXPRESS Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')


        #------------Associate ID------------#
        elif"amex" in text and y ==True:
            rsp=text.lower()
            assocaiteid=int(re.search(r'\d+', rsp).group())
            #assocaiteid=map(int, re.findall(r'\d+', rsp)) #- for mutiple int values
            print(assocaiteid)
            project = 'AMERICAN EXPRESS'

            file = 'D:\\Python\\CCA\\QA2QE Transform India - Weekly Progress Report.xlsb'
            wb = open_workbook(file)
            if assocaiteid is not None:
                c=0
                sheet=wb.get_sheet(4)
                for row in sheet.rows():
                    values = [r.v for r in row]
                    count = count+1
                    if(count>2):
                        values = [r.v for r in row]
                        if values[15]== project:
                            t1adata1=values[0]
                            if(t1adata1==assocaiteid):
                                LCCC=LCCC+round(values[24]*100)
                                KBA=KBA+round(values[51]*100)
                                SBA=SBA+round(values[52]*100)
                                name=values[1]
                                c+=1
                                print("LC and CC",int(LCCC),"%")
                                print("KBA",int(KBA),"%")
                                print("SBA",int(SBA),"%")
                                print("Name",name)
                                return HttpResponse("Please find the KBA details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(KBA))+'%'+'<br/>'+"Please find the SBA details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(SBA))+'%'+'<br/>'+"Please find the LC+CC details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(LCCC))+"%"+'<br/>')
                                break
                if(c==0):
                    return HttpResponse("Associate ID is not available please re-check the ID")
        elif"full stack" not in text or "automation" not in text or "devops" not in text or "digital" not in text or "overall" not in text not in text :
            return HttpResponse("Please re-check the cluster name/CCA role entered")


#---------------------------------WESTERN UNION--------------------------------

    elif"western" in text:
        #-----------S2 FS----------------#
        if "western" in text and "full stack" in text:
            project = 'WESTERN UNION'
            track = 'S2-FS QE'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1A Tech Avg of completed KBA=",round(kbasum/count))
            print("From T1A Tech Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From S2 Full Stack of WESTERN UNION Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From S2 Full Stack of WESTERN UNION Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From S2 Full Stack of WESTERN UNION Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #-------------T1B Auto--------------#
        elif "western" in text and "automation" in text:
            track = 'T1b-Automation'
            project = 'WESTERN UNION'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From T1B Automation of WESTERN UNION Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From T1B Automation of WESTERN UNION Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From T1B Automation of WESTERN UNION Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------S1 DA------------#
        elif "western" in text and "digital" in text:
            track = 'S1-DA Ready'
            project = 'WESTERN UNION'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From S1 Digital Automation of WESTERN UNION Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From S1 Digital Automation of WESTERN UNION Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From S1 Digital Automation of WESTERN UNION Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------T1a-Technical------------#
        elif "western" in text and "technical" in text:
            track = 'T1a-Technical'
            project = 'WESTERN UNION'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From T1A Tech of WESTERN UNION Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From T1A Tech of WESTERN UNION Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From T1A Tech of WESTERN UNION Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------Overall Stats------------#
        elif "western" in text and "overall" in text:
            #track = 'T1c-WS & DevOps'
            project = 'WESTERN UNION'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project:
                        count = count +1
                        kbasum = kbasum+round((values[51]*100),1)
                        sbasum = sbasum+round((values[52]*100),1)
                        lc_cc=lc_cc+round((values[24]*100),1)
                        overall=(round((kbasum/count),1)+round((sbasum/count),1))/2
            print("Overall completed KBA=",overall)
            return HttpResponse("Overall WESTERN UNION Progress Avg="+str(round(overall))+"%")
        #------------CCA Role - Test Analyst------------#
        elif "western" in text and "Test Analyst" in text:
            role = 'Test Analyst'
            project = 'WESTERN UNION'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Analyst of WESTERN UNION Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Analyst of WESTERN UNION Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Analyst of WESTERN UNION Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------CCA Role - Sr Test Analyst------------#
        elif "western" in text and "Senior" in text:
            role = 'Sr. Test Analyst'
            project = 'WESTERN UNION'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Sr. Test Analyst of WESTERN UNION Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Sr. Test Analyst of WESTERN UNION Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Sr. Test Analyst of WESTERN UNION Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
         #------------CCA Role - Test Lead------------#
        elif "western" in text and "Test Lead" in text:
            role = 'Test Lead'
            project = 'WESTERN UNION'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Lead of WESTERN UNION Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Lead of WESTERN UNION Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Lead of WESTERN UNION Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------Associate ID------------#
        elif"western" in text and y ==True:
            rsp=text.lower()
            assocaiteid=int(re.search(r'\d+', rsp).group())
            #assocaiteid=map(int, re.findall(r'\d+', rsp)) #- for mutiple int values
            print(assocaiteid)
            project = 'WESTERN UNION'

            file = 'D:\\Python\\CCA\\QA2QE Transform India - Weekly Progress Report.xlsb'
            wb = open_workbook(file)
            if assocaiteid is not None:
                c=0
                sheet=wb.get_sheet(4)
                for row in sheet.rows():
                    values = [r.v for r in row]
                    count = count+1
                    if(count>2):
                        values = [r.v for r in row]
                        if values[15]== project:
                            t1adata1=values[0]
                            if(t1adata1==assocaiteid):
                                LCCC=LCCC+round(values[24]*100)
                                KBA=KBA+round(values[51]*100)
                                SBA=SBA+round(values[52]*100)
                                name=values[1]
                                c+=1
                                print("LC and CC",int(LCCC),"%")
                                print("KBA",int(KBA),"%")
                                print("SBA",int(SBA),"%")
                                print("Name",name)
                                return HttpResponse("Please find the KBA details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(KBA))+'%'+'<br/>'+"Please find the SBA details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(SBA))+'%'+'<br/>'+"Please find the LC+CC details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(LCCC))+"%"+'<br/>')
                                break
                if(c==0):
                    return HttpResponse("Associate ID is not available please re-check the ID")
        elif"full stack" not in text or "automation" not in text or "digital" not in text or "technical" not in text or "overall" not in text not in text :
            return HttpResponse("Please re-check the cluster name/CCA role entered")


#---------------------------------DISCOVER--------------------------------
    elif"discover" in text:
        #-----------S2 FS----------------#
        if "discover" in text and "full stack" in text:
            project = 'DISCOVER'
            track = 'S2-FS QE'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1A Tech Avg of completed KBA=",round(kbasum/count))
            print("From T1A Tech Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From S2 Full Stack of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From S2 Full Stack of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From S2 Full Stack of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #-------------T1B Auto--------------#
        elif "discover" in text and "automation" in text:
            track = 'T1b-Automation'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From S2 Full Stack of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From S2 Full Stack of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From S2 Full Stack of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------S1 DA------------#
        elif "discover" in text and "digital" in text:
            track = 'S1-DA Ready'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From S1 Digital Automation of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From S1 Digital Automation of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From S1 Digital Automation of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------T1a-Technical------------#
        elif "discover" in text and "technical" in text:
            track = 'T1a-Technical'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From T1A Tech of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From T1A Tech of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From T1A Tech of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')

        #------------T1c-WS & DevOps------------#
        elif "discover" in text and "devops" in text:
            track = 'T1c-WS & DevOps'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project and values[30]== track:
                        count = count +1
                        kbasum = kbasum+float(values[51]*100)
                        sbasum = sbasum+float(values[52]*100)
                        lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From DevOps of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From DevOps of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From DevOps of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------Overall Stats------------#
        elif "discover" in text and "overall" in text:
            #track = 'T1c-WS & DevOps'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    values = [r.v for r in row]
                    if values[15]== project:
                        count = count +1
                        kbasum = kbasum+round((values[51]*100),1)
                        sbasum = sbasum+round((values[52]*100),1)
                        overall=(round((kbasum/count),1)+round((sbasum/count),1))/2
            print("Overall completed KBA=",overall)
            return HttpResponse("Overall DISCOVER Progress Avg="+str(round(overall))+"%")
        #------------CCA Role - Test Analyst------------#
        elif "discover" in text and "Test Analyst" in text:
            role = 'Test Analyst'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Analyst of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Analyst of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Analyst of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        #------------CCA Role - Sr Test Analyst------------#
        elif "discover" in text and "Senior" in text:
            role = 'Sr. Test Analyst'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Sr. Test Analyst of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Sr. Test Analyst of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Sr. Test Analyst of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
         #------------CCA Role - Test Lead------------#
        elif "discover" in text and "Test Lead" in text:
            role = 'Test Lead'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Lead of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Lead of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Lead of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')
        elif "discover" in text and "Test Manager" in text:
            role = 'Test Manager'
            project = 'DISCOVER'
            with wb.get_sheet(4) as sheet:
                 for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[15]== project and values[8]== role:
                            count = count +1
                            kbasum = kbasum+float(values[51]*100)
                            sbasum = sbasum+float(values[52]*100)
                            lc_cc=lc_cc+float(values[24]*100)
            print("From T1B Auto Avg of completed KBA=",round(kbasum/count))
            print("From T1B Auto Avg of completed SBA=",round(sbasum/count))
            print("From T1A Tech Avg of completed LC and CC=",round(lc_cc/count))
            return HttpResponse("From Test Manager of DISCOVER Account Avg completed KBA="+str(round(kbasum/count))+"%"+'<br/>'
                            +"From Test Manager of DISCOVER Account Avg completed SBA="+str(round(sbasum/count))+'%'+'<br/>'
                                +"From Test Manager of DISCOVER Account Avg completed LC+CC="+str(round(lc_cc/count))+'%')

        #------------Associate ID------------#
        elif"discover" in text and y ==True:
            rsp=text.lower()
            assocaiteid=int(re.search(r'\d+', rsp).group())
            #assocaiteid=map(int, re.findall(r'\d+', rsp)) #- for mutiple int values
            print(assocaiteid)
            project = 'DISCOVER'
            file = 'D:\\Python\\CCA\\QA2QE Transform India - Weekly Progress Report.xlsb'
            wb = open_workbook(file)
            if assocaiteid is not None:
                c=0
                sheet=wb.get_sheet(4)
                for row in sheet.rows():
                    values = [r.v for r in row]
                    count = count+1
                    if(count>2):
                        values = [r.v for r in row]
                        if values[15]== project:
                            t1adata1=values[0]
                            if(t1adata1==assocaiteid):
                                LCCC=LCCC+round(values[24]*100)
                                KBA=KBA+round(values[51]*100)
                                SBA=SBA+round(values[52]*100)
                                name=values[1]
                                c+=1
                                print("LC and CC",int(LCCC),"%")
                                print("KBA",int(KBA),"%")
                                print("SBA",int(SBA),"%")
                                print("Name",name)
                                return HttpResponse("Please find the KBA details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(KBA))+'%'+'<br/>'+"Please find the SBA details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(SBA))+'%'+'<br/>'+"Please find the LC+CC details for "+'<br/>'+str(name)+'('+str(assocaiteid)+')'+"= "+str(int(LCCC))+"%"+'<br/>')
                                break
                if(c==0):
                    return HttpResponse("Associate ID is not available please re-check the ID")
        elif"full stack" not in text or "automation" not in text or "digital" not in text or "technical" not in text or "overall" not in text not in text :
            return HttpResponse("Please re-check the cluster name/CCA role entered")
    elif"head" in text and "punit" in text:
            head = 'Punit Pandey'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[2]== head:
                            count = count +1
                            kbasum = kbasum+round((values[51]*100),1)
                            sbasum = sbasum+round((values[52]*100),1)
                            overall=(round((kbasum/count),1)+round((sbasum/count),1))/2
            print("Overall completed KBA=",overall)
            return HttpResponse("Overall Progress Avg under SBU Head Punit Pandey ="+str(round(overall))+"%")
    elif"head" in text and "kamal" in text:
            head = 'Kamal Raj Bhansali'
            with wb.get_sheet(4) as sheet:
                for row in sheet.rows():
                    c = c + 1
                    if(c>2):
                        values = [r.v for r in row]
                        if values[2]== head:
                            count = count +1
                            kbasum = kbasum+round((values[51]*100),1)
                            sbasum = sbasum+round((values[52]*100),1)
                            overall=(round((kbasum/count),1)+round((sbasum/count),1))/2
            print("Overall completed KBA=",overall)
            return HttpResponse("Overall Progress Avg under SBU Head Kamal Raj Bhansali ="+str(round(overall))+"%")


    else:
        return HttpResponse("Please enter the Correct Account/SBU Head Name you are looking for, to fectch the CCA details")

