import csv
import math
def ed (l1,l2):
    dist = 0
    #print(l1,l2)
    for i in range (0,len(l1)):
        dist = dist + ((l1[i] - l2[i]) ** 2)
        #print(dist)
    return (round(math.sqrt(dist),4))
flag = True
reviewers = []
reviews = []
my_dict = {}
while(flag):
    try:
        file_name = input("Give the name of the restaurant reviews file: ")
        with open(file_name) as f:
            csv_reader = csv.reader(f, delimiter=',')
            #print("csv_reader",csv_reader)
            for row in csv_reader:
                #print(row)
                reviewers.append(row[0])
                #print("reviewers",reviewers)
                reviews.append(row[1:])

            for i in range(len(reviewers)):
                my_dict[reviewers[i]] = reviews[i]
            
            for key,values in my_dict.items():
                res = {values[i]: values[i + 1] for i in range(0, len(values), 2)}
                my_dict[key] = res
        #print (my_dict)
        flag1 = True
        while(flag1):
            userInp = int(input("What do you want to do? Input 1 for similarity between two reviewers, or Input 2 for similarity between one reviewer and all others in the database or 3 to quit: "))
            #print(type(userInp))
            if (userInp == 1):
                rev1 = input("Provide Reviewer1 name: ")
                rev2 = input("Provide Reviewer2 name: ")
                temprev1 = []
                temprev2 = []
                #print(my_dict[rev1].keys())
                for keys in my_dict[rev1].keys():
                    val = float(my_dict[rev1][keys])
                    #print(val)
                    temprev1.append(val)
                    if keys in my_dict[rev2].keys():
                        val1 = float(my_dict[rev2][keys])
                        temprev2.append(val1)
                print("The similarity score between", rev1,"and",rev2,"is:",ed(temprev1,temprev2))
                #print(len(temprev1),len(temprev2))
            elif (userInp == 2):
                rev1 = input("Provide Reviewer name: ")     
                 
                if rev1 in my_dict.keys():
                    list_keys=list(my_dict.keys())
                    list_keys.remove(rev1)
                    user_movie=list(my_dict[rev1].keys())
                    print("The Similarity Scores are: "+"\n")
                    for j in range(len(list_keys)):
                        sum2=0.0
                        for k in range(len(user_movie)):
                            if user_movie[k] in my_dict[list_keys[j]].keys():
                                diff=float(my_dict[rev1][user_movie[k]])-float(my_dict[list_keys[j]][user_movie[k]])
                                sum2=sum2+math.pow(diff,2)
                        print(str(rev1)+"   "+str(list_keys[j])+"   "+str(round(math.sqrt(sum2),2)))
                #flag1=False
                else:
                    print("Please enter valid username")
                
                
            elif (userInp == 3):
                print("Goodbye!")
                flag1 = False
                break
            else:
                print("Enter valid choice[1, 2 or 3]: ")

        if(flag1 == False):
            flag = False
            break
        else: 
            break
    except:
        print("Enter valid inputs!")
