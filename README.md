# CSV2RDF - convert data tables to RDF format

Specify the namespaces for your triples and convert tabular data to Resource Description Framework.
Currently only TSV / CSV are supported.

## How is it different from other tools?

Comparing to [OpenRefine](https://openrefine.org/) this tool leaves the issue of semantics away (to the specified namespaces), and does not require *manual processing*. This tool is really built for *automation*. 

Comparing to [rdflib.tools.csv2rdf](https://rdflib.readthedocs.io/en/7.1.1/_modules/rdflib/tools/csv2rdf.html), this interface does not run on CLI and has a shorter (yet less flexible) code.

There is a great tool [Swate](https://github.com/nfdi4plants/Swate) that lets you annotate fields in tabular data (Excel) which this tool can learn much from, and I would be happy to implement more of automated semantic lookup in the upcoming releases.
