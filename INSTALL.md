g# Installing using conan


If want llvm it must be under 17

Conan:

```
python -m venv ./.venv
source .venv/bin/activate
pip install conan
```
Prepare dependencies

```
cd bitwuzla
conan create . -pr <profile> --build=missing
```


```
conan install . -pr <profile> --build=missing
```

```
pip install .
```