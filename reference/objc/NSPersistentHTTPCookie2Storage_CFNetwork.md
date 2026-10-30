# `NSPersistentHTTPCookie2Storage`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSInternalHTTPCookie2Storage`
- 6 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
^{sqlite3=} persistentDb;
^{sqlite3_stmt=} insertCookiesStmt;
^{sqlite3_stmt=} selectDomainCookiesStmt;
^{sqlite3_stmt=} selectAllCookiesStmt;
^{sqlite3_stmt=} deleteCookiesStmt;
@"NSURL" _path;
```

## Properties

```
@property (T@"NSURL",&,V_path) path;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NSPersistentHTTPCookie2Storage beginTransaction];
-[NSPersistentHTTPCookie2Storage initWithPath:];
-[NSPersistentHTTPCookie2Storage init];
-[NSPersistentHTTPCookie2Storage setCookies:];
-[NSPersistentHTTPCookie2Storage setPath:];
-[NSPersistentHTTPCookie2Storage path];
-[NSPersistentHTTPCookie2Storage commitTransaction];
-[NSPersistentHTTPCookie2Storage deleteAllCookies];
-[NSPersistentHTTPCookie2Storage deleteCookie:];
-[NSPersistentHTTPCookie2Storage deleteCookies:];
-[NSPersistentHTTPCookie2Storage deleteCookiesWithFilter:];
-[NSPersistentHTTPCookie2Storage getAllCookies];
-[NSPersistentHTTPCookie2Storage getCookiesWithFilter:];
-[NSPersistentHTTPCookie2Storage setCookie:];
```
