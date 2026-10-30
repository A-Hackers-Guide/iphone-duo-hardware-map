# `NSHTTPCookieStorage`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 33 instance methods, 4 class methods

## Instance variables

```
@"NSHTTPCookieStorageInternal" _internal;
B __overrideSessionCookieAcceptPolicy;
```

## Properties

```
@property (TB,N,V__overrideSessionCookieAcceptPolicy) _overrideSessionCookieAcceptPolicy;
@property (T@"NSArray",R,C) cookies;
@property (TQ) cookieAcceptPolicy;
```

## Class methods

```
+[NSHTTPCookieStorage _setSharedHTTPCookieStorage:];
+[NSHTTPCookieStorage sharedCookieStorageForGroupContainerIdentifier:];
+[NSHTTPCookieStorage _csff:];
+[NSHTTPCookieStorage sharedHTTPCookieStorage];
```

## Instance methods

```
-[NSHTTPCookieStorage init];
-[NSHTTPCookieStorage dealloc];
-[NSHTTPCookieStorage _initWithIdentifier:private:];
-[NSHTTPCookieStorage description];
-[NSHTTPCookieStorage cookies];
-[NSHTTPCookieStorage _cookieStorage];
-[NSHTTPCookieStorage _getCookiesForURL:mainDocumentURL:partition:policyProperties:completionHandler:];
-[NSHTTPCookieStorage _initWithCFHTTPCookieStorage:];
-[NSHTTPCookieStorage _setCookies:forURL:mainDocumentURL:policyProperties:];
-[NSHTTPCookieStorage _cookiesForURL:mainDocumentURL:];
-[NSHTTPCookieStorage _getCookieStoragePartitionsCompletionHandler:];
-[NSHTTPCookieStorage _getCookiesForDomain:];
-[NSHTTPCookieStorage _getCookiesForPartition:completionHandler:];
-[NSHTTPCookieStorage _getCookiesForURL:mainDocumentURL:partition:completionHandler:];
-[NSHTTPCookieStorage _overrideSessionCookieAcceptPolicy];
-[NSHTTPCookieStorage _saveCookies];
-[NSHTTPCookieStorage _saveCookies:];
-[NSHTTPCookieStorage _setCookiesChangedHandler:onQueue:];
-[NSHTTPCookieStorage _setCookiesRemovedHandler:onQueue:];
-[NSHTTPCookieStorage _setPrivateBrowsingEnabled:];
-[NSHTTPCookieStorage _setSubscribedDomainsForCookieChanges:];
-[NSHTTPCookieStorage _testingOfStoringOfCookie:];
-[NSHTTPCookieStorage cookieAcceptPolicy];
-[NSHTTPCookieStorage cookiesForURL:];
-[NSHTTPCookieStorage deleteCookie:];
-[NSHTTPCookieStorage getCookiesForTask:completionHandler:];
-[NSHTTPCookieStorage removeCookiesSinceDate:];
-[NSHTTPCookieStorage setCookie:];
-[NSHTTPCookieStorage setCookieAcceptPolicy:];
-[NSHTTPCookieStorage setCookies:forURL:mainDocumentURL:];
-[NSHTTPCookieStorage set_overrideSessionCookieAcceptPolicy:];
-[NSHTTPCookieStorage sortedCookiesUsingDescriptors:];
-[NSHTTPCookieStorage storeCookies:forTask:];
```
