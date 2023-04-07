# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID (UoW): w1898954
# Student ID (IIT): 20211381
# Date: 29.04.2021

def Progression_Outcome():
    global Progress
    global Trailer
    global Retriever
    global Excluded
    if credits_at_pass ==120:
        print('Progress')
        Progress = Progress + 1
    elif credits_at_pass ==100:
        print('Progress (module trailer)')
        Trailer = Trailer + 1
    elif credits_at_pass ==80 or credits_at_pass ==60:
        print('Do not Progress - module retriever')
        Retriever = Retriever + 1
    elif credits_at_pass ==40 and credits_at_defer ==0:
        print('Exclude')
        Excluded = Excluded + 1
    elif credits_at_pass ==40:
        print('Do not Progress - module retriever')
        Retriever = Retriever + 1
    elif credits_at_pass ==20 and (credits_at_defer ==20 or credits_at_defer ==0):
        print('Exclude')
        Excluded = Excluded + 1
    elif credits_at_pass ==20:
        print('Do not Progress - module retriever')
        Retriever = Retriever + 1
    elif credits_at_fail ==120:
        print('Exclude')
        Excluded = Excluded + 1
    elif credits_at_pass ==0 and (credits_at_defer ==20 or credits_at_defer ==40):
        print('Exclude')
        Excluded = Excluded + 1
    elif credits_at_pass ==0:
        print('Do not Progress - module retriever')
        Retriever = Retriever + 1

def border():
    print('---------------------------------------------------------------------------------------------------------')

def horizontal_histogram():
    print('\nProgress',Progress,'\t: ','*'*Progress)
    print('Trailer',Trailer,'\t: ','*'*Trailer)
    print('Retriever',Retriever,'\t: ','*'*Retriever)
    print('Excluded',Excluded,'\t: ','*'*Excluded,'\n')

Pass=[120,100,100,80,60,40,20,20,20,0]
Defer=[0,20,0,20,40,40,40,20,0,0]
Fail=[0,0,20,20,20,40,60,80,100,120]
no_of_data=len(Pass)

Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0

border()
print('')
for data in range(no_of_data):
    credits_at_pass =Pass[data]
    credits_at_defer =Defer[data]
    credits_at_fail =Fail[data]
    Progression_Outcome()
horizontal_histogram()
Outcome = Progress + Trailer + Retriever + Excluded 
print(Outcome,'outcomes in total.')
border()

