import sys, json, os
try:
    data = json.load(sys.stdin)
    for poc in data.get('pocs', []):
        cve = poc.get('cve_id', '')
        if not cve: continue
        year = cve.split('-')[1]
        path = f'pocs/{year}/{cve}.json'
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump(poc, f, indent=2)
            print(f'NEW: {cve}')
except: pass
