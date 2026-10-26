"""Read a locally supplied XLSX using only stdlib; never modifies the workbook."""
from pathlib import Path
import argparse,hashlib,json,re,unicodedata,zipfile
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def norm(s):
    s=unicodedata.normalize('NFKD',s).casefold().replace('&',' and ')
    return ' '.join(re.findall(r'\w+',s))
def lookup(query,path=None):
    if path is None:raise ValueError('Supply the official workbook path with --list; no workbook is bundled')
    path=Path(path)
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    matches=[];q=norm(query)
    if not q:raise ValueError('Nonempty journal query required')
    if q=='informs journal on computing':q='journal on computing'
    with zipfile.ZipFile(path) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            shared=[''.join(el.itertext()) for el in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',ns)]
        for sheet in sorted(n for n in z.namelist() if re.fullmatch(r'xl/worksheets/sheet\d+\.xml',n)):
            for row in ET.fromstring(z.read(sheet)).findall('.//s:sheetData/s:row',ns):
                cells={}
                for c in row.findall('s:c',ns):
                    v=c.find('s:v',ns);value=v.text if v is not None else ''
                    if c.get('t')=='s':value=shared[int(value)]
                    elif c.get('t')=='inlineStr':value=''.join(c.find('s:is',ns).itertext())
                    cells[re.sub(r'\d','',c.get('r'))]=value
                title=cells.get('B','');grade=cells.get('A','').strip()
                if grade in {'A*','A','M','B'} and q in norm(title):
                    matches.append(dict(journal=title.strip(),category=grade,points={'A*':200,'A':100,'M':100,'B':50}[grade],sheet_xml=sheet,row=int(row.get('r')),cells='A'+row.get('r')+':B'+row.get('r')))
    return dict(query=query,list_version='user-supplied; confirm from official source/version label',source=str(path),source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),matches=matches,status='listed_matches' if matches else 'no_match_points_not_established',qualification='Points for full-length research articles under supplied explanation; confirm title identity and applicable policy/version')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('query');parser.add_argument('--list',required=True,type=Path);args=parser.parse_args()
    print(json.dumps(lookup(args.query,args.list),indent=2,ensure_ascii=False))
