"""Runs learner graph against fictional cases. Offline unless --live is explicitly supplied."""
import argparse, json, os
from pathlib import Path
from time import perf_counter

CASES=['refund','hours','unknown','weak','lookup:refund-red','lookup:missing',
       'lookup:broken','retriever-fails','model-fails refund','slow refund',
       'bad citation refund','injection']

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true', help='send fictional traces to your configured LangSmith project')
    parser.add_argument('--out', required=True, help='new JSONL path; refuses overwrite')
    args=parser.parse_args()
    if args.live:
        if not os.getenv('LANGSMITH_API_KEY') or not os.getenv('LANGSMITH_PROJECT'):
            parser.error('live mode requires LANGSMITH_API_KEY and LANGSMITH_PROJECT')
        os.environ['LANGSMITH_TRACING']='true'
    else:
        os.environ['LANGSMITH_TRACING']='false'
    from langsmith import Client, traceable
    from langchain_core.tracers.langchain import wait_for_all_tracers
    from bridge import FixtureRag
    from workflow import build_graph
    from langsmith.run_helpers import get_current_run_tree
    graph=build_graph(FixtureRag())
    client=Client() if args.live else None
    @traceable(name='week09_case', run_type='chain', client=client)
    def execute(question):
        result=graph.invoke({'question':question,'tenant':'red'},
                            {'recursion_limit':12,'metadata':{'prompt_version':'fixture-v1','model':'fixture'}})
        tree=get_current_run_tree()
        return result, str(tree.id) if tree else None
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as f:
        for question in CASES:
            start=perf_counter()
            result,run_id=execute(question)
            row={'case':question,'elapsed_ms':round((perf_counter()-start)*1000,2),
                 'status':result['status'],'reason':result['reason'],
                 'mode':'live' if args.live else 'offline','run_id':run_id}
            f.write(json.dumps(row)+'\n')
    if args.live:
        wait_for_all_tracers()
        client.flush(timeout=15)
    print(f'{len(CASES)} cases written to {out}; inspect actual live delivery separately.')

if __name__=='__main__': main()
