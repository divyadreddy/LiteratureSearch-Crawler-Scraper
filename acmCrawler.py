from bs4 import BeautifulSoup as sp
import requests

def getDOI(citation):
	try:
		title = citation.find("span",{"class":"hlFld-Title"})
		for a in title.findAll("a", href=True):
			dois = a['href']
		dois = dois[5:]
	except:
		dois = "Error Finding DOI"
	return dois

def parsed_bibText(dois):
	try:
		url = "https://dl.acm.org/action/exportCiteProcCitation"
		data = {'dois':dois,'targetFile':'custom-bibtex','format':'bibTex'}
		response = requests.post(url,data = data).json()
		bib = response

	except:
		bib = "Error Fetching BibText"
	return bib


def scrape(parsed_html):
	contents = parsed_html.findAll("div",{"class":"issue-item issue-item--search clearfix"})
	print("no. of contents = ",len(contents))
	for citation in contents:
		dois = getDOI(citation)
		# print("dois = ",dois)
		bibText = parsed_bibText(dois)
		print("bib = ",bibText)
		# return

def main():

	myurl = str(input("Search:"))
	myurl.replace(' ','+')
	myurl = "https://dl.acm.org/action/doSearch?fillQuickSearch=false&expand=dl&field1=AllField&text1="+myurl

	x = requests.get(myurl)
	parsed_html = sp(x.text,"html.parser")

	totalNumber = int(parsed_html.find("span",{"class":"hitsLength"}).string.strip().replace(',',''))
	totalPages = int(totalNumber/20)
	print("Total Results: ",totalNumber)
	print("Total Pages: ",totalPages)


	# Extract first page
	scrape(parsed_html)
	# return

	for i in range(1,totalPages+1):
		print("Page ",i)
		try:
			next_page = myurl + "&pageSize=20&startPage="+str(i)
			x = requests.get(next_page)
			parsed_html = sp(x.text,"html.parser")
			scrape(parsed_html)
		except KeyboardInterrupt:
			print("Exiting...")


if __name__ == '__main__':
	main()
