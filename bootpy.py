
#I have tried to divided each module to work independently so that i can pinpoint errors easily i know that the variable names are not clear right now
#but i plan on assigning them meaningfull names regarding to their purpose description of anything i deem neccessary is written below it if you still have an
#issue please report

global head
head=1
global nav
nav=""
global c
c=""
global f
f=""

#These are some variables that i use to manage all the code during execution of the program , like how to arrange , which to put in start and which in last

def paragraph():
    print("""How big you want the text to be with 'h1' being biggest to 'h6' being the smallest
h1,h2,h3,h4,h5,h6""")
    y=raw_input("Select an option:")
    x=raw_input("Okay great now enter the text:\n")
    z="\n<"+y+">"+x+"</"+y+">"
    return z

##This is a simple pragraph module which spurts out a simple paragraph in html the user can decide the size 

def end():
    c="""
    <!----------------Bootstrap core JavaScript------------------->
    <!--   ==================================================   -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
  </body>
</html>"""
    return c

#As the name suggests its a module which simply gives a fixed code which is supposed to be merged to the end of all the other code

def start():
    c="""<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>"""+str(title)+"""</title>\n
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">\n"""+nav+"""\n  </head>\n  <body>"""
    if head!=2:
        c=c+f
    if head==2:
        c=c+"""
    <!--Custom CSS -->
    <link href="http://startbootstrap.com/templates/simple-sidebar/css/simple-sidebar.css" rel="stylesheet">\n  </head>\n    <div id="wrapper">
<div id="sidebar-wrapper">
  <ul class="sidebar-nav">
    <li class="sidebar-brand">
      <a href="#">"""+Name+"""</a>
    </li>"""
        c=c+f
    return c

#It is a module which decides what to write in the head of the document depending upon the choice of the navigation bar if no navigation bar is chosen it will
#print out a code without including the css file for any navigation bar

def navigation():
    z=raw_input("How many items do you want in your menu: ")
    z=int(z)
    f=""
    a=raw_input("""Please classify the type of Nav-bar that you want from the following:
1)Pils(Will look like buttons)
2)Sticky(Fixed to top)\n""")
    if a=="1":
        head=1
        y=raw_input("What kind of menu do you want:\n1) Horizontal\n2) Vertical\n")
        y=str(y)
        if y=="1":
            x='nav class="nav nav-pills"'
        elif y=="2":
            x='nav class="nav nav-pills nav-stacked"'
        b=raw_input("What is the name of first item: ")
        b=str(b)
        f='<ul '+str(x)+'>\n  <li class="active"><a href="#">'+b+'</a></li>'
        if z is not 1:
            for i in range(1,z):
                b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                b=str(b)
                f=f+'\n  <li><a href="#">'+b+'</a></li>'
            f=f+'\n</ul>'
    elif a=="2":
        Type=raw_input("What type of sticky bar would you like:\n1)Top\n2)Sidebar\n")
        Type=int(Type)
        if Type==1:
            type_top=raw_input("What kind of top nav bar do you want?\n1)Fixed\n2)Static\n")
            type_top=int(type_top)
            if type_top==1:
                nav='    <link rel="stylesheet" href="http://getbootstrap.com/examples/navbar-fixed-top/navbar-fixed-top.css">'
                f=f+"""\n    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">"""+Name+"""</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">"""
                b=raw_input("What is the name of first item: ")
                b=str(b)
                f=f+'\n        <li class="active"><a href="#">'+b+'</a></li>'
                if z is not 1:
                    for i in range(1,z):
                        b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                        b=str(b)
                        f=f+'\n        <li><a href="#'+b+'">'+b+'</a></li>'
                    f=f+'\n      </ul>\n    </div>\n  </div>\n' 
            elif type_top==2:
                nav='    <link rel="stylesheet" href="http://getbootstrap.com/examples/navbar-static-top/navbar-static-top.css">'
                f=f+"""\n<div class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">"""+Name+"""</a>
          </div>
          <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">"""
                b=raw_input("What is the name of first item: ")
                b=str(b)
                f=f+'\n        <li class="active"><a href="#">'+b+'</a></li>'
                if z is not 1:
                    for i in range(1,z):
                        b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                        b=str(b)
                        f=f+'\n        <li><a href="#'+b+'">'+b+'</a></li>'
                    f=f+'\n      </ul>\n    </div>\n  </div>\n'
        elif Type==2:
             head=2
             for i in range(0,z):
                b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                b=str(b)
                f=f+'\n    <li><a href="#">'+b+'</a></li>'
             f=f+'\n  </ul>\n</div>'
    else:
        print"Wrong input"
    return f

#This module is the most complex in the program it allows the user to make a navigation bar of thier choice right now the types of these navigation bars
#are picked from the getbootstrap site though not all are included also it might be correct to state that it is a pseudo navigation bar as it does have those buttons
# but they dont do anything meaningfull so the interpage relationship is zero right now so it is only good for one page i am planing to fix this issue next

def table(td,tr):
    y='\n<table class="table table-hover">\n  <tr>\n'
    for x in range(0,b):
        z=raw_input("Enter heading for "+str(x+1)+" colomn: ")
        z="    <th>"+z+"</th>\n"
        y=y+z
    y=y+"  </tr>\n"
    for i in range(0,tr):
        y=y+'  <tr>\n'
        for p in range(0,td):
            y=y+'    <td>'
            y=y+raw_input("Enter value of cell at "+str(i)+" rows * "+str(p)+" colomns: ")
            y=y+("</td>\n")
        y=y+"  </tr>\n"
    y=y+"</table>"
    return y

#This programs enables the end users to write tables in html as easy as it gets

def menu():
    print("""What do you want to do first:\n1) Generate a table \n2) Generate a paragraph \n3) Generate a navigation menu\n4) Save the document\n5)Exit\n""")
    y=raw_input("Please Choose your option.")
    y=str(y)
    return y

#A simple menu function for enabling the user to choose the feature they want to use

def skeleton():
    try:
        f= open("Your website.html","r")
        x=""
        f.close()
    except IOError:
        f= open("Your website.html","w")
        f.close()
        
#This function generates a html file if one by the name already does not exist
        
print'          Welcome to our Website for noobs program\n'

#The program starts here

skeleton()
Final=[]

#An array which hosts the text spitted out by various modules and i plan on using techniques so that it can arrange what text to place where intelegently

global title
title=raw_input("What do you want the title of the document to be? : ")

#it will name the document as the user input which will appear in the tab
# What happens from here is quite self explanatory we call functions by passing appropriate variables and they return us code which we add to the array
# and in the end the program arranges the code ie putting the code from start function on the start of the program and end function to end
# and writes it all in a file

global Name
Name=raw_input("Enter the Name of your site: ")
while True:
    a=menu()
    if a=="1":
        z=[]
        a=int(raw_input("Please enter the number of rows in your table: "))
        b=int(raw_input("Please enter the number of colomns in your table: "))
        y=table(a,b)
        Final.append(y)
        print"\nDone\n"
    elif a=="2":
        y=paragraph()
        Final.append(y)
        print"\nDone\n"
    elif a=="3":
        y=navigation()
        Final.append(y)
        print"\nDone\n"
    elif a=="4":
        x=end()
        Final.append(x)
        c=start()
        Final.insert(0,c)
        # This will insert code till the head from the start appropriate to the code requested by the user
        f= open("Your website.html","a")
        for i in Final:
            f.write(i)
        f.close()
        print"Done saving the document"
    elif a=="5":
        break
    else:
        print "Wrong Input"
        print"\n"
#Notes for the current program which will be updated upon each new revision:
#This is a very dumb code write now but i plan on enhancing it i will try to release newer version as fast i can.
#Right now my goal is to work on adding more modules neccessary and integrating them inteligently also a more clear goal would be to integrate a better way to use
# the navigation  bar by generating new pages as well as joining them which i will commit personaly in the next few revisions
#Regards
#Sarim Zafar
