# `MobileGestaltHelperProxy`

- Image: [`/usr/lib/libMobileGestaltExtensions.dylib`](../userland/usr__lib__libMobileGestaltExtensions.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _error;
@"<MobileGestaltHelper>" _helper;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (Ti,V_error) error;
@property (T@"<MobileGestaltHelper>",R,V_helper) helper;
@property (T@"NSXPCConnection",R,V_connection) connection;
```

## Class methods

```
+[MobileGestaltHelperProxy proxy];
```

## Instance methods

```
-[MobileGestaltHelperProxy helper];
-[MobileGestaltHelperProxy setError:];
-[MobileGestaltHelperProxy proxyRebuildCache];
-[MobileGestaltHelperProxy init];
-[MobileGestaltHelperProxy dealloc];
-[MobileGestaltHelperProxy error];
-[MobileGestaltHelperProxy invalidate];
-[MobileGestaltHelperProxy connection];
-[MobileGestaltHelperProxy proxySetCacheSentinel];
```
