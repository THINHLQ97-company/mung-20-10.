"""Đóng gói index.html (bản dùng cho Claude Artifact) thành trang web độc lập trong dist/ để deploy (Vibe Host, GitHub Pages...).
Chạy: python3 tools/build.py"""
import shutil, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
dist = root / 'dist'
shutil.rmtree(dist, ignore_errors=True); (dist / 'assets').mkdir(parents=True)
page = (root / 'index.html').read_text(encoding='utf-8')
head = ('<!doctype html>\n<html lang="vi">\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>\n')
(dist / 'index.html').write_text(head + page + '\n</html>\n', encoding='utf-8')
for f in (root / 'assets').iterdir():
    shutil.copy2(f, dist / 'assets' / f.name)
print('Đã tạo', dist)
