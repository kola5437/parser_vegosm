# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
from xml.dom import minidom
import datetime
import time
from progress.bar import IncrementalBar


FILE = 'vegosm'


number = 1
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://www.vegosm.ru'

num = 1

today = datetime.datetime.today()
time1 = today.strftime("%Y-%m-%d %H:%M:%S")

URL = ['https://www.vegosm.ru/catalog/stroymaterialy/gipsokarton/?PAGEN_1={0}','https://www.vegosm.ru/catalog/stroymaterialy/profili_ugolki_i_mayaki/?PAGEN_1={0}','https://www.vegosm.ru/catalog/stroymaterialy/listovye_materialy/fanera/?PAGEN_1={0}',
'https://www.vegosm.ru/catalog/stroymaterialy/listovye_materialy/dsp/?PAGEN_1={0}','https://www.vegosm.ru/catalog/stroymaterialy/listovye_materialy/dvp/?PAGEN_1={0}','https://www.vegosm.ru/catalog/stroymaterialy/kirpichi/?PAGEN_1={0}',
'https://www.vegosm.ru/catalog/stroymaterialy/listovye_materialy/osb_plita/?PAGEN_1={0}','https://www.vegosm.ru/catalog/sukhie_smesi/shtukaturka/?PAGEN_1={0}','https://www.vegosm.ru/catalog/sukhie_smesi/shpatlevka/?PAGEN_1={0}',
'https://www.vegosm.ru/catalog/sukhie_smesi/tsement/?PAGEN_1={0}','https://www.vegosm.ru/catalog/sukhie_smesi/nalivnye_poly/?PAGEN_1={0}','https://www.vegosm.ru/catalog/sukhie_smesi/kley_plitochnyy/?PAGEN_1={0}',
'https://www.vegosm.ru/catalog/stroymaterialy/pilomaterial/brusok/?PAGEN_1={0}','https://vegosm.ru/catalog/stroymaterialy/pilomaterial/doska_pola/?PAGEN_1={0}','https://vegosm.ru/catalog/stroymaterialy/pilomaterial/vagonka/?PAGEN_1={0}',
'https://vegosm.ru/catalog/dveri_i_okna/pogonazh_mezhkomnatnykh_dverey/?PAGEN_1={0}','https://vegosm.ru/catalog/stroymaterialy/pilomaterial/brusok/?PAGEN_1={0}','https://vegosm.ru/catalog/napolnye_pokrytiya/plintus/?PAGEN_1={0}',
'https://vegosm.ru/catalog/krepezhnye_izdeliya/perforirovannyy_krepezh/?PAGEN_1={0}','https://vegosm.ru/catalog/teploshumoizolyatsiya/utepliteli/bazaltovye_utepliteli/?PAGEN_1={0}','https://vegosm.ru/catalog/teploshumoizolyatsiya/penoplast/?PAGEN_1={0}',
'https://vegosm.ru/catalog/teploshumoizolyatsiya/plenka/?PAGEN_1={0}','https://vegosm.ru/catalog/teploshumoizolyatsiya/porolon/?PAGEN_1={0}','https://vegosm.ru/catalog/teploshumoizolyatsiya/paklya/?PAGEN_1={0}',
'https://vegosm.ru/catalog/elektrika/elektrody/?PAGEN_1={0}','https://vegosm.ru/catalog/stroymaterialy/pechnoe_lite/?PAGEN_1={0}','https://vegosm.ru/catalog/stroymaterialy/trotuarnye_pokrytiya/?PAGEN_1={0}',
'https://vegosm.ru/catalog/krovlya_i_sayding/metallocherepitsa/?PAGEN_1={0}','https://vegosm.ru/catalog/krovlya_i_sayding/ondulin/?PAGEN_1={0}','https://vegosm.ru/catalog/krovlya_i_sayding/shifer/?PAGEN_1={0}',
'https://vegosm.ru/catalog/krovlya_i_sayding/sayding/?PAGEN_1={0}','https://vegosm.ru/catalog/stroymaterialy/profnastil/?PAGEN_1={0}','https://vegosm.ru/catalog/krovlya_i_sayding/vodostok/?PAGEN_1={0}',
'https://vegosm.ru/catalog/krovlya_i_sayding/gibkaya_cherepitsa/?PAGEN_1={0}','https://vegosm.ru/catalog/lakokrasochnye_materialy/izvest/?PAGEN_1={0}','https://vegosm.ru/catalog/lakokrasochnye_materialy/kolera/?PAGEN_1={0}',
'https://vegosm.ru/catalog/lakokrasochnye_materialy/gotovaya_shpatlevka/?PAGEN_1={0}','https://vegosm.ru/catalog/lakokrasochnye_materialy/emal/?PAGEN_1={0}','https://vegosm.ru/catalog/lakokrasochnye_materialy/gruntovka/?PAGEN_1={0}',
'https://vegosm.ru/catalog/lakokrasochnye_materialy/lak/?PAGEN_1={0}','https://vegosm.ru/catalog/lakokrasochnye_materialy/olifa/?PAGEN_1={0}','https://vegosm.ru/catalog/napolnye_pokrytiya/laminat/?PAGEN_1={0}',
'https://vegosm.ru/catalog/napolnye_pokrytiya/linoleum/?PAGEN_1={0}','https://vegosm.ru/catalog/napolnye_pokrytiya/plitka_pvkh/?PAGEN_1={0}','https://vegosm.ru/catalog/napolnye_pokrytiya/plintus/?PAGEN_1={0}',
'https://vegosm.ru/catalog/napolnye_pokrytiya/porogi/?PAGEN_1={0}','https://vegosm.ru/catalog/plitka/keramicheskaya_plitka/kerama_marazzi/kovry/?PAGEN_1={0}','https://vegosm.ru/catalog/napolnye_pokrytiya/kovrolin/?PAGEN_1={0}',
'https://vegosm.ru/catalog/napolnye_pokrytiya/gryazezashchita/?PAGEN_1={0}','https://vegosm.ru/catalog/oboi_i_dekor/oboi/steklooboi/?PAGEN_1={0}','https://vegosm.ru/catalog/oboi_i_dekor/oboi/fotooboi/?PAGEN_1={0}',
'https://vegosm.ru/catalog/dveri_i_okna/mezhkomnatnye_dveri/?PAGEN_1={0}','https://vegosm.ru/catalog/dveri_i_okna/vkhodnye_dveri/?PAGEN_1={0}','https://vegosm.ru/catalog/dveri_i_okna/pogonazh_mezhkomnatnykh_dverey/?PAGEN_1={0}',
'https://vegosm.ru/catalog/plitka/keramicheskaya_plitka/alma_ceramica/alva/?PAGEN_1={0}','https://vegosm.ru/catalog/osveshchenie/lyustry_i_svetilniki/?PAGEN_1={0}','https://vegosm.ru/catalog/osveshchenie/sadovo_parkovoe_osveshchenie/?PAGEN_1={0}',
'https://vegosm.ru/catalog/otoplenie_i_vodosnabzhenie/vodonagrevateli/?PAGEN_1={0}','https://vegosm.ru/catalog/santekhnika/vanny/?PAGEN_1={0}','https://vegosm.ru/catalog/santekhnika/dushevye_kabiny/?PAGEN_1={0}',
'https://vegosm.ru/catalog/santekhnika/mebel_dlya_vannoy/?PAGEN_1={0}','https://vegosm.ru/catalog/santekhnika/polotentsesushiteli/?PAGEN_1={0}','https://vegosm.ru/catalog/santekhnika/moyki/?PAGEN_1={0}',
'https://vegosm.ru/catalog/santekhnika/smesiteli/?PAGEN_1={0}','https://vegosm.ru/catalog/elektrika/batareyki_i_akkumulyatory/?PAGEN_1={0}','https://vegosm.ru/catalog/elektroinstrumenty/betonomeshalki/?PAGEN_1={0}',
'https://vegosm.ru/catalog/elektroinstrumenty/dreli/?PAGEN_1={0}','https://vegosm.ru/catalog/elektroinstrumenty/kompressory/?PAGEN_1={0}','https://vegosm.ru/catalog/elektroinstrumenty/lobziki/?PAGEN_1={0}',
'https://vegosm.ru/catalog/elektroinstrumenty/pily_tsirkulyarnye/?PAGEN_1={0}','https://vegosm.ru/catalog/elektroinstrumenty/rubanki/?PAGEN_1={0}','https://vegosm.ru/catalog/elektroinstrumenty/svarochnye_apparaty/?PAGEN_1={0}',
'https://vegosm.ru/catalog/elektroinstrumenty/feny_tekhnicheskie/?PAGEN_1={0}','https://vegosm.ru/catalog/elektroinstrumenty/shlifmashiny/?PAGEN_1={0}','https://vegosm.ru/catalog/elektroinstrumenty/shurupoverty/?PAGEN_1={0}',
'https://vegosm.ru/catalog/klimaticheskoe_oborudovanie/ventilyatsiya/?PAGEN_1={0}','https://vegosm.ru/catalog/klimaticheskoe_oborudovanie/greyushchie_kabeli/?PAGEN_1={0}','https://vegosm.ru/catalog/elektrika/rozetki_i_vyklyuchateli/?PAGEN_1={0}',
'https://vegosm.ru/catalog/otoplenie_i_vodosnabzhenie/vodoschetchiki/?PAGEN_1={0}','https://vegosm.ru/catalog/elektrika/udliniteli_i_setevye_filtry/?PAGEN_1={0}','https://vegosm.ru/catalog/klimaticheskoe_oborudovanie/teplyy_pol/?PAGEN_1={0}',
'https://vegosm.ru/catalog/elektroinstrumenty/lazernye_dalnomery/?PAGEN_1={0}','https://vegosm.ru/catalog/instrumenty/verevki_kanaty_i_shnury/?PAGEN_1={0}','https://vegosm.ru/catalog/instrumenty/lestnitsy_stremyanki_i_stellazhi/?PAGEN_1={0}',
'https://vegosm.ru/catalog/instrumenty/sredstva_zashchity/?PAGEN_1={0}','https://vegosm.ru/catalog/instrumenty/meshki_polipropilenovye/?PAGEN_1={0}','https://vegosm.ru/catalog/klimaticheskoe_oborudovanie/ventilyatsiya/?PAGEN_1={0}',
'https://vegosm.ru/catalog/krepezhnye_izdeliya/samorezy/?PAGEN_1={0}','https://vegosm.ru/catalog/krepezhnye_izdeliya/ankera/?PAGEN_1={0}','https://vegosm.ru/catalog/krepezhnye_izdeliya/gvozdi/?PAGEN_1={0}',
'https://vegosm.ru/catalog/krepezhnye_izdeliya/dyubeli/?PAGEN_1={0}','https://vegosm.ru/catalog/krepezhnye_izdeliya/zaklepki/?PAGEN_1={0}','https://vegosm.ru/catalog/krepezhnye_izdeliya/perforirovannyy_krepezh/?PAGEN_1={0}',
'https://vegosm.ru/catalog/krepezhnye_izdeliya/takelazh/?PAGEN_1={0}','https://vegosm.ru/catalog/dveri_i_okna/zamok_vreznoy/?PAGEN_1={0}','https://vegosm.ru/catalog/instrumenty/lenty_skotchi_i_serpyanki/?PAGEN_1={0}',
'https://vegosm.ru/catalog/pena_klei_germetiki/pena_montazhnaya/?PAGEN_1={0}','https://vegosm.ru/catalog/pena_klei_germetiki/germetiki/?PAGEN_1={0}','https://vegosm.ru/catalog/pena_klei_germetiki/kley/?PAGEN_1={0}',
'https://vegosm.ru/catalog/oboi_i_dekor/karnizy_dlya_shtor/?PAGEN_1={0}','https://vegosm.ru/catalog/tovary_dlya_doma/tekstil/?PAGEN_1={0}','https://vegosm.ru/catalog/mebel/spalni_i_korpusnaya_mebel/?PAGEN_1={0}',
'https://vegosm.ru/catalog/santekhnika/aksessuary_dlya_vannoy/?PAGEN_1={0}','https://vegosm.ru/catalog/stroymaterialy/polikarbonat/?PAGEN_1={0}','https://vegosm.ru/catalog/dacha_i_sad/teplitsy_i_parniki/?PAGEN_1={0}',
'https://vegosm.ru/catalog/dveri_i_okna/okna_pvkh/?PAGEN_1={0}']
id = ['152','154','153','146','150','151','155','139','141'
      '144','145','143','142','159','157','158','156','161',
      '166','164','178','179','177','176','181','182','184',
      '131','198','197','196','193','192','186','187','211',
      '210','209','206','205','214','213','222','226','225',
      '227','229','223','221','220','237','234','241','246',
      '243','247','256','252','263','267','266','264','262',
      '261','258','281','283','279','280','278','275','276',
      '272','273','270','269','286','292','295','289','288',
      '294','297','301','300','298','296','304','312','314',
      '313','310','311','309','307','323','322','332','331',
      '330','336','342','333','343','353','345','173']
