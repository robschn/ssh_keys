import yaml
from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))

baseline = ENV.get_template("template.txt")

with open("data.yml") as y:
    host_obj = yaml.load(y)
    f = open('config.txt', 'w')
    config = baseline.render(host_obj)
    f.write(config)
    f.close