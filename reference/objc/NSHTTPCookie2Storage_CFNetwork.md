# `NSHTTPCookie2Storage`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSPersistentHTTPCookie2Storage" persistentStore;
@"NSMemoryHTTPCookie2Storage" memoryStore;
@"NSObject<OS_dispatch_queue>" _workQueue;
@? _defaultNotificationHandler;
```

## Class methods

```
+[NSHTTPCookie2Storage sharedNSHTTPCookie2Storage];
```

## Instance methods

```
-[NSHTTPCookie2Storage initWithPath:];
-[NSHTTPCookie2Storage init];
-[NSHTTPCookie2Storage identifyingData];
-[NSHTTPCookie2Storage deleteAllCookiesWithCompletionHandler:];
-[NSHTTPCookie2Storage deleteCookie:withCompletionHandler:];
-[NSHTTPCookie2Storage deleteCookiesWithFilter:completionHandler:];
-[NSHTTPCookie2Storage getAllCookiesWithCompletionHandler:];
-[NSHTTPCookie2Storage getCookiesWithFilter:completionHandler:];
-[NSHTTPCookie2Storage initInNSMemoryHTTPCookie2Storage];
-[NSHTTPCookie2Storage initWithIdentifyingData:];
-[NSHTTPCookie2Storage setCookie:withFilter:completionHandler:];
-[NSHTTPCookie2Storage setCookies:withFilter:completionHandler:];
```
