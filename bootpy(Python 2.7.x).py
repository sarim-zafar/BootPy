#I have tried to divided each module to work independently so that i can pinpoint errors easily i know that the variable names are not clear right now
#but i plan on assigning them meaningfull names regarding to their purpose.Description of anything i deem neccessary is written below it if you still have an
#issue please report/contact me

#removes extra spaces in between html code
def space_corrector(file):
    temp=[]
    try:
        final_file= open(file+".html","r")
        for elements in final_file:
            if elements!="\n":
                temp.append(elements)
        final_file.close()
        final_file= open(file+".html","w")
        for elements in temp:
            final_file.write(elements)
        final_file.close()
    except IOError:
        print("File does not exist")
        
#This function calls other various functions which generate code for their respective nvaigations bars
#It acts as a hub for all those function and helps me avoid creating alot of mess in just one function
def navigation():
    global transparent_scroll
    transparent_scroll=False
    global transparent_fixed
    transparent_fixed=False
    global sidebar_nav_exists
    sidebar_nav_exists=False
    global scroll_nav
    scroll_nav=False
    global nav
    nav=""
    pages=[]
    temp=""
    
    #This asks the user how many items does he/she require
    #in most cases it will create pages with those names and copy
    #the same nav bar code to them
    z=raw_input("How many items do you want in your menu: ")
    z=int(z)
    f=""
    while True:
        
        #Asks if the user would like to add a logo to the navigation bar alongside the name of the website works pretty neat
        #but only if the dimensions of the logo added a re appropriate it will mess up the body of nav bar if you add logo
        #with big dimensions
        logo=raw_input("Do you want to add a logo to the navigation bar?\n1)Yes\n2)No\nPlease Choose your option:")
        if(logo=="1" or logo=="2"):
            break
        print("Wrong Input")
    while  True:
        type_nav=raw_input("""Please classify the type of Nav-bar that you want from the following:
1)Pils(Will look like buttons)\n2)Sticky(Fixed to top)\n3)Sidebar\nPlease Choose your option:""")
        if (type_nav=="1" or type_nav=="2" or type_nav=="3"):
            break
        print("Wrong Input")
    if type_nav=="1":
        f=pills_nav(z,pages,logo)
        
    elif type_nav=="2":
        while True:
            type_top=raw_input("What kind of top nav bar do you want?\n1)Fixed\n2)Static\n3)Scrolling nav\n4)Fixed(Transparent)\n5)Scrolling nav(Transparent)\nPlease Choose your option:")
            type_top=int(type_top)
            if (type_top>=1 and type_top<=5 ):
                break
            print("Wrong Input")
        if type_top==1:
            nav="""\t\t<link rel="stylesheet" href="css/navbar-fixed-top.css">
\t</head>
\t<body>\n"""
            f=fixed_nav(z,logo,pages,f)
        elif type_top==2:
            nav="""\t\t<link rel="stylesheet" href="css/navbar-static-top.css">
\t</head>
\t<body>\n"""
            f=Static_nav(z,logo,pages,f)
        elif type_top==3:
            scroll_nav=True
            nav="""\t\t<!-- Custom CSS -->
\t\t<link href="css/scrolling-nav.css" rel="stylesheet">
\t</head>
\t<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">\n"""
            f=Scrolling_nav(z,logo,f)
        elif type_top==4:
            transparent_fixed=True
            nav="""\t\t<!--Custom CSS -->   
\t\t<link href="css/transparent_fixed_navbar.css" rel="stylesheet">
\t</head>
\t<body>\n"""
        elif type_top==5:
            transparent_scroll=True
            nav="""\t\t<!-- Plugin CSS -->
\t\t<link rel="stylesheet" href="css/animate.min.css" type="text/css">
\t\t<!-- Custom CSS -->
\t\t<link rel="stylesheet" href="css/creative.css" type="text/css">
\t</head>
\t<body id="page-top">\n"""
            f=transparent_scroll_navbar(z,logo,f)
    elif type_nav=="3":
        sidebar_nav_exists=True
        nav="""\t\t<!--Custom CSS -->
\t\t<link href="css/simple-sidebar.css" rel="stylesheet">
\t</head>
\t<body>\n"""
        f=sidebar_nav(z,logo,pages,f)
    else:
        print"Wrong input"
        
    #This part adds the same nav bar for the other pages that user as well
    if (scroll_nav==False and transparent_scroll==False):
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
            temp4 = open((temp+".html"),"w")
            for t in temp3:
                temp4.write(t)
            temp4.close()
            
