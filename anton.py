from selenium import webdriver
from credential import USERNAME, PASSWORD
import csv
from bs4 import BeautifulSoup

print("""
   ___   _  ____________  _  __  _____  __
  / _ | / |/ /_  __/ __ \/ |/ / / _ ) \/ /
 / __ |/    / / / / /_/ /    / / _  |\  / 
/_/ |_/_/|_/ /_/  \____/_/|_/ /____/ /_/                                                                            
    ___ _    ______   _  __    ___   _____ __  __
   /   | |  / /  _/  | |/ /   /   | / ___// / / /
  / /| | | / // /    |   /   / /| | \__ \/ /_/ / 
 / ___ | |/ // /    /   |   / ___ |___/ / __  /  
/_/  |_|___/___/   /_/|_|  /_/  |_/____/_/ /_/   
                                                                                                                                                                                                                   
""")
print(""">>INITIATING ANTON""")
print(">>LAUNCHING CHROME TO COLLECT DATA")

#DATACOLLECTOR AKA-SELENIUM
browser = webdriver.Chrome()
print(">>VISITING EDUMATE.RAOIIT.COM")
browser.get("https://edumate.raoiit.com/login/index.php")
print(">>LOGGIN IN")
browser.find_element_by_id("username").send_keys(USERNAME)
browser.find_element_by_id("password").send_keys(PASSWORD)
browser.find_element_by_id("loginbtn").click()
print(">>SEARCHING FOR TIMETABLE")
browser.find_element_by_link_text("View Week Timetable").click()
print(">>EXTRACTING HTML DATA")
timetable = browser.find_element_by_id("accordion")
newtry = timetable.get_attribute("outerHTML")
print(">>SYNCHRONIZING DATA")
fnew = open("tabledata.html", "w+")
fnew.write(newtry)
fnew.__exit__("tabledata.html")
print(">>EXITING CHROME")
browser.close()

#CONVERTING COLLECTED RESOURCES AND STORING
print(">>CONVERTING COLLECTED DATA TO CSV")
with open("tabledata.html", "r") as f:
    contents = f.read()
    outfile = open("tabledata.csv", "w", newline='')
    writer = csv.writer(outfile)
    tree = BeautifulSoup(contents, "lxml")

    dates = tree.findAll(class_="date")
    list_of_dates = [date.text for date in dates]

    try:
        table_tag = tree.select("table")[0]
        print(">>TABLE 1 FOUND")
        tab_data = [[item.text for item in row_data.select("th,td")]
                    for row_data in table_tag.select("tr")]
        writer.writerow(list_of_dates[0])
        for data in tab_data:
            writer.writerow(data)
        print(">>TABLE 1 UPDATED")
    except:
        pass

    try:
        table_tag1 = tree.select("table")[1]
        print(">>TABLE 2 FOUND")
        tab_data1 = [[item.text for item in row_data.select("th,td")]
                     for row_data in table_tag1.select("tr")]
        writer.writerow(list_of_dates[1])
        for data1 in tab_data1:
            writer.writerow(data1)
        print(">>TABLE 2 UPDATED")
    except:
        pass

    try:
        table_tag2 = tree.select("table")[2]
        print(">>TABLE 3 FOUND")
        tab_data2 = [[item.text for item in row_data.select("th,td")]
                     for row_data in table_tag2.select("tr")]
        writer.writerow(list_of_dates[2])
        for data2 in tab_data2:
            writer.writerow(data2)
        print(">>TABLE 3 UPDATED")
    except:
        pass

    try:
        table_tag3 = tree.select("table")[3]
        print(">>TABLE 4 FOUND")
        tab_data3 = [[item.text for item in row_data.select("th,td")]
                     for row_data in table_tag3.select("tr")]
        writer.writerow(list_of_dates[3])
        for data3 in tab_data3:
            writer.writerow(data3)
        print(">>TABLE 4 UPDATED")
    except:
        pass

    try:
        table_tag4 = tree.select("table")[4]
        print(">>TABLE 5 FOUND")
        tab_data4 = [[item.text for item in row_data.select("th,td")]
                     for row_data in table_tag4.select("tr")]
        writer.writerow(list_of_dates[4])
        for data4 in tab_data4:
            writer.writerow(data4)
        print(">>TABLE 5 UPDATED")
    except:
        pass

    try:
        table_tag5 = tree.select("table")[5]
        print(">>TABLE 6 FOUND")
        tab_data5 = [[item.text for item in row_data.select("th,td")]
                     for row_data in table_tag4.select("tr")]
        writer.writerow(list_of_dates[5])
        for data5 in tab_data5:
            writer.writerow(data5)
        print(">>TABLE 6 UPDATED")
    except:
        pass

    try:
        table_tag6 = tree.select("table")[6]
        print(">>TABLE 7 FOUND")
        tab_data6 = [[item.text for item in row_data.select("th,td")]
                     for row_data in table_tag6.select("tr")]
        writer.writerow(list_of_dates[6])
        for data6 in tab_data6:
            writer.writerow(data6)
        print(">>TABLE 7 UPDATED")
    except:
        pass

    outfile.__exit__("tabledata.csv")
print(">>ALL AVAILABLE TABLES UPDATED SUCCESSFULLY")

#CONVERTING EXCEL DATA INTO PIPE SEPERATED TEXT
print(">>COPYING CSV DATA INTO PIPE SEPERATED TEXT FILE")
text_list = []
with open("tabledata.csv", "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",")
        text_list.append(" | ".join(line))

with open("tabledata.txt", "w") as my_output_file:
    for line in text_list:
        my_output_file.write("" + line)
print(">>DONE")

#REMOVING UNNECESSARY DATA:
print(">>CLEANING TEXT FILE FOR FURTHER APPLICATION")
with open("tabledata.txt", "r") as f:
    lines = f.readlines()
with open("tabledata.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "From | To | Faculty | Topics/Test | Notes | Batch":
            f.write(line)
print(">>DONE")
