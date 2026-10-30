# `NSHTTPCookie`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 1 instance variables, 15 properties, 50 instance methods, 8 class methods

## Instance variables

```
@"NSHTTPCookieInternal" _cookiePrivate;
```

## Properties

```
@property (T^{HTTPCookie=^^?},R,D) _inner;
@property (T@"NSDictionary",R,C) properties;
@property (TQ,R) version;
@property (T@"NSString",R,C) name;
@property (T@"NSString",R,C) value;
@property (T@"NSDate",R,C) expiresDate;
@property (TB,R,GisSessionOnly) sessionOnly;
@property (T@"NSString",R,C) domain;
@property (T@"NSString",R,C) path;
@property (TB,R,GisSecure) secure;
@property (TB,R,GisHTTPOnly) HTTPOnly;
@property (T@"NSString",R,C) comment;
@property (T@"NSURL",R,C) commentURL;
@property (T@"NSArray",R,C) portList;
@property (T@"NSString",R,C) sameSitePolicy;
```

## Class methods

```
+[NSHTTPCookie _cookieForSetCookieString:forURL:partition:];
+[NSHTTPCookie requestHeaderFieldsWithCookies:];
+[NSHTTPCookie cookieWithProperties:];
+[NSHTTPCookie cookiesWithResponseHeaderFields:forURL:];
+[NSHTTPCookie _cf2nsCookies:];
+[NSHTTPCookie _ns2cfCookies:];
+[NSHTTPCookie _parsedCookiesWithResponseHeaderFields:forURL:];
+[NSHTTPCookie cookieWithCFHTTPCookie:];
```

## Instance methods

```
-[NSHTTPCookie isSecure];
-[NSHTTPCookie properties];
-[NSHTTPCookie initWithProperties:];
-[NSHTTPCookie domain];
-[NSHTTPCookie init];
-[NSHTTPCookie _inner];
-[NSHTTPCookie dealloc];
-[NSHTTPCookie value];
-[NSHTTPCookie version];
-[NSHTTPCookie _initWithHeader:];
-[NSHTTPCookie comment];
-[NSHTTPCookie encodeWithCoder:];
-[NSHTTPCookie hash];
-[NSHTTPCookie description];
-[NSHTTPCookie initWithCoder:];
-[NSHTTPCookie _initWithCookie:partition:];
-[NSHTTPCookie _initWithReference:index:];
-[NSHTTPCookie isEqual:];
-[NSHTTPCookie name];
-[NSHTTPCookie _initWithProperties:fromString:];
-[NSHTTPCookie path];
-[NSHTTPCookie _key];
-[NSHTTPCookie isSessionOnly];
-[NSHTTPCookie commentURL];
-[NSHTTPCookie expiresDate];
-[NSHTTPCookie isHTTPOnly];
-[NSHTTPCookie portList];
-[NSHTTPCookie sameSitePolicy];
-[NSHTTPCookie Comment];
-[NSHTTPCookie Expires];
-[NSHTTPCookie Domain];
-[NSHTTPCookie MaxAge];
-[NSHTTPCookie OriginURL];
-[NSHTTPCookie Port];
-[NSHTTPCookie Secure];
-[NSHTTPCookie Discard];
-[NSHTTPCookie CommentURL];
-[NSHTTPCookie Name];
-[NSHTTPCookie Path];
-[NSHTTPCookie SameSitePolicy];
-[NSHTTPCookie Version];
-[NSHTTPCookie StoragePartition];
-[NSHTTPCookie Value];
-[NSHTTPCookie _CFHTTPCookie];
-[NSHTTPCookie _GetInternalCFHTTPCookie];
-[NSHTTPCookie _compareForHeaderOrder:];
-[NSHTTPCookie _initWithInternal:];
-[NSHTTPCookie _isExpired];
-[NSHTTPCookie _storagePartition];
-[NSHTTPCookie initWithCFHTTPCookie:];
```