#It is a module which decides what to write in the head of the document depending upon the choice of the navigation bar if no navigation bar is chosen it will
#print out a code without including the css file for any navigation bar
    f=f+"\n"
    return f

#this is one of the sub modules for the navigation function it simply generates the code for its relevant nav bar and turns on any flag if required
#this nav doesnot creaate extra pages as its basic idea is for it to be used a single page site hence scrolling nav 
def transparent_scroll_navbar(z,logo,f):
    global Name
    f=f+"""\n\t\t<!-- Navigation -->
\t\t<nav id="mainNav" class="navbar navbar-default navbar-fixed-top">
\t\t\t<div class="container-fluid">
\t\t\t\t<!-- Brand and toggle get grouped for better mobile display -->
\t\t\t\t<div class="navbar-header">
\t\t\t\t\t<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t</button>
"""
    if logo=="1":            
        logo1=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
        f=f+'\n\t\t\t\t\t\t<a href="index.html"><img src="images/'+logo1+'" alt=""></a>\n'
        print("Great!!! all done now copy the image into the 'images' folder")
        print("""Warning by adding a logo to the nav-bar you might end up make it look messy
you can avoid/fix such issues by adding a logo with appropriate dimension""")
    f=f+"""\t\t\t\t\t<a class="navbar-brand page-scroll" href="#page-top" style="color:black">"""+Name+"""</a>
\t\t\t\t</div>
\t\t\t\t<!-- Collect the nav links, forms, and other content for toggling -->
\t\t\t\t<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
\t\t\t\t\t<ul class="nav navbar-nav navbar-right">"""
    g=""
    print("----------------Important message----------------\nPlease note that though n portions will be created only n-1 will have tabs and the first portion will become your default or main page and you can access it by clicking on the site name\n----------------Important message----------------")
    if z is not 1:
        g=""
        for i in range(0,z):
            b=str(raw_input("Please enter the name of item number "+str(i+1)+" : "))
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
\t\t\t\t\t\t<li><a class="page-scroll" href="#'''+(temp[0])+'''" style="color:black">'''+b+'''</a></li>'''
    f=f+"""               
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</nav>"""
    f=f+g
    return f

#this is one of the sub modules for the navigation function it simply generates the code for its relevant nav bar and turns on a specific flag if required
def transparent_fixed_navbar(z,logo,pages,f):
    global Name
    f=f+"""\t\t<!-- Navigation -->
\t\t<nav class="navbar navbar-default navbar-custom navbar-fixed-top">
\t\t\t<div class="container-fluid">
\t\t\t\t<div class="navbar-header page-scroll">
\t\t\t\t\t<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t</button>"""
    if logo=="1":            
        logo1=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
        f=f+'\n\t\t\t\t\t<a href="index.html"><img src="images/'+logo1+'" alt=""></a>\n'
        print("Great!!! all done now copy the image into the 'images' folder")
        print("""Warning by adding a logo to the nav-bar you might end up make it look messy
you can avoid/fix such issues by adding a logo with appropriate dimension""")
    else:
        f=f+"\n"
    f=f+"""\t\t\t\t\t<a class="navbar-brand" href="index.html" style="color:black">"""+Name+"""</a>
\t\t\t\t</div>
\t\t\t\t<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
\t\t\t\t\t<ul class="nav navbar-nav navbar-right">"""
    b=str(raw_input("What is the name of first item(This will be your current page): "))
    f=f+'''\t\t\t\t\t\t<li><a href="index.html" style="color:black">'''+str(b)+'''</a></li>'''
    for i in range(1,z):
        b=str(raw_input("Please enter the name of item number "+str(i+1)+" : "))
        pages.append(b)
        f=f+'''\n\t\t\t\t\t\t<li><a href='''+b+'''.html style="color:black">'''+b+'''</a></li>'''
        skeleton(b)
    f=f+"""
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</nav>"""
    return f

#this is one of the sub modules for the navigation function it simply generates the code for its relevant nav bar and turns on a specific flag if required
def sidebar_nav(z,logo,pages,f):
    global Name
    f=f+"""\t\t<!-- Navigation -->
\t\t<div id="wrapper">
\t\t\t<div id="sidebar-wrapper">
\t\t\t\t<ul class="sidebar-nav">"""
    if logo=="1":            
        logo1=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
        f=f+'\n\t\t\t\t\t<a href="index.html"><img src="images/'+logo1+'" alt=""></a>\n'
        print("Great!!! all done now copy the image into the 'images' folder")
        print("""Warning by adding a logo to the nav-bar you might end up make it look messy
you can avoid/fix such issues by adding a logo with appropriate dimension""") 
    else:
        f=f+"\n"
    f=f+"""\t\t\t\t\t<li class="sidebar-brand"><a href="index.html">"""+Name+"""</a></li>\n"""
    b=str(raw_input("What is the name of first item(This will be your current page): "))
    f=f+'''\t\t\t\t\t<li><a href="index.html">'''+b+'''</a></li>\n'''
    for i in range(1,z):
        b=str(raw_input("Please enter the name of item number "+str(i+1)+" : "))
        pages.append(b)
        f=f+'''\n\t\t\t\t\t<li><a href="'''+b+'''.html">'''+b+'''</a></li>'''
        skeleton(b)
    f=f+"""\n\t\t\t\t</ul>
\t\t\t</div>
\t\t\t<a href="#menu-toggle" id="menu-toggle" class="btn btn-default">Toggle Menu
\t\t\t\t<i class="fa fa-angle-double-down animated"></i>
\t\t\t</a>"""
    return f

#this is one of the sub modules for the navigation function it simply generates the code for its relevant nav bar and turns on any flag if required
#this nav doesnot creaate extra pages as its basic idea is for it to be used a single page site hence scrolling nav 
def Scrolling_nav(z,logo,f):
    global Name
    temp=""
    f=f+"""\t\t<!-- Navigation -->
\t\t<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
\t\t\t<div class="container">
\t\t\t\t<div class="navbar-header page-scroll">"""
    if logo=="1":
        logo1=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
        f=f+'\n\t\t\t\t\t<a href="index.html"><img src="images/'+logo1+'" alt=""></a>'
        print("Great!!! all done now copy the image into the 'images' folder")            
    f=f+"""
\t\t\t\t\t<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t</button>
\t\t\t\t\t<a class="navbar-brand page-scroll" href="#page-top">"""+Name+"""</a>
\t\t\t\t</div>
\t\t\t\t<!-- Collect the nav links, forms, and other content for toggling -->
\t\t\t\t<div class="collapse navbar-collapse navbar-ex1-collapse">
\t\t\t\t\t<ul class="nav navbar-nav">
\t\t\t\t\t\t<li class="hidden"><a class="page-scroll" href="#page-top"></a></li>"""
    g=""
    print("----------------Important message----------------\nPlease note that though n portions will be created only n-1 will have tabs and the first portion will become your default or main page and you can access it by clicking on the site name\n----------------Important message----------------")
    if z is not 1:
        g=""
        for i in range(0,z):
            b=str(raw_input("Please enter the name of item number "+str(i+1)+" : "))
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
    return f

#this is one of the sub modules for the navigation function it simply generates the code for its relevant nav bar and turns on a specific flag if required
def Static_nav(z,logo,pages,f):
    global Name
    f=f+"""\t\t<!-- Navigation -->
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
        logo1=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
        f=f+'\n\t\t\t\t\t<a href="index.html"><img src="images/'+logo1+'" alt=""></a>'
        print("Great!!! all done now copy the image into the 'images' folder")
    f=f+"""
\t\t\t\t\t<a class="navbar-brand" href="index.html">"""+Name+"""</a>
\t\t\t\t</div>
\t\t\t\t<div class="navbar-collapse collapse">
\t\t\t\t\t<ul class="nav navbar-nav">"""
    b=str(raw_input("What is the name of first item(This will be your current page): "))
    f=f+'''
