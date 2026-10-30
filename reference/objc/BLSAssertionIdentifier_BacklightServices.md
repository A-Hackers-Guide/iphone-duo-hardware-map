# `BLSAssertionIdentifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCCoding`
- 3 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
i _hostPid;
i _clientPid;
Q _count;
```

## Properties

```
@property (Ti,R,N,V_hostPid) hostPid;
@property (Ti,R,N,V_clientPid) clientPid;
@property (TQ,R,N,V_count) count;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSAssertionIdentifier supportsSecureCoding];
+[BLSAssertionIdentifier nextCount];
```

## Instance methods

```
-[BLSAssertionIdentifier initWithXPCDictionary:];
-[BLSAssertionIdentifier count];
-[BLSAssertionIdentifier clientPid];
-[BLSAssertionIdentifier initWithClientPid:hostPid:count:];
-[BLSAssertionIdentifier encodeWithXPCDictionary:];
-[BLSAssertionIdentifier encodeWithCoder:];
-[BLSAssertionIdentifier hash];
-[BLSAssertionIdentifier description];
-[BLSAssertionIdentifier initWithCoder:];
-[BLSAssertionIdentifier hostPid];
-[BLSAssertionIdentifier copyWithZone:];
-[BLSAssertionIdentifier isEqual:];
```
