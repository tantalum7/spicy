# coding: utf8
import re
import jinja2
import os

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


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(context)



if __name__ == "__main__":

    with open("output.html", "w") as fp:
        fp.write(render("spicy.html",{'data_list': process_spices("spices.txt")}))

    print("done")