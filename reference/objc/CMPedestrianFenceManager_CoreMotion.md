# `CMPedestrianFenceManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 11 instance methods, 2 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (T@"CMPedestrianFenceManagerInternal",R,N,V_internal) _internal;
```

## Class methods

```
+[CMPedestrianFenceManager isAvailable];
+[CMPedestrianFenceManager availableFenceTypes];
```

## Instance methods

```
-[CMPedestrianFenceManager _internal];
-[CMPedestrianFenceManager init];
-[CMPedestrianFenceManager dealloc];
-[CMPedestrianFenceManager endSession];
-[CMPedestrianFenceManager startSession];
-[CMPedestrianFenceManager clearFence:];
-[CMPedestrianFenceManager forceClearAllFences];
-[CMPedestrianFenceManager forceClearFence:];
-[CMPedestrianFenceManager setFence:withRadius:withCompletion:];
-[CMPedestrianFenceManager simulateFence:withExitAfterDelay:wake:withCompletion:];
-[CMPedestrianFenceManager startSessionWithStatusHandler:];
```
