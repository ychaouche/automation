from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
import sys
#ff = Firefox(capabilities={"marionette":True})

def click_on(id):
    WebDriverWait(ff,10).until(lambda x:ff.find_element_by_id(id))
    ff.find_element_by_id(id).click()

def get_price_list():
    global out
    price_list = ff.find_element_by_id("pricelist")
    rows       = price_list.find_elements_by_xpath("./tbody")[0]
    rows       = rows.get_property("innerHTML").encode("utf-8")
    out.write(rows)

    # for row in rows:
    #     pass

URL="https://csgo.steamanalyst.com/list"
URL2="https://dota2.steamanalyst.com/list"
OUTFILE="/tmp/table.xls"
out=open(OUTFILE,"w")

ff = Firefox()
ff.get(URL)
for x in xrange(10):
    raw_input("Press Enter to continue")
    get_price_list()
    ff.find_element_by_id("pricelist_next").find_elements_by_tag_name("a")[0].click()
out.close
