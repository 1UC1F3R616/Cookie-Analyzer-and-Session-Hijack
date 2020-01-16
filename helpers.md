## Instructions to run

* directions to install
```bash
pip install CookieAnalysis==0.1.1
```

* directions to execute

```bash
python3 env/lib/python3.7/site-packages/CookieAnalysis/analysis.py browser

python3 env/lib/python3.7/site-packages/CookieAnalysis/analysis.py web https://github.com

python3 env/lib/python3.7/site-packages/CookieAnalysis/analysis.py search
```

* Make sure you are executing file from right path, creation of environment is preferable
* *browser* will genrate your browser analysis report in your current directory
*  *web* will give live cookies from any web, it needs to be upgraded with *requests* modeule to allow passing of user login parameters. Usage is *web websitename*
*   *search* is to find analysis for a particular website if it exsists. It gives console output.
