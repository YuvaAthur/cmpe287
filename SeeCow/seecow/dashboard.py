from flask import Flask, jsonify, request
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import json,sys
from flask_restful import Resource, Api
import math
from seecow import db


bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard/overview.html')