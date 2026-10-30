# `CMFlickGestureManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 16 instance methods, 2 class methods

## Instance variables

```
@ _internal;
```

## Class methods

```
+[CMFlickGestureManager isAvailable];
+[CMFlickGestureManager sharedManager];
```

## Instance methods

```
-[CMFlickGestureManager connect];
-[CMFlickGestureManager init];
-[CMFlickGestureManager dealloc];
-[CMFlickGestureManager stopUpdates];
-[CMFlickGestureManager deallocPrivate];
-[CMFlickGestureManager onNotification:];
-[CMFlickGestureManager logClientEventWithType:payload:];
-[CMFlickGestureManager feedFlickGestureEvent:timestamp:];
-[CMFlickGestureManager onFlickGestureData:];
-[CMFlickGestureManager sendEventToClientPrivate];
-[CMFlickGestureManager sendServiceRequestPrivate];
-[CMFlickGestureManager startService];
-[CMFlickGestureManager startUpdatesPrivateToQueue:withHandler:];
-[CMFlickGestureManager startUpdatesToQueue:withHandler:];
-[CMFlickGestureManager stopService];
-[CMFlickGestureManager stopUpdatesPrivate];
```