list_data = []
b = '1'
categories = ''
n = 0
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def parser_first():
    global url_for_parser
    bar = IncrementalBar('Прогресс ', max = len(URL))

    global id_num
    global n
    for items in URL:
        bar.next()

        id_num = id[n]
        n += 1
        url_for_parser = items
        url = items.format('1')
        html = get_html(url)
        if html.status_code == 200:
            get_page(html.text)
        else:
            pass
def get_page(html):
    global page
    global number_for
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all('div',class_='nums')
    if pages:
        for item in pages:
            page_num = item.find_all('a',class_='dark_link')
            page = int(page_num[-1].get_text())    
    else:
    
        page = 1
    number_for = page
    parser_links(page)

def parser_links(page):
    global num
    num = 1
    for i in range(page):
        url_list = url_for_parser.format(num)
        num += 1
        html = get_html(url_list)
        if html.status_code == 200:
            get_links(html.text)
        else:
            pass
            

def get_links(html):
    global link
    global categories
    soup = BeautifulSoup(html, 'html.parser')
    
    categories_list = soup.find_all('h1', id='pagetitle')
    categories = categories_list[0].get_text()

    pages = soup.find_all('div', class_='image_wrapper_block')
    for item in pages:
        link = HOST + item.find('a',class_='thumb shine').get('href')
        parser(link)

