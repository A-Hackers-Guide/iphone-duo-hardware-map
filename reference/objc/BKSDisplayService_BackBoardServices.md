# `BKSDisplayService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _screenBlankLock;
@"BSServiceInitiatingConnection" _screenBlankLock_connection;
@"NSSet" _screenBlankLock_suppressedDisplayUUIDs;
```

## Class methods

```
+[BKSDisplayService sharedInstance];
```

## Instance methods

```
-[BKSDisplayService init];
-[BKSDisplayService _lock_connectIfNeeded];
-[BKSDisplayService _lock_server];
-[BKSDisplayService setScreenBlankNotificationSuppressedDisplayUUIDs:];
-[BKSDisplayService traitsForDisplayUUID:];
```
