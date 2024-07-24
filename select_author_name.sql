SELECT author_name
FROM library.book, library.author
WHERE book.authorID = author.id