#I have tried to divided each module to work independently so that i can pinpoint errors easily i know that the variable names are not clear right now
#but i plan on assigning them meaningfull names regarding to their purpose description of anything i deem neccessary is written below it if you still have an
#issue please report
def image():
    b=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
    while True:
        x=int(raw_input("Choose how you want to align the image:\n1)Center\n2)Left\n3)Right\nPlease Choose your option: "))
        if(x==1):
            z='<img src="images/'+b+'" class="img-responsive center-block">\n'
            break
        elif(x==2):
            z='<img src="images/'+b+'" class="img-responsive align="left">\n'
            break
        elif(x==3):
            z='<img src="images/'+b+'" class="img-responsive align="right">\n'
            break
        else:
            print("wrong input")     
    print("Great!!! all done now copy the image into the 'images' folder")
    return z


def paragraph():
    print("""How big you want the text to be with 'h1' being biggest to 'h6' being the smallest
h1,h2,h3,h4,h5,h6""")
    y=raw_input("Select an option:")
    x=raw_input("Okay great now enter the text:\n")
    z="\n<"+y+">"+x+"</"+y+">"
    return z

#This is a simple pragraph module which spurts out a simple paragraph in html the user can decide the size 

def end():
    c="""
        <!----------------Bootstrap core JavaScript------------------->
        <!--   ==================================================   -->
        <!-- Placed at the end of the document so the pages load faster -->
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <!-- jQuery -->
        <script src="js/jquery.js"></script>
        <script src="js/bootstrap.min.js"></script>"""
    if(scroll_nav==False):
        c=c+"""\n      <!-- Scrolling Nav JavaScript -->
        <script src="js/jquery.easing.min.js"></script>
        <script src="js/scrolling-nav.js"></script>"""
    c=c+"""\n    </body>
</html>"""
    return c

#As the name suggests its a module which simply gives a fixed code which is supposed to be merged to the end of all the other code

def start():
    c="""<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>"""+str(title)+"""</title>\n
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- Optional theme -->
    <link rel="stylesheet" href="css/bootstrap-theme.min.css">\n"""+nav
    c=c+f
    return c

#It is a module which decides what to write in the head of the document depending upon the choice of the navigation bar if no navigation bar is chosen it will
#print out a code without including the css file for any navigation bar

def navigation():
    global scroll_nav
    scroll_nav=True
    global nav
    nav=""
    pages=[]
    temp=""
    z=raw_input("How many items do you want in your menu: ")
    z=int(z)
    f=""
    a=raw_input("""Please classify the type of Nav-bar that you want from the following:
1)Pils(Will look like buttons)\n2)Sticky(Fixed to top)\n3)Sidebar\nPlease Choose your option:""")
    if a=="1":
        y=raw_input("What kind of menu do you want:\n1) Horizontal\n2) Vertical\nPlease Choose your option:")
        y=str(y)
        if y=="1":
            x='nav class="nav nav-pills"'
        elif y=="2":
            x='nav class="nav nav-pills nav-stacked"'
        b=raw_input("What is the name of first item(This will be your current page): ")
        b=str(b)
        f='\n    <ul '+str(x)+'>\n      <li class="active"><a href="index.html">'+b+'</a></li>'
        if z is not 1:
            for i in range(1,z):
                b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                b=str(b)
                pages.append(b)
                f=f+'\n      <li><a href="'+b+'.html">'+b+'</a></li>'
                skeleton(b)
            f=f+'\n    </ul>'
            
    elif a=="2":
        type_top=raw_input("What kind of top nav bar do you want?\n1)Fixed\n2)Static\n3)Scrolling nav\nPlease Choose your option:")
        type_top=int(type_top)
        if type_top==1:
            nav='    <link rel="stylesheet" href="css/navbar-fixed-top.css">\n  </head>\n  <body>'
            f=f+"""\n    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="index.html">"""+Name+"""</a>
    </div>
    <div class="navbar-collapse collapse">
      <ul class="nav navbar-nav">"""
            b=raw_input("What is the name of first item(This will be your current page): ")
            b=str(b)
            f=f+'\n            <li class="active"><a href="index.html">'+b+'</a></li>'
            if z is not 1:
                for i in range(1,z):
                    b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                    b=str(b)
                    pages.append(b)
                    f=f+'\n            <li><a href="'+b+'.html">'+b+'</a></li>'
                    skeleton(b)
                f=f+'\n           </ul>\n        </div>\n      </div>\n    </div>\n' 
        elif type_top==2:
            nav="""    <link rel="stylesheet" href="css/navbar-static-top.css">\n  </head>\n  <body>"""
            f=f+"""\n  <div class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="index.html">"""+Name+"""</a>
      </div>
      <div class="navbar-collapse collapse">
        <ul class="nav navbar-nav">"""
            b=raw_input("What is the name of first item(This will be your current page): ")
            b=str(b)
            f=f+'\n            <li class="active"><a href="index.html">'+b+'</a></li>'
            if z is not 1:
                for i in range(1,z):
                    b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                    b=str(b)
                    pages.append(b)
                    f=f+'\n            <li><a href="'+b+'.html">'+b+'</a></li>'
                    skeleton(b)
                f=f+'\n           </ul>\n        </div>\n      </div>\n    </div>\n'
        elif type_top==3:
            nav="""    <!-- Custom CSS -->
<link href="css/scrolling-nav.css" rel="stylesheet">\n  </head>\n  <body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">"""
            f=f+"""\n    <!-- Navigation -->
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
<div class="container">
    <div class="navbar-header page-scroll">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand page-scroll" href="#page-top">"""+Name+"""</a>
    </div>
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse navbar-ex1-collapse">
        <ul class="nav navbar-nav">\n<li class="hidden"><a class="page-scroll" href="#page-top"></a></li>"""
            g=""
            print("----------------Important message----------------\nPlease note that though three portions will be created only two will have tabs and the first portion will become your default or main page and you can access it by clicking on the site name\n----------------Important message----------------")
            if z is not 1:
                g=""
                for i in range(0,z):
                    b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
                    b=str(b)
                    temp=b.split(" ")
                    g=g+'\n<!-- '+b+' Section -->'
                    g=g+'\n    <section id="'+(temp[0])+'" class="contact-section">'
                    g=g+"""\n    <div class="container">
    <div class="row">
        <div class="col-lg-12">
            <h1>"""+b+""" section</h1>
        </div>
    </div>
</div>
</section>\n"""
                    temp=b.split(" ")
                    if i is not 0:
                        f=f+'\n                <li><a class="page-scroll" href="#'+(temp[0])+'">'+b+'</a></li>'
            f=f+"\n               </ul>\n        </div>\n      </div>\n    </nav>\n"
            f=f+g
            scroll_nav=False
    elif (a=="3"):
        nav='    <!--Custom CSS -->\n    <link href="css/simple-sidebar.css" rel="stylesheet">\n  </head>\n  <body>'
        f=f+"""\n    <div id="wrapper">
      <div id="sidebar-wrapper">
        <ul class="sidebar-nav">
          <li class="sidebar-brand">
            <a href="index.html">"""+Name+"""</a>
          </li>
          <ul>"""
        b=raw_input("What is the name of first item(This will be your current page): ")
        b=str(b)
        f=f+'\n            <li><a href="index.html">'+b+'</a></li>'
        for i in range(1,z):
            b=raw_input("Please enter the name of item number "+str(i+1)+" : ")
            b=str(b)
            pages.append(b)
            f=f+'\n            <li><a href="'+b+'.html">'+b+'</a></li>'
            skeleton(b)
        f=f+'\n          </ul>\n        </div>\n    </div>'
    else:
        print"Wrong input"
    #This part adds the same nav bar for the other pages as well
    if (scroll_nav==True):
        for h in range(0,z-1):
            temp3=[]
            temp=pages[h]
            temp5=f
            temp5=temp5.replace('<li class="active">', '<li>');
            temp5=temp5.replace('<li><a href="'+temp+'.html">'+temp+'</a></li>', '<li class="active"><a href="'+temp+'.html">'+temp+'</a></li>');
            temp3.append(temp5)
            temp1=""
            temp2=""
            temp1=end()
            temp3.append(temp1)
            temp2=start()
            temp3.insert(0,temp2)
            # This will insert code till the head from the start appropriate to the code requested by the user
            temp4 = open((temp+".html"),"a")
            for t in temp3:
                temp4.write(t)
            temp4.close()
    return f

#This module is the most complex in the program it allows the user to make a navigation bar of thier choice right now the types of these navigation bars
#are picked from the getbootstrap site though not all are included fixed the inter page relationship everything now works[HOPEFULLY]

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
    print("What do you want to do first:\n1) Generate a table \n2) Generate a paragraph \n3) Generate a navigation menu\n4) Add an Image\n5)Save the document\n6)Exit\n")
    y=raw_input("Please Choose your option:")
    y=str(y)
    return y

#A simple menu function for enabling the user to choose the feature they want to use

def skeleton(y):
    try:
        a= open(y+".html","r")
        x=""
        a.close()
    except IOError:
        a= open(y+".html","w")
        a.close()
        
#This function generates a html file if one by the name already does not exist
        
print'          Welcome to our Website for noobs program\n'

#The program starts here

skeleton("index")
Final=[]

#An array which hosts the text spitted out by various modules and i plan on using techniques so that it can arrange what text to place where intelegently
# What happens from here is quite self explanatory we call functions by passing appropriate variables and they return us code which we add to the array
# and in the end the program arranges the code ie putting the code from start function on the start of the program and end function to end
# and writes it all in a file
global title
#it will name the document as the user input which will appear in the tab
global Name
#These are some variables that i use to manage all the code during execution of the program , like how to arrange , which to put in start and which in last

Name=raw_input("Enter the Name of your site: ")
title=Name
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
        global f
        f=""
        f=navigation()
        print"\nDone\n"
    elif a=="4":
        y=image()
        Final.append(y)
        print"\nDone\n"
    elif a=="5":
        x=end()
        Final.append(x)
        c=start()
        Final.insert(0,c)
        # This will insert code till the head from the start appropriate to the code requested by the user
        Z= open("index.html","a")
        for i in Final:
            Z.write(i)
        Z.close()
        print"Done saving the document\n"
    elif a=="6":
        break
    else:
        print "Wrong Input"
        print"\n"
#Notes for the current program which will be updated upon each new revision:
#This is a very dumb code write now but i plan on enhancing it i will try to release newer version as fast i can.
#Right now my goal is to work on adding more modules neccessary and integrating them inteligently,
#Some minor bug fixes and give me suggestions what to do next
#Regards
#Sarim Zafar