\t\t\t\t\t\t<li class="active"><a href="index.html">'''+b+'''</a></li>'''
    if z is not 1:
        for i in range(1,z):
            b=str(raw_input("Please enter the name of item number "+str(i+1)+" : "))
            pages.append(b)
            f=f+'''
\t\t\t\t\t\t<li><a href="'''+b+'''.html">'''+b+'''</a></li>'''
            skeleton(b)
        f=f+"""
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</div>"""
        return f
    
#this is one of the sub modules for the navigation function it simply generates the code for its relevant nav bar and turns on a specific flag if required
def fixed_nav(z,logo,pages,f):
    f=f+"""\t\t<!-- Navigation -->
\t\t<div class="navbar navbar-default navbar-fixed-top" role="navigation">
\t\t\t<div class="container">
\t\t\t\t<div class="navbar-header">
\t\t\t\t\t<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t\t<span class="icon-bar"></span>
\t\t\t\t\t</button>"""
    if logo=="1":
        logo1=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
        f=f+'\n\t\t\t\t\t<a href="index.html"><img src="images/'+logo1+'" alt=""></a>'
        print("Great!!! all done now copy the image into the 'images' folder")
    f=f+"""\n\t\t\t\t\t<a class="navbar-brand" href="index.html">"""+Name+"""</a>
\t\t\t\t</div>
\t\t\t\t<div class="navbar-collapse collapse">
\t\t\t\t\t<ul class="nav navbar-nav">"""
    b=str(raw_input("What is the name of first item(This will be your current page): "))
    f=f+'''\n\t\t\t\t\t\t<li class="active"><a href="index.html">'''+b+'''</a></li>'''
    if z is not 1:
        for i in range(1,z):
            b=str(raw_input("Please enter the name of item number "+str(i+1)+" : "))
            pages.append(b)
            f=f+'''\n\t\t\t\t\t\t<li><a href="'''+b+'''.html">'''+b+'''</a></li>'''
            skeleton(b)
        f=f+"""
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</div>"""
        return f
    
#this is one of the sub modules for the navigation function it simply generates the code for its relevant nav bar 
def pills_nav(z,pages,logo):
    y=raw_input("What kind of menu do you want:\n1) Horizontal\n2) Vertical\nPlease Choose your option:")
    y=str(y)
    if y=="1":
        x=' nav class="nav nav-pills"'
    elif y=="2":
        x=' nav class="nav nav-pills nav-stacked"'
    if logo=="1":
        logo1=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
        print("Great!!! all done now copy the image into the 'images' folder")
    b=str(raw_input("What is the name of first item(This will be your current page): "))
    f='\t</head>\n\t<body>\n\t\t<ul '+str(x)+'>\n'
    if logo=="1":
        f=f+'\t\t\t<a href="index.html"><img src="images/'+logo1+'" alt=""></a>'
    f=f+'\n\t\t\t<li class="active"><a href="index.html">'+b+'</a></li>'
    if z is not 1:
        for i in range(1,z):
            b=str(raw_input("Please enter the name of item number "+str(i+1)+" : "))
            pages.append(b)
            f=f+'\n\t\t\t<li><a href="'+b+'.html">'+b+'</a></li>'
            skeleton(b)
    f=f+'\n\t\t</ul>'
    return f

#This function generates code for footer of the website right now its
#limited to one style and a limited(only 6 at the time of writing) sites
#that you can link it to
def footer():
    k="""\n\t\t<footer>
\t\t\t<div class="container">
\t\t\t\t<div class="row">
\t\t\t\t\t<div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
\t\t\t\t\t\t<ul class="list-inline text-center">"""
    while True:
        a=int(raw_input("\nPlease Choose from the following:\n1)Link to Twitter\n2)Link to Facebook\n3)Link to github\n4)Link to google plus\n5)Link to yahoo\n6)Link to reddit\nPlease Choose your option:"))
        x=raw_input("\nEnter the link you want to embed in regard to the chosen option:")
        if a==1:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>'''        
        if a==2:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>'''
        if a==3:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-github fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>'''
        if a==4:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-google-plus fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>'''
        if a==5:
             k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-yahoo fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>'''
        if a==6:
            k=k+'''\n\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t<a href='''+x+'''>
\t\t\t\t\t\t\t\t\t<span class="fa-stack fa-lg">
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-circle fa-stack-2x"></i>
\t\t\t\t\t\t\t\t\t\t<i class="fa fa-reddit fa-stack-1x fa-inverse"></i>
\t\t\t\t\t\t\t\t\t</span>
\t\t\t\t\t\t\t\t</a>
\t\t\t\t\t\t\t</li>'''
        b=int(raw_input("Do you want to add more links:\n1)Yes\n2)No\nPlease Choose your option:"))
        if b==2:
            k=k+"""\n\t\t\t\t\t\t\t<p class="copyright text-muted">Copyright &copy; """+Name+""" 2015</p>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</div>
\t\t</footer>\n"""
            break
    else:
        print("\nWrong Input")
    return k

# generates code for image tag and returns all of the code in the variable returned
def image():
    b=raw_input("Enter the name of the image with extension(e.g image.jpg): ")
    while True:
        x=int(raw_input("Choose how you want to align the image:\n1)Center\n2)Left\n3)Right\nPlease Choose your option: "))
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

#generates code for headings
def paragraph():
    print("""How big you want the text to be with 'h1' being biggest to 'h6' being the smallest
h1,h2,h3,h4,h5,h6""")
    y=raw_input("Select an option:")
    x=raw_input("Okay great now enter the text:\n")
    z="\n\t\t<"+y+">"+x+"</"+y+">\n"
    return z

#generates code that is placed at the end of file whcih includes the jquery/jscript links neccessary for the working of the code
def end():
    global scroll_nav
    c="""
\t\t<!----------------Bootstrap core JavaScript------------------->
\t\t<!--   ==================================================   -->
\t\t<!-- Placed at the end of the document so the pages load faster -->
\t\t<!-- Include all compiled plugins (below), or include individual files as needed -->
\t\t<!-- jQuery -->
\t\t<script src="js/jquery.js"></script>
\t\t<script src="js/bootstrap.min.js"></script>"""
    if(scroll_nav==True):
        c=c+"""
\t\t<!-- Scrolling Nav JavaScript -->
\t\t<script src="js/jquery.easing.min.js"></script>
\t\t<script src="js/scrolling-nav.js"></script>"""
    if (sidebar_nav_exists==True):
        c=c+"""\n\t\t<script>
\t\t\t$("#menu-toggle").click(function(e) {
\t\t\t\te.preventDefault();
\t\t\t\t$("#wrapper").toggleClass("toggled");
\t\t\t});
\t\t</script>"""
    if(transparent_fixed==True):
        c=c+'\n\t\t<script src="js/transparent_fixed_navbar.js"></script>'
    if(transparent_scroll==True):
        c=c+"""
\t\t<!-- Plugin JavaScript -->
\t\t<script src="js/jquery.easing.min.js"></script>
\t\t<!-- Plugin JavaScript -->
\t\t<script src="js/jquery.fittext.js"></script>
\t\t<!-- Custom Theme JavaScript -->
\t\t<script src="js/creative.js"></script>"""
    c=c+"""
\t</body>
</html>"""
    return c

#generates code which is placeed at the start of the file which includes the head of the html documents
def start():
    global nav
    c="""<!DOCTYPE html>
<html lang="en">
\t<head>
\t\t<meta charset="utf-8">
\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge">
\t\t<meta name="viewport" content="width=device-width, initial-scale=1">
\t\t<title>"""+str(title)+"""</title>
\t\t<!-- Latest compiled and minified CSS -->
\t\t<link rel="stylesheet" href="css/bootstrap.min.css">\n"""
    if footer_exists==True or transparent_scroll==True:
        c=c+'\n\t\t<!-- Footer CSS -->\n\t\t<link href="css/font-awesome.min.css" rel="stylesheet" type="text/css">\n'+nav
        if transparent_scroll==False:
            c='\n\t\t<!-- Optional theme -->\n\t\t<link rel="stylesheet" href="css/bootstrap-theme.min.css">'+c   
    else:
        c=c+'\n\t\t<!-- Optional theme -->\n\t\t<link rel="stylesheet" href="css/bootstrap-theme.min.css">\n'
        c=c+nav
    if nav_exists==False:
       c=c+'\t</head>\n\t<body>'
    return c

#generates code for a table written in html by getting input from the user
def table(td,tr):
    y="""
\t\t<table class="table table-hover">
\t\t\t<tr>"""
    for x in range(0,b):
        z=raw_input("Enter heading for column number "+str(x+1)+":" )
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
            y=y+raw_input("Enter value of cell at position ("+str(i)+","+str(p)+") columns: ")
            y="""\t"""+y+"""</td>"""
        y=y+"""
\t\t\t</tr>"""
    y=y+"""       
\t\t</table>\n"""
    return y

