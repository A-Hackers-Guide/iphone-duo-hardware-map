# `BKSHIDEventDeferringResolution`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSMutableCopying`, `NSSecureCoding`, `BKSHIDEventBaseAttributeSubsetProviding`, `NSCopying`
- 8 instance variables, 12 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"BKSHIDEventDisplay" _display;
@"BKSHIDEventDeferringEnvironment" _environment;
q _versionedPID;
i _pid;
@"BKSHIDEventDeferringToken" _token;
@"NSString" _processDescription;
@"BKSHIDEventDispatchingTarget" _dispatchingTarget;
B _isBuffer;
```

## Properties

```
@property (T@"BKSHIDEventDisplay",R,C,N,V_display) display;
@property (Tq,R,N,V_versionedPID) versionedPID;
@property (TB,R,N,V_isBuffer) isBuffer;
@property (T@"BKSHIDEventDispatchingTarget",R,N,V_dispatchingTarget) dispatchingTarget;
@property (T@"NSString",R,C,N,V_processDescription) processDescription;
@property (T@"BKSHIDEventDeferringEnvironment",R,C,N,V_environment) environment;
@property (Ti,R,N,V_pid) pid;
@property (T@"BKSHIDEventDeferringToken",R,C,N,V_token) token;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringResolution build:];
+[BKSHIDEventDeferringResolution supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventDeferringResolution display];
-[BKSHIDEventDeferringResolution mutableCopyWithZone:];
-[BKSHIDEventDeferringResolution debugDescription];
-[BKSHIDEventDeferringResolution init];
-[BKSHIDEventDeferringResolution versionedPID];
-[BKSHIDEventDeferringResolution pid];
-[BKSHIDEventDeferringResolution encodeWithCoder:];
-[BKSHIDEventDeferringResolution hash];
-[BKSHIDEventDeferringResolution description];
-[BKSHIDEventDeferringResolution initWithCoder:];
-[BKSHIDEventDeferringResolution appendDescriptionToStream:];
-[BKSHIDEventDeferringResolution token];
-[BKSHIDEventDeferringResolution copyWithZone:];
-[BKSHIDEventDeferringResolution isEqual:];
-[BKSHIDEventDeferringResolution processDescription];
-[BKSHIDEventDeferringResolution environment];
-[BKSHIDEventDeferringResolution dispatchingTarget];
-[BKSHIDEventDeferringResolution isBuffer];
-[BKSHIDEventDeferringResolution modifiedResolution:];
```
