# PyCOM STUBS for for VSCode Intellisense Autocomplete

This is all based on the good work by @Josver's [MicroPython Stubber](https://github.com/Josverl/micropython-stubber)

> This assumes you're using [PyMakr Extentsion for VSCode](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr).

1. Save any data off your board. We're going to overwrite files.
2. If your board does not connect. Edit the address in your pymakr.conf to match the IP, COM, or Serial connection you normally use in development.
3. Upload this repo to your PyCom Board.
4. In the REPL `import createstubs`. This will generate the files needed into a '/stubs/BOARD_VERSION folder.
5. When this completed Download the files from your board back into your repo.

Your new STUBS will now be in the /stubs folder.

In each of your Project Workspaces where you're writing code for you Pycom boards, you need to create a .vscode/settings.json file which has _at least_ these settings.

```json
    {
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.autoComplete.extraPaths": [
        "./lib/",
        "/YOUR_PATH_TO_REPO_FILES/pycom_stubs/stubs/GPy_v1_11",
        "YOUR NEW STUBS GO HERE",
    ],
    "python.autoComplete.typeshedPaths": [
        "/YOUR_PATH_TO_REPO_FILES/pycom_stubs/stubs/GPy_v1_11",
        "YOUR NEW STUBS GO HERE",
    ],
    "python.analysis.typeshedPaths": [
        "/YOUR_PATH_TO_REPO_FILES/pycom_stubs/stubs/GPy_v1_11",
        "YOUR NEW STUBS GO HERE",
    ]
}
```

## Submitting New PyCom stubs
1. Generate your stubs and download them into your branch.
2. Update the README.MD so it includes your newly generated stubs in each section. Just like the GPy_v1_11 version.
3. Submit a PR! :-)

