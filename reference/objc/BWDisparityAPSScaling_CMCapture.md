# `BWDisparityAPSScaling`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
f _focusRegionDisparityPercentile;
f _focusRegionMinArea;
f _focusRegionMinApsDistanceMeters;
f _focusRegionMaxApsDistanceMeters;
f _focusRegionMinDisparityDistanceMeters;
f _focusRegionMaxDisparityDistanceMeters;
f _scaleRecoveryMinScalingFactor;
f _scaleRecoveryMaxScalingFactor;
i _focusRegionDisparitySamplingRate;
```

## Class methods

```
+[BWDisparityAPSScaling initialize];
```

## Instance methods

```
-[BWDisparityAPSScaling initWithDepthScalingTuningParameters:];
-[BWDisparityAPSScaling initWithPortType:sensorIDString:];
-[BWDisparityAPSScaling isAPSScalingNeededForSbuf:];
-[BWDisparityAPSScaling previewScalingFactorWithDisparityBuffer:sbuf:];
-[BWDisparityAPSScaling stillImageScalingFactorWithDisparityBuffer:sbuf:scaleFactorFromEFL:];
```
