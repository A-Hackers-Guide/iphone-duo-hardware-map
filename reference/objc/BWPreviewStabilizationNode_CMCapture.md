# `BWPreviewStabilizationNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 28 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"BWPreviewGyroStabilization" _previewStabilization;
@"NSDictionary" _staticParametersByPortType;
B _updateFinalCropRectWithStabilizationShift;
B _stabilizeFallbackCamera;
B _enableStabilizationTransitionRamps;
B _rampOffStabilizationForGraphStop;
@"BWRamp" _stabilizationTransitionRamp;
@"BWRamp" _stabilizationCameraFallbackRamp;
B _stabilizationCameraFallbackRampEnabled;
i _stabilizationEnterRampFrameCount;
i _stabilizationExitRampFrameCount;
i _stabilizationCameraFallbackRampFrameCount;
i _stabilizationGraphStopRampOffFrameCount;
i _lastRecommendedMasterSelectionReason;
@"NSString" _lastRecommendedMasterPortType;
@"NSString" _lastPortType;
B _lastStabilizingEnabled;
{CGPoint="x"d"y"d} _lastTranslationBeforeStatusChange;
f _lastQuadraAdjustedBaseZoomFactorBeforeStatusChange;
f _lastQuadraAdjustedBaseZoomFactor;
B _lastUseISPFrameCorrectionShift;
{CGPoint="x"d"y"d} _appliedTranslation;
{CGPoint="x"d"y"d} _lastTranslationBeforeCameraFallbackRampStart;
B _isStillImagePreview;
f _minimumSupportedUIZoomFactor;
f _photoModeFullStrengthUIZoomFactor;
B _enablePreviewStabilizationOISRecenteringCompensation;
@"<BWPreviewStabilizationNodeDelegate>" _delegate;
```

## Properties

```
@property (TB,N,V_rampOffStabilizationForGraphStop) rampOffStabilizationForGraphStop;
@property (T@"<BWPreviewStabilizationNodeDelegate>",N,V_delegate) delegate;
```

## Class methods

```
+[BWPreviewStabilizationNode initialize];
```

## Instance methods

```
-[BWPreviewStabilizationNode renderSampleBuffer:forInput:];
-[BWPreviewStabilizationNode dealloc];
-[BWPreviewStabilizationNode setDelegate:];
-[BWPreviewStabilizationNode delegate];
-[BWPreviewStabilizationNode nodeSubType];
-[BWPreviewStabilizationNode didSelectFormat:forInput:];
-[BWPreviewStabilizationNode nodeType];
-[BWPreviewStabilizationNode initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:minimumSupportedUIZoomFactor:oisRecenteringCompensationEnabled:];
-[BWPreviewStabilizationNode rampOffStabilizationForGraphStop];
-[BWPreviewStabilizationNode setRampOffStabilizationForGraphStop:];
```
