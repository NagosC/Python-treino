import asana
from datetime import datetime
import os
import pytz
import sys

def load_config(filename):
    config_data = {}

    with open(filename, 'r') as file:
        for line in file:
            key, valeu = line.strip().split(': ', 1)
            config_data[key.strip()] = valeu.strip()
    return config_data

def get_resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def convert_to_iso(data_str, hora_str=False):

    data_hora_str = data_str

    if hora_str:
        data_hora_str += f" {hora_str}"


    try:

        if hora_str is False:
            data_hora = datetime.strptime(data_hora_str, "%d/%m/%Y")
        else:
            data_hora = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")

        fuso_br = pytz.timezone("America/Sao_Paulo")

        
        data_hora = fuso_br.localize(data_hora)

        data_hora_utc = data_hora.astimezone(pytz.utc)

    except ValueError as e:
        print(f"Erro ao converter data e hora: {e}")
        return None 

    return data_hora_utc.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
 
def cria_task(task_name, consultor, data, assunto , hora=False):

    confing_file_path = get_resource_path('dados.txt')
    configuration = load_config(confing_file_path)

    access_token = configuration['acesstoken']
    
    data_formatada = convert_to_iso(data, hora)

    config = asana.Configuration()
    config.access_token = access_token

    api_cliente = asana.ApiClient(config)
    tasks_api_instance = asana.TasksApi(api_cliente)

    stories_api_instance = asana.StoriesApi(api_cliente)

    if hora:
        if consultor == "Larissa":
            email = configuration['Larissa']
            project_id  = configuration['projetoid2']
            body = {
        
            "data": {
                "name": task_name,
                "assignee": email,
                "projects": [project_id],
                "due_at": data_formatada,
                }
        
            }

        else:
            email = configuration['Gustavo']
            project_id = configuration['projetoid']

            body = {
        
            "data": {
                "name": task_name,
                "projects": [project_id],
                "assignee": email,
                "due_at": data_formatada,
                "notes": assunto,
                }
        
            }
    else:
        if consultor == "Larissa":
            email = configuration['Larissa']
            project_id  = configuration['projetoid2']
            body = {
        
            "data": {
                "name": task_name,
                "assignee": email,
                "projects": [project_id],
                "due_on": data_formatada,
                }
        
            }

        else:
            email = configuration['Gustavo']
            project_id = configuration['projetoid']

            body = {
        
            "data": {
                "name": task_name,
                "projects": [project_id],
                "assignee": email,
                "due_on": data_formatada,
                "notes": assunto,
                }
        
            }


    opts = {}

    try:
        task = tasks_api_instance.create_task(body, opts)

        task_id = str(task['gid'])

        comment_text = "Segue para continuidade"

        body2 = {
            "data":{
            "text": comment_text,

         }
        }

        stories_api_instance.create_story_for_task(body2, task_id, opts)

    except asana.rest.ApiException as e:
        return f"Exception when calling TasksApi->create_task: {e}\n"

    return f"{task.get("name")} inserida" 

