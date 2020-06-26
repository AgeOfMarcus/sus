# SUS - Single Use Scripts

This is a repository for lazy scripts I write that have a single purpose. You're welcome to reuse whatever you can get. For every script there is a directory named whatever best suits the purpose of said script. In each directory there is a `script.json` file which contains data that should allow you to search through directories. 

# `script.json` example (see `example/script.json`)
```
{
    "name": "Script name",
    "desc": "This is a script that does x with y",
    "auto": false, // the script requires the user to do stuff
    "vars": {
        "name": "Name of z to search for",
    },
    "output": "var", // can be str, bool, list, json, or var (varied)
    "docs": true, // this means the script dir contains a README.md file
    "files": [
        "example.py",
        "data.db",
    ],
    "entry": "example.py", // the "main" file
}
```