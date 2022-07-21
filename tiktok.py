def tk(link):
	import requests
	import json
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url": link}

	headers = {
		"X-RapidAPI-Key": "91b6cdab00msh8889f7b6f903d49p16d229jsnaea11a8cc3e2",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	result = response.text
	rest = json.loads(result) 
	return {"video":rest['video'][0],"music":rest['music'][0]}

