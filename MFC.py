from bs4 import BeautifulSoup
import urllib.request


class MFC():

    def search(search, sort="date", order="desc", show_draft=False):
        source = urllib.request.urlopen("https://myfigurecollection.net/browse.v4.php?rootId=0&sort=" + sort + "&order=" + order + "&character=" + search.replace(" ", "%20")).read()
        soup = BeautifulSoup(source, 'html.parser')
        search_results = soup.findAll("span", class_="item-icon")
        figure_list = []
        
        for result in search_results:
            a = result.find("a")
            draft = a.find("span", class_="item-is-draft")
            
            if not draft or show_draft:
                url = "https://myfigurecollection.net" + a['href']
                figure_id = url.split("/")[-1]
                thumbnail = a.find("img")['src']
                name = a.find("img")['alt']
            
                figure_list.append(FigureResult(name, figure_id, url, thumbnail))
        
        return figure_list
    
    def searchFigure(figure_id):
        source = urllib.request.urlopen('https://myfigurecollection.net/item/' + figure_id).read()
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.findAll("div", class_="form-field")
        
        name = soup.find("span", class_="headline").text
        image = soup.find("div", class_="tbx-pswp").find("img")['src']
        url = 'https://myfigurecollection.net/item/' + figure_id
        category = ""
        origin = ""
        character = ""
        company = ""
        artist = ""
        version = ""
        release = ""
        material = ""
        dimensions = ""
            
        for d in data:
            if "category" in d.text.lower():
                category = str(d.text[8:])
            if "origin" in d.text.lower():
                origin = str(d.text[6:])
            if "character" in d.text.lower():
                character = str(d.text[9:])
            if "company" in d.text.lower():
                company = str(d.text[7:])
            if "companies" in d.text.lower():
                company = str(d.text[9:])
            if "artist" in d.text.lower():
                artist = str(d.text[6:])
            if "version" in d.text.lower():
                version = str(d.text[7:])
            if "release" in d.text.lower():
                release = str(d.text[8:])
            if "material" in d.text.lower():
                material = str(d.text[8:])
            if "dimensions" in d.text.lower():
                dimensions = str(d.text[10:])
        
        return Figure(name, image, figure_id, url, category, origin, character, company, artist, version, release, material, dimensions)
        
class FigureResult():
    def __init__(self, name, figure_id, url, thumbnail):
        self.name = name
        self.figure_id = figure_id
        self.url = url
        self.thumbnail = thumbnail
    
    def __repr__(self):
        return self.url

class Figure():
    def __init__(self, name, image, figure_id, url, category, origin, character, company, artist, version, release, material, dimensions):
        self.name = name
        self.image = image
        self.figure_id = figure_id
        self.url = url
        self.category = category
        self.origin = origin
        self.character = character
        self.company = company
        self.artist = artist
        self.version = version
        self.release = release
        self.material = material
        self.dimensions = dimensions
    
    def __repr__(self):
        return self.url