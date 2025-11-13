thonimport requests

def follow_redirects(url):
    try:
        response = requests.get(url, allow_redirects=True)
        return {
            "originalUrl": url,
            "attemptedUrl": response.url,
            "loadedUrl": response.url,
            "loadedUrlNormalized": response.url.rstrip('/'),
            "isOk": response.status_code == 200,
            "statusCode": response.status_code,
            "statusText": response.reason,
            "errorMessage": "",
            "isFailed": False if response.status_code == 200 else True
        }
    except requests.exceptions.RequestException as e:
        return {
            "originalUrl": url,
            "attemptedUrl": url,
            "loadedUrl": "",
            "loadedUrlNormalized": "",
            "isOk": False,
            "statusCode": 0,
            "statusText": "Failed",
            "errorMessage": str(e),
            "isFailed": True
        }