from dotenv import load_dotenv

load_dotenv()

from stalebot.gitlab import merge_requests
import pytest
import vcr
import re
import logging


def scrub_ids(request):
    p = re.compile(r"\d{5,10}")
    request.uri = p.sub("XXXXX", request.uri)
    return request


def scrub_link(response):
    logging.info(response["headers"]["Link"])
    del response["headers"]["Link"]
    return response


vcr = vcr.VCR(
    filter_headers=["PRIVATE-TOKEN"],
    before_record_request=scrub_ids,
    before_record_response=scrub_link,
)


@vcr.use_cassette()
def test_find_stale():
    stale_mrs = merge_requests.find_stale()

    assert len(stale_mrs) > 0
