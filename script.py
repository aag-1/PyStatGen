
import time #this is so that we can benchmark the time required for the entired build 
from markdown2 import markdown # converts markdown file to html 
from jinja2 import Environment, FileSystemLoader  #inject everything into the layout.html file and create a final output html 
from json import load  

start_time = time.perf_counter()

template_env = Environment(loader=FileSystemLoader(searchpath="./"))

#in the above line all this does is basically specify how will we load the template 
'''
Environment - this keyword initializes the jinja2 enviroment, which is used to load templates, basically jinja uses it to control most of the stuff going on 
FileSystemLoader - this keyword is used to load templates from the file system 
searchpath="./"  - this means that jinja2 will look for template files in the current directory 
'''

template = template_env.get_template("layout.html") #  ???*******???

'''
we want to take the contents of the markdown.md file and convert it to html and put it in the layout
so we do as below
'''

#we open the markdown file, and we need to take the content from that
with open("article.md") as markdown_file:
    article = markdown(   # &&&^^&&& article variable consists of the stuff present in the markdown file, we have also used the term "markdown", which is basically a keyword for reading the stuff present in the markdown file
        markdown_file.read(),
        extras=['fenced-code-blocks', 'code-friendly']  #this line is so that we can add code snippets in our markdown file and make it appear in the correct format in the index.html             
    )

#we also want to load in the configuration for the article as well, using the config.json 
with open("config.json") as config_file: 
    config = load(config_file)  # assigning config variable such that its loaded up with the properties and attributes of the config file
#and now we will pass this config to the template 

# Read CSS
with open("styles.css") as css_file:
    css = css_file.read()

with open("index.html", "w") as output_file:
    output_file.write(
        template.render(# ???*******??? rendering, basically rendering the layout.html
            title=config['title'], # we take the properties and stuff of the title from the config file directly, understand the use of the config variable here and how we have declared it above
            logo=config['logo'],
            nav_links=config['nav_links'],
            social_links=config['social_links'],
            content=article, # &&&^^&&& here from the markdown file we take the stuff present in the article variable and put it in here i.e the layout 
            css=css,
            generator_credit=config['generator_credit']
        )
    )

end_time = time.perf_counter()

print(f"The total time taken for the build of the static site : {end_time - start_time:.6f} seconds" )
