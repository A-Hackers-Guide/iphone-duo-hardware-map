# `BKSHIDEventDeferringPredicate`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSDescriptionStreamable`, `NSCopying`, `NSMutableCopying`
- 3 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"BKSHIDEventDeferringEnvironment" _environment;
@"BKSHIDEventDisplay" _display;
@"BKSHIDEventDeferringToken" _token;
```

## Properties

```
@property (T@"BKSHIDEventDeferringEnvironment",R,C,N,V_environment) environment;
@property (T@"BKSHIDEventDisplay",R,C,N,V_display) display;
@property (T@"BKSHIDEventDeferringToken",R,C,N,V_token) token;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringPredicate supportsSecureCoding];
```

## Instance methods

```
-[BKSHIDEventDeferringPredicate display];
-[BKSHIDEventDeferringPredicate mutableCopyWithZone:];
-[BKSHIDEventDeferringPredicate init];
-[BKSHIDEventDeferringPredicate _initWithEnvironment:display:token:];
-[BKSHIDEventDeferringPredicate appendDescriptionToFormatter:];
-[BKSHIDEventDeferringPredicate encodeWithCoder:];
-[BKSHIDEventDeferringPredicate hash];
-[BKSHIDEventDeferringPredicate description];
-[BKSHIDEventDeferringPredicate initWithCoder:];
-[BKSHIDEventDeferringPredicate token];
-[BKSHIDEventDeferringPredicate copyWithZone:];
-[BKSHIDEventDeferringPredicate isEqual:];
-[BKSHIDEventDeferringPredicate environment];
```
