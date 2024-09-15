from src.clean_scrapping.shared import use_case as uc
from src.clean_scrapping.shared import response_object as res


class MatchListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_match = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_match)
