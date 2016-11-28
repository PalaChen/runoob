import os


dirpath = os.path.dirname(__file__)

class HtmlOutputer(object):
    def save(self,content,title):
        with open(os.path.join(dirpath, 'html')+'\\'+title+'.html', 'w', encoding='utf-8') as file:
            file.write(content)

