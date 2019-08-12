from flask import Flask, jsonify, request
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
# from bson.json_util import dumps
import json,sys
from flask_restful import Resource, Api
import math
from seecow.db import get_db

bp = Blueprint('camfeed', __name__)

@bp.route('/')
def index():
    return current_status()

@bp.route('/current_status', methods=['GET'])
def current_status():
    """Show all status, most recent first."""
    db = get_db()
    cattle_status = db.execute(
        'SELECT *'
        ' FROM parlor_status'
        ' ORDER BY time_in DESC',
    ).fetchall()    # returns a list
    msg = 'Number of records = {0}.'.format(len(cattle_status))
    # flash(msg)
    return render_template('camfeed/list.html', cattle_status=cattle_status)
    # return cattle_status


# def current_status():
#     return jsonify({'result' : json.loads(dumps(CATTLE_STATUS.find().limit(5).sort("time", -1)))})


@bp.route('/cattle/<id>', methods=['GET'])
def get_one_cattle(id):
    cattle = get_db().execute(
        'SELECT *'
        ' FROM parlor_status'
        ' WHERE cattle_id LIKE ?',
        (id,)
    ).fetchone()
    return cattle           # returns a list

# def get_one_cattle(id):

#     q = CATTLE_STATUS.find_one({'CATTLE_ID' : id})

#     if q:
#         output = {'id' : q['CATTLE_ID'], 'Cattle Status' : q['Status']}
#     else:
#         output = 'No results found'

#     return jsonify({'result' : output})


@bp.route('/insert_status/<id>/<status>/<location>', methods=['GET','POST'])
def insert_status(id,status,location):
    cattle = get_db().execute(
        'INSERT '
        ' INTO parlor_status'
        ' VALUES(ID, STATUS, LOCATION)',
        (id,status,location)
    )


# 	NEW_CATTLE_STATUS = CATTLE_STATUS.update({'CATTLE_ID' : id}, {'CATTLE_ID' : id,'Status' : Status,'LOCATION' : LOCATION})
# 	return jsonify({'New Status of CATTLE_ID' : Status})
# #   new_status_details = CATTLE_STATUS.find_one({'CATTLE_ID' : id})
# #   output = {'Status' : new_status_details['Status']}
