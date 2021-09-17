from web_poet.pages import ItemWebPage, WebPage

# ------ Base page objects ------


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
    def to_item(self):
        return {
            "last_visited_url": self.url.strip("/"),
            "url": self.url,
            "name": self.css("title::text").get(),
        }

