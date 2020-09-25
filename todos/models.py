from django.db import models

# Estos modelos sirven para relacionar los datos en la base de datos
class Todo(models.Model):
    # Se crean los modelos y patrones para los datos de los que constara cada To Do
    todo_title = models.CharField(max_length=30)
    todo_text = models.CharField(max_length=200)
    todo_date = models.DateTimeField('date added')
    todo_completed = models.BooleanField(default=False)
    # esta funcion hace que se devuelva por defecto el texto de cada To Do
    def __str__(self):
        return self.todo_title

class Subtodo(models.Model):
    # Cada sub todo esta relacionado con el todo principal por lo que hay que relacionar las classes
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    subtodo_text = models.CharField(max_length=100)
    subtodo_date = models.DateTimeField('date subtodo added')
    subtodo_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.subtodo_text
    
    