
DROP TABLE IF EXISTS sums;

CREATE TABLE sums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number1 INTEGER NOT NULL,
    number2 INTEGER NOT NULL,
    answer INTEGER
);