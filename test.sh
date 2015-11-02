#!/bin/bash

A="Test number 2: Francois Doray"
B="end"
echo $A 

mongo
show dbs
use mydb_bash
db.createCollection("mycollection")
db.movie.insert({"name":"tutorials point"})
show collections
quit()

echo $B
