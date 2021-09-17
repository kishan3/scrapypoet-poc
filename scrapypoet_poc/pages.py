from web_poet.pages import ItemWebPage, WebPage

# ------ Base page objects ------
from scrapypoet_poc.helpers import _first_or_none


class JobListPage(WebPage):
    def job_urls(self):
        return []


class JobPage(ItemWebPage):
    def to_item(self):
        return None


# ------ Concrete page objects for glassdoor.com ------


class GlassdoorJobListPage(JobListPage):
    def job_urls(self):
        return self.css(".image_container a::attr(href)").getall()


class GlassdoorJobsPage(JobPage):
    def get_job_id(self):
        qdata = self.meta.get('qdata') or self.meta.get('old_item') or {}

        return _first_or_none(
            self.css('.empLinks ::attr(data-jobid)').getall() or
            self.css('.empLinks ::attr(data-job-id)').getall() or
            self.css('.applyButton ::attr(data-job-id)').getall() or
            [qdata.get('job_id')])

    def to_item(self):
        return {
            "last_visited_url": self.url.strip("/"),
            "url": self.url,
            "job_id": self.get_job_id(),
            "name": self.css("title::text").get(),
        }
