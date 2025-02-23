import pandas as pd
import json

#open csv file with the states and their abbreviations
path = "/Users/elisacascudo/Desktop/Universidad/4º-2S/idkd/experiment/Map Project/States - Sheet1.csv"
df = pd.read_csv(path)
print(df.head())

#connect to the json file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data:dict=json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

path_json = "/Users/elisacascudo/Desktop/Universidad/4º-2S/idkd/experiment/Map Project/states.json"
state_df : dict = load_knowledge_base(path_json)

length = df['State'].shape[0]

for i in range(int(length)):
    state =  str(df.iloc[i,0])
    abbreviation = str(df.iloc[i,2])
    state_df['states'].append({'state': state, "abbreviation": abbreviation})
    save_knowledge_base(path_json, state_df)