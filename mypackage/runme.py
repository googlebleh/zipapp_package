def zipmain():
    global __package__
    if (__package__ is None) or (__package__ == ""):
        print("zipapp")

        print("run zipmain")
        __package__ = "mypackage.pyz"
        import runpy
        runpy.run_path("mypackage.pyz", run_name="__main__")
        # runpy.run_module("mypackage", run_name="__main__")
        print("end zipmain")

    else:
        print("not zipapp")
        print("F", repr(__file__))
        print("P", repr(__package__))
        print("N", repr(__name__))
        import sys
        print(sys.modules)
        from . import main
        main()