#A simple menu function for enabling the user to choose the feature they want to use
def menu():
    print("What do you want to do first:\n1) Generate a table \n2) Generate a paragraph \n3) Generate a navigation menu\n4) Add an Image\n5) Add an Footer\n6)Save the document\n7)Exit")
    y=raw_input("Please Choose your option:")
    y=str(y)
    return y

#creates the file in directory to which all of the data is to be written
def skeleton(y):
    try:
        a= open(y+".html","r")
        x=""
        a.close()
    except IOError:
        a= open(y+".html","w")
        a.close()
        
#The main program starts here        
print'\t\tWelcome to our Website for noobs program\n'

#creates the file
skeleton("index")

#An array which hosts the text spitted out by various modules and i plan on using techniques so that it can arrange what text to place where intelegently
# What happens from here is quite self explanatory we call functions by passing appropriate variables and they return us code which we add to the array
# and in the end the program arranges the code i.e putting the code from start function on the start of the program and end function to end
# and writes it all in a file
Final=[]

#it will name the document as the user input which will appear in the tab in the browser
global title
#the name of the website is stored here
global Name

#These are some variables that i use to manage all the code during execution of the program , like how to arrange , which to put in start and which in last
#Insure wheather user added a transparent fixed navigation or not if he did then it will add the script that is neccesary for the working of navigation
transparent_fixed=False

#Insure wheather user added a  scroll navigation or not if he did then it will add the script that is neccesary for the working of navigation
scroll_nav=False

#Insure wheather user added a nav bar or not if he didnt then it will add the close tag for head and open tag for body without adding
#any stylesheets used for the navigation bar
nav_exists=False

#Insure wheather user added a footer or not if he didnt then it will add the close tag for head and open tag for body without adding any stylesheets used for the footer
footer_exists=False

#Insure wheather user added a sidebar navigation or not if he did then it will add the script that is neccesary for the working of toggle button
sidebar_nav_exists=False

#Insure wheather user added a  transparent scroll navigation or not if he did then it will add the script that is neccesary for the working of navigation
transparent_scroll=False

#some other global variables
nav=""
f=""
foot=""
Name=raw_input("Enter the Name of your site: ")
title=Name

#iterates until the user specifies if he/she wants to exit the program
while True:
    
    #prints the main menu of the program
    a=menu()
    if a=="1":
        z=[]
        a=int(raw_input("Please enter the number of rows in your table: "))
        b=int(raw_input("Please enter the number of columns in your table: "))
        y=table(a,b)
        Final.append(y)        
        print"\nDone\n"
    elif a=="2":
        y=paragraph()
        Final.append(y)      
        print"\nDone\n"
    elif a=="3":
        f=navigation()
        print"\nDone\n"
        nav_exists=True
    elif a=="4":
        y=image()
        Final.append(y)      
        print"\nDone\n"
    elif a=="5":
        foot=footer()
        print"\nDone\n"
        footer_exists=True
    elif a=="6":
        #Extremely poorly written code i will revise it once i get to it
        #i will rewrite most of this code and place it in a function
        x=end()
        c=start()
        try:
            for i in range(0,len(Final)-1):
                for j in range(i+1,len(Final)-1):
                    if Final[j]==Final[i]:
                        Final.remove(Final[j])
                        i=i+1
        except IndexError:
            pass
        w=0
        Z= open("index.html","w")
        Z.write(c)
        if scroll_nav==True or transparent_scroll==True:
            i=f.split("</h1>")
            Z.write(i[0]+"</h1>")
            for n in Final:
                emp=n.split("\n")
                for xz in emp:
                    if xz!="":   
                        xz="\t\t\t\t"+xz
                        Z.write(xz+"\n")
                        w=w+1
                w=0
            for m in range(1,len(i)):
                if w>=0 and m!="":
                    Z.write(i[m])
                    if(m<len(i)-1):
                        Z.write("</h1>")
                w=w+1
            Z.write(foot)
        else:
            f=f.strip()
            Z.write(f)  
            w=0
            if sidebar_nav_exists==True:
                for i in Final:
                    emp=i.split("\n")
                    for xz in emp:
                        if xz!="":   
                            xz="\t"+xz
                            Z.write(xz)
                            if(w!=0 or w!=len(emp)-1):
                                Z.write("\n")
                            w=w+1
            w=0
            if sidebar_nav_exists==True:
                if footer_exists==True:
                    emp=foot.split("\n")
                    for xz in emp:
                        if xz!="":                  
                            xz="\t"+xz
                            Z.write(xz)
                            if(w!=0 or w!=len(emp)-1):
                                Z.write("\n")
                            w=w+1
            if sidebar_nav_exists==False:
                w=0
                for i in Final:
                    emp=i.split("\n")
                    for xz in emp:
                        if xz!="":   
                            Z.write(xz)
                            if(w!=0 or w!=len(emp)-1):
                                Z.write("\n")
                            w=w+1
                if footer_exists==True:
                    Z.write(foot)
            if sidebar_nav_exists==True:
                Z.write("\n\t\t</div>\n")
        Z.write(x)
        Z.close()
        space_corrector("index")
        print"""------------------------------------------\nDone saving the document\n------------------------------------------"""
    elif a=="7":
        break
    else:
        print "Wrong Input\n"
        
#Notes for the current program which will be updated upon each new revision:
#This is a very dumb code write now but i plan on enhancing it i will try to release newer version as fast i can.
#Right now my goal is to work on adding more modules neccessary and integrating them inteligently,
#Some minor bug fixes and give me suggestions what to do next
#Regards
#Sarim Zafar