def parser(link):
   
    html = get_html(link)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Повторное подключение')
        time.sleep(2)
        return 1    


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    img = HOST + soup.find('link',itemprop="image").get('href') # Фотография товара
    title = soup.find('div',class_='preview_text dotdot').get_text() # Название товара
    price = soup.find('span',class_='price_value').get_text() # Цена

   

    # Добавление хар-тик
    specifications_list = soup.find_all('tr',itemprop='additionalProperty')
    if len(specifications_list) == 1: # Если такая форма есть
        char_value = specifications_list[0].find('td',class_='char_value').get_text()
        char_name = specifications_list[0].find('td',class_='char_name').get_text()
        char_name1 = ''
        char_value1 = ''
        char_value3 = ''
        char_name3 = ''
    elif len(specifications_list) == 2:
        char_value1 = specifications_list[1].find('td',class_='char_value').get_text()
        char_name1 = specifications_list[1].find('td',class_='char_name').get_text()
        char_value = specifications_list[0].find('td',class_='char_value').get_text()
        char_name = specifications_list[0].find('td',class_='char_name').get_text()
        char_value3 = ''
        char_name3 = ''
    elif len(specifications_list) == 3:
        char_value1 = specifications_list[1].find('td',class_='char_value').get_text()
        char_name1 = specifications_list[1].find('td',class_='char_name').get_text()
        char_value = specifications_list[0].find('td',class_='char_value').get_text()
        char_name = specifications_list[0].find('td',class_='char_name').get_text()    
        char_value3 = specifications_list[2].find('td',class_='char_value').get_text()
        char_name3 = specifications_list[2].find('td',class_='char_name').get_text()  
        
    else:
        char_name1 = ''
        char_value1 = ''
        char_name = ''
        char_value = ''
        char_value3 = ''
        char_name3 = ''
    # Добавление описание
    description_list = soup.find_all('div',id='descr')
    if len(description_list) != 0: # Если такая форма есть
        for item in description_list:
            description_text = item.find('div',class_='detail_text').get_text()
    else:
        description_text = ''
    
    list_data.append({
                'id':id_num,
                'price':price,
                'title': title,
                'xar':description_text,
                'categories':categories,
                'p1': char_name + ' ' + char_value,
                'p2': char_name1 + ' ' + char_value1,
                'p3': char_name3 + ' ' + char_value3,
                'p4': '',
                'p5': '',
                'p6': '',
                'image':img
                })


