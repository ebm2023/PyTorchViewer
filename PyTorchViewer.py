import json
import re
import sys
import torch


def add_code_and_save(file):
    with open(file, 'r') as orig_json:
        dict = json.load(orig_json)
        dict["file_info"] = {"files": {}, "functions": {}}
        pattern = re.compile(r"^(torch\/.*)\((\d+)\):")
        file_dict, func_dict  = dict["file_info"]["files"], dict["file_info"]["functions"]
        torch_path = torch.__path__[0][:-5]

        for event in dict["traceEvents"]:
                if event["ph"] == 'X':
                    if event["name"] not in func_dict:
                        try:
                            m = pattern.match(event["name"])
                            if m:
                                file_name, lineno = torch_path + m.group(1), int(m.group(2))
                                if file_name not in file_dict:
                                    with open(file_name, "r", encoding="utf-8") as f:
                                        content = f.read()
                                        file_dict[file_name] = [content, content.count("\n")]
                                func_dict[event["name"]] = [file_name, lineno]
                        except Exception:
                            pass
        with open("profile_with_code.json", "w") as f:
           json.dump(dict, f)


add_code_and_save(sys.argv[1])

print("To view trace, run command: vizviewer  profile_with_code.json")