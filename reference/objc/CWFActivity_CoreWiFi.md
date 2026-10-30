# `CWFActivity`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 18 instance methods, 3 class methods

## Instance variables

```
i _processIdentifier;
@"NSUUID" _UUID;
@"NSString" _reason;
q _type;
Q _timeout;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (Ti,V_processIdentifier) processIdentifier;
@property (T@"NSString",C,N,V_reason) reason;
@property (Tq,N,V_type) type;
@property (TQ,N,V_timeout) timeout;
```

## Class methods

```
+[CWFActivity supportsSecureCoding];
+[CWFActivity activityWithType:reason:];
+[CWFActivity activityWithType:reason:UUID:];
```

## Instance methods

```
-[CWFActivity setProcessIdentifier:];
-[CWFActivity init];
-[CWFActivity setUUID:];
-[CWFActivity UUID];
-[CWFActivity setReason:];
-[CWFActivity timeout];
-[CWFActivity setType:];
-[CWFActivity setTimeout:];
-[CWFActivity type];
-[CWFActivity encodeWithCoder:];
-[CWFActivity hash];
-[CWFActivity description];
-[CWFActivity initWithCoder:];
-[CWFActivity processIdentifier];
-[CWFActivity reason];
-[CWFActivity copyWithZone:];
-[CWFActivity isEqual:];
-[CWFActivity isEqualToActivity:];
```
