"""Rebuild index.html from src/app.html by inlining PDF.js 3.11.174 and pdf-lib 1.17.1.

    npm pack pdfjs-dist@3.11.174 pdf-lib@1.17.1   # then extract both tarballs here
    python3 build.py
"""
r = lambda p: open(p, encoding='utf-8').read()
s = r('src/app.html')
s = s.replace('/*__PDFJS_WORKER__*/', r('pdfjs-dist-3.11.174/package/build/pdf.worker.min.js'), 1)
s = s.replace('<script>/*__PDFJS__*/</script>', '<script>' + r('pdfjs-dist-3.11.174/package/build/pdf.min.js') + '</script>', 1)
s = s.replace('<script>/*__PDFLIB__*/</script>', '<script>' + r('pdf-lib-1.17.1/package/dist/pdf-lib.min.js') + '</script>', 1)
open('index.html', 'w', encoding='utf-8').write(s)
