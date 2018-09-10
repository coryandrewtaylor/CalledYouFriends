set INPUT_DOC=README.md
set BUILD_DOC=README_build.md
set OUTPUT_DOC="..\doc\README.md"
set BIBLIOGRAPHY=literature.bib
REM set CSL=society-of-biblical-literature-fullnote-bibliography.csl

pandoc ^
    --smart ^
    --atx-headers ^
    --from markdown ^
    --to markdown_phpextra ^
    --wrap none ^
    --reference-location document ^
    --bibliography %BIBLIOGRAPHY% ^
    --output %BUILD_DOC% ^
    %INPUT_DOC%

REM --csl %CSL% 
REM --metadata link-citations

pipenv run custom-tags -i %BUILD_DOC% -o %OUTPUT_DOC%
del %BUILD_DOC%