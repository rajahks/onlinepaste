from django.shortcuts import render, HttpResponse, redirect, reverse
from clip.models import Clip
from clip.forms import ClipForm
from django.utils.text import slugify
import random, string
import datetime

import logging
#Get an instance of a logger
logger = logging.getLogger(__name__)
# logger = logging.getLogger('django')

# These are keyword which take us to views and so cannot be used while
# creating a clip.
blockedKeywords = [ 'admin', 'iskeywordused', 'faq' ]

# Create your views here.

def check_post(request,clipId):  #TODO: Rename to a more meaningfull name.
    """
    This function handles the GET and POST requests. It fetches the object
    and renders the response
    """

    # get the complete uri pertaining to this clip.
    # clipUri = request.build_absolute_uri(clipId)
    if request.is_secure():
        clipUri = 'https://' + request.get_host() + '/' + clipId
    else:
        clipUri = 'http://' + request.get_host() + '/' + clipId

    logger.debug("ClipUri=" + clipUri)

    if request.method != 'POST':
        try:
            clip = Clip.objects.get(clipId=clipId)
            # if clip didnt exist it would raise a ObjectDoesNotExist exception
            # else it means it exists, display it

            # object has been accessed. If Delete on access set. Remove it.
            if clip.link_duration == 0:
                Clip.objects.filter(clipId=clipId).delete()
                logger.debug("Deleted Clip %s"%(clipId,))

            return render(request,'clip/clip_detail.html',{ 'clipId':clipId,
                                                            'clip':clip }
                         )
        except Clip.DoesNotExist:
            # object DoesNotExist redirect to  a view which would allow the User
            # to create it
            clipForm = ClipForm()
            clipUri = request.build_absolute_uri()
            logger.info("User accessing Clip which Doesnot exist uri:%s. Redirecting to index view" % (clipUri,))
            # context = { 'clipId':clipId, 'uri':clipUri, 'form':clipForm }

            # return render(request,'clip/clip_create.html', context )
            context = {'form':clipForm ,'randClipId':clipId,}
            return render(request,'clip/index.html',context)
    else:
        # the clip was submitted.

        # double POST can cause multiple objects to be created.
        # check if the object exists before creating it.
        if Clip.objects.filter(clipId=clipId).count() !=0:
            logger.warning("Double post for clip:%s"%(clipId,))
            return redirect(reverse('index'))

        # extract the form and the model and save it.
        clipForm = ClipForm(request.POST)
        if clipForm.is_valid():
            # print("Form is valid")
            # from the form get the object
            clipObj = clipForm.save(commit=False)
            clipObj.clipId = clipId
            linkDuration = clipObj.link_duration
            logger.debug("Clip form is valid. clipId:%s linkDuration:%d"%(clipId,linkDuration))
            timeDelta = 0
            if clipObj.link_duration == 0:
                #delete on access link. But we allow saving maximum upto 30 days
                timeDelta = 720 # change the value corresponding to 30 days, 720 hrs
                # for testing had set this to 30 mins
            else:
                timeDelta = linkDuration

            clipObj.expiry_date = clipObj.create_date + datetime.timedelta(hours=timeDelta)
            # save the object to DB
            clipObj.save()
            context = { 'clipId':clipId, 'clipObj':clipObj , 'clipUri':clipUri }
            return render(request,"clip/success.html", context )
        else:
            logger.debug("Form for clip %s is invalid"%(clipId,)) #TODO: Log errors as well here
            context = {'form':clipForm ,'randClipId':clipId}
            return render(request,'clip/index.html',context)

def index(request):
    # Generate a random clip ID which is not in DB
    if request.method != 'POST':
        randClipId = getRandomClipId()
        clipForm = ClipForm()
        context = {'form':clipForm ,'randClipId':randClipId}
        return render(request,'clip/index.html',context)
    else:
        # submit was pressed.
        clipIdToUse = request.POST.get("clip-url")
        # clean it up using slugify
        sClipIdToUse = slugify(clipIdToUse)
        logger.debug("clipId: " + clipIdToUse + " sluggedId:" + sClipIdToUse )

        try:
            if len(sClipIdToUse) == 0:
                clipIdErr = "Enter a valid keyword! Consisting of letters, numbers, underscores or hyphens"
            elif sClipIdToUse.lower() in blockedKeywords:
                logger.debug("Clip id in blocked keywords:" + sClipIdToUse )
                clipIdErr = "Keyword already in use. Why don't you choose another one?"
            else:
                clip = Clip.objects.get(clipId=sClipIdToUse)
                # clip found so id already used.
                # A non used id will raise a DoesNotExist exception and
                # we will create a clip using the check_post api
                logger.debug("Clip id already used:" + sClipIdToUse )
                clipIdErr = "Keyword already in use. Why don't you choose another one?"

            clipForm = ClipForm(request.POST)
            context = {'form':clipForm ,'randClipId':sClipIdToUse, 'clipIdErr':clipIdErr}
            return render(request,'clip/index.html',context)

        except Clip.DoesNotExist:
            # unused clip id.
            return check_post(request,sClipIdToUse)

def isKeywordUsed(request):
    """
    Function used to determine if the keyword is already used.
    """

    used = True
    if request.method == 'GET':
        keyword = request.GET['keyword']

    if keyword.lower() in blockedKeywords:
        return HttpResponse(True)

    if keyword:
        count = Clip.objects.filter(clipId=keyword).count()
        if count == 0:
            used = False
        else:
            used = True

    #TODO: Log an error if keyword was null

    return HttpResponse(used)


def getRandomClipId():
    """
    Function to generate random clip id. 
    Returns the random id generated.
    """

    found = False
    size = 5
    # Number of iterations that were required to find an free keyword.
    # As long as this number is small we should be OK. However if we
    # this number is large then we need to refactor this code to have a
    # efficient method.
    loopCount = 1 
    
    while found==False:
        # IMP: removed upper case letters as slugify automatically converts
        # everything to lowercase. This decreases the probability of finding
        # a link by a little. Maybe optimize this later.
        letterSet = string.digits + string.ascii_lowercase
        genId = ''.join(random.choices(letterSet, k=size))

        if Clip.objects.filter(clipId=genId).count() == 0:
            # unused keyword found.
            logger.info("Loop count to find a free keyword:%d keyword:%s"%(loopCount,genId))
            return genId
        else:
            # continue until found. Possibilty of not finding is very low.
            loopCount += 1
            continue

def faqView(request):
    return render(request,"clip/faq.html")
