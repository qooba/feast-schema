# feast-schema

Package which show [feast](https://feast.dev/) schema directly in Jupyter Notebook.

To use run:
```python
from feast_schema import FeastSchema
FeastSchema(".").show_schema()
```

Or for single feature table:
```python
from feast_schema import FeastSchema
FeastSchema(".").show_table_schema("driver_statistics")
```


