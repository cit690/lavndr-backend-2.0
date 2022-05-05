from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile
from api.models.message import Message
from api.models.conversation import Conversation
conversations = Blueprint('conversations', 'conversation')