# `SBSystemNotesSwipeMetricSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
d _panDistanceBeforeScaling;
d _panInitialThumbnailScale;
d _panDistancePer1xScaling;
d _scaleThresholdBeforeFullSize;
d _flickVelocityThreshold;
d _cornerDistanceBeforeScalingForDismiss;
```

## Properties

```
@property (Td,N,V_panDistanceBeforeScaling) panDistanceBeforeScaling;
@property (Td,N,V_panInitialThumbnailScale) panInitialThumbnailScale;
@property (Td,N,V_panDistancePer1xScaling) panDistancePer1xScaling;
@property (Td,N,V_scaleThresholdBeforeFullSize) scaleThresholdBeforeFullSize;
@property (Td,N,V_flickVelocityThreshold) flickVelocityThreshold;
@property (Td,N,V_cornerDistanceBeforeScalingForDismiss) cornerDistanceBeforeScalingForDismiss;
```

## Class methods

```
+[SBSystemNotesSwipeMetricSettings ignoresKey:];
+[SBSystemNotesSwipeMetricSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemNotesSwipeMetricSettings setDefaultValues];
-[SBSystemNotesSwipeMetricSettings cornerDistanceBeforeScalingForDismiss];
-[SBSystemNotesSwipeMetricSettings flickVelocityThreshold];
-[SBSystemNotesSwipeMetricSettings panDistanceBeforeScaling];
-[SBSystemNotesSwipeMetricSettings panDistancePer1xScaling];
-[SBSystemNotesSwipeMetricSettings panInitialThumbnailScale];
-[SBSystemNotesSwipeMetricSettings scaleThresholdBeforeFullSize];
-[SBSystemNotesSwipeMetricSettings setCornerDistanceBeforeScalingForDismiss:];
-[SBSystemNotesSwipeMetricSettings setFlickVelocityThreshold:];
-[SBSystemNotesSwipeMetricSettings setPanDistanceBeforeScaling:];
-[SBSystemNotesSwipeMetricSettings setPanDistancePer1xScaling:];
-[SBSystemNotesSwipeMetricSettings setPanInitialThumbnailScale:];
-[SBSystemNotesSwipeMetricSettings setScaleThresholdBeforeFullSize:];
```
