def marks_grades(n):
    if n>=90:
        grades.append(10)
    elif n>=80:
        grades.append(9)
    elif n>=70:
        grades.append(8)
    elif n>=60:
        grades.append(7)
    elif n>=50:
        grades.append(6)
    elif n>=40:
        grades.append(5)

def fail():
    print("You FAILED the above subject,so we do not find your GPA....!")

choice=input("""
select the Regulation
[20]R-20
[23]R-23
""")
grades=[]


#R20

#SEM1
r20_sem_1=["20A54101T Linear Algebra and Multivariate Calculus:",
           "20A51101T Chemistry:",
           "20A05201T Problem Solving and C Programming:",
           "20A04101T Basic Electrical and Electronics Engineering:",
           "20A03202P Engineering Workshop: ",
           "20A05202P Computer Engineering Workshop: ",
           "20A51101P Chemistry Lab:",
           "20A05201P Problem Solving and C Programming Lab:",
           "20A04101P Basic Electrical Electronics Engineering Lab:"]
r20_sem_c1=[3.0,3.0,3.0,3.0,1.0,2.0,1.5,1.5,1.5]
t_semc1=19.5

#SEM2
r20_sem_2=["20A54202T Differential Equations & Vector Calculus:",
           "20A56201 Applied Physics:",
           "20A52101 Communicative English:",
           "20A05101 PythonProgramming:",
           "20A03101 Engineering Drawing:",
           "20A03101P Engineering Drawing Lab:",
           "20A52101P Communicative English Lab:",
           "20A56201P Applied Physics Lab:",
           "20A05101P Python Programming Lab:"]
r20_sem_c2=[3.0,3.0,3.0,3.0,2.0,1.0,1.5,1.5,1.5]
t_semc2=19.5

#SEM3
r20_sem_3=["20CS301 Discrete MathematiCS & Graph Theory:",
           "20CS302 Digital ElectroniCS& Microprocessors:",
           "20CS303 Advanced Data Structures & Algorithms:" ,
           "20CS304 Object Oriented Programming Through Java :",
           "20CS305 Computer Organization:",
           "20CS306P Digital ElectroniCS& Microprocessors Lab:" ,
           "20CS307P Advanced Data Structures And Algorithms Lab:",
           "20CS308P Object Oriented Programming Through Java Lab:",
           "20CS309P Web Application Development:"]
r20_sem_c3=[3.0,3.0,3.0,3.0,3.0,1.5,1.5,1.5,2]
t_semc3=21.5

#SEM4
r20_sem_4=["20CS401 Deterministic & Stochastic Statistical Methods:",
"20CS402 Database Management Systems:",
"20CS403 Operating Systems:" ,
"20CS404 Software Engineering:", 
"20CS405A Managerial Economics & Financial Analysis:", 
"20CS406P Database Management Systems Lab:",
"20CS407P Operating Systems Lab:", 
"20CS408P Software Engineering Lab:",
"20CS409P Skill Oriented Course II Exploratory Data Analysis With R:"]
t_semc4=21.5
r20_sem_c4=[3.0,3.0,3.0,3.0,3.0,1.5,1.5,1.5,2]

#SEM5
r20_sem_5=["20CS501 Computer Networks:",	
"20CS502 Artificial Intelligence:",
"20CS503 Formal Languages and Automata Theory:",
"20CS504B INTERNET OF THINGS:",
"20CS505B Wireless Communication System:",	
"20CS506P Computer Networks Lab:",	
"20CS507P Artificial Intelligence Lab:"	,
"20CS508 Skill oriented course-III Mobile Application Development:",
"20CS509 Evaluation of Community Service Project:"]
r20_sem_c5=[3.0,3.0,3.0,3.0,3.0,1.5,1.5,2,1.5]
t_semc5=21.5

#SEM6
r20_sem_6=["20CS601 Compiler Design:",
"20CS602 Machine Learning:",	
"20CS603 Data Warehousing and Data Mining:",	
"20CS604B Computer Graphics:",
"20CS605B Embedded Systems:",	
"20CS606P Compiler De0sign:",
"20CS607P Machine Learning Lab:",	
"20CS608P Data Warehousing and Data Mining Lab:",	
"20CS609P Skill Oriented Course - IV Soft Skills:"]
r20_sem_c6=[3.0,3.0,3.0,3.0,3.0,1.5,1.5,1.5,2]
t_semc6=21.5

#SEM7
r20_sem_7=["20CS701A Cloud Computing:",
"20CS702C Cryptography & Network Security:",	
"20CS703A Data Sciences:",
"20CS704B Management Science:",	
"20CS705B Principles of Communication Systems:",	
"20CS706B Principles of Cellular & Mobile Communications:",	
"20CS707B Internet of Things Lab (SOC-V):",	
"20CS708  Evaluation of Industry Internship:"]
r20_sem_c7=[3.0,3.0,3.0,3.0,3.0,3.0,2,3.0]
t_semc7=23

#R23

#SEM1

r23_sem_1=["23CS101 Communicative English:",	
"23CS102 Chemistry:",	
"23CS103 Linear Algebra & Calculus:",	
"23CS104 Basic Civil & Mechanical Engineering:",	
"23CS105 Introduction to Programming:",	
"23CS101P Communicative English Lab:",	
"23CS102P Chemistry Lab:",
"23CS105P Computer Programming Lab:",	
"23CS106P Engineering Workshop:",
"23CS107 Health and wellness, Yoga and sports:"]

r23_sem_c1=[2,3,3,3,3,1,1,1.5,1.5,0.5]
t23_semc1=19.5


#SEM2

r23_sem_2=["23CS201 Engineering Physics:",	
"23CS202 Differential Equations & Vector Calculus:",	
"23CS203 Basic Electrical and Electronics Engineering:",	
"23CS204 Engineering Graphies:",	
"23CS205 Data Structures:",	
"23CS201P Engineering Physics Lab:",	
"23CS202P Electrical and Electronics Engineering Workshop:",
"23CS205P Data Structures Lab:",	
"23CS206P IT Workshop:",
"23CS207 NSS/NCC/Scouts & Guides/Community Service:"]

r23_sem_c2=[3,3,3,3,3,1,1.5,1.5,1,0.5]
t23_semc2=20.5

#SEM3

r23_sem_3=["23CS301 Discrete Mathematics & Graph Theory :",
"23CS302 Universal Human Values–Understanding Harmony:",
"23CS303 Digital Logic &Computer Organization:",
"23CS304 Advanced Data Structures & Algorithm Analysis:",
"23CS305 Object Oriented Programming Through Java:",
"23CS306P Advanced Data Structures and Algorithm Analysis Lab:",
"23CS307P Object Oriented Programming Through Java Lab:",
"23CS308P Python Programming:"]

r23_sem_c3=[3,3,3,3,3,1.5,1.5,2]
t23_semc3=20

#SEM4
r23_sem_4=["23CS401 Managerial Economics and Financial Analysis:",
"23CS402 Probability & Statistics:",
"23CS403 Operating Systems:",
"23CS404 Database Management Systems:",
"23CS405 Software Engineering:",
"23CS406P Operating Systems Lab:",
"23CS407P Database Management Systems Lab:",
"23CS408P Full Stack Development-I:",
"23CS409 Design Thinking &Innovation:"
]

r23_sem_c4=[2,3,3,3,3,1.5,1.5,2,2]
t23_semc4=21


all_sems=[r20_sem_1,r20_sem_2,r20_sem_3,r20_sem_4,r20_sem_5,r20_sem_6,r20_sem_7,r23_sem_1,r23_sem_2,r23_sem_3,r23_sem_4]
all_sems_credits=[r20_sem_c1,r20_sem_c2,r20_sem_c3,r20_sem_c4,r20_sem_c5,r20_sem_c6,r20_sem_c7,r23_sem_c1,r23_sem_c2,r23_sem_c3,r23_sem_c4]
all_t_credits=[t_semc1,t_semc2,t_semc3,t_semc4,t_semc5,t_semc6,t_semc7,t23_semc1,t23_semc2,t23_semc3,t23_semc4]

def gpa(m):
    sum_1=0
    subs=all_sems_credits[m]
    t_credits=all_t_credits[m]
    if len(grades)==len(all_sems[m]):
        for i in range(0,len(grades)):
            mul_1=grades[i]*subs[i]
            sum_1+=mul_1
            gpa_1=sum_1/t_credits
        print(round(gpa_1,2))

def marks(k):
    l_sem=all_sems[k]
    print("Enter marks")
    for i in range(0,len(l_sem)):
        sem1_marks=int(input(f"{l_sem[i]}"))
        if sem1_marks<40:
            fail()
            return(0)
        marks_grades(sem1_marks)
    


if choice=="20":

    choice1=input("""
Year:
        [1] 1st year
        [2] 2nd year
        [3] 3rd year
        [4] 4th year
        """)
    if choice1=="1":

        year_1=input("""
Sem:
        [1] I sem
        [2] II sem
        """)
        if year_1=="1":
            marks(0)
            gpa(0)
        if year_1=='2':
            marks(1)
            gpa(1)

        
    if choice1=="2":
         year_2=input("""
Sem:
        [3] III sem
        [4] IV sem
        """)
         if year_2=="3":
             marks(2)
             gpa(2)
         if year_2=="4":
             marks(3)
             gpa(3)
    if choice1=="3":
         year_3=input("""
Sem:
        [5] V sem
        [6] VI sem
        """)
         if year_3=="5":
             marks(4)
             gpa(4)
         if year_3=="6":
             marks(5)
             gpa(5)
    if choice1=="4":
         year_4=input("""
Sem:
        [7] VII sem
        [8] VIII sem
        """)
         if year_4=="7":
             marks(6)
             gpa(6)
         if year_4=="8":
             print("In this semester,we only have project with 12 credits")

if choice=="23":
    choice1=input("""
Year:
        [1] 1st year
        [2] 2nd year
        """)
    if choice1=="1":
        year23=input("""
Sem:
        [1] I sem
        [2] II sem
        """)
        if year23=="1":
            marks(7)
            gpa(7)
        if year23=="2":
            marks(8)
            gpa(8)
            
    if choice1=="2":
        year23=input("""
Sem:
        [3] III sem
        [4] IV sem
        """)
        if year23=="3":
            marks(9)
            gpa(9)
        if year23=="4":
            marks(10)
            gpa(10)



             


