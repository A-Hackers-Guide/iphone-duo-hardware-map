# `BWInferenceVideoFormatRequirements`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWVideoFormatRequirements`
- 9 instance variables, 9 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _deviceOriented;
B _landscapeOriented;
B _applyHorizontalFlip;
q _videoContentMode;
B _includesInvalidContent;
@"<BWInferenceCropDescriptor>" _cropDescriptor;
@? _histogramRequest;
i _rotationDegrees;
i _singleStepRotationDegrees;
```

## Properties

```
@property (Ti,N) singleStepRotationDegrees;
@property (TB,N,V_deviceOriented) deviceOriented;
@property (TB,N,V_applyHorizontalFlip) applyHorizontalFlip;
@property (TB,N,V_landscapeOriented) landscapeOriented;
@property (Ti,N,V_rotationDegrees) rotationDegrees;
@property (Tq,N,V_videoContentMode) videoContentMode;
@property (TB,N,V_includesInvalidContent) includesInvalidContent;
@property (T@"<BWInferenceCropDescriptor>",&,N,V_cropDescriptor) cropDescriptor;
@property (T@?,C,N,V_histogramRequest) histogramRequest;
```

## Class methods

```
+[BWInferenceVideoFormatRequirements defaultEspressoFormatRequirementsWithWidth:height:];
```

## Instance methods

```
-[BWInferenceVideoFormatRequirements landscapeOriented];
-[BWInferenceVideoFormatRequirements histogramRequest];
-[BWInferenceVideoFormatRequirements includesInvalidContent];
-[BWInferenceVideoFormatRequirements applyHorizontalFlip];
-[BWInferenceVideoFormatRequirements videoContentMode];
-[BWInferenceVideoFormatRequirements singleStepRotationDegrees];
-[BWInferenceVideoFormatRequirements setSingleStepRotationDegrees:];
-[BWInferenceVideoFormatRequirements setIncludesInvalidContent:];
-[BWInferenceVideoFormatRequirements rotationDegrees];
-[BWInferenceVideoFormatRequirements dealloc];
-[BWInferenceVideoFormatRequirements deviceOriented];
-[BWInferenceVideoFormatRequirements setDeviceOriented:];
-[BWInferenceVideoFormatRequirements setLandscapeOriented:];
-[BWInferenceVideoFormatRequirements setRotationDegrees:];
-[BWInferenceVideoFormatRequirements setVideoContentMode:];
-[BWInferenceVideoFormatRequirements cropDescriptor];
-[BWInferenceVideoFormatRequirements setHistogramRequest:];
-[BWInferenceVideoFormatRequirements initWithFormat:];
-[BWInferenceVideoFormatRequirements setCropDescriptor:];
-[BWInferenceVideoFormatRequirements setApplyHorizontalFlip:];
```
