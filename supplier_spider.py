import scrapy
import csv

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


def load_domains(csv_path="domain100_remaining4.csv"):
    entries = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            domain = row["domain"].strip()
            clean_domain = domain.replace("https://", "").replace("http://", "").rstrip("/")

            start_url = domain if domain.startswith("http") else f"https://{clean_domain}"

            entries.append({
                "domain": clean_domain,
                "start_url": start_url
            })

    return entries


ENTRIES = load_domains()


class MultiDomainSpider(scrapy.Spider):
    name = "multi_domain_spider"

    allowed_domains = [e["domain"] for e in ENTRIES]
    start_urls = [e["start_url"] for e in ENTRIES]

    custom_settings = {
        "FEEDS": {
            "output100_remaining4.csv": {
                "format": "csv",
                "overwrite": True
            }
        },
        "DEPTH_LIMIT": 3,
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