# `CMDeviceOrientationManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 21 instance methods, 4 class methods

## Instance variables

```
@ _internal;
```

## Class methods

```
+[CMDeviceOrientationManager isAvailable];
+[CMDeviceOrientationManager initialize];
+[CMDeviceOrientationManager dummySelector:];
+[CMDeviceOrientationManager isAlwaysOn];
```

## Instance methods

```
-[CMDeviceOrientationManager stopDeviceOrientationUpdatesPrivate];
-[CMDeviceOrientationManager deviceOrientationBlocking];
-[CMDeviceOrientationManager startDeviceOrientationUpdatesToQueue:withHandler:];
-[CMDeviceOrientationManager onMotionPreferencesUpdated];
-[CMDeviceOrientationManager init];
-[CMDeviceOrientationManager stop];
-[CMDeviceOrientationManager orientationNotificationsDisabled];
-[CMDeviceOrientationManager initPrivate];
-[CMDeviceOrientationManager onDeviceOrientation:];
-[CMDeviceOrientationManager dealloc];
-[CMDeviceOrientationManager startDeviceOrientationUpdatesPrivateToQueue:withHandler:];
-[CMDeviceOrientationManager start];
-[CMDeviceOrientationManager updateAggregateDictionaryPrivate];
-[CMDeviceOrientationManager isDeviceOrientationActive];
-[CMDeviceOrientationManager stringForOrientation:];
-[CMDeviceOrientationManager stopDeviceOrientationUpdates];
-[CMDeviceOrientationManager setDeviceOrientationCallbackModePrivate:];
-[CMDeviceOrientationManager deallocPrivate];
-[CMDeviceOrientationManager isDeviceOrientationAvailable];
-[CMDeviceOrientationManager onNotification:];
-[CMDeviceOrientationManager signalAndReleaseSemaphoreIfNecessaryPrivate];
```
