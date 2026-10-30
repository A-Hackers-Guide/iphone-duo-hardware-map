# `AVRouteDetector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"AVRouteDetectorInternal" _routeDetectorInternal;
```

## Properties

```
@property (TB,GisRouteDetectionEnabled) routeDetectionEnabled;
@property (TB,R) multipleRoutesDetected;
@property (TB,N) detectsCustomRoutes;
```

## Class methods

```
+[AVRouteDetector initialize];
```

## Instance methods

```
-[AVRouteDetector init];
-[AVRouteDetector dealloc];
-[AVRouteDetector _didEnterBackground];
-[AVRouteDetector _didEnterForeground];
-[AVRouteDetector _isAirPlayDevicePresenceDetected];
-[AVRouteDetector _isCustomRoutePresenceDetected];
-[AVRouteDetector _updateMultipleRoutesDetected];
-[AVRouteDetector _updateRouteDetectionEnabled];
-[AVRouteDetector detectsCustomRoutes];
-[AVRouteDetector isRouteDetectionEnabled];
-[AVRouteDetector multipleRoutesDetected];
-[AVRouteDetector setDetectsCustomRoutes:];
-[AVRouteDetector setRouteDetectionEnabled:];
```
