# `BKHIDEventDeliveryClient`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 9 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
B _terminating;
i _pid;
@"NSString" _processDescription;
@"NSArray" _deliveryRoots;
@"NSArray" _keyCommandDeliveryRoots;
@"NSArray" _deferringRules;
@"NSSet" _keyCommandsRegistrations;
@"NSSet" _observerResolutions;
@"BSContinuousMachTimer" _bufferTimer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDEventDeliveryClient invalidate];
```
