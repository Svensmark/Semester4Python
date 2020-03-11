from selenium import webdriver
import bs4


def get_country_data(country):
    base_url = 'https://worldpopulationreview.com'
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    search_field = browser.find_element_by_id('website-search')
    search_field.send_keys("Denmark")
    search_field.submit()
    browser.implicitly_wait(3)

    search_result = browser.find_element_by_id("search_results")
    result_table = search_result.find_element_by_id("content")
    result = result_table.find_element_by_link_text(country)
    result.click()
    browser.find_element_by_link_text(country).click()
    browser.implicitly_wait(3)

    page_source = browser.page_source
    soup = bs4.BeautifulSoup(page_source, 'html.parser')

    content = soup.find_all('div', {"class": "datatableStyles__TableContainer-bwtkle-0 dvLKHZ"})
    rows = content[2].find_all('tr')
    rows.pop(0)

    years = []

    for row in rows:
        datas = row.find_all('td')
        rowl = []
        #print(datas)
        for data in datas:   
            value = str(data)
            x = value.split(">")
            y = x[1].split("<")
            rowl.append(y[0])
        rowl.pop(len(rowl)-1)
        years.append(rowl)
        
    print(years)

get_country_data('Denmark')