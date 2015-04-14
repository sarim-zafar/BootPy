#I have tried to divided each module to work independently so that i can pinpoint errors easily i know that the variable names are not clear right now
#but i plan on assigning them meaningfull names regarding to their purpose description of anything i deem neccessary is written below it if you still have an
#issue please report

def footer():
    k="""\n\t\t<footer>
\t\t\t<div class="container">
\t\t\t\t<div class="row">
\t\t\t\t\t<div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
\t\t\t\t\t\t<ul class="list-inline text-center">"""
    while True:
        a=int(input("\nPlease Choose from the following:\n1)Link to Twitter\n2)Link to Facebook\n3)Link to github\n4)Link to google plus\n5)Link to yahoo\n6)Link to reddit\nPlease Choose your option:"))
        x=input("\nEnter the link you want to embed in regard to the chosen option:")
        if a==1:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>\n'''        
        if a==2:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>\n'''
        if a==3:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-github fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>\n'''
        if a==4:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-google-plus fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>\n'''
        if a==5:
             k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-yahoo fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>\n'''
        if a==6:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-reddit fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>\n'''
        b=int(input("Do you want to add more links:\n1)Yes\n2)No\nPlease Choose your option:"))
        if b==2:
            k=k+"""\t\t\t\t\t\t\t<p class="copyright text-muted">Copyright &copy; """+Name+""" 2015</p>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</div>
\t\t</footer>"""
            break
        else:
            print("\nWrong Input")
    return k

def image():
    b=input("Enter the name of the image with extension(e.g image.jpg): ")
    while True:
        x=int(input("Choose how you want to align the image:\n1)Center\n2)Left\n3)Right\nPlease Choose your option: "))
        if(x==1):
            z='\t\t<img src="images/'+b+'" class="img-responsive center-block">\n'
            break
        elif(x==2):
            z='\t\t<img src="images/'+b+'" class="img-responsive align="left">\n'
            break
        elif(x==3):
            z='\t\t<img src="images/'+b+'" class="img-responsive align="right">\n'
            break
        else:
            print("wrong input")     
    print("Great!!! all done now copy the image into the 'images' folder")
    return z


def paragraph():
    print("""How big you want the text to be with 'h1' being biggest to 'h6' being the smallest
h1,h2,h3,h4,h5,h6""")
    y=input("Select an option:")
    x=input("Okay great now enter the text:\n")
    z="\n\t\t<"+y+">"+x+"</"+y+">"
    return z

#This is a simple pragraph module which spurts out a simple paragraph in html the user can decide the size 

def end():
    c="""
\t\t<!----------------Bootstrap core JavaScript------------------->
\t\t<!--   ==================================================   -->
\t\t<!-- Placed at the end of the document so the pages load faster -->
\t\t<!-- Include all compiled plugins (below), or include individual files as needed -->
\t\t<!-- jQuery -->
\t\t<script src="js/jquery.js"></script>
\t\t<script src="js/bootstrap.min.js"></script>"""
    try:
        if(scroll_nav==False):
            c=c+"""
\t\t<!-- Scrolling Nav JavaScript -->
\t\t<script src="js/jquery.easing.min.js"></script>
\t\t<script src="js/scrolling-nav.js"></script>"""
    except NameError:
        c=c
    c=c+"""
\t</body>
</html>"""
    return c

#As the name suggests its a module which simply gives a fixed code which is supposed to be merged to the end of all the other code

def start():
    try:
        c="""<!DOCTYPE html>
<html lang="en">
\t<head>
\t\t<meta charset="utf-8">
\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">
\t\t<meta name="viewport" content="width=device-width, initial-scale=1">
\t\t<title>"""+str(title)+"""</title>
\t\t<!-- Latest compiled and minified CSS -->
\t\t<link rel="stylesheet" href="css/bootstrap.min.css">
\t\t<!-- Optional theme -->
\t\t<link rel="stylesheet" href="css/bootstrap-theme.min.css">\n"""+nav
    except NameError:
        c="""<!DOCTYPE html>
<html lang="en">
\t<head>
\t\t<meta charset="utf-8">
\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">
\t\t<meta name="viewport" content="width=device-width, initial-scale=1">
\t\t<title>"""+str(title)+"""</title>
\t\t<!-- Latest compiled and minified CSS -->
\t\t<link rel="stylesheet" href="css/bootstrap.min.css">
\t\t<!-- Optional theme -->
\t\t<link rel="stylesheet" href="css/bootstrap-theme.min.css">\n"""
    try:
        c=c+f
    except NameError:
        return c
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
    z=input("How many items do you want in your menu: ")
    z=int(z)
    f=""
    logo=input("Do you want to add a logo to the navigation bar?\n 1)Yes\n2)No\nPlease Choose your option:")                                        
    a=input("""Please classify the type of Nav-bar that you want from the following:
1)Pils(Will look like buttons)\n2)Sticky(Fixed to top)\n3)Sidebar\nPlease Choose your option:""")
    if a=="1":
        y=input("What kind of menu do you want:\n1) Horizontal\n2) Vertical\nPlease Choose your option:")
        y=str(y)
        if y=="1":
            x=' nav class="nav nav-pills"'
        elif y=="2":
            x='\t\tnav class="nav nav-pills nav-stacked"'
        b=input("What is the name of first item(This will be your current page): ")
        b=str(b)
        f='\t</head>\n\t<body>\n\t\t<ul '+str(x)+'>\n'
        if logo=="1":
            logo1=input("Enter the name of the image with extension(e.g image.jpg): ")
            f=f+'\t\t\t<img src="images/"'+logo1+'" alt="">'
            print("Great!!! all done now copy the image into the 'images' folder")
        f=f+'\t\t\t<li class="active"><a href="index.html">'+b+'</a></li>'
        if z is not 1:
            for i in range(1,z):
                b=input("Please enter the name of item number "+str(i+1)+" : ")
                b=str(b)
                pages.append(b)
                f=f+'\n\t\t\t<li><a href="'+b+'.html">'+b+'</a></li>'
                skeleton(b)
            f=f+'\n\t\t</ul>'
            
    elif a=="2":
        type_top=input("What kind of top nav bar do you want?\n1)Fixed\n2)Static\n3)Scrolling nav\nPlease Choose your option:")
        type_top=int(type_top)
        if type_top==1:
            nav="""
\t\t<link rel="stylesheet" href="css/navbar-fixed-top.css">
\t</head>
\t<body>"""
            f=f+"""
\t\t<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
\t\t\t<div class="container">
\t\t\t\t<div class="navbar-header">
\t\t\t\t\t<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t</button>"""
            if logo=="1":
                logo1=input("Enter the name of the image with extension(e.g image.jpg): ")
                f=f+'\n\t\t\t\t\t<img src="images/"'+logo1+'" alt="">'
                print("Great!!! all done now copy the image into the 'images' folder")
            f=f+"""\t\t\t\t\t<a class="navbar-brand" href="index.html">"""+Name+"""</a>
    \t\t\t\t</div>
    \t\t\t\t<div class="navbar-collapse collapse">
    \t\t\t\t\t<ul class="nav navbar-nav">"""
            b=input("What is the name of first item(This will be your current page): ")
            b=str(b)
            f=f+'''
    \t\t\t\t\t\t<li class="active"><a href="index.html">'''+b+'''</a></li>\n'''
            if z is not 1:
                for i in range(1,z):
                    b=input("Please enter the name of item number "+str(i+1)+" : ")
                    b=str(b)
                    pages.append(b)
                    f=f+'''
\t\t\t\t\t\t<li><a href="'''+b+'''.html">'''+b+'''</a></li>\n'''
                    skeleton(b)
                f=f+"""
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</div>"""
        elif type_top==2:
            nav="""\t\t<link rel="stylesheet" href="css/navbar-static-top.css">
\t</head>
\t<body>"""
            f=f+"""
\t\t<div class="navbar navbar-default" role="navigation">
\t\t\t<div class="container-fluid">
\t\t\t\t<div class="navbar-header">
\t\t\t\t\t<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t</button>"""
            if logo=="1":
                logo1=input("Enter the name of the image with extension(e.g image.jpg): ")
                f=f+'\n\t\t\t\t\t<img src="images/"'+logo1+'" alt="">'
                print("Great!!! all done now copy the image into the 'images' folder")
            f=f+"""
\t\t\t\t\t<a class="navbar-brand" href="index.html">"""+Name+"""</a>
\t\t\t\t</div>
\t\t\t\t<div class="navbar-collapse collapse">
\t\t\t\t\t<ul class="nav navbar-nav">"""
            b=input("What is the name of first item(This will be your current page): ")
            b=str(b)
            f=f+'''
\t\t\t\t\t\t<li class="active"><a href="index.html">'''+b+'''</a></li>\n'''
            if z is not 1:
                for i in range(1,z):
                    b=input("Please enter the name of item number "+str(i+1)+" : ")
                    b=str(b)
                    pages.append(b)
                    f=f+'''
\t\t\t\t\t\t<li><a href="'''+b+'''.html">'''+b+'''</a></li>\n'''
                    skeleton(b)
                f=f+"""
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</div>"""
        elif type_top==3:
            nav="""\t\t<!-- Custom CSS -->
\t\t<link href="css/scrolling-nav.css" rel="stylesheet">
\t</head>
\t<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">"""
            f=f+"""
\t\t<!-- Navigation -->
\t\t<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
\t\t\t<div class="container">
\t\t\t\t<div class="navbar-header page-scroll">
\t\t\t\t\t<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t</button>"""
            if logo=="1":
                logo1=input("Enter the name of the image with extension(e.g image.jpg): ")
                f=f+'\n\t\t\t\t\t<img src="images/"'+logo1+'" alt="">'
                print("Great!!! all done now copy the image into the 'images' folder")            
            f=f+"""
\t\t\t\t\t<a class="navbar-brand page-scroll" href="#page-top">"""+Name+"""</a>
\t\t\t\t</div>
\t\t\t\t<!-- Collect the nav links, forms, and other content for toggling -->
\t\t\t\t<div class="collapse navbar-collapse navbar-ex1-collapse">
\t\t\t\t\t<ul class="nav navbar-nav">
\t\t\t\t\t\t<li class="hidden"><a class="page-scroll" href="#page-top"></a></li>"""
            g=""
            print("----------------Important message----------------\nPlease note that though three portions will be created only two will have tabs and the first portion will become your default or main page and you can access it by clicking on the site name\n----------------Important message----------------")
            if z is not 1:
                g=""
                for i in range(0,z):
                    b=input("Please enter the name of item number "+str(i+1)+" : ")
                    b=str(b)
                    temp=b.split(" ")
                    g=g+'''
\t\t<!-- '''+b+''' Section -->'''
                    g=g+'''
\t\t<section id="'''+(temp[0])+'''" class="contact-section">'''
                    g=g+"""
\t\t\t<div class="container">
\t\t\t\t<div class="row">
\t\t\t\t\t<div class="col-lg-12">
\t\t\t\t\t\t<h1>"""+b+""" section</h1>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</div>
\t\t</section>"""
                    temp=b.split(" ")
                    if i is not 0:
                        f=f+'''              
\t\t\t\t\t\t<li><a class="page-scroll" href="#'''+(temp[0])+'''">'''+b+'''</a></li>'''
            f=f+"""               
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</nav>"""
            f=f+g
            scroll_nav=False
    elif (a=="3"):
        nav="""\t\t<!--Custom CSS -->
\t\t<link href="css/simple-sidebar.css" rel="stylesheet">
\t</head>
\t<body>"""
        f=f+"""
\t\t<div id="wrapper">
\t\t\t<div id="sidebar-wrapper">
\t\t\t\t<ul class="sidebar-nav">
\t\t\t\t\t<li class="sidebar-brand">
\t\t\t\t\t\t<a href="index.html">"""+Name+"""</a>
\t\t\t\t\t</li>"""
        b=input("What is the name of first item(This will be your current page): ")
        b=str(b)
        f=f+'''
\t\t\t\t\t<li>
\t\t\t\t\t\t<a href="index.html">'''+b+'''</a>
\t\t\t\t\t</li>'''
        for i in range(1,z):
            b=input("Please enter the name of item number "+str(i+1)+" : ")
            b=str(b)
            pages.append(b)
            f=f+'''
\t\t\t\t\t<li>
\t\t\t\t\t\t<a href="'''+b+'''.html">'''+b+'''</a>
\t\t\t\t\t</li>'''
            skeleton(b)
        f=f+"""
\t\t\t\t</ul>
\t\t\t</div>
\t\t</div>"""
    else:
        print("Wrong input")
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
    y="""
\t\t<table class="table table-hover">
\t\t\t<tr>"""
    for x in range(0,b):
        z=input("Enter heading for "+str(x+1)+" colomn: ")
        z="""
\t\t\t\t<th>"""+z+"""</th>"""
        y=y+z
    y=y+"""
\t\t\t</tr>"""
    for i in range(0,tr):
        y=y+"""
\t\t\t<tr>"""
        for p in range(0,td):
            y=y+"""
\t\t\t\t<td>"""
            y=y+input("Enter value of cell at "+str(i)+" rows * "+str(p)+" colomns: ")
            y="""\t"""+y+"""</td>"""
        y=y+"""
\t\t\t</tr>"""
    y=y+"""       
\t\t</table>"""
    return y

#This programs enables the end users to write tables in html as easy as it gets

def menu():
    print("What do you want to do first:\n1) Generate a table \n2) Generate a paragraph \n3) Generate a navigation menu\n4) Add an Image\n5) Add an Footer\n6)Save the document\n7)Exit")
    y=input("Please Choose your option:")
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
#The program starts here        
print('          Welcome to our Website for noobs program\n')
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

global nav_exists
nav_exists=False
#Insure wheather user added a nav bar or not if he didnt then it will add the close tag for head and open tag for body without adding any stylesheets used for the nav bar
global footer_exists
footer_exists=False
#Insure wheather user added a footer or not if he didnt then it will add the close tag for head and open tag for body without adding any stylesheets used for the footer

Name=input("Enter the Name of your site: ")
title=Name
while True:
    a=menu()
    if a=="1":
        z=[]
        a=int(input("Please enter the number of rows in your table: "))
        b=int(input("Please enter the number of colomns in your table: "))
        y=table(a,b)
        Final.append(y)
        print("\nDone\n")
    elif a=="2":
        y=paragraph()
        Final.append(y)
        print("\nDone\n")
    elif a=="3":
        global f
        f=""
        f=navigation()
        print("\nDone\n")
        nav_exists=True
    elif a=="4":
        y=image()
        Final.append(y)
        print("\nDone\n")
    elif a=="5":
        y=footer()
        Final.append(y)
        print("\nDone\n")
        footer_exists=True
    elif a=="6":
        x=end()
        Final.append(x)
        c=start()
        Final.insert(0,c)
        # This will insert code till the head from the start appropriate to the code requested by the user
        for i in range(0,len(Final)-1):
            for j in range(i+1,len(Final)-1):
                if Final[j]==Final[i]:
                    Final.remove(Final[j])
                    i=i+1
        i=len(Final)-1
        j=len(Final)-2
        if Final[i]==Final[j]:
            Final.remove(Final[j])
        if footer_exists==True:
            x='''\t\t<link href="css/font-awesome.min.css" rel="stylesheet" type="text/css">\n'''
            Final.insert(1, x)
        if nav_exists==False:
            x="\t</head>\n\t<body>"
            if footer_exists==True:
                Final.insert(2, x)
            else:
                Final.insert(1, x)
        Z= open("index.html","a")
        for i in Final:
            Z.write(i)
        Z.close()
        print("""------------------------------------------
Done saving the document\n------------------------------------------""")
    elif a=="7":
        break
    else:
        print("Wrong Input")
        print("\n")
#Notes for the current program which will be updated upon each new revision:
#This is a very dumb code write now but i plan on enhancing it i will try to release newer version as fast i can.
#Right now my goal is to work on adding more modules neccessary and integrating them inteligently,
#Some minor bug fixes and give me suggestions what to do next
#Regards
#Sarim Zafar
