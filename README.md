# conan-jerryscript

Conan package for [JerryScript](https://github.com/jerryscript-project/jerryscript)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/JerryScript%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/JerryScript%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-jerryscript.svg?branch=release%2F1.0-a0a6eaa)](https://travis-ci.org/AtaLuZiK/conan-jerryscript)|[![Build status](https://ci.appveyor.com/api/projects/status/ffdeij178r320pfa/branch/release/1.0-a0a6eaa?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-jerryscript/branch/release/1.0-a0a6eaa)|

## Reuse the packages

### Basic setup

```
conan install JerryScript/1.0-a0a6eaa@zimmerk/stable
```

### Project setup

```
[requires]
JerryScript/1.0-a0a6eaa@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
