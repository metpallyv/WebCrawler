# WebCrawler

# The goal of this project is to implement web crawler in python with the following requirements

1. You should start from the seed document http://en.wikipedia.org/wiki/Gerard_Salton, the Wikipedia article on Gerald Salton, an important early researcher in information retrieval.
2. You should only follow links with the prefix http://en.wikipedia.org/wiki/. In other words, do not follow links to non-English articles or to non-Wikipedia pages.
3. Do not follow links with a colon (:) in the rest of the URL.
4. Do not follow links to the main page http://en.wikipedia.org/wiki/Main_Page.
5. Crawl to at most depth 3 from the seed page. In other words, you should retrieve the seed page, pages it links to, and pages those pages link to.
6. Your crawler should take two arguments: the seed page and an optional "keyphrase" that must be present, in any combination of upper and lower case, on any page you crawl. If the keyphrase is not present, stop crawling. This is a very simple version of focused crawling, where the presence or absence of a single feature is used to determine whether a document is relevant.
7. The pages crawled when the keyphrase is "information retrieval".
