cls
echo "Julien is happy to great you in this friendly win-python installer"
SET WHEELS="G:\Public\JR\Py35\wheels-windows"
SET DEV_DRIVE=c:
SET DEV="c:\dev"
SET PY_ENV=p35


:: 0 - for a fresh build start with the following
conda update conda
:: deactivate
:: conda env remove -n %PY_ENV%

:: 1 - Clone Pybam repository in your c:\dev\ either from PyCharm or
:: git clone ssh://git.tobam.local:29418/research/PyBam.git
%DEV_DRIVE%
cd %DEV%\PyBam
:: we assume the clone is already OK
git pull 

:: 2 - Create a new python 3.5 environment (either in PyCharm) or
conda create -n %PY_ENV% python=3.5

:: 3 - Go to the py35 newly created environment and install the library from wheels:
activate %PY_ENV%

:: the following lines seem not to execute after the activate statement...
pip install --use-wheel --no-index --find-links=%WHEELS% ffn bt
pip install --use-wheel --no-index --find-links=%WHEELS% %DEV%\PyBam\shared_library\.

::4 - Check that unit-tests run correctly
cd %DEV%\PyBam\shared_library\
nosetests

coverage report