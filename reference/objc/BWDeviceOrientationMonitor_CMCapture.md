# `BWDeviceOrientationMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
i _orientationDispatchToken;
@"NSObject<OS_dispatch_queue>" _orientationNotificationDispatchQueue;
i _mostRecentPortraitLandscapeOrientation;
i _currentOrientation;
@"<BWDeviceOrientationMonitorPortraitLandscapeUpdateDelegate>" _portraitLandscapeUpdateDelegate;
^{OpaqueFigSimpleMutex=} _stateMutex;
```

## Properties

```
@property (Ti,R,N,V_mostRecentPortraitLandscapeOrientation) mostRecentPortraitLandscapeOrientation;
@property (Ti,R,N,V_currentOrientation) currentOrientation;
@property (T@"<BWDeviceOrientationMonitorPortraitLandscapeUpdateDelegate>",N,V_portraitLandscapeUpdateDelegate) portraitLandscapeUpdateDelegate;
```

## Class methods

```
+[BWDeviceOrientationMonitor initialize];
+[BWDeviceOrientationMonitor deviceOrientationAsString:];
```

## Instance methods

```
-[BWDeviceOrientationMonitor currentOrientation];
-[BWDeviceOrientationMonitor init];
-[BWDeviceOrientationMonitor stop];
-[BWDeviceOrientationMonitor dealloc];
-[BWDeviceOrientationMonitor start];
-[BWDeviceOrientationMonitor portraitLandscapeUpdateDelegate];
-[BWDeviceOrientationMonitor mostRecentPortraitLandscapeOrientation];
-[BWDeviceOrientationMonitor rotationDegreesFromOrientation:portType:isMirrored:clientExpectsCameraMountedInLandscapeOrientation:];
-[BWDeviceOrientationMonitor setPortraitLandscapeUpdateDelegate:];
```
