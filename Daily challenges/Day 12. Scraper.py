from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
import json

# Open the URL
class Pokemon:

    def __init__(self, idx):

       
        # opt = FirefoxOptions()
        # opt.add_argument('--headless')
        # self.driver = webdriver.Firefox(options=opt)
        
        self.driver = webdriver.Firefox()
        self.ROOT_DOMAIN = "https://www.pokemon.com/us/pokedex"
        self.idx = idx
        self.pokedex = {}


    def get_page(self):
        self.driver.get(f'{self.ROOT_DOMAIN}/{self.idx}')
        self.driver.implicitly_wait(5)

    def get_id_and_name(self):    
        pokemon_name, pokemon_id = self.driver.find_element_by_xpath('//div[@class="pokedex-pokemon-pagination-title"]').text.split()
        self.pokedex['id'] = pokemon_id
        self.pokedex['name'] = pokemon_name

    def get_info(self):
        info_table = self.driver.find_element_by_xpath('//div[contains(@class, "pokemon-ability-info")]')
        
        titles = [t.text for t in info_table.find_elements_by_xpath('//span[contains(@class, "attribute-title")]')]
        values = [v.text if len(v.text) > 0 else [cl.get_attribute('class').split()[1].split('_')[1] for cl in v.find_elements_by_xpath('./i')] for v in info_table.find_elements_by_xpath('//span[contains(@class, "attribute-value")]')]
        
        for t,v in zip(titles, values):
            self.pokedex[t] = v

    def get_img_url(self):
        self.pokedex['img_url'] = self.driver.find_element_by_xpath('//div[contains(@class, "profile-images")]/img').get_attribute('src')


    def get_version_description(self):
        
        desc = self.driver.find_element_by_xpath('//div[contains(@class, "version-descriptions")]')
        self.pokedex['version_x'] = desc.find_element_by_xpath('./p[contains(@class, "active")]').text
        
        button_to_click = self.driver.find_element_by_xpath('//span[contains(@class, "version-y")]')
        self.driver.execute_script("arguments[0].click();", button_to_click)

        self.pokedex['version_y'] = desc.find_element_by_xpath('./p[contains(@class, "active")]').text


    def get_all_attribute(self):
                
        try:
            self.get_page()
            self.get_id_and_name()
            self.get_img_url()
            self.get_info()
            self.get_version_description()
            print(self.pokedex)
        
        except NoSuchElementException as e:
            print(e)
            self.pokedex = None
        
        except Exception as e:
            print(e)
        
        finally:
            self.driver.close()
            return self.pokedex


def read_all_pokemons_to_file(start=1):

    idx = start
    result = []

    while True: 
        res = Pokemon(idx).get_all_attribute()
        if res is None:
            break
        
        result.append(res)
        idx += 1

    with open('All pokemons', 'w') as f:
        f.write(json.dumps(result))


if __name__ == "__main__":
    read_all_pokemons_to_file()