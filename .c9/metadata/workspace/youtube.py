{"filter":false,"title":"youtube.py","tooltip":"/youtube.py","undoManager":{"mark":0,"position":0,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":55,"column":18},"action":"insert","lines":["#","# Includes","#","from urllib.request import urlopen","import re","","#","# Exceptions","#","class YoutubeException(Exception): pass","","#","# Regex","#","def tag_regex_construct(tag): ","\treturn re.compile(r\"<%s ?[^>]*>(.*?)</%s>\" %(tag, tag), re.IGNORECASE | re.DOTALL )","","title_re = tag_regex_construct(\"title\")","desc_re  = tag_regex_construct(\"content\")","auth_re  = tag_regex_construct(\"name\")","","#","# Video class","#","class Video: ","\tdef __init__(self, vid, update = True): ","\t\tself.vid = vid ","\t\tif(update): self.update() ","\t","\tdef update(self):","\t\tresp = urlopen(self.get_api_link()) ","\t\tif(resp):","\t\t\tdata = resp.read().decode() ","\t\t\tself.title = title_re.search(data).group(1)","\t\t\ttry:","\t\t\t\tself.desc = desc_re.search(data).group(1)","\t\t\texcept:","\t\t\t\tself.desc = \"No description avaiable.\"","\t\t\tself.auth = auth_re.search(data).group(1) ","\t\telse:","\t\t\traise YoutubeException(\"video id seems invalid\")","","\tdef get_api_link(self): ","\t\treturn \"http://gdata.youtube.com/feeds/api/videos/%s\" %(self.vid)","\t\t","\tdef get_id(self): ","\t\treturn self.vid ","\t\t","\tdef get_title(self): ","\t\treturn self.title ","","\tdef get_desc(self): ","\t\treturn self.desc","","\tdef get_auth(self): ","\t\treturn self.auth"]}]}]]},"ace":{"folds":[],"scrolltop":60,"scrollleft":0,"selection":{"start":{"row":24,"column":13},"end":{"row":24,"column":13},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1420742208072,"hash":"29a8ce7d891cf0572d574870b929256898738f01"}