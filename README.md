# galpy-repl
A Jupyterlite-based REPL for galpy

## General REPL live at **[www.galpy.org/repl/repl/?kernel=python](https://www.galpy.org/repl/repl/?kernel=python)** 

Immediate version available at [www.galpy.org.s3-website.us-east-2.amazonaws.com/repl/repl/?kernel=python](http://www.galpy.org.s3-website.us-east-2.amazonaws.com/repl/repl/?kernel=python). Uses [jobovy/jupyterlite:quiet-prerun](https://github.com/jobovy/jupyterlite/tree/quiet-prerun), a slightly modified version of [jupyterlite](https://github.com/jupyterlite/jupyterlite).

## REPL with `galpy` pre-installed available at **[www.galpy.org/repl](https://www.galpy.org/repl)**

Immediate version available at [www.galpy.org.s3-website.us-east-2.amazonaws.com/repl](http://www.galpy.org.s3-website.us-east-2.amazonaws.com/repl).

This REPL supports the usual URL parameters of the `jupyterlite` REPL, for example, `code` for code to pre-populate the REPL with.

## Using this repository as a way to set up your own REPL with code to pre-run (or not!)

If you'd like to build your own REPL and host it on a static website in an AWS S3 bucket, you could use this repository as a template (note: not a real GitHub template). The following should work.
1. Fork the repository
2. Set the secrets `AWS_S3_BUCKET` (the S3 bucket hosting your site), `AWS_ACCESS_KEY_ID`, and `AWS_SECRET_ACCESS_KEY` (the latter two API keys of an IAM user with write access to the bucket).
3. Put any code that you want to silently pre-run in the `prerun.py` file. These could be things like `import micropip` and `await micropip.install(...)` to install packages not included in `pyodide`, or any other Python code.

This will create a general `jupyterlite` REPL at `/repl/repl/index.html` and a redirect `/repl` that opens the REPL with the `prerun.py` code run. Both REPLs support the usual `juyterlite` URL parameters.

To host using another provider, you would need to change the parts of the deploy workflows that upload to AWS S3 to point to your other provider instead.

