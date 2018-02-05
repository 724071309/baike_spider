#coding:utf8
from baike_spider import url_manager, html_outputer, html_downloader, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)         #向管理器添加一个新的url
        while self.urls.has_new_url():          #是否有待爬取的url
            try:
                new_url = self.urls.get_new_url()      #从管理器获取一个新的待爬取url
                print('craw %d: %s' % (count, new_url))
                html_count = self.downloader.download(new_url)    #下载器下载网页
                new_urls, new_data = self.parser.parse(new_url, html_count)  #抓取网页中有用信息
                self.urls.add_new_urls(new_urls)       #向管理器添加新的url
                self.outputer.collect_data(new_data)   #将网页数据传给outputer

                if count == 1000:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()

if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/2018%E5%B9%B4"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)








