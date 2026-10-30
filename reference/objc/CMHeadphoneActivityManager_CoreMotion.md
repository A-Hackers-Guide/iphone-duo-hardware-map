# `CMHeadphoneActivityManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"CMHeadphoneActivityManagerInternal" _internal;
```

## Properties

```
@property (TB,R,N,GisActivityAvailable) activityAvailable;
@property (TB,R,N,GisActivityActive) activityActive;
@property (TB,R,N,GisStatusAvailable) statusAvailable;
@property (TB,R,N,GisStatusActive) statusActive;
```

## Class methods

```
+[CMHeadphoneActivityManager authorizationStatus];
```

## Instance methods

```
-[CMHeadphoneActivityManager stopActivityUpdates];
-[CMHeadphoneActivityManager init];
-[CMHeadphoneActivityManager dealloc];
-[CMHeadphoneActivityManager startActivityUpdatesToQueue:withHandler:];
-[CMHeadphoneActivityManager isActivityAvailable];
-[CMHeadphoneActivityManager hasConnectionClients];
-[CMHeadphoneActivityManager isActivityActive];
-[CMHeadphoneActivityManager isStatusActive];
-[CMHeadphoneActivityManager isStatusAvailable];
-[CMHeadphoneActivityManager mslLoggingEnabled];
-[CMHeadphoneActivityManager notifyDeviceConnectedEventToClientPrivate];
-[CMHeadphoneActivityManager notifyDeviceDisconnectedEventToClientPrivate];
-[CMHeadphoneActivityManager onActivityPrivate:error:];
-[CMHeadphoneActivityManager onStatusEventPrivate:];
-[CMHeadphoneActivityManager pauseActivityStreamingPrivate];
-[CMHeadphoneActivityManager pauseStatusStreamingPrivate];
-[CMHeadphoneActivityManager resumeActivityStreamingPrivate];
-[CMHeadphoneActivityManager resumeStatusStreamingPrivate];
-[CMHeadphoneActivityManager startActivityUpdatesPrivateToQueue:withHandler:];
-[CMHeadphoneActivityManager startMslLoggingWithFilenamePrefix:filePath:];
-[CMHeadphoneActivityManager startStatusUpdatesPrivateToQueue:withHandler:];
-[CMHeadphoneActivityManager startStatusUpdatesToQueue:withHandler:];
-[CMHeadphoneActivityManager stopActivityUpdatesPrivate];
-[CMHeadphoneActivityManager stopMslLogging];
-[CMHeadphoneActivityManager stopStatusUpdates];
-[CMHeadphoneActivityManager stopStatusUpdatesPrivate];
```
