class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_urls(self):
        return len(self.new_urls) != 0

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url not in self.old_urls and url not in self.new_urls:
                if '/python3/' in url:
                    url = url.get('href')
                else:
                    url = '/python3/' + url.get('href')
                self.new_urls.add(url)

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url