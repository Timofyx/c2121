import requests
res_parse_list = []
response = requests.get("https://coinmaerketcap.com/")
res_text = response.text
res_parse = res_text.split("<span>")
for parse_elem in res_parse:
    if parse_elem.startswith("$"):
        for parse_elem_2 in parse_elem.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)
print(f"Bitcoin {res_parse_list[0]}")