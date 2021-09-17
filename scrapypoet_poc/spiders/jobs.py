import scrapy
from scrapy_poet import callback_for
from scrapypoet_poc.pages import GlassdoorJobListPage, GlassdoorJobsPage


class GlassdoorJobsSpider(scrapy.Spider):
    name = "glassdoor_jobs"
    start_urls = ["https://www.glassdoor.com/job-listing/trainee-real-estate-deals-team-pwc-JV_IC2440450_KO0,30_KE31,34.htm?jl=1007269401222"]
    parse = callback_for(GlassdoorJobsPage)

    # def parse(self, response, page: GlassdoorJobListPage):
        # yield from response.follow_all(page.job_urls(), self.parse_job)
