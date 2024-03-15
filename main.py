def index(keywords):
  refined_search = keywords.lower()
  article_info = []
  pubmed = PubMed(tool="MyTool", email="sejaldua@gmail.com")
  results = pubmed.query(refined_search , max_results=5)
  result_list = list(results)
  if len(result_list) == 0:
    record = ("Try Again")

  else:
    print(i)
    for i, article in enumerate(result_list):
       article_info.insert(i, article.toDict())
       dicts = article_info[i]
       doi = dicts.get("doi")
       id = dicts.get("pubmed_id")
       if doi != None:
         if "\n" in doi:
             doi_index = doi.index("\n")
             dicts.update({"doi" : article.doi[0:doi_index]})
       if id != None:
         if "\n" in id:
             id_index = id.index("\n")
             dicts.update({"pubmed_id" : article.pubmed_id[0:id_index]})
       elif id == None:
           dicts.update({"pubmed_id" : "None"})
       dicts["link"] = "https://pubmed.ncbi.nlm.nih.gov/" + dicts.get("pubmed_id")
       print(
        f'Title: {dicts.get("title")} | Publication Date: {dicts.get("publication_date")} | | PubMed Id: {dicts.get("pubmed_id")}\nJournal: {dicts.get("journal")}\nAuthors: {dicts.get("authors")}\nKeywords: "{dicts.get("keywords")}"\nAbstract: {dicts.get("abstract")}\nLink: {dicts.get("link")}\n'
       )
search = input("Keyword: ")
index(search)
