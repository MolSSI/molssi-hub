from pathlib import Path
import json

def html_context_generator(json_file_path=Path("../molssiai_hub")):

    if isinstance(json_file_path, str):
        json_file_path_list = sorted(Path(json_file_path).glob("**/*.json"))
    elif isinstance(json_file_path, Path):
        json_file_path_list = sorted(json_file_path.glob("**/*.json"))
    else:
        raise TypeError("The 'json_file_path' should be of either str or Path type.")
    
    html_context = {}
    for directory in json_file_path_list:
        dir_parts = directory.parts[2:-1]
        name = dir_parts[-1]
        mydir = Path(".")
        for itm in dir_parts: 
            mydir = mydir.joinpath(itm)
        with open("./_templates/catalog.rst", "r") as t:
            target_dir = Path(".")
            for target in mydir.parts[:-1]:
                target_dir = target_dir.joinpath(target)
            if not target_dir.exists():
                Path.mkdir(target_dir)
            my_rst_file = str(target_dir) + "/" + name + ".rst"
            with open(my_rst_file,"w") as g:
                g.write(t.read().replace("NAME", name))
        with open(str(directory.resolve()), "r", encoding='utf-8') as f:
            idx = json.load(f)
            html_context[name] = idx
    
    return html_context