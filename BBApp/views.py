from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from pathlib import Path

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def compare(request):
	return render(request, 'compare.html', {})

def feature(request):
	return render(request, 'feature.html', {})

def Oneplus7(request):
	return render(request, 'Oneplus7.html', {})

def oneplus8t(request):
	return render(request, 'oneplus8t.html', {})

def oneplus9rt(request):
	return render(request, 'oneplus9rt.html', {})

def oneplusnord(request):
	return render(request, 'oneplusnord.html', {})

def Realmec35(request):
	return render(request, 'Realmec35.html', {})

def realmegt(request):
	return render(request, 'realmegt.html', {})

def pr1(request):
	#source1 = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70"
	source1 = "https://vlebazaar.in/OnePlus-8T-5G-12GB-RAM-256GB-Storage?gclid=CjwKCAjw9e6SBhB2EiwA5myr9j5k2ynpFRNl-sSA1xLfFI3djgmJdimE47CODUzHjoB7op9S3GOEwxoCnDMQAvD_BwE"
	source2 = "https://www.reliancedigital.in/oneplus-8t-128-gb-8-gb-ram-lunar-silver-mobile-phone/p/491901346"
	source3 = "https://shop.gadgetsnow.com/smartphones/oneplus-8t-5g-256-gb-aquamarine-green-12gb-ram-/10021/p_G201995?gclid=CjwKCAjw9e6SBhB2EiwA5myr9qdcfp-qkcyUaonV-uxImKKbYrbn5gtrxw1b4fpYazr4heVOnDm9IhoCQT4QAvD_BwE"
	wait_imp = 8
	s = Service("C:\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chromium\\chromedriver.exe")
	wd = webdriver.Chrome(service=s)
	wd.maximize_window()
	print ("*************************************************************************** \n")
	print("                     Starting Program, Please wait ..... \n")

	print ("Connecting to VLE Bazaar")
	wd.get(source1)
	wd.implicitly_wait(wait_imp)
	#f_price = wd.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div")
	f_price = wd.find_element(By.CLASS_NAME,"product-price-new")
	r_price = f_price.text
	print (" ---> Successfully retrieved the price from VLE Bazaar \n")
	time.sleep(2)
	print("Connecting to Reliance")
	wd.get(source2)
	wd.implicitly_wait(wait_imp)
	c_price = wd.find_element(By.CLASS_NAME,"pdp__offerPrice")
	raw_c = c_price.text
	print (" ---> Successfully retrieved the price from Reliance\n")
	time.sleep(2)
	print("Connecting to GADGETSNOW")
	wd.get(source3)
	wd.implicitly_wait(wait_imp)
	t_price = wd.find_element(By.CLASS_NAME,"amazon-price")
	raw_t = t_price.text
	print(raw_t)
	print (" ---> Successfully retrieved the price from GADGETSNOW\n")
	time.sleep(2)

	print ("#------------------------------------------------------------------------#")
	res=[]
	x= "Price available at VLE Bazaar is: "+r_price[1:]
	y="Price available at Reliance is: "+raw_c[1:7]
	z ="Price available at GadgetsNow is: "+raw_t[1:8]
	res.append(x)
	res.append(y)
	res.append(z)
	return render(request, 'pr1.html', {'res':res})

def pr2(request):
	source1 = "https://www.vijaysales.com/oneplus-nord-ce-2-5g-8-gb-ram-128-gb-rom-bahama-blue/19270?gclid=CjwKCAjw9e6SBhB2EiwA5myr9sGAG3p05O4yxSPxWoAIPx8YBzNxY5oca9qwUNJSKjQRzaflfqtiLxoCXGoQAvD_BwE"
	source2 = "https://www.reliancedigital.in/oneplus-nord-ce-2-5g-128-gb-8-gb-ram-blue-mobile-phone/p/492664463?gclid=CjwKCAjw9e6SBhB2EiwA5myr9vQKPKuAmfYksOLNg-jPTkC4Dh5kK2Ot2CZUp4RPXosAaPujo6UbexoC9IgQAvD_BwE"
	source3 = "https://www.customkicks.in/product/oneplus-nord-ce-2-5g-bahama-blue-8gb-128gb/"
	wait_imp = 8
	s = Service("C:\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chromium\\chromedriver.exe")
	wd = webdriver.Chrome(service=s)
	wd.maximize_window()
	print ("*************************************************************************** \n")
	print("                     Starting Program, Please wait ..... \n")

	print ("Connecting to Vijay Sales")
	wd.get(source1)
	wd.implicitly_wait(wait_imp)
	#f_price = wd.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div")
	f_price = wd.find_element(By.CLASS_NAME,"priceMRP")
	r_price = f_price.text
	print (" ---> Successfully retrieved the price from VLE Bazaar \n")
	time.sleep(2)
	print("Connecting to Reliance")
	wd.get(source2)
	wd.implicitly_wait(wait_imp)
	c_price = wd.find_element(By.CLASS_NAME,"pdp__offerPrice")
	raw_c = c_price.text
	print (" ---> Successfully retrieved the price from Reliance\n")
	time.sleep(2)
	print("Connecting to CustomKicks")
	wd.get(source3)
	wd.implicitly_wait(wait_imp)
	t_price = wd.find_element(By.CLASS_NAME,"woocommerce-Price-amount")
	raw_t = t_price.text
	print(raw_t)
	print (" ---> Successfully retrieved the price from CustomKicks\n")
	time.sleep(2)

	print ("#------------------------------------------------------------------------#")
	res2=[]
	x= "Price available at Vijay Sales is: "+r_price[3:11]
	y="Price available at Reliance is: "+raw_c[0:]
	z ="Price available at CustomKicks is: "+raw_t[0:7]
	res2.append(x)
	res2.append(y)
	res2.append(z)
	return render(request, 'pr2.html', {'res2':res2})

def pr3(request):
	source1 = "https://www.vijaysales.com/oneplus-9rt-5g-12-gb-ram-256-gb-rom-nano-silver/18683?gclid=CjwKCAjw9e6SBhB2EiwA5myr9hFXHKi1RC1QbKDfMvCmiMWLGEg-PuK2-USHWhBMA5iL2SFwCGj-exoCmeUQAvD_BwE"
	source2 = "https://www.reliancedigital.in/oneplus-9rt-5g-256-gb-12-gb-hacker-black-mobile-phone/p/492574870?gclid=CjwKCAjw9e6SBhB2EiwA5myr9hoRYHQ_Qc_dyTPfXKvt_m7xksDEUhcOa-DseELIewEJ2sERrCa61hoCY68QAvD_BwE"
	source3 = "https://www.croma.com/oneplus-9rt-5g-256gb-rom-12gb-ram-mt2111-hacker-black-/p/247072?utm_source=google&utm_medium=ps&utm_campaign=Sok_Pmax_Mobiles-OnePlus&gclid=CjwKCAjw9e6SBhB2EiwA5myr9okGPIj3ZR6gkRyKd_lwbCirviDWL6ygs4xR1a9uWlwwsqTaou0ssBoCEuoQAvD_BwE"
	wait_imp = 8
	s = Service("C:\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chromium\\chromedriver.exe")
	wd = webdriver.Chrome(service=s)
	wd.maximize_window()
	print ("*************************************************************************** \n")
	print("                     Starting Program, Please wait ..... \n")

	print ("Connecting to Vijay Sales")
	wd.get(source1)
	wd.implicitly_wait(wait_imp)
	#f_price = wd.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div")
	f_price = wd.find_element(By.CLASS_NAME,"priceMRP")
	r_price = f_price.text
	print (" ---> Successfully retrieved the price from Vijay Sales \n")
	time.sleep(2)
	print("Connecting to Reliance")
	wd.get(source2)
	wd.implicitly_wait(wait_imp)
	c_price = wd.find_element(By.CLASS_NAME,"pdp__offerPrice")
	raw_c = c_price.text
	print (" ---> Successfully retrieved the price from Reliance\n")
	time.sleep(2)
	print("Connecting to Croma")
	wd.get(source3)
	wd.implicitly_wait(wait_imp)
	t_price = wd.find_element(By.CLASS_NAME,"amount")
	raw_t = t_price.text
	print(raw_t)
	print (" ---> Successfully retrieved the price from Croma\n")
	time.sleep(2)

	print ("#------------------------------------------------------------------------#")
	res3=[]
	x= "Price available at Vijay Sales is: "+r_price[3:11]
	y="Price available at Reliance is: "+raw_c[0:]
	z ="Price available at Croma is: "+raw_t[0:]
	res3.append(x)
	res3.append(y)
	res3.append(z)
	return render(request, 'pr3.html', {'res3':res3})

def pr4(request):
	source1 = "https://vlebazaar.in/OnePlus-7-Mirror-Grey-8GB-RAM-256GB?gclid=CjwKCAjw9e6SBhB2EiwA5myr9kLkisB8U_7-yGhgth6Sd6soFXix5HC8o7NTIrZRHLmEDfWxhniLGRoCFocQAvD_BwE"
	source2 = "https://sutribomb.com/product/oneplus-7-mobile-phone-256-gb-8-gb-ram-red/"
	source3 = "https://www.kuchbhilo.in/product/oneplus-7-mobile-phone-256-gb-8-gb-ram-red/?gclid=CjwKCAjw9e6SBhB2EiwA5myr9v3n6aewy5L9sASt2jNUQseMJKUdR7rvQ-O8AN_8Dsj5AuQSHrEx1RoCvvwQAvD_BwE"
	wait_imp = 8
	s = Service("C:\\Python\\Python37\\Lib\\site-packages\\selenium\\webdriver\\chromium\\chromedriver.exe")
	wd = webdriver.Chrome(service=s)
	wd.maximize_window()
	print ("*************************************************************************** \n")
	print("                     Starting Program, Please wait ..... \n")

	print ("Connecting to VLE Bazaar")
	wd.get(source1)
	wd.implicitly_wait(wait_imp)
	#f_price = wd.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div")
	f_price = wd.find_element(By.CLASS_NAME,"product-price-new")
	r_price = f_price.text
	print (" ---> Successfully retrieved the price from VLE Bazaar \n")
	time.sleep(2)
	print("Connecting to SutriBomb")
	wd.get(source2)
	wd.implicitly_wait(wait_imp)
	c_price = wd.find_element(By.CLASS_NAME,"woocommerce-Price-amount")
	raw_c = c_price.text
	print (" ---> Successfully retrieved the price from SutriBomb\n")
	time.sleep(2)
	print("Connecting to Kuchbhilo")
	wd.get(source3)
	wd.implicitly_wait(wait_imp)
	t_price = wd.find_element(By.CLASS_NAME,"woocommerce-Price-amount")
	raw_t = t_price.text
	print(raw_t)
	print (" ---> Successfully retrieved the price from Kuchbhilo\n")
	time.sleep(2)

	print ("#------------------------------------------------------------------------#")
	res4=[]
	x= "Price available at Vijay Sales is: "+r_price[1:]
	y="Price available at SutriBomb is: "+raw_c[0:7]
	z ="Price available at Croma is: "+raw_t[0:7]
	res4.append(x)
	res4.append(y)
	res4.append(z)
	return render(request, 'pr4.html', {'res4':res4})
