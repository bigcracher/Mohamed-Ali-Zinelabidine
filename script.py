import requests
with open(r"C:\Users\dalil\Downloads\wordpress_exploits.txt",'r') as wp_exploits:
    wexploits = wp_exploits.read().split('\n')
url =input("donner l'URL")
print('starting wordpress exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
#print(f"Status Code: {r.status_code}, Content: {r.json()}")#
with open(r"C:\Users\dalil\Downloads\drupal.txt",'r') as drupal:
    wexploits = drupal.read().split('\n')
url =input("donner l'URL")
print('starting drupal exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\sharepoint.txt",'r') as sharepoint_exploits:
    wexploits = sharepoint_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting sharepoint exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\ColdFusion.txt",'r') as ColdFusion_exploits:
    wexploits = ColdFusion_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting ColdFusion exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\Django.txt",'r') as Django_exploits:
    wexploits = Django_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting Django exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\joomla-plugins.txt",'r') as joomlaplugins_exploits:
    wexploits = joomlaplugins_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting joomla_plugins exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\joomla-themes.txt",'r') as joomlathemes_exploits:
    wexploits = joomlathemes_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting joomla_themes exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\php-nuke.txt",'r') as php_nuke_exploits:
    wexploits = php_nuke_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting php_nuke exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\SAP.txt",'r') as SAP_exploits:
    wexploits = SAP_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting SAP exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\SiteMinder.txt",'r') as SiteMinder_exploits:
    wexploits = SiteMinder_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting SiteMinder exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\Umbraco.txt",'r') as Umbraco_exploits:
    wexploits = Umbraco_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting Umbraco exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\Sitefinity.txt",'r') as Sitefinity_exploits:
    wexploits = Sitefinity_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting Sitefinity exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\dotnetnuke.txt",'r') as dotnetnuke_exploits:
    wexploits = dotnetnuke_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting dotnetnuke exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)   
with open(r"C:\Users\dalil\Downloads\wp-themes.txt",'r') as wp_themes_exploits:
    wexploits = wp_themes_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting wordpress themes exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)
with open(r"C:\Users\dalil\Downloads\wp-plugins.txt",'r') as wp_plugins_exploits:
    wexploits =  wp_plugins_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting wordpress plugins exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)     
with open(r"C:\Users\dalil\Downloads\sitecore.txt",'r') as sitecore_exploits:
    wexploits =  sitecore_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting sitecore exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)     
with open(r"C:\Users\dalil\Downloads\sitemap-magento.txt",'r') as sitemap_magento_exploits:
    wexploits =  sitemap_magento_exploits.read().split('\n')
url = url =input("donner l'URL")
print('starting sitemap-magento exploits:\n')
for i in (wexploits):
    r = requests.get(url+i, 
                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},
                 allow_redirects=False)
    if (r.status_code == 200):
        print(url+i)
    else:
        print(r.status_code)     