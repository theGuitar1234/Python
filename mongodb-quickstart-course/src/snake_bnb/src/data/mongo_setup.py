import mongoengine

alias_core = 'core'
db = 'snakebnb'

def global_init():
    mongoengine.register_connection(alias='core', name='snake_bnb')

