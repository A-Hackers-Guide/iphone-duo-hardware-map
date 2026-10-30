# `BKSHIDEventKeyCommandsRegistration`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 3 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"BKSHIDEventDeferringEnvironment" _environment;
@"BKSHIDEventDeferringToken" _token;
@"NSSet" _keyCommands;
```

## Properties

```
@property (T@"BKSHIDEventDeferringEnvironment",R,C,N,V_environment) deferringEnvironment;
@property (T@"BKSHIDEventDeferringToken",R,C,N,V_token) deferringToken;
@property (T@"NSSet",R,C,N,V_keyCommands) keyCommands;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventKeyCommandsRegistration supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventKeyCommandsRegistration deferringEnvironment];
-[BKSHIDEventKeyCommandsRegistration mutableCopyWithZone:];
-[BKSHIDEventKeyCommandsRegistration deferringToken];
-[BKSHIDEventKeyCommandsRegistration debugDescription];
-[BKSHIDEventKeyCommandsRegistration init];
-[BKSHIDEventKeyCommandsRegistration keyCommands];
-[BKSHIDEventKeyCommandsRegistration succinctDescription];
-[BKSHIDEventKeyCommandsRegistration encodeWithCoder:];
-[BKSHIDEventKeyCommandsRegistration hash];
-[BKSHIDEventKeyCommandsRegistration description];
-[BKSHIDEventKeyCommandsRegistration initWithCoder:];
-[BKSHIDEventKeyCommandsRegistration appendDescriptionToStream:];
-[BKSHIDEventKeyCommandsRegistration copyWithZone:];
-[BKSHIDEventKeyCommandsRegistration isEqual:];
-[BKSHIDEventKeyCommandsRegistration _initWithEnvironment:token:keyCommands:];
```
