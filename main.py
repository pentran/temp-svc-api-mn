from fastapi import FastAPI 
import pandas as pd 

df = pd.read_csv('./data/smallservices2019.csv')

app = FastAPI()

@app.route('/', methods=["GET"])
async def home():
    return {'this is a API service for MN SVC code details'}

@app.route('/preview', methods=["GET"])
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return {result}

@app.route('/svc/<value>', methods=['GET'])
async def svccode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return {filtered.to_json(orient="records")}

@app.route('/svc/<value>/sex/<value2>')
async def svccode2(value, value2):
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return {'There is nothing here'}
    else: 
        return {filtered2.to_json(orient="records")}    
    


