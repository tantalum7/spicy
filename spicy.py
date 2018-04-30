# coding: utf8
import re
from jinja2 import Environment, BaseLoader


class Spice(object):
    def __init__(self, name, info="", category=""):
        self._name = name
        self._info = info
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def info(self):
        return self._info

    @property
    def category(self):
        return self._category

    def __repr__(self):
        return 'Spice(category="{}", name="{}", info="{}'.format(self.category, self.name, self.info)

def process_spices(file):

    spice_list = []
    category = ""
    with open(file, "r") as fp:
        for line in fp.readlines():
            if len(line) > 2:
                if line.startswith("["):
                    category = re.sub(r'[[\]\n]', '', line)
                else:
                    split_line = line.split(",")
                    name = split_line[0].strip()
                    info = "" if len(split_line) < 2 else split_line[1].strip()
                    spice_list.append(Spice(name=name, info=info, category=category))

    return spice_list

def render(data_list):
    html = """
    {% for item in data_list %}
    <div class="label">
      <div class="name">{{item.name}}</div>
      <div class="info">{{item.info}}</div>
    </div>
    {% endfor %}
    """
    template = Environment(loader=BaseLoader()).from_string(html)
    return template.render(data_list=data_list)

if __name__ == "__main__":

    sl = process_spices("spices.txt")
    print(render(sl))