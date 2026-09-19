"""Minimal fixture for unfinished Week 8. Exact keyword matches, no embeddings or LLM."""
import json
from pathlib import Path
from time import sleep
from langsmith import traceable

class FixtureRag:
    def __init__(self):
        self.rows = json.loads((Path(__file__).parent / 'data/documents.json').read_text())
        self.calls = []

    @traceable(run_type='retriever', name='fixture_search')
    def search(self, question, tenant):
        self.calls.append(('search', question, tenant))
        if question == 'retriever-fails':
            raise TimeoutError('synthetic retrieval timeout')
        if question == 'slow refund':
            sleep(0.05)
        return [dict(row) for row in self.rows
                if row['tenant'] == tenant and row['keyword'] in question.lower()]

    @traceable(run_type='chain', name='fixture_answer')
    def generate(self, question, hits):
        self.calls.append(('generate', question))
        if question == 'model-fails refund':
            raise TimeoutError('synthetic model timeout')
        if question == 'bad citation refund':
            return {'answer': 'Refund in 30 days.', 'citations': ['foreign']}
        return {'answer': hits[0]['text'], 'citations': [hits[0]['id']]}

    @traceable(run_type='tool', name='fixture_lookup')
    def lookup(self, doc_id, tenant):
        self.calls.append(('lookup', doc_id, tenant))
        if doc_id == 'broken':
            raise TimeoutError('synthetic tool timeout')
        return next((dict(row) for row in self.rows
                     if row['id'] == doc_id and row['tenant'] == tenant), None)
