# SeleniumEngine
An AutoPkg url provider that can crawl more complex websites than the built in command which relies on CURL.
&nbsp;
> **Caution**: Using the Selenium processor allows python script to execute locally on the system.  When using this processor, be sure you understand and have vetted each of the commands that will be run.

## History
AutoPkg's native URLDownloader processor relies on curl commands being able to simply read the source code for website called via HTTP GET request. Certain websites, however, will hide their download links/urls behind pop-up windows or other techniques. SeleniumEngine aims to allow for admins to intelligently anticipate many of those hurdles and retrieve download urls that would previously have been inaccessible via autopkg recipes. Take the below example.
&nbsp;

## Example Use Case
You browse to dictionary.com and due your normal browser settings, you see the page normally.

![normal-site](docs/images/site.png)

When your autopkg URLTextSearcher pulls the website, however, it hits a popup.
![site-with-popup-displayed-on-load](/docs/images/site-with-popup-on-entry.png)

You do some digging and find that you can just inject search term into the url, so you load that. However you occassionally, but only occassionally hit a second popup.
![site-with-popup](/docs/images/site-with-popup.png)

SeleniumEngine allows recipes to search a website's HTML to impersonate an active user session, by clicking through popups when displayed, or otherwise navigating a site where, for example, a search term needs to be entered, or a drop down menu needs to be used.
