# `CAHostingToken`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 2 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _xPort;
{?="sid"I"pid"i"cid"I"type"I} _data;
I _port;
```

## Properties

```
@property (TB,R,GisAuthoritative) authoritative;
@property (Ti,R) pid;
```

## Class methods

```
+[CAHostingToken supportsSecureCoding];
+[CAHostingToken tokenFromXPCRepresentation:error:];
+[CAHostingToken tokenWithPort:data:error:];
```

## Instance methods

```
-[CAHostingToken encodeWithBlock:];
-[CAHostingToken isAuthoritative];
-[CAHostingToken createXPCRepresentation];
-[CAHostingToken init];
-[CAHostingToken dealloc];
-[CAHostingToken pid];
-[CAHostingToken encodeWithCoder:];
-[CAHostingToken hash];
-[CAHostingToken description];
-[CAHostingToken initWithCoder:];
-[CAHostingToken isEqual:];
```
