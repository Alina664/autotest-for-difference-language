import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_element_present(browser):
        
    browser.get(link)
    time.sleep(5)
    x = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert x is not None, 'Кнопки на странице нет!!!'
    
    