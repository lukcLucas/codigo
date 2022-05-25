import webbrowser
import subprocess
import Keira

def parse_command(command_action, argument=""):
  # print(command_action[0:3])
  # print(command_action)
  # print('argument -> ', argument)

  if command_action[0:3]=="web":
    open_link(command_action[4:], argument)
    Keira.speak("Pesquisando " + argument)
  elif command_action[0:4]=="path":
    open_program(command_action[5:])
    Keira.speak("Abrindo " + argument)
  elif command_action=='commands':
    reload_commands()
    Keira.speak("Atualizado")


def open_link(link, argument=""):
  print(f'{link}/search?q={argument}')
  webbrowser.get('windows-default').open_new(f'{link}/search?q={argument}')

def open_program(path):
  subprocess.Popen([path, '-new-tab'])

def reload_commands():
  Keira.read_commands_file()