import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain():
    def __init__(self):
        self.url = url_manager.UrlManager()
        self.download = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        html_content = self.download.download(root_url)
        new_urls = self.parser.parser_url(html_content)
        self.url.add_new_urls(new_urls)

        while self.url.has_new_urls():
            new_url = self.url.get_new_url()
            print(new_url)
            content = self.download.download('http://www.runoob.com'+new_url)
            title = self.parser.parser_title(content)
            self.outputer.save(content, title)



if __name__ == '__main__':
    root_url = 'http://www.runoob.com/python3/python3-tutorial.html'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
