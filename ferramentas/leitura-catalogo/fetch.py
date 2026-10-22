import csv,subprocess,os,re,time,hashlib,sys
rows=list(csv.DictReader(open(sys.argv[1]),delimiter='\t'))
urls=sorted({r['url'] for r in rows if r['url']})
for u in urls:
    fn='html/'+hashlib.md5(u.encode()).hexdigest()+'.html'
    if os.path.exists(fn): continue
    r=subprocess.run(['curl','-sSL','--max-time','40','-o',fn,'-w','%{http_code} %{url_effective}',u],capture_output=True,text=True)
    open('html/index.tsv','a').write(f"{u}\t{r.stdout}\t{fn}\n")
    time.sleep(0.5)
print(len(urls))
