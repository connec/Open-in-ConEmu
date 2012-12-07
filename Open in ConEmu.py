import sublime, sublime_plugin
from subprocess import call

class OpenInConemuCommand(sublime_plugin.WindowCommand):
  def run(self, dirs):
    args = [ '/single', '/dir', "%s" % dirs[0] ]

    try:
      call(['ConEmu'] + args)
      return None
    except WindowsError:
      pass

    try:
      call(['ConEmu64'] + args)
      return None
    except WindowsError:
      pass

    raise Exception("Could not find ConEmu or ConEmu64 on path")

  def is_visible(self, dirs):
    return len(dirs) == 1