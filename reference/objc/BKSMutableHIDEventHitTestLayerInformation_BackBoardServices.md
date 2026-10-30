# `BKSMutableHIDEventHitTestLayerInformation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventHitTestLayerInformation`
- 1 instance variables, 13 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _backgroundStatisticsValid;
```

## Properties

```
@property (TQ,D,N) validMask;
@property (T{CATransform3D=dddddddddddddddd},D,N) cumulativeLayerTransform;
@property (T{CATransform3D=dddddddddddddddd},D,N) cumulativeContentsTransform;
@property (Tf,D,N) cumulativeOpacity;
@property (TB,D,N) hasInsecureFilter;
@property (TB,D,N) detectedOcclusion;
@property (TB,N,V_backgroundStatisticsValid) backgroundStatisticsValid;
@property (Tf,D,N) backgroundAverage;
@property (Tf,D,N) backgroundStandardDeviation;
@property (Tf,D,N) backgroundAverageContrastThreshold;
@property (T@"NSArray",C,D,N) minimumBackgroundColor;
@property (T@"NSArray",C,D,N) maximumBackgroundColor;
@property (T{CATransform3D=dddddddddddddddd},D,N) cumulativeTransform;
```

## Instance methods

```
-[BKSMutableHIDEventHitTestLayerInformation setMaximumBackgroundColor:];
-[BKSMutableHIDEventHitTestLayerInformation setBackgroundAverage:];
-[BKSMutableHIDEventHitTestLayerInformation setCumulativeTransform:];
-[BKSMutableHIDEventHitTestLayerInformation setHasInsecureFilter:];
-[BKSMutableHIDEventHitTestLayerInformation backgroundStatisticsValid];
-[BKSMutableHIDEventHitTestLayerInformation setValidMask:];
-[BKSMutableHIDEventHitTestLayerInformation setCumulativeOpacity:];
-[BKSMutableHIDEventHitTestLayerInformation setMinimumBackgroundColor:];
-[BKSMutableHIDEventHitTestLayerInformation setBackgroundStatisticsValid:];
-[BKSMutableHIDEventHitTestLayerInformation setCumulativeContentsTransform:];
-[BKSMutableHIDEventHitTestLayerInformation setDetectedOcclusion:];
-[BKSMutableHIDEventHitTestLayerInformation setCumulativeLayerTransform:];
-[BKSMutableHIDEventHitTestLayerInformation setBackgroundAverageContrastThreshold:];
-[BKSMutableHIDEventHitTestLayerInformation setBackgroundStandardDeviation:];
```
