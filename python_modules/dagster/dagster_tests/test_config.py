import pytest
import yaml

from dagster import config


def test_construct_full_environment():
    document = '''
context:
    name: default
    args:
        context_arg: context_value
'''

    environment = config.construct_environment(yaml.load(document))

    assert environment == config.Environment(
        context=config.Context('default', {'context_arg': 'context_value'}),
    )