def save():
    root = minidom.Document()

    xml_root = root.createElement('listings')
    root.appendChild(xml_root)
    for item in list_data:
        id = item['id']
        price = item['price']
        title = item['title']
        content = item['xar']
        categories = item['categories']
        p1 = item['p1']
        p2 = item['p2']
        p3 = item['p3']
        p4 = item['p4']
        p5 = item['p5']
        p6 = item['p6']
        image = item['image']

        categoriesChild = root.createElement('listing')
        xml_root.appendChild(categoriesChild)

        categoryChild = root.createElement('title')
        categoryChild.setAttribute('lang', f'ru-RU')
        categoryText = root.createCDATASection(title)
        categoryChild.appendChild(categoryText)

        contentChild = root.createElement('content')
        contentChild.setAttribute('lang', f'ru-RU')
        content = root.createCDATASection(content)
        contentChild.appendChild(content)

        catChild = root.createElement('category')
        catChild.setAttribute('lang', f'ru-RU')
        catText = root.createTextNode(categories)
        catChild.appendChild(catText)

        categoryidChild = root.createElement('categoryid')
        categoryidText = root.createTextNode(id)
        categoryidChild.appendChild(categoryidText)

        contactemailChild = root.createElement('contactemail')
        contactemailText = root.createTextNode('avtor2@mail.ru')
        contactemailChild.appendChild(contactemailText)

        contactnameChild = root.createElement('contactname')
        contactnameText = root.createTextNode('Avtor2')
        contactnameChild.appendChild(contactnameText)

        priceChild = root.createElement('price')
        priceText = root.createTextNode(price)
        priceChild.appendChild(priceText)

        currencyChild = root.createElement('currency')
        currencyText = root.createTextNode('RUB')
        currencyChild.appendChild(currencyText)

        city_areaChild = root.createElement('city_area')
        city_areaText = root.createTextNode('670000')
        city_areaChild.appendChild(city_areaText)
        
        cityChild = root.createElement('city')
        cityText = root.createTextNode('Улан-Удэ')
        cityChild.appendChild(cityText)

        regionChild = root.createElement('region')
        regionText = root.createTextNode('Республика Бурятия')
        regionChild.appendChild(regionText)

        countryIdChild = root.createElement('countryId')
        countryIdText = root.createTextNode('RUS')
        countryIdChild.appendChild(countryIdText)

        countryChild = root.createElement('country')
        countryText = root.createTextNode('Россия')
        countryChild.appendChild(countryText)

        tgChild = root.createElement('custom')
        tgChild.setAttribute('name', f'tip')
        tgText = root.createTextNode('ТГ СМИТ')
        tgChild.appendChild(tgText)

        artChild = root.createElement('custom')
        artChild.setAttribute('name',f'p1')
        artText = root.createTextNode(p1)
        artChild.appendChild(artText)

        waterChild = root.createElement('custom')
        waterChild.setAttribute('name',f'p2')
        waterText = root.createTextNode(p2)
        waterChild.appendChild(waterText)

        markChild = root.createElement('custom')
        markChild.setAttribute('name',f'p3')
        markText = root.createTextNode(p3)
        markChild.appendChild(markText)

        materialChild = root.createElement('custom')
        materialChild.setAttribute('name',f'p4')
        materialText = root.createTextNode(p4)
        materialChild.appendChild(materialText)

        application_typeChild = root.createElement('custom')
        application_typeChild.setAttribute('name',f'p5')
        application_typeText = root.createTextNode(p5)
        application_typeChild.appendChild(application_typeText)

        scope_of_applicationChild = root.createElement('custom')
        scope_of_applicationChild.setAttribute('name',f'p6')
        scope_of_applicationText = root.createTextNode(p6)
        scope_of_applicationChild.appendChild(scope_of_applicationText)

        imageChild = root.createElement('image')
        imageText = root.createTextNode(image)
        imageChild.appendChild(imageText)

        dataChild = root.createElement('datetime')
        dataText = root.createTextNode(time1)
        dataChild.appendChild(dataText)


        categoriesChild.appendChild(categoryChild)
        categoriesChild.appendChild(contentChild)
        categoriesChild.appendChild(catChild)
        categoriesChild.appendChild(categoryidChild)
        categoriesChild.appendChild(contactemailChild)
        categoriesChild.appendChild(contactnameChild)
        categoriesChild.appendChild(priceChild)
        categoriesChild.appendChild(currencyChild)
        categoriesChild.appendChild(city_areaChild)
        categoriesChild.appendChild(cityChild)
        categoriesChild.appendChild(regionChild)
        categoriesChild.appendChild(countryIdChild)
        categoriesChild.appendChild(countryChild)
        categoriesChild.appendChild(tgChild)
        categoriesChild.appendChild(artChild)
        categoriesChild.appendChild(waterChild)
        categoriesChild.appendChild(markChild)
        categoriesChild.appendChild(materialChild)
        categoriesChild.appendChild(application_typeChild)
        categoriesChild.appendChild(scope_of_applicationChild)
        categoriesChild.appendChild(imageChild)
        categoriesChild.appendChild(dataChild)


    xml_root.appendChild(categoriesChild)
    xml_str = root.toprettyxml(indent="\t")
    save_path_file = (str(FILE) + '.yml')
    
    with open(save_path_file, "w",encoding='utf-8') as f:
        f.write(xml_str)



if __name__ == '__main__':
    parser_first()

save()
