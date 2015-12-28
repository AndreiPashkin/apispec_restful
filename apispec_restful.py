import re
from textwrap import dedent

import yaml


def path_from_resource(spec, api, resource, **kwargs):
    """Extracts swagger spec from `resource` methods."""
    from apispec import Path
    assert resource is not None

    for endpoint, view in api.app.view_functions.iteritems():
        if getattr(view, 'view_class', None) == resource:
            break
    else:
        raise RuntimeError

    for rule in api.app.url_map.iter_rules():
        if rule.endpoint == endpoint:
            break
    else:
        raise RuntimeError

    path = re.sub(r'<(?:[^:<>]+:)?([^<>]+)>', r'{\1}', rule.rule)

    operations = {}
    for method in map(str.lower, resource.methods):
        doc = re.sub('^.*(?=---)', '', getattr(resource, method).__doc__)
        doc = dedent(doc)
        operations[method] = yaml.load(doc)

    return Path(path=path, operations=operations)


def setup(spec):
    spec.register_path_helper(path_from_resource)
