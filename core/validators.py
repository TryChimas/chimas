from marshmallow import validate

def validate_username(value):
    validate.Length( min=3, max=15 ).__call__(value)
    validate.Regexp( regex = "^[a-zA-Z0-9_.-]+$" ).__call__(value)

def board_title(value):
    validate.Length( min=3, max=15 ).__call__(value)
    validate.Regexp( regex = "^(?:\w+\s*)*$" ).__call__(value)

def board_description(value):
    validate.Length( min=0, max=32 ).__call__(value)
    validate.Regexp( regex = "^(?:\w+\s*)*$" ).__call__(value)

def post_title(value):
    validate.Length( min=3, max=32 ).__call__(value)
    validate.Regexp( regex = "^(?:\w+\s*)*$" ).__call__(value)

def post_text(value):
    validate.Length( min=1, max=1024 ).__call__(value)
    #validate.Regexp( regex = "^(?:\w+\s*)*$" ).__call__(value)
