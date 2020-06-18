import matplotlib.pyplot as plt
import numpy as np

def Z_test(exp_mean, ctrl_mean, exp_std, ctrl_std, exp_N, ctrl_N ):
    #delta=(exp_N-ctrl_N)
    z=(exp_mean-ctrl_mean-0)/(np.sqrt((exp_std**2/exp_N)+(ctrl_std**2/ctrl_N)))
    
    return z

def effect_size(exp_mean,ctrl_mean,exp_std,ctrl_std, exp_N, ctrl_N):
    
    d=abs(exp_mean-ctrl_mean)/(np.sqrt(((exp_N-1)*exp_std**2+(ctrl_N-1)*ctrl_std**2)/(exp_N+ctrl_N-2)))
    
    return d


#===============Calculate score in a simpler way==============
def Scores(data):
    pre_scores=data[data.columns[4:65]]
    post_scores=data[data.columns[68:129]]
    
    final_pre_score=pre_scores.sum(axis=1)
    final_post_score=post_scores.sum(axis=1)
    scores=[final_pre_score, final_post_score]
    
    return scores
#======================== perform some stat analysis==========

def Stat_Analysis(data, val ):
    Gender_data, labels= Gender_spliter(data)
    M_data, F_data, O_data = Gender_data[0],Gender_data[1],Gender_data[2]
    
    M_scores=Scores(M_data)
    F_scores=Scores(F_data)
    O_scores=Scores(O_data)
    
    pre_mean=[round(M_scores[0].mean(),2), round(F_scores[0].mean(),2), round(O_scores[0].mean(),2)]
    post_mean=[round(M_scores[1].mean(),2), round(F_scores[1].mean(),2), round(O_scores[1].mean(),2)]
    
    pre_std=[round(M_scores[0].std(),2), round(F_scores[0].std(),2), round(O_scores[0].mean(),2)]
    post_std=[round(M_scores[1].std(),2), round(F_scores[1].std(),2), round(O_scores[1].mean(),2)]
    
    mean=[pre_mean,post_mean]
    std=[pre_std, post_std]
    
    if val==0:
        cat="Traditional"
    elif val==1:
        cat="Transformed"
    
    axes=plt.figure(figsize=(15,10))
    axes.suptitle('Mean and Standard deviation for {} Courses'.format(cat), fontsize=16)

    ax1=axes.add_subplot(221)
    ax1.scatter(labels,mean[0], label="pre")
    ax1.scatter(labels,mean[1], label="post")
    ax1.set_title("Average Score")
    ax1.legend()

    ax2=axes.add_subplot(222)
    ax2.scatter(labels,std[0], label="pre")
    ax2.scatter(labels,std[1], label="post")
    ax2.set_title("Standard Deviation")
    ax2.legend()
    
    return mean, std, labels

#=============Calculate scores on pre-test===================
def Score_pre(data):
    pre_scores=data[data.columns[4:65]]
    final_score=pre_scores.sum(axis=1)
    
    return final_score

#=============Calculate scores on post-test===================

def Score_post(data):
    post_scores=data[data.columns[68:129]]
    final_score=post_scores.sum(axis=1)
    
    return final_score

#========splits the given data into subset of genders=========

def Gender_spliter(dataset):
    male_data = dataset[dataset["Gender"]=="M"]
    female_data = dataset[dataset["Gender"]=="F"]
    other_g = dataset[dataset["Gender"]=="Other"]
    
    Gen_data=[male_data, female_data, other_g]
    Gen_labels=["Male", "Female", "Other"]
    
    return Gen_data, Gen_labels

#==============extracts represented etnicit==================

def Ethnicity (data):
    
    Values=[data["AmerInd.AlaskaNat"].sum(), data["Asian"].sum(), data["Black"].sum(), data["Hispanic"].sum(),
            data["NatHaw.PacIsl"].sum(), data["White"].sum(),data["Other"].sum()]
    
    Ethnicity=["American_Indian_Or_Alaskan_Native", "Asian", "Black", "Hispanic", "Native_Hawaian_or_Pacific_Islander",
               "White", "Other"]
    
    return Values, Ethnicity
    
#-------------------------------------------------------

def Gain(pre,post):
    
    return post-pre

#=======Displays gender and ethnicity representations=======

def Demographic_plotter (data):
    race_data=Ethnicity(data)
    Gen_data, Gen_labels=Gender_spliter(data)
    
    Gen_values=[len(Gen_data[0]), len(Gen_data[1]), len(Gen_data[2])]
    
    axes=plt.figure(figsize=(15,8))
    ax1=axes.add_subplot(221)
    ax2=axes.add_subplot(222)
    ax1.pie(race_data[0],labels=race_data[1],radius=1.5, autopct='%0.2f%%', shadow=True, explode=[0,0,0,0,0.2,0.1,0])
    ax2.pie(Gen_values,labels=Gen_labels,radius=1.5, autopct='%0.2f%%', shadow=True, explode=[0,0.1,0])
    plt.tight_layout()
    plt.show()
    
#======Displays performance histograms given a test criteria=======

def Perfomance_plotter (data,t_value):
    Values, labels = Gender_spliter(data)
    if t_value == "Pre" :
        
        #Pre test
        axes=plt.figure(figsize=(15,8))
        ax1=axes.add_subplot(241)
        ax1.hist(Score_pre(Values[0]))
        ax1.set_title("Male")

        ax2=axes.add_subplot(242)
        ax2.hist(Score_pre(Values[1]), color='r')
        ax2.set_title("Female")

        ax3=axes.add_subplot(243)
        ax3.hist(Score_pre(Values[2]), color='g')
        ax3.set_title("Other")

        
    elif t_value == "Post" :
        #Post test
        axes=plt.figure(figsize=(15,8))
        ax1=axes.add_subplot(241)
        ax1.hist(Score_post(Values[0]))
        ax1.set_title("Male")

        ax2=axes.add_subplot(242)
        ax2.hist(Score_post(Values[1]), color='r')
        ax2.set_title("Female")

        ax3=axes.add_subplot(243)
        ax3.hist(Score_post(Values[2]), color='g')
        ax3.set_title("Other")
    else:
        print("invalid value")
        
    plt.tight_layout()
