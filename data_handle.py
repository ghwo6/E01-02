import os,json


folder = os.path.dirname(__file__)
file = os.path.join(os.path.dirname(__file__),"state.json")

def read_json_data():
    if not os.path.exists(file):
        print("state.json 파일이 없습니다.")
        return None
    try:
        with open(file,'rt',encoding="UTF-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        print("파일을 찾지 못했습니다. ",e)
    except PermissionError as e:
        print("권한이 없습니다. ",e)
    except json.JSONDecodeError as e:
        print("JSON 파일 포맷이 아닙니다.")
    except Exception as e:
        print("오류가 발생했습니다. " ,e)

def save_json_data(data:dict):
    try:
        with open(file,'wt',encoding="UTF-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
    except PermissionError as e:
        print("파일 저장 권한이 없습니다. ",e)

