class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"


book1 = Book("Noli Me Tángere", "José Rizal", 1887)
book2 = Book("A Song of Ice and Fire", "George R. R. Martin", 1996)
book3 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)

print(book1.describe())
print("\n" + "-"*30 + "\n")
print(book2.describe())
print("\n" + "-"*30 + "\n")
print(book3.describe())
