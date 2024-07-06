-- Create Authors table
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Create Books table
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

INSERT INTO authors (name) VALUES ('George Orwell');
INSERT INTO authors (name) VALUES ('Harper Lee');
INSERT INTO authors (name) VALUES ('F. Scott Fitzgerald');

INSERT INTO books (title, genre, author_id) VALUES ('1984', 'Dystopian', 1);
INSERT INTO books (title, genre, author_id) VALUES ('Animal Farm', 'Political satire', 1);
INSERT INTO books (title, genre, author_id) VALUES ('To Kill a Mockingbird', 'Fiction', 2);
INSERT INTO books (title, genre, author_id) VALUES ('The Great Gatsby', 'Classic', 3);
