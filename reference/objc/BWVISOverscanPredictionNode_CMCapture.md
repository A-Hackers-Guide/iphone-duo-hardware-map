# `BWVISOverscanPredictionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 4 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"GVSOverscanPredictor" _visOverscanPredictor;
@"NSDictionary" _cameraInfoByPortType;
f _visInputAspectRatio;
@"<BWVISOverscanPredictionDelegate>" _delegate;
```

## Class methods

```
+[BWVISOverscanPredictionNode initialize];
```

## Instance methods

```
-[BWVISOverscanPredictionNode prepareForCurrentConfigurationToBecomeLive];
-[BWVISOverscanPredictionNode renderSampleBuffer:forInput:];
-[BWVISOverscanPredictionNode dealloc];
-[BWVISOverscanPredictionNode nodeSubType];
-[BWVISOverscanPredictionNode didSelectFormat:forInput:];
-[BWVISOverscanPredictionNode nodeType];
-[BWVISOverscanPredictionNode initWithCameraInfoByPortType:visInputAspectRatio:delegate:];
```
