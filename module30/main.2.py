from bs4 import BeautifulSoup

html_content =m"""
<!DOCTYPE html>
<html lang="en">
<head>

    <title>Document</title>
</head>
<body>
   <h1>Welcome to Beautiful soup</h1>
   <p class="intro">Web Scraping</p>
   
   <div id="content">
      <a href="http://example.com/page1>Link 1</a>
      <a href="http://example.com/page1>Link 2</a>
      <a href="http://example.com/page1>Link 3</a>
      <a href="http://example.com/page1>Link 4</a>
   </div
   
</body>
</html>

"""

soup = BeautifulSoup(html_content, 'html.parser')
print("Title per page: ", soup.title.text)

intro_text = sou8p