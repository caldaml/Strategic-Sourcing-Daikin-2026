# **Complete Guide To Setting Up Scrapy Web Crawler**


## **STEP 1**

The first step to setting up any sort of program is downloading ore verifying that you have the correct packages installed.

>[!NOTE]
>For this script, you need to packages. The `scrapy` and `csv` packages. Look at the following command below. (in command prompt or bash)

```bash
pip install scrapy csv
```

Put this at the top of your script

```python
import scrapy
import csv
```


## **STEP 2**

Our next step before operating is to setting up our actual script

>[!IMPORTANT]
>The script is setup to only source pdfs which contain one of the strings listed. e.g.


```python
IGNORE_PATTERNS = ['/archive/', '/interview/', '/episode/', '/search', '?', '#']
FOLLOW_KEYWORDS = [
    "product", "products", "service", "services",
    "solution", "solutions", "portfolio", "catalog",
    "offering", "capability", "capabilities",

    "industry", "industries", "application",

    "datasheet", "spec", "specification",
    "technical", "documentation", "manual",

    "supplier", "manufacturing", "production",

    "certification", "iso", "compliance",
    "quality", "standard",

    "report", "annual", "investor", "sustainability"
]
```

Make sure that the words you want are stored as a strings like as seen above.

You can also to crawl everything in which you would use this alternative script. I'll denote if its the alt script by noting `# alt`





