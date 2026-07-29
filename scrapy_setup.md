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

Add this below the key word denotation if there is one. Otherwise just put it right under the package import

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

As stated in the note, the `domaintt.csv` has a data structure like the following (your domain list needs to look like this)

```csv
domain
row1.org
row2.org
row3.org
rown.org
```

>[!IMPORTANT]
>The data NEEDS to be in a csv delimited file as it is parsed as such


Next paste the following code below the reference loop

```python
class MultiDomainSpider(scrapy.Spider):
    name = "multi_domain_spider"

    allowed_domains = [e["domain"] for e in ENTRIES]
    start_urls = [e["start_url"] for e in ENTRIES]

    custom_settings = {
        "FEEDS": {
            "output_supplier.csv": {
                "format": "csv",
                "overwrite": True
            }
        },
        "DEPTH_LIMIT": 4,
        "CLOSESPIDER_PAGECOUNT": 5000,
    }

    def parse(self, response):
        for href in response.css("a::attr(href)").getall():
            if href.lower().endswith(".pdf"):
                yield {
                    "pdf_url": response.urljoin(href)
                }

            elif (
                not any(p in href for p in IGNORE_PATTERNS)
                and any(k in href.lower() for k in FOLLOW_KEYWORDS)
            ):
                yield response.follow(href, callback=self.parse)
```

>[!NOTE]
>The above code is used if you choose to include the keywords. Note you also need to specify the output csv name. (as seen in the script "output_supplier.csv")
>Also, you have the option to customize the depth limit. This is essentially how deep the spider will look.
>e.g. https://github.com/caldaml/Strategic-Sourcing-Daikin-2026/edit/main/scrapy_setup.md this domain has a depth of 6 starting from the base domain.

If you didn't include the keywords choose the code below


```python
class MultiDomainSpider(scrapy.Spider):
    name = "multi_domain_spider"

    allowed_domains = [e["domain"] for e in ENTRIES]
    start_urls = [e["start_url"] for e in ENTRIES]

    custom_settings = {
        "FEEDS": {"output.csv": {"format": "csv", "overwrite": True}},
    }

    def parse(self, response):
        for href in response.css("a::attr(href)").getall():
            if href.lower().endswith(".pdf"):
                yield {"pdf_url": response.urljoin(href)}
            else:
                yield response.follow(href, callback=self.parse)
```

All this loop is doing is parsing the response as it gives the data back in JSON.

## **STEP 3**

All there is left to do is run the script. In powershell, put the following. (in the example below, the python file is name supplier spider)

```bash
scrapy runspider supplier_spider.py
```




