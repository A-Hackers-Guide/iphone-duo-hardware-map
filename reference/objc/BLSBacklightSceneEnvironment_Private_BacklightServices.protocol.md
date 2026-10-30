# `BLSBacklightSceneEnvironment_Private` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSBacklightSceneEnvironment`
- 0 instance variables, 5 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSDate",R) presentationDate;
@property (TQ,R) lowPowerRenderingPresentationTime;
@property (T@"BLSAlwaysOnSession",&) alwaysOnSession;
@property (TB,GisAnimatingVisualState) animatingVisualState;
@property (T@"<BLSBacklightSceneEnvironmentUpdating>",&) updater;
```

## Instance methods

```
-[BLSBacklightSceneEnvironment_Private updater];
-[BLSBacklightSceneEnvironment_Private setUpdater:];
-[BLSBacklightSceneEnvironment_Private presentationDate];
-[BLSBacklightSceneEnvironment_Private lowPowerRenderingPresentationTime];
-[BLSBacklightSceneEnvironment_Private alwaysOnSession];
-[BLSBacklightSceneEnvironment_Private setAlwaysOnSession:];
-[BLSBacklightSceneEnvironment_Private isAnimatingVisualState];
-[BLSBacklightSceneEnvironment_Private setAnimatingVisualState:];
```
