
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Issue;
DROP TABLE IF EXISTS Metric;

CREATE TABLE Product (
  Product_Id INTEGER PRIMARY KEY AUTOINCREMENT ,
  Title TEXT UNIQUE NOT NULL,
  Description TEXT NOT NULL
);

CREATE TABLE Metric (
  MetricId INTEGER PRIMARY KEY AUTOINCREMENT,
  Title TEXT UNIQUE NOT NULL,
  Description TEXT NOT NULL,
  Product_Id INTEGER);

CREATE TABLE Issue (
  IssueId INTEGER PRIMARY KEY AUTOINCREMENT,
  Title TEXT UNIQUE NOT NULL,
  Category TEXT NOT NULL,
  Product_Id INTEGER ,  
  Metric_Id INTEGER   
);

INSERT into Product values(12,'Product12','Product12 Description');
INSERT into Issue ('Title','category')values('Issue12','Low');
INSERT into Metric ('Title','Description')values('Metric12','Metric 12 Description');

INSERT into Product values(13,'Product13','Product13 Description');
INSERT into Issue ('Title','category','Product_ID')values('Issue13','Low',13);
INSERT into Metric ('Title','Description','Product_ID','MetricID')values('Metric13','Metric 13 Description',13,2);
