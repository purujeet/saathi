from django.shortcuts import render
from django.http import HttpResponse
from  .forms import SUBMIT
from .chatbot import bot_start

ls=[('','',''), ('','','') , ('','','') , ('','','')]
user_res0=''
bot_resp0=''
bot_resp_hi0=''


user_res1=''
bot_resp1=''
bot_resp_hi1=''


user_res2=''
bot_resp2=''
bot_resp_hi2=''


def index(request):
    form = SUBMIT()

    return render(request,"app1/index.html",{'form':form})

def submit(request):
    form = SUBMIT(request.POST)
    form1=SUBMIT()

    if form.is_valid():
        user_res= form.cleaned_data['user_resp']
        bot_resp, bot_resp_hi = bot_start(user_res)

        x=(user_res,bot_resp,bot_resp_hi)
        if len(ls) == 4:
            ls[0]=ls[1]
            ls[1]=ls[2]
            ls[2]=ls[3]
            ls[3]=x
            user_res0,bot_resp0,bot_resp_hi0=ls[0]
            user_res1,bot_resp1,bot_resp_hi1=ls[1]
            user_res2,bot_resp2,bot_resp_hi2=ls[2]
            user_res3,bot_resp3,bot_resp_hi3=ls[3]

        else:
            ls.append(x)
            user_res0,bot_resp0,bot_resp_hi0=ls[0]
            user_res1,bot_resp1,bot_resp_hi1=ls[1]
            user_res2,bot_resp2,bot_resp_hi2=ls[2]
            user_res3,bot_resp3,bot_resp_hi3=ls[3]


        print(ls)



        return render(request,"app1/index.html",{'form': form1 ,
                                                 'user_res0' : user_res0, 'bot_resp0': bot_resp0 , 'bot_resp_hi0' : bot_resp_hi0,
                                                 'user_res1' : user_res1, 'bot_resp1': bot_resp1 , 'bot_resp_hi1' : bot_resp_hi1,
                                                 'user_res2' : user_res2, 'bot_resp2': bot_resp2 , 'bot_resp_hi2' : bot_resp_hi2,
                                                 'user_res3' : user_res3, 'bot_resp3': bot_resp3 , 'bot_resp_hi3' : bot_resp_hi3,})
    else:
        return HttpResponse("Error: Form is not validated")


# Create your views here.
