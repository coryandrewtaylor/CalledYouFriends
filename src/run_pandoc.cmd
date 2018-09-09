pandoc --smart --atx-headers --from markdown --to markdown_mmd --reference-location section --metadata bibliography=literature.bib -o README_build.md README.md
REM --metadata link-citations 

copy README_build.md ..\doc\README.md
del README_build.md