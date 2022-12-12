<h1 align="center">MFCScraper</h1>

<font size="3">

<a href="https://github.com/Aeonss/MFCScraper/blob/master/MFC.py">MFCScraper</a> scrapes results of figures and figure information on [MyFigureCollection](https://myfigurecollection.net/).


## 🔨 &nbsp; Installation
Install python:
``` bash
https://www.python.org/downloads/
```

Download source file and add to your project folder
``` bash
https://github.com/Aeonss/MFCScraper/blob/master/MFC.py
```

Download the requirements:
``` bash
pip install -r requirements.txt
```

## 🚀 &nbsp; Usage


Get figure information with figure id
``` bash
from MFC import MFC
figure = MFC.searchFigure("1711391")

# Get information of the figure
name = figure.name
image = figure.image
figure_id = figure.figure_id
url = figure.url
category = figure.category
origin = figure.origin
character = figure.character
company = figure.company
artist = figure.artist
version = figure.version
release = figure.release
material = figure.material
dimensions = figure.dimensions

```

Get a list of figures with character name
``` bash
from MFC import MFC
result = MFC.search("hatsune miku")

# Alternatively, show draft figures that have no yet been released
# result = MFC.search("hatsune miku", show_draft=True)

# Get information of the first figure in the results
name = result[0].name
figure_id = result[0].figure_id
url = result[0].url
thumbnail = result[0].thumbnail
```


## 📘 &nbsp; License
MFCScraper is released under the [MIT license](https://github.com/Aeonss/MFCScraper/blob/master/LICENSE.md).

</font>