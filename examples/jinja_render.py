import jinja2
from os.path import abspath, join, dirname

hdl = jinja2.Environment(
    loader=jinja2.FileSystemLoader(abspath(join(dirname(__file__), "template")))
)

sep = "-"*50
print("\n".join([
    "Availiable templates:",
    sep,
    *hdl.list_templates(),
    sep,
    "Template Render Example",
    hdl.get_template("FORMAT.vhd.j2").render(
        name="apa",
        ports=[
            dict(name="clk", dir="in", size="1"),
            dict(name="tEsT", dir="IN", size="2"),
            dict(name="clk2", dir="in")
        ]
    )
]))