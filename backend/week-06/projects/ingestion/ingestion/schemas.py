"""Learner: Pydantic response models Accepted and JobView.
Accepted: job_id:str, state:Literal['pending'].
JobView: job_id, state (five-state Literal), attempts:int,
characters:int|None, words:int|None, error_code:str|None.
Never expose storage paths, original filename or credentials in responses.
"""
from pydantic import BaseModel
# TODO define both models; see project contract.
