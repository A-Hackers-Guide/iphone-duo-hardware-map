# `NSCachedURLResponse`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSCachedURLResponseInternal" _internal;
```

## Properties

```
@property (T@"NSURLResponse",R,C) response;
@property (T@"NSData",R,C) data;
@property (T@"NSDictionary",R,C) userInfo;
@property (TQ,R) storagePolicy;
```

## Class methods

```
+[NSCachedURLResponse supportsSecureCoding];
```

## Instance methods

```
-[NSCachedURLResponse userInfo];
-[NSCachedURLResponse data];
-[NSCachedURLResponse dealloc];
-[NSCachedURLResponse encodeWithCoder:];
-[NSCachedURLResponse initWithCoder:];
-[NSCachedURLResponse copyWithZone:];
-[NSCachedURLResponse response];
-[NSCachedURLResponse _wrappedRequest];
-[NSCachedURLResponse initWithResponse:data:userInfo:storagePolicy:];
-[NSCachedURLResponse storagePolicy];
-[NSCachedURLResponse initWithResponse:data:];
-[NSCachedURLResponse dataArray];
-[NSCachedURLResponse _CFCachedURLResponse];
-[NSCachedURLResponse _deallocInternalCFCachedURLResponse];
-[NSCachedURLResponse _initWithCFCachedURLResponse:];
-[NSCachedURLResponse _reestablishInternalCFCachedURLResponse:];
-[NSCachedURLResponse initWithResponse:dataArray:userInfo:storagePolicy:];
```
