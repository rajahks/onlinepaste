from django_cron import CronJobBase, Schedule
from clip.models import Clip
from datetime import datetime,timezone
from clip.models import testFun

import logging
logger = logging.getLogger(__name__)

class DelExpiredPosts(CronJobBase):
    RUN_EVERY_MINS = 1 # every 5 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'clip.del_expired_posts'    # a unique code
    # print("$$ class ran " )
    clipList = Clip.objects.all()
    # print("clipList: " + str(clipList))
    logger.info("DelExpiredPosts was triggered. count=%d"%(clipList.count(),))

    def do(self):
        # print("$$ job ran. Count:"  + str(self.clipList.count()) )
        # print("$$ job ran Entries:" +  str(self.clipList.all()) )
        # //testFun()
        logger.info("DelExpiredPosts do function was triggered. count=%d list: %s"%(self.clipList.count(),str(self.clipList.all()),))
        for clip in self.clipList.all():
            # print("$$ clip:" + str(clip))
            curTime = datetime.now(tz=timezone.utc)
            if curTime > clip.expiry_date:
                # print("Exipired clip: " + str(clip))
                clipName = str(clip)
                clip.delete()
                # print("\tDeleted clip:" + clipName)
                logger.info("Expired clip %s deleted"%(clipName,))
            else:
                # print("Clip: "+ str(clip) +" not yet expired")
                logger.info("Clip: "+ str(clip) +" not yet expired")
        return
