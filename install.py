import neko

if not neko.is_installed("regex"):
    print("Installing requirements for Prompt Formatter")
    neko.run_pip("install regex", "support for variable lookbehind")