import tempfile
from feast_schema import FeastSchema

def test_project_schema(construct_test_environment):

    feast_schema = FeastSchema(construct_test_environment)
    schema = feast_schema.store_schema()
    assert schema["driver_hourly_stats"] is not None

