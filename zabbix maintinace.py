from pyzabbix import ZabbixAPI
import datetime
import csv 
zurl = "http://" + "172.29.57.33"+ "/zabbix/"
zapi = ZabbixAPI(url=zurl, user="Admin", password="zabbix")
filepath = "C:\\Users\\vivek.kumar\\Desktop\\a.csv"
with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # skip the column
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                sNodename = row[0]
                sStartTime = row[1]
                sEndTime = row[2]
                sRequesterEmailAddress = row[3]
                #print(sNodename, sStartTime, sEndTime, sRequesterEmailAddress)
               # line_count += 1
            #for lines in csv_reader:
                zhost = sNodename
                starttime = sStartTime
                endtime = sEndTime
                print(zhost ,starttime ,starttime)
                print("Searching host:" + zhost + " Please wait...")
                result = zapi.host.get(selectGroups="extend", filter={"host":zhost})
                print(result)
                if result:
                    host_id = result[0]["hostid"]
                    print("Found host id {0}".format(host_id))
                    hostgroups = result[0]["groups"]
                if hostgroups:
                    hostgroupid = hostgroups[0]["groupid"]
                    print(hostgroupid)
                epochstart = datetime.datetime.strptime(starttime, "%d-%m-%Y %H:%M").timestamp().__trunc__()
                epochend = datetime.datetime.strptime(endtime, "%d-%m-%Y %H:%M").timestamp().__trunc__()
                maintenance = {
                                #"groupids": [hostgroupid],
                                "hostids": [host_id],
                                "name": zhost + " | " + starttime,
                                "maintenance_type": 0,
                                "active_since": epochstart,
                                "active_till": epochend,
                                "description": "Maintenance from Python Zabbix API",
                                "timeperiods": [{
                                "timeperiod_type": "0",
                                "start_date": epochstart,
                                "period": 3600
                                   }]
                                    }
                zapi.maintenance.create(maintenance)
