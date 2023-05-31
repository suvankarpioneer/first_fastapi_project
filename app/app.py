from fastapi import FastAPI

app=FastAPI()

#homepage
@app.get('/', tags=["ROOT"])
async def root() -> dict:
    return {'greetings': 'Hello world'}

#get
@app.get('/todo', tags=["TODOS"])
async def get_todos() ->dict:
    return{'data':todos}

#post -->add
@app.post('/todo', tags=["TODOS"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        'mssg': 'A todo has been added to the list' 
    }

#put --> update
@app.put('/todo/{id}', tags=["TODOS"])
async def update_todo(id:int, body:dict) -> dict:
    for i in todos:
        if int(i['id'])==id:
            i['activity']=body['activity']
            return {
                'data': f'The activity of id {id} is updated'
            }
    return {
        'data': f'The activity of if {id} is not found' 
    }
#delete --> remove
@app.delete('/todo/{id}', tags=["TODOS"])
async def delete_todo(id:int) -> dict:
    for i in todos:
        if int(i['id'])==id:
            todos.remove(i)
            return {
                'mssg':f'The activity with id {id} has been removed'
            }
    return {
        'data':f'The activity with id {id} was not found'
    }




todos=[
    {'id':'1',
     'activity': 'code a fastapi intro project'},
    {'id':'2',
      'activity': 'watch breaking bad'}
]
