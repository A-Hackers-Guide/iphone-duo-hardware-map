# `MSPKIStatusInfo`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _hasFailInfo;
q _status;
@"NSString" _statusString;
q _failInfo;
```

## Properties

```
@property (Tq,R,V_status) status;
@property (T@"NSString",R,V_statusString) statusString;
@property (Tq,R,V_failInfo) failInfo;
@property (TB,R,V_hasFailInfo) hasFailInfo;
```

## Class methods

```
+[MSPKIStatusInfo supportsSecureCoding];
```

## Instance methods

```
-[MSPKIStatusInfo statusString];
-[MSPKIStatusInfo status];
-[MSPKIStatusInfo encodeWithCoder:];
-[MSPKIStatusInfo hash];
-[MSPKIStatusInfo initWithCoder:];
-[MSPKIStatusInfo isEqual:];
-[MSPKIStatusInfo failInfo];
-[MSPKIStatusInfo hasFailInfo];
-[MSPKIStatusInfo initWithStatus:statusString:failInfo:hasFailInfo:];
```
