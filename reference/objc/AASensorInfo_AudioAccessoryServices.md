# `AASensorInfo`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _pid;
@"NSString" _btAddress;
@"NSString" _transport;
Q _usage;
Q _usagePage;
```

## Properties

```
@property (T@"NSString",R,C,N,V_transport) transport;
@property (TQ,R,N,V_usage) usage;
@property (TQ,R,N,V_usagePage) usagePage;
@property (Ti,N,V_pid) pid;
@property (T@"NSString",R,C,N,V_btAddress) btAddress;
```

## Class methods

```
+[AASensorInfo supportsSecureCoding];
```

## Instance methods

```
-[AASensorInfo usage];
-[AASensorInfo update:];
-[AASensorInfo setPid:];
-[AASensorInfo transport];
-[AASensorInfo pid];
-[AASensorInfo usagePage];
-[AASensorInfo encodeWithCoder:];
-[AASensorInfo initWithCoder:];
-[AASensorInfo clearData];
-[AASensorInfo copyWithZone:];
-[AASensorInfo btAddress];
-[AASensorInfo initWithBTAddress:];
```
