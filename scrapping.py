import json
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import mysql.connector
name = "ritvik.jain.52206"
db = mysql.connector.connect(host="localhost", user="Sec_year", passwd="Second@#Pass123", database="python")
class Person:
        def __init__(self, username, name, city="Roorkee", work = []):
            self.username = username
            self.name = name
            self.city = city
            if len(work) != 0:
                self.work = work
            self.City = city[0] 
            self.Work = work[0]

        def show(self):
            show_this = "My name is {} and my current city is {}".format(self.name, self.City)
            #print(f"Checkpoint 1")
            #print(show_this)
            #print(f"Checkpoint 2")
            return show_this

def D(func):
    def inner(name):
        A=db.cursor()
        query="SELECT username FROM user WHERE username = %s"
        A.execute(query,(name,))
        B=A.fetchone()
        C=A.fetchall()
        if B==None:
            x = "Name not found!!!"
            print(x)
            return x
        else:
            x = func(name) 
            return x  
    return inner
         
@D
def scrapping(name):
    driver = webdriver.Firefox()
    driver.maximize_window()
    url="https://en-gb.facebook.com"
    driver.get(url)
    mail = driver.find_element_by_id("email")
    pswd = driver.find_element_by_id("pass")
    mail.send_keys("sakshamiitr2512@gmail.com")
    pswd.send_keys("(qwerty)")
    pswd.send_keys(Keys.RETURN)
    time.sleep(5)
    #driver.quit()
    url = url + "/" + name
    #print(soup.prettify())
    driver.get(url)
    r = requests.get(url)
    h = r.content
    soup = BeautifulSoup(h, 'lxml')
    Name = soup.title
    Name = Name.string
    #print("Name : ",Name.string) 
    url1 = url + "/about_work_and_education"
    #print(url)
    driver.get(url1)
    time.sleep(3)
    work = []
    """all_keys = driver.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v b1v8xokw oo9gr5id']")
    for span in all_keys:
        lis.append = span.text
        a = a+1
    b = 0"""
    all_values1 = driver.find_elements_by_xpath("//span[@class='nc684nl6']")
    for span in all_values1:
        work.append(span.text)
    #print("WORK :",work)
    url2 = url + "/about_places"
    driver.get(url2)
    time.sleep(3)
    city = []
    all_values2 = driver.find_elements_by_xpath("//span[@class='nc684nl6']")
    for span in all_values2:
        city.append(span.text)
    #print("CITY :",city)
    user = Person(name,Name,city,work) 
    url3 = url +"/likes"
    driver.get(url3)
    fav = ([])
    all_values3 = driver.find_elements_by_class_name('d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j keod5gw0 nxhoafnm aigsh9s9 fe6kdd0r mau55g9w c8b282yb d9wwppkn hrzyx87i jq4qci2q a3bd9o3v lrazzd5p oo9gr5id hzawbc8m')
    time.sleep(10)
    for span in all_values3:
        fav.append(span.text)
    if len(fav) == 0:
        #print("FVTS :",fav)
        pass
    else:
        #print("No favourites!!!")
        pass
    driver.quit()
    op = user.show()
    #print(op)
    return op

    #print(f"Checkpoint 4")

scrapping(name) 

"""def username():
    name=input("Enter the username:")
    check(name)

def check(name):
    A=db.cursor()
    query="SELECT username FROM user WHERE username = %s"
    A.execute(query,(name,))
    B=A.fetchone()
    if B==None:
        print("ERROR")
    else: 
        scrapping(name)"""

#print(f"Checkpoint 3")


