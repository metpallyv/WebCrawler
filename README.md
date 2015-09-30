# WebCrawler
The goal of this project is to implement a simple web crawler using python 

# The goal of this project is to implement web crawler in python with the following requirements

    1. Start crawling with the same seed: www.ccs.neu.edu
    2. Implement your own code to keep track of what you crawled and decide what to crawl next.
    3. Extract links from HTML pages. Note that pages of type text/html will not necessarily have URLs that end in .html.
    4. Record both HTML and PDF pages. PDF pages will be dead ends (sinks). Ignore other document types.
    5. Repect robots.txt. For ccs.neu.edu, it looks like:

                  User-agent: htdig
                  Disallow: /tools/checkbot/
                  Disallow: /home/ftp/
                  Disallow: /home/www/
              
                  User-agent: *
                  Disallow: /tools/checkbot/
                  Disallow: /tools/hypermail/dox/
                  Disallow: /home/ftp/
                  Disallow: /home/www/
                  Disallow: /home/sxhan/com1105/
                  Disallow: /course/com1390/roster.pdf 
                  Disallow: /home/yimin/grades.html
                  Disallow: /home/fceria01/

    5. Use a five-second delay between requests.
    6. Crawl until you have 100 unique links. You do not need to keep the page contents.

