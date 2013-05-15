import sublime, sublime_plugin
from subprocess import Popen

class OpenInConemuCommand(sublime_plugin.WindowCommand):
  def run(self, dirs):
    args = [ '/single', '/dir', "%s" % dirs[0] ]

    try:
      Popen(['ConEmu'] + args)
      return None
    except WindowsError:
      pass

    try:
      Popen(['ConEmu64'] + args)
      return None
    except WindowsError:
      pass

    raise Exception("Could not find ConEmu or ConEmu64 on path")

  def is_visible(self, dirs):
    return len(dirs) == 1