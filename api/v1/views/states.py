#!/usr/bin/python3
'''view for State'''

from flask import Blueprint, jsonify
from models import storage
from models.state import State

states = Blueprint('states', __name__)

@states.route('/states', method=['GET'])
def all_states():
    ''' list all states in json format '''
    stored_states = storage.all(State)
    states_list = []
    for state in stored_states:
        state_dict = state.to_dict()
        state_list.append(state_dict)
    return states_list
