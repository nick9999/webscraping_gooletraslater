# encoding: utf-8
import urllib2

def translate(to_translate, to_langage="auto", langage="auto"):
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

if __name__ == '__main__':
	to_translate = raw_input('Enter word to translate: ')
	#print("%s >> %s" % (to_translate, translate(to_translate)))
	which_language=raw_input('Enter the language in which you want to translate(French = fr, English = en, Spanish = es,German = de,Irish=ga,Portugese=pt,Greek=el): ')
	print("%s >> %s" % (to_translate, translate(to_translate,which_language )))
        
