# `BWPreviewGyroStabilizationPanningDetection`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
[10] _translationVector;
i _inputIndex;
i _ringCount;
f _panningSpeedThreshold;
B _isPanning;
```

## Properties

```
@property (TB,R,N,V_isPanning) isPanning;
```

## Instance methods

```
-[BWPreviewGyroStabilizationPanningDetection reset];
-[BWPreviewGyroStabilizationPanningDetection isPanning];
-[BWPreviewGyroStabilizationPanningDetection _computePanningStatistics];
-[BWPreviewGyroStabilizationPanningDetection _updateWithTranslation:];
-[BWPreviewGyroStabilizationPanningDetection detectPanningUsingTranslation:maxAvgTranslationOut:];
-[BWPreviewGyroStabilizationPanningDetection initWithPanningThreshold:];
```
