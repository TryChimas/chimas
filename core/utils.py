#from .boards import Boards

def all_required_fields_dict(required_fields, user_input_data):
    user_data = {}
    for field in required_fields:
        if not user_input_data[field]:
            return False
        else:
            user_data.update( { field : user_input_data[field] })
    return user_data

def board_id_exists(cls, board_id):
    if Boards.query.filter_by( id=board_id ).first():
        return True
    else:
        return False

def post_id_exists(cls, post_id):
    if Posts.query.filter_by( id=post_id ).first():
        return True
    else:
        return False
