import pandas as pd
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def generate_phone_number():
    return '08' + ''.join(random.choices(string.digits, k=10))

def generate_xpath(question_number, option_number):
    # Generate the XPath based on the given question and option numbers
    base_index = 2 + question_number  # Adjust base index for the question
    return f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{base_index}]/div/div/div[2]/div/span/div/label[{option_number}]/div[2]/div/div/div[3]/div'

def select_random_option(driver, question_number):
    # Randomly select an option for the given question number
    option_number = random.choice([4, 5])
    xpath_option = generate_xpath(question_number, option_number)
    option_element = driver.find_element("xpath", xpath_option)
    option_element.click()
    time.sleep(0.2)

def fill_form():
    data = pd.read_csv('data.csv')
    recycle = data.shape[0]
    service = Service(r"(lokasi chromedriver)")
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    
    for i in range(recycle):
        print(f"Processing row: {i}")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('link googlefrom')
        time.sleep(2)  # Increased wait time for page load

        # Mengisi Email, Nama Lengkap, NIM, Jenis Kelamin, Tahun Angkatan, dan Fakultas
        email = data.iloc[i]['email']
        inputEmail = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        inputEmail.send_keys(email)

        namalengkap = data.iloc[i]['namalengkap']
        inputNamaLengkap = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        inputNamaLengkap.send_keys(namalengkap)

        nim = str(data.iloc[i]['nim'])
        inputNim = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        inputNim.send_keys(nim)

        jeniskelamin = data.iloc[i]['jeniskelamin']
        xpath_jeniskelamin = '//*[@id="i17"]/div[3]/div/div' if jeniskelamin == 'Perempuan' else '//*[@id="i20"]/div[3]/div'
        inputJenisKelamin = driver.find_element("xpath", xpath_jeniskelamin)
        inputJenisKelamin.click()

        tahunangkatan = str(data.iloc[i]['tahunangkatan'])
        xpath_tahunangkatan = f'//*[@id="i{27 + (int(tahunangkatan) - 2020) * 3}"]/div[3]/div'
        inputTahunAngkatan = driver.find_element("xpath", xpath_tahunangkatan)
        inputTahunAngkatan.click()

        fakultas = data.iloc[i]['fakultas']
        xpath_fakultas = {
            'FIPP': '//*[@id="i43"]/div[3]/div',
            'FBS': '//*[@id="i46"]/div[3]/div',
            'FISIP': '//*[@id="i49"]/div[3]/div',
            'FMIPA': '//*[@id="i52"]/div[3]/div',
            'FT': '//*[@id="i55"]/div[3]/div',
            'FIK': '//*[@id="i58"]/div[3]/div',
            'FEB': '//*[@id="i61"]/div[3]/div',
            'FH': '//*[@id="i64"]/div[3]/div',
            'FK': '//*[@id="i67"]/div[3]/div'
        }
        inputFakultas = driver.find_element("xpath", xpath_fakultas[fakultas])
        inputFakultas.click()

        nowhatsapp = generate_phone_number()
        inputNoWhatsApp = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
        inputNoWhatsApp.send_keys(nowhatsapp)

        # Navigasi ke halaman kedua
        next_button_2 = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        next_button_2.click()
        time.sleep(1)

         # Navigasi ke halaman ketiga
        next_button_3 = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button_3.click()

        time.sleep(1)
        for question_number in range(0, 9):
            select_random_option(driver, question_number)

        # Navigasi ke halaman ketiga
        next_button_4 = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button_4.click()
        time.sleep(1)

        for question_number in range(0, 14):
            select_random_option(driver, question_number)

        # Navigasi ke halaman keempat
        next_button_5 = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button_5.click()
        time.sleep(1)

        for question_number in range(0, 7):
            select_random_option(driver, question_number)
        
         # Navigasi ke halaman keempat
        next_button_6 = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        next_button_6.click()
        time.sleep(1)

        for question_number in range(0, 13):
            select_random_option(driver, question_number)

        # Submit form
        submit_button = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
        submit_button.click()
        time.sleep(3)

        # Kembali ke form awal
        try:
            back_form = driver.find_element("xpath", '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            back_form.click()
        except:
            pass

        time.sleep(3)
        driver.quit()

fill_form()
