# `BKDisplayOrientationController`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableDictionary" _orientationByDisplayUUID;
@"NSMutableArray" _observers;
```

## Class methods

```
+[BKDisplayOrientationController sharedInstance];
```

## Instance methods

```
-[BKDisplayOrientationController init];
-[BKDisplayOrientationController addObserver:];
-[BKDisplayOrientationController setInterfaceOrientation:forDisplayUUID:];
-[BKDisplayOrientationController _removeObserverEntry:];
-[BKDisplayOrientationController addObserver:priority:];
-[BKDisplayOrientationController interfaceOrientationForDisplayUUID:];
```
