-- SeeCow Tables
-- Initialize the database.
-- Drop any existing data and create empty tables.
-- Default SQLite datatype for timestamp

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS parlor_status;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE parlor_status (
  cattle_id TEXT PRIMARY KEY,
  info TEXT NOT NULL,
  place TEXT NOT NULL,
  time TEXT
 );