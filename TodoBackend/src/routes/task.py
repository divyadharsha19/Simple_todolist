from flask import Blueprint, request, jsonify
from src.models.task import Task, db

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return jsonify({
            'success': True,
            'tasks': [task.to_dict() for task in tasks]
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    try:
        data = request.get_json()
        
        if not data or 'title' not in data:
            return jsonify({
                'success': False,
                'error': 'Title is required'
            }), 400
        
        title = data['title'].strip()
        if not title:
            return jsonify({
                'success': False,
                'error': 'Title cannot be empty'
            }), 400
        
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'task': task.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    try:
        task = Task.query.get(task_id)
        if not task:
            return jsonify({
                'success': False,
                'error': 'Task not found'
            }), 404
        
        data = request.get_json()
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        if 'title' in data:
            title = data['title'].strip()
            if not title:
                return jsonify({
                    'success': False,
                    'error': 'Title cannot be empty'
                }), 400
            task.title = title
        
        if 'completed' in data:
            task.completed = bool(data['completed'])
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'task': task.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    try:
        task = Task.query.get(task_id)
        if not task:
            return jsonify({
                'success': False,
                'error': 'Task not found'
            }), 404
        
        db.session.delete(task)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Task deleted successfully'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@task_bp.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    """Toggle task completion status"""
    try:
        task = Task.query.get(task_id)
        if not task:
            return jsonify({
                'success': False,
                'error': 'Task not found'
            }), 404
        
        task.completed = not task.completed
        db.session.commit()
        
        return jsonify({
            'success': True,
            'task': task.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

