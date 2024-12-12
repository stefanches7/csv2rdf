import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace
import numpy as np
from urllib.parse import urlparse

def is_valid_uri(uri_string):
    """
    Check if a string is a valid URI.
    
    Args:
        uri_string: String to validate as URI
        
    Returns:
        bool: True if valid URI, False otherwise
    """
    try:
        result = urlparse(uri_string)
        # Check if scheme and netloc/path are present
        return all([result.scheme, (result.netloc or result.path)])
    except ValueError:
        return False
    
def make_rdf_term(namespace, value):
    """
    Convert a string to an RDF term.
    """
    
    value_uri = value.replace(" ", "_")
    
    if is_valid_uri(namespace + value_uri):
        return URIRef(namespace + value_uri)
    else:
        return Literal(namespace + value)

def csv2rdf(data, subj_prefix, pred_prefix, obj_prefix, delim=",", skip=0, header=0, index = None):
    """
    This method parses tsv and csv files and creates triples for the data.
    :param delim: delimiter (tab or comma)
    :param skip: number of rows to skip
    :param header: number of header 
    :param subj_prefix: subject prefix namespace
    :param pred_prefix: predicate prefix namespace
    :param obj_prefix: object prefix namespace
    """
    if index and type(index) != int:
        raise ValueError("Index must be an integer or None")
    
    skip_col = index if index else None # skip column vals if index is provided
    
    df = pd.read_csv(data, delimiter=delim, skiprows=skip, header=header)
    
    for namespace in [subj_prefix, pred_prefix, obj_prefix]:
        if not namespace.endswith("/"):
            namespace = namespace + "/"
    
    index_terms = np.zeros((df.shape[0],), dtype=object)
    predicate_terms = np.zeros((df.shape[1],), dtype=object)
    
    if not index:
        for i in range(df.shape[0]):
            index_terms[i] = make_rdf_term(subj_prefix, str(i))
    else:
        for i,val in enumerate(df.iloc[:,index]):
            index_terms[i] = make_rdf_term(subj_prefix, str(val))
        
    
    for i in range(df.shape[1]):
        predicate_terms[i] = make_rdf_term(pred_prefix, df.columns[i])
        
    g = Graph()
    
    for i, row in df.iterrows():
        for j in range(len(row)): 
            if j == skip_col: # j was the index column
                continue
            subj = index_terms[i]
            pred = predicate_terms[j]
            obj = make_rdf_term(obj_prefix, str(df.iloc[i,j]))
            g.add((subj, pred, obj))

    return g
