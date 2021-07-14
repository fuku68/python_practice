import logging
import time 
from django.views.generic import View

logger = logging.getLogger(__name__)

class SampleView(View):
    def post(self, request, *args, **kwargs):
        start_time = time.time()
        logger.info("User({}) posted.".format(request.user.id))

        # ... （略）... 

        logger.debug("Finished in {:.2f} sec.".format(time.time() - start_time))

        # ...
