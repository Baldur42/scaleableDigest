# Pre-Alpha! 
Working and updating just to get a feeling for the end goal of this project. Commits messages will be nonsense for the most part and breakage and removals will be a fact.

# scaleableDigest
Python project for digesting a data base format to other things like vhdl, cpp headers and documentation. This just aims to showcase the possibilities

# [`__main__.py`](YAML2STAR/__main__.py)
The name `__main__.py` is a python convention. It makes it so that if u run the module after installation with `python -m YAML2STAR` this file runs.

*(Working on the end user interface, adding basic logger)*

```python
# fancy stuff like 
import pkgutil
import inspect
# NOTE: MY_PACKAGE & MY_MODULE are placeholders
# get modules
list(filter(lambda x: not x.ispkg, pkgutil.iter_modules(MY_PACKAGE)))

# or get packages
list(filter(lambda x: x.ispkg, pkgutil.iter_modules(MY_PACKAGE)))

# or get functions, variables and classes, ignore underscore methods 
list(filter(lambda x: not x.startswith("_"), dir(MY_MODULE)))

# or get classes
list(filter(inspect.isclass, dir(MY_MODULE)))

#...

# could be used to process allowed choices
```


# jinja2 example for vhdl usage
| [render](examples\jinja_render.py) | [macros](YAML2STAR\template\helpers.vhd.j2) | [template](YAML2STAR\template\FORMAT.vhd.j2) | 
|-|-|-|   
| | | |

If you are new with jinja2 play aroud with it! I found it really useful :)