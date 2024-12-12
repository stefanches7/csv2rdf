
from csv2rdf import csv2rdf


file_path = "/home/ubuntu/src/omero-crawler/data/idr0065-anno.csv"
file_out = "output.ttl"
delimiter = ","
skip = 0
index = None # int of the column for subject values, none to use integer index
subject_namespace = "http://example.org/subject/"
predicate_namespace = "http://example.org/predicate/"
object_namespace = "http://example.org/object/"

# Example usage
g = csv2rdf(file_path, 
            subject_namespace, predicate_namespace, object_namespace,
            delim=",", index = 2)

with open(file_out, "wb") as f: 
    print(f, g.serialize(format="turtle"))    