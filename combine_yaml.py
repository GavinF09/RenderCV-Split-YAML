# Using ruamel.yaml instead of PyYAML as
#   1. PyYAML does not keep the order from the dictionary when dumping and that affects the order sections appear in
#   2. It is already used in RenderCV, no need to install another library
from ruamel.yaml import YAML
# import json
    
def load_configs(yamlConfig):
    # note this also loads comments
    folder = "./data_files_yaml/"
    yaml=YAML()
    with open(folder + yamlConfig, 'r') as fn:
        return yaml.load(fn)

def main(): 
    # getting 'main' sections
    cv = load_configs("cv.yaml")
    if 'sections' not in cv["cv"]: 
        cv["cv"]["sections"] = {}
    design = load_configs("design.yaml")
    locale_catalog = load_configs("locale_catalog.yaml")

    # getting the list of files in the sections folder
    with open("./data_files_yaml/sections/order.txt", 'r') as fn:
        contentFiles = [f.strip() for f in fn.readlines()]

    # Adding section data to cv section
    for file in contentFiles:
        contentData = load_configs("sections/" + file)
        cv["cv"]["sections"].update(contentData)
        print(f"Loaded {file} to the CV")

    # print(cv["cv"]["sections"])
    combinedYaml = {**cv, **design, **locale_catalog}

    # write to file
    with open("rendercvResume.yaml", 'w') as fn:
        yaml=YAML()
        yaml.indent(mapping=2)
        yaml.dump(combinedYaml, fn)

if __name__ == "__main__": 
    main()