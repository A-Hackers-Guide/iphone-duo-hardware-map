# `CFXApplicationState`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _isRegisteredForEvents;
q _applicationState;
```

## Properties

```
@property (TB,N,V_isRegisteredForEvents) isRegisteredForEvents;
@property (Tq,N,V_applicationState) applicationState;
```

## Class methods

```
+[CFXApplicationState sharedInstance];
+[CFXApplicationState beginMonitoringApplicationState];
```

## Instance methods

```
-[CFXApplicationState applicationWillResignActive:];
-[CFXApplicationState applicationDidEnterBackground:];
-[CFXApplicationState applicationDidBecomeActive:];
-[CFXApplicationState applicationState];
-[CFXApplicationState init];
-[CFXApplicationState dealloc];
-[CFXApplicationState setApplicationState:];
-[CFXApplicationState registerForEvents];
-[CFXApplicationState unregisterForEvents];
-[CFXApplicationState isRegisteredForEvents];
-[CFXApplicationState setIsRegisteredForEvents:];
```
