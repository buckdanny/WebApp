__author__ = 'Joan'



from mako.template import Template
import Dealing
clients = Dealing.get_client_list(file = "C:\\Users\\Joan\Desktop\\web\\data\\Clients.txt")


mytemplate = Template(filename = "C:\\Users\\Joan\\Desktop\\WebApp\\templates\\list.mako",enable_loop="True")
print(mytemplate.render(clients = clients))
