# `NSHTTPCookieStorageToCookie2Storage`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSHTTPCookieStorage`
- 3 instance variables, 0 properties, 24 instance methods, 0 class methods

## Instance variables

```
Q _acceptPolicy;
B _behavesLikeNS;
@"NSHTTPCookie2Storage" _store;
```

## Instance methods

```
-[NSHTTPCookieStorageToCookie2Storage init];
-[NSHTTPCookieStorageToCookie2Storage dealloc];
-[NSHTTPCookieStorageToCookie2Storage _initWithIdentifier:private:];
-[NSHTTPCookieStorageToCookie2Storage cookies];
-[NSHTTPCookieStorageToCookie2Storage _cookieStorage];
-[NSHTTPCookieStorageToCookie2Storage _getCookiesForURL:mainDocumentURL:partition:policyProperties:completionHandler:];
-[NSHTTPCookieStorageToCookie2Storage _initWithCFHTTPCookieStorage:];
-[NSHTTPCookieStorageToCookie2Storage _setCookies:forURL:mainDocumentURL:policyProperties:];
-[NSHTTPCookieStorageToCookie2Storage _cookiesForURL:mainDocumentURL:];
-[NSHTTPCookieStorageToCookie2Storage _getCookiesForPartition:completionHandler:];
-[NSHTTPCookieStorageToCookie2Storage _getCookiesForURL:mainDocumentURL:partition:completionHandler:];
-[NSHTTPCookieStorageToCookie2Storage _saveCookies];
-[NSHTTPCookieStorageToCookie2Storage _saveCookies:];
-[NSHTTPCookieStorageToCookie2Storage _setPrivateBrowsingEnabled:];
-[NSHTTPCookieStorageToCookie2Storage _testingOfStoringOfCookie:];
-[NSHTTPCookieStorageToCookie2Storage cookieAcceptPolicy];
-[NSHTTPCookieStorageToCookie2Storage cookiesForURL:];
-[NSHTTPCookieStorageToCookie2Storage deleteCookie:];
-[NSHTTPCookieStorageToCookie2Storage getCookiesForTask:completionHandler:];
-[NSHTTPCookieStorageToCookie2Storage removeCookiesSinceDate:];
-[NSHTTPCookieStorageToCookie2Storage setCookie:];
-[NSHTTPCookieStorageToCookie2Storage setCookieAcceptPolicy:];
-[NSHTTPCookieStorageToCookie2Storage setCookies:forURL:mainDocumentURL:];
-[NSHTTPCookieStorageToCookie2Storage storeCookies:forTask:];
```
