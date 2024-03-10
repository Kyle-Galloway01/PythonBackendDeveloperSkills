from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy object
db = SQLAlchemy(app)

# Initialize Marshmallow object for serialization
ma = Marshmallow(app)

# Define Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)

# Define Task Schema for serialization
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'completed')

# Initialize Task Schema
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result), 200

# Route to get a single task by id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    result = task_schema.dump(task)
    return jsonify(result), 200

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    title = request.json.get('title')
    description = request.json.get('description')
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

# Route to update an existing task by id
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    title = request.json.get('title')
    description = request.json.get('description')
    completed = request.json.get('completed')
    task.title = title if title else task.title
    task.description = description if description else task.description
    task.completed = completed if completed is not None else task.completed
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'}), 200

# Route to delete a task by id
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
