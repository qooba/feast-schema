import os
import pytest
import tempfile
import yaml
import feast
import json
from pathlib import Path
from distutils.dir_util import copy_tree
import importlib.util


@pytest.fixture
def construct_test_environment() -> str:
    repo_path = tempfile.mkdtemp()
    template = "local"
    template_path = str(Path(Path(feast.__file__).parent / "templates" / template).absolute())

    copy_tree(template_path, str(repo_path))

    bootstrap_path = Path(repo_path) / "bootstrap.py"
    spec = importlib.util.spec_from_file_location("bootstrap", str(bootstrap_path))
    bootstrap = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bootstrap)
    bootstrap.bootstrap()
    os.remove(bootstrap_path)

    os.chdir(repo_path)
    os.system("feast apply")

    return repo_path


