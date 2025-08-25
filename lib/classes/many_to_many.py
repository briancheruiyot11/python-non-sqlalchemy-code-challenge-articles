class Article:
    all = []  # keeps track of every article created

    def __init__(self, author, magazine, title):
        # make sure the title is a string and between 5–50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be a string between 5 and 50 characters")

        self._title = title
        self.author = author      
        self.magazine = magazine  

        Article.all.append(self)

    # title is read-only once set
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # do nothing if someone tries to reset the title
        pass

    # author must always be an Author object
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    # magazine must always be a Magazine object
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("name must be a non-empty string")
        self._name = name

    # name can’t be changed once set
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # ignore attempts to rename the author
        pass

    # get all articles written by this author
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # get all magazines this author has written for
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    # create and add a new article
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # get all unique categories the author has written in
    def topic_areas(self):
        cats = {mag.category for mag in self.magazines()}
        return list(cats) if cats else None


class Magazine:
    all = []  # keeps track of every magazine created

    def __init__(self, name, category):
        self.name = name      
        self.category = category
        Magazine.all.append(self)

    # name can be changed but must be 2–16 characters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # if invalid, ignore the change

    # category can be changed but must be a non-empty string
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # ignore invalid values

    # get all articles published in this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # get all authors who wrote for this magazine
    def contributors(self):
        return list({article.author for article in self.articles()})

    # get just the titles of the articles in this magazine
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    # get authors who have written more than 2 articles here
    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [a for a in set(authors) if authors.count(a) > 2]
        return result if result else None

    # find the magazine with the most articles overall
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))
