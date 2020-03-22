from selenium import webdriver
import bs4
import csv


def get_top(amount, filename):
    base_url = 'https://www.worldometers.info/coronavirus/'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    page_source = browser.page_source
    soup = bs4.BeautifulSoup(page_source, 'html.parser')

    content = soup.find_all('table', {"id": "main_table_countries_today"})
    thead = content[0].find_all('thead')
    theadrows = thead[0].find_all('th')

    header = []
    for row in theadrows:
        header.append(str(row.text).replace(",","/"))

    tbody = content[0].find_all('tbody')
    tbodyrows = tbody[0].find_all('tr')
    count = 0
    bodies = []
    for row in tbodyrows:
        count = count + 1
        vals = []
        for value in row:
            if value.string != '\n':
                vals.append(str(value.string).replace(" ",""))
        bodies.append(vals)
        if count == amount:
            break

    with open(filename, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(header)
        for row in bodies:
            wr.writerow(row)


#Example of usage
#Gets the top 5 most infected countries
#Saves to "corona.csv" file, overwrites the file if already exists
get_top(5, "corona.csv")