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

>[!TIP]
>You can also to crawl everything in which you would use this alternative script. All you need to do is omit the key words and paste the next loop.

Add this below the key word denotation if there is one, otherwise just put it right under the package import

```python
# csv referece -> single column being referenced (i.e. domain)
# this acts as both the starting url and the allowed domain
def load_domains(csv_path="domaintt.csv"):
    entries = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row["domain"].strip()
            clean_domain = domain.replace("https://", "").replace("http://", "").rstrip("/")
            start_url = domain if domain.startswith("http") else f"https://{clean_domain}"
            entries.append({"domain": clean_domain, "start_url": start_url})
    return entries

ENTRIES = load_domains("domaintt.csv")
```

As stated in the note, the domaintt.csv has a data structure like the following

```csv
domain
row1.org
row2.org
row3.org
rown.org
```

>[!IMPORTANT]
>The data NEEDS to be in a csv delimited file as is parsed as such





