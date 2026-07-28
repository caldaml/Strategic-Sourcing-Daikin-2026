# **Complete Guide To Setting Up Scrapy Web Crawler**


## **STEP 1**

The first step to setting up any sort of program is downloading ore verifying that you have the correct packages installed.

>[!NOTE]
>For this script, you need to packages. The `scrapy` and `csv` packages. Look at the following command below. (in command prompt or bash)

```bash
pip install scrapy csv
```

## **STEP 2**

Our next step before operating is to setting up our script

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


Once the words are 





