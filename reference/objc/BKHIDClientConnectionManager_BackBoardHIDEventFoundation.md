# `BKHIDClientConnectionManager`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDEventSystem=} _hidEventSystem;
@"BSMutableIntegerMap" _taskPortToClientConnectionMapping;
@"BSMutableIntegerMap" _pidToClientConnectionMapping;
@"NSMutableDictionary" _versionedPIDToClientConnectionMapping;
^{__CFDictionary=} _hidConnectionToBKConnection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[BKHIDClientConnectionManager dealloc];
-[BKHIDClientConnectionManager description];
-[BKHIDClientConnectionManager pidForBundleID:];
-[BKHIDClientConnectionManager bundleIDForPID:];
-[BKHIDClientConnectionManager clientForDestination:];
-[BKHIDClientConnectionManager clientForTaskPort:];
-[BKHIDClientConnectionManager copyClientForDestination:];
-[BKHIDClientConnectionManager copyClientForTaskPort:];
-[BKHIDClientConnectionManager initWithHIDEventSystem:];
-[BKHIDClientConnectionManager sendEvent:toClientTaskPort:];
-[BKHIDClientConnectionManager sendEvent:toDestination:];
-[BKHIDClientConnectionManager succinctDescriptionForPID:];
-[BKHIDClientConnectionManager versionedPIDForPID:];
```
