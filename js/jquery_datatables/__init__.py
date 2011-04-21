from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_datatables', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

datatables = Resource(
    library, 'media/js/jquery.dataTables.js',
    depends=[jquery],
    minified='media/js/jquery.dataTables.min.js'
)
