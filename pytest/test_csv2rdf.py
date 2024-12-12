import pytest
import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace
from csv2rdf import csv2rdf  

@pytest.fixture
def sample_csv_file(tmp_path):
    """Create a sample CSV file for testing"""
    df = pd.DataFrame({
        'col1': ['A', 'B', 'C'],
        'col2': ['id1', 'id2', 'id3'],
        'col3': [1, 2, 3]
    })
    csv_path = tmp_path / "test.csv"
    df.to_csv(csv_path, index=None)
    return csv_path

def test_csv_to_rdf_without_index(sample_csv_file):
    """Test CSV to RDF conversion without using any index column"""
    subject_namespace = "http://example.org/subject/"
    predicate_namespace = "http://example.org/predicate/"
    object_namespace = "http://example.org/object/"

    # Convert
    g = csv2rdf(sample_csv_file, 
                subject_namespace, predicate_namespace, object_namespace,
                index=None)
    
    # Assert
    assert len(g) > 0  # Graph should not be empty

def test_csv_to_rdf_with_second_column_index(sample_csv_file):
    """Test CSV to RDF conversion using second column as index"""
    subject_namespace = "http://example.org/subject/"
    predicate_namespace = "http://example.org/predicate/"
    object_namespace = "http://example.org/object/"
    # Convert
    g = csv2rdf(sample_csv_file,
                subject_namespace, predicate_namespace, object_namespace,
                index=1)
    
    # Assert
    assert len(g) > 0