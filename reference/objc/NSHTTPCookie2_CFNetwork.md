# `NSHTTPCookie2`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 17 instance variables, 13 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _value;
@"NSString" _domain;
@"NSString" _path;
@"NSString" _partition;
@"NSString" _etldPlusOne;
Q _sCreationDate;
Q _sExpirationDate;
Q _sLastAccessTime;
B _secure;
B _httpOnly;
B _hostOnly;
B _session;
q _sameSite;
q _source;
B _sesion;
@"NSDate" creationDate;
```

## Properties

```
@property (T@"NSString",R,V_name) name;
@property (T@"NSString",R,V_value) value;
@property (T@"NSString",R,V_domain) domain;
@property (T@"NSString",R,V_path) path;
@property (T@"NSDate",R,VcreationDate) creationDate;
@property (T@"NSDate",R) expirationDate;
@property (TB,R,V_sesion) sesion;
@property (TB,R,V_secure) secure;
@property (TB,R,V_httpOnly) httpOnly;
@property (TB,R,V_hostOnly) hostOnly;
@property (T@"NSString",R,V_partition) partition;
@property (Tq,R,V_source) source;
@property (Tq,R,V_sameSite) sameSite;
```

## Instance methods

```
-[NSHTTPCookie2 mutableCopyWithZone:];
-[NSHTTPCookie2 domain];
-[NSHTTPCookie2 expirationDate];
-[NSHTTPCookie2 value];
-[NSHTTPCookie2 partition];
-[NSHTTPCookie2 creationDate];
-[NSHTTPCookie2 description];
-[NSHTTPCookie2 copyWithZone:];
-[NSHTTPCookie2 name];
-[NSHTTPCookie2 source];
-[NSHTTPCookie2 path];
-[NSHTTPCookie2 secure];
-[NSHTTPCookie2 hostOnly];
-[NSHTTPCookie2 httpOnly];
-[NSHTTPCookie2 initWithName:value:domain:];
-[NSHTTPCookie2 sameSite];
-[NSHTTPCookie2 sesion];
```
