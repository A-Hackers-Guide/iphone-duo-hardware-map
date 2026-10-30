# `CEKLightingFrameCache`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSIndexSet" __availableAbsoluteAngles;
@"NSMutableDictionary" __foregroundFramesByAvailableAngle;
@"NSDictionary" __backgroundFrameMapsByLightingType;
```

## Properties

```
@property (T@"NSIndexSet",R,N,V__availableAbsoluteAngles) _availableAbsoluteAngles;
@property (T@"NSMutableDictionary",&,N,V__foregroundFramesByAvailableAngle) _foregroundFramesByAvailableAngle;
@property (T@"NSDictionary",&,N,V__backgroundFrameMapsByLightingType) _backgroundFrameMapsByLightingType;
@property (TQ,R,N) angleCount;
```

## Instance methods

```
-[CEKLightingFrameCache init];
-[CEKLightingFrameCache _appearanceForLightingType:];
-[CEKLightingFrameCache _availableAbsoluteAngles];
-[CEKLightingFrameCache _backgroundFrameMapsByLightingType];
-[CEKLightingFrameCache _foregroundFramesByAvailableAngle];
-[CEKLightingFrameCache _needsBackgroundFrame];
-[CEKLightingFrameCache _needsForegroundFrames];
-[CEKLightingFrameCache _renderBackgroundFramesForAbsoluteAngles:lightingType:scale:];
-[CEKLightingFrameCache _renderForegroundFramesForAbsoluteAngles:scale:];
-[CEKLightingFrameCache _renderFrameForAngle:scale:components:appearance:];
-[CEKLightingFrameCache angleCount];
-[CEKLightingFrameCache angleOfAvailableFrameForAngle:];
-[CEKLightingFrameCache backgroundFrameForAngle:lightingType:];
-[CEKLightingFrameCache foregroundFrameForAngle:];
-[CEKLightingFrameCache preloadBackgroundFrames];
-[CEKLightingFrameCache preloadForegroundFrames];
-[CEKLightingFrameCache set_backgroundFrameMapsByLightingType:];
-[CEKLightingFrameCache set_foregroundFramesByAvailableAngle:];
```
