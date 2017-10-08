class Command(object):
  def __init__(self, name, args_list, function):
    self.args = {
      'names' : [a for a,b in args_list],
      'types' : [b for a,b in args_list]
    }
    self.name = name

    self.function = function
