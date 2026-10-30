# `LACAuditToken`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSString" _signingID;
@"NSNumber" _belongsToPlatformBinary;
{?="val"[8I]} _rawValue;
```

## Properties

```
@property (T{?=[8I]},R,N,V_rawValue) rawValue;
@property (T@"NSData",R,N) data;
```

## Class methods

```
+[LACAuditToken currentProcess];
+[LACAuditToken nullInstance];
```

## Instance methods

```
-[LACAuditToken rawValue];
-[LACAuditToken data];
-[LACAuditToken hash];
-[LACAuditToken description];
-[LACAuditToken initWithRawValue:];
-[LACAuditToken initWithData:];
-[LACAuditToken isEqual:];
-[LACAuditToken belongsToPlatformBinary:];
-[LACAuditToken signingID:];
```
