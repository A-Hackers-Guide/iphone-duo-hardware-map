# `BKSHIDEventDeferringTarget`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSProtobufSerializable`, `BSDescriptionStreamable`, `NSCopying`, `NSMutableCopying`
- 2 instance variables, 6 properties, 15 instance methods, 3 class methods

## Instance variables

```
i _pid;
@"BKSHIDEventDeferringToken" _token;
```

## Properties

```
@property (Ti,R,N,V_pid) pid;
@property (T@"BKSHIDEventDeferringToken",R,C,N,V_token) token;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringTarget build:];
+[BKSHIDEventDeferringTarget supportsSecureCoding];
+[BKSHIDEventDeferringTarget protobufSchema];
```

## Instance methods

```
-[BKSHIDEventDeferringTarget initWithToken:];
-[BKSHIDEventDeferringTarget mutableCopyWithZone:];
-[BKSHIDEventDeferringTarget initForProtobufDecoding];
-[BKSHIDEventDeferringTarget init];
-[BKSHIDEventDeferringTarget initWithPID:token:];
-[BKSHIDEventDeferringTarget appendDescriptionToFormatter:];
-[BKSHIDEventDeferringTarget pid];
-[BKSHIDEventDeferringTarget encodeWithCoder:];
-[BKSHIDEventDeferringTarget hash];
-[BKSHIDEventDeferringTarget description];
-[BKSHIDEventDeferringTarget initWithCoder:];
-[BKSHIDEventDeferringTarget token];
-[BKSHIDEventDeferringTarget copyWithZone:];
-[BKSHIDEventDeferringTarget isEqual:];
-[BKSHIDEventDeferringTarget mutableCopy];
```
