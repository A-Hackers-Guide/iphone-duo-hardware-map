# `HIDBasicTimeSync`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `HIDTimeSync`
- 4 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _clockID;
@"TSClockManager" _tsMgr;
@"TSUserFilteredClock" _tsClock;
B _active;
```

## Instance methods

```
-[HIDBasicTimeSync init];
-[HIDBasicTimeSync handleCancel];
-[HIDBasicTimeSync dataFromSyncedTime:error:];
-[HIDBasicTimeSync handleActivate];
-[HIDBasicTimeSync handlePropertyUpdate:];
-[HIDBasicTimeSync syncedTimeFromData:error:];
```
