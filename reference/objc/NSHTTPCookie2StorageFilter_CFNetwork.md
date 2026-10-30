# `NSHTTPCookie2StorageFilter`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isTrusted;
B _isTrustedCached;
@"NSString" _urlScheme;
B _isTopLevelNavigation;
B _isSafe;
B _overwriteHTTPOnlyCookies;
@"NSURL" _url;
@"NSURL" _mainDocumentURL;
@"NSURL" _siteForCookies;
@"NSString" _partition;
Q _acceptPolicy;
```

## Properties

```
@property (T@"NSURL",&,N,V_url) url;
@property (T@"NSURL",&,N,V_mainDocumentURL) mainDocumentURL;
@property (T@"NSURL",&,N,V_siteForCookies) siteForCookies;
@property (T@"NSString",&,N,V_partition) partition;
@property (TB,V_isTopLevelNavigation) isTopLevelNavigation;
@property (TB,V_isSafe) isSafe;
@property (TB,V_overwriteHTTPOnlyCookies) overwriteHTTPOnlyCookies;
@property (TQ,V_acceptPolicy) acceptPolicy;
```

## Instance methods

```
-[NSHTTPCookie2StorageFilter init];
-[NSHTTPCookie2StorageFilter mainDocumentURL];
-[NSHTTPCookie2StorageFilter setMainDocumentURL:];
-[NSHTTPCookie2StorageFilter partition];
-[NSHTTPCookie2StorageFilter setUrl:];
-[NSHTTPCookie2StorageFilter setPartition:];
-[NSHTTPCookie2StorageFilter url];
-[NSHTTPCookie2StorageFilter isSafe];
-[NSHTTPCookie2StorageFilter acceptPolicy];
-[NSHTTPCookie2StorageFilter isTopLevelNavigation];
-[NSHTTPCookie2StorageFilter isTrusted];
-[NSHTTPCookie2StorageFilter overwriteHTTPOnlyCookies];
-[NSHTTPCookie2StorageFilter setAcceptPolicy:];
-[NSHTTPCookie2StorageFilter setIsSafe:];
-[NSHTTPCookie2StorageFilter setIsTopLevelNavigation:];
-[NSHTTPCookie2StorageFilter setOverwriteHTTPOnlyCookies:];
-[NSHTTPCookie2StorageFilter setSiteForCookies:];
-[NSHTTPCookie2StorageFilter siteForCookies];
```
