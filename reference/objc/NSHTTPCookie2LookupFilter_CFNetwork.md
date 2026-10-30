# `NSHTTPCookie2LookupFilter`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 23 properties, 49 instance methods, 0 class methods

## Instance variables

```
B _secure;
B _httpOnly;
B _ignoreHostOnlyFlag;
B _ignoreHTTPOnlyCookie;
B _ignoreSecureFlag;
B _isTopLevelNavigation;
B _isSafe;
@"NSString" _name;
@"NSString" _value;
@"NSString" _domain;
@"NSString" _path;
@"NSString" _partition;
q _sameSite;
@"NSDate" _newerThanCreationDate;
@"NSDate" _newerThanExpirationDate;
@"NSDate" _newerThanLastAccess;
@"NSDate" _olderThanCreationDate;
@"NSDate" _olderThanExpirationDate;
@"NSDate" _olderThanLastAccess;
@"NSURL" _inURL;
@"NSURL" _mainDocumentURL;
@"NSURL" _siteForCookies;
Q _acceptPolicy;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_value) value;
@property (T@"NSString",C,N,V_domain) domain;
@property (T@"NSString",C,N,V_path) path;
@property (T@"NSString",C,N,V_partition) partition;
@property (Tq,V_sameSite) sameSite;
@property (T@"NSDate",C,N,V_newerThanCreationDate) newerThanCreationDate;
@property (T@"NSDate",C,N,V_newerThanExpirationDate) newerThanExpirationDate;
@property (T@"NSDate",C,N,V_newerThanLastAccess) newerThanLastAccess;
@property (T@"NSDate",C,N,V_olderThanCreationDate) olderThanCreationDate;
@property (T@"NSDate",C,N,V_olderThanExpirationDate) olderThanExpirationDate;
@property (T@"NSDate",C,N,V_olderThanLastAccess) olderThanLastAccess;
@property (TB,V_secure) secure;
@property (TB,V_httpOnly) httpOnly;
@property (TB,V_ignoreHostOnlyFlag) ignoreHostOnlyFlag;
@property (TB,V_ignoreHTTPOnlyCookie) ignoreHTTPOnlyCookie;
@property (TB,V_ignoreSecureFlag) ignoreSecureFlag;
@property (T@"NSURL",C,N,V_inURL) inURL;
@property (T@"NSURL",C,N,V_mainDocumentURL) mainDocumentURL;
@property (T@"NSURL",C,N,V_siteForCookies) siteForCookies;
@property (TB,V_isTopLevelNavigation) isTopLevelNavigation;
@property (TB,V_isSafe) isSafe;
@property (TQ,V_acceptPolicy) acceptPolicy;
```

## Instance methods

```
-[NSHTTPCookie2LookupFilter setDomain:];
-[NSHTTPCookie2LookupFilter setSecure:];
-[NSHTTPCookie2LookupFilter domain];
-[NSHTTPCookie2LookupFilter mainDocumentURL];
-[NSHTTPCookie2LookupFilter setMainDocumentURL:];
-[NSHTTPCookie2LookupFilter value];
-[NSHTTPCookie2LookupFilter partition];
-[NSHTTPCookie2LookupFilter setValue:];
-[NSHTTPCookie2LookupFilter setName:];
-[NSHTTPCookie2LookupFilter setPath:];
-[NSHTTPCookie2LookupFilter setPartition:];
-[NSHTTPCookie2LookupFilter name];
-[NSHTTPCookie2LookupFilter _flags];
-[NSHTTPCookie2LookupFilter isSafe];
-[NSHTTPCookie2LookupFilter path];
-[NSHTTPCookie2LookupFilter secure];
-[NSHTTPCookie2LookupFilter initWithCookie:];
-[NSHTTPCookie2LookupFilter acceptPolicy];
-[NSHTTPCookie2LookupFilter httpOnly];
-[NSHTTPCookie2LookupFilter ignoreHTTPOnlyCookie];
-[NSHTTPCookie2LookupFilter ignoreHostOnlyFlag];
-[NSHTTPCookie2LookupFilter ignoreSecureFlag];
-[NSHTTPCookie2LookupFilter inURL];
-[NSHTTPCookie2LookupFilter isTopLevelNavigation];
-[NSHTTPCookie2LookupFilter matchCookie:];
-[NSHTTPCookie2LookupFilter newerThanCreationDate];
-[NSHTTPCookie2LookupFilter newerThanExpirationDate];
-[NSHTTPCookie2LookupFilter newerThanLastAccess];
-[NSHTTPCookie2LookupFilter olderThanCreationDate];
-[NSHTTPCookie2LookupFilter olderThanExpirationDate];
-[NSHTTPCookie2LookupFilter olderThanLastAccess];
-[NSHTTPCookie2LookupFilter sameSite];
-[NSHTTPCookie2LookupFilter setAcceptPolicy:];
-[NSHTTPCookie2LookupFilter setHttpOnly:];
-[NSHTTPCookie2LookupFilter setIgnoreHTTPOnlyCookie:];
-[NSHTTPCookie2LookupFilter setIgnoreHostOnlyFlag:];
-[NSHTTPCookie2LookupFilter setIgnoreSecureFlag:];
-[NSHTTPCookie2LookupFilter setInURL:];
-[NSHTTPCookie2LookupFilter setIsSafe:];
-[NSHTTPCookie2LookupFilter setIsTopLevelNavigation:];
-[NSHTTPCookie2LookupFilter setNewerThanCreationDate:];
-[NSHTTPCookie2LookupFilter setNewerThanExpirationDate:];
-[NSHTTPCookie2LookupFilter setNewerThanLastAccess:];
-[NSHTTPCookie2LookupFilter setOlderThanCreationDate:];
-[NSHTTPCookie2LookupFilter setOlderThanExpirationDate:];
-[NSHTTPCookie2LookupFilter setOlderThanLastAccess:];
-[NSHTTPCookie2LookupFilter setSameSite:];
-[NSHTTPCookie2LookupFilter setSiteForCookies:];
-[NSHTTPCookie2LookupFilter siteForCookies];
```
