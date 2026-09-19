"""Supplied real CPU inference probe. Run only after Lesson 10's download/hardware checks."""
import argparse, json, os, platform, resource, time
from pathlib import Path

MODEL='HuggingFaceTB/SmolLM2-135M-Instruct'
PROMPTS=[
 'Answer using only this fact: Refunds take 30 days. How long do refunds take?',
 'Return only JSON with one key days and the integer value 30.',
 'Context: Support opens at 09:00 UTC. What is the refund policy? If absent, say unknown.'
]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--revision',required=True,help='full model commit SHA from Hugging Face')
    parser.add_argument('--out',required=True,help='new JSON file; refuses overwrite')
    args=parser.parse_args()
    if len(args.revision)!=40 or any(c not in '0123456789abcdef' for c in args.revision):
        parser.error('revision must be a full lowercase 40-character commit SHA')
    out=Path(args.out)
    if out.exists(): parser.error('choose a fresh output filename')
    import torch, transformers
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    torch.set_num_threads(2)
    t=time.perf_counter()
    tokenizer=AutoTokenizer.from_pretrained(MODEL,revision=args.revision,trust_remote_code=False)
    model=AutoModelForCausalLM.from_pretrained(MODEL,revision=args.revision,
                                            trust_remote_code=False,use_safetensors=True).to('cpu')
    generator=pipeline('text-generation',model=model,tokenizer=tokenizer,device=-1)
    load_s=time.perf_counter()-t
    rows=[]
    for repeat in range(2):
        for prompt in PROMPTS:
            text=tokenizer.apply_chat_template([{'role':'user','content':prompt}],
                                              tokenize=False,add_generation_prompt=True)
            start=time.perf_counter(); cpu_start=time.process_time()
            result=generator(text,max_new_tokens=32,do_sample=False,return_full_text=False,
                             pad_token_id=tokenizer.eos_token_id)[0]['generated_text']
            rows.append({'repeat':repeat,'input_tokens':len(tokenizer.encode(text,add_special_tokens=False)),
                         'wall_s':time.perf_counter()-start,'process_cpu_s':time.process_time()-cpu_start,
                         'prompt':prompt,'output':result})
    report={'model':MODEL,'revision':args.revision,'python':platform.python_version(),
            'torch':torch.__version__,'transformers':transformers.__version__,
            'cpu':platform.processor(),'logical_cpus':os.cpu_count(),'threads':2,
            'load_s':load_s,'max_rss_kib_linux':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runs':rows}
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as f: json.dump(report,f,indent=2)
    print(out)

if __name__=='__main__': main()
