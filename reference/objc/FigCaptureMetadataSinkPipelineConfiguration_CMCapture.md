# `FigCaptureMetadataSinkPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"FigMetadataObjectCaptureConnectionConfiguration" _metadataObjectConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _videoDataConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _sceneClassifierConnectionConfiguration;
B _mrcLowPowerModeEnabled;
B _useSceneClassifierToGateMetadataDetectors;
{?="major"S"minor"S"patch"S} _smartCameraPipelineVersion;
B _vitalityScoringEnabled;
B _previewEnabled;
i _motionAttachmentsSource;
B _boxedMetadataEnabled;
B _compressed8BitInputEnabled;
i _pearlModuleType;
@"NSArray" _detectedObjectMovieFileOutputMetadataConnectionConfigurations;
{BWLensSmudgeDetectionConfiguration="lensSmudgeDetectionEnabled"B"lensSmudgeDetectionInterval"{?="value"q"timescale"i"flags"I"epoch"q}} _lensSmudgeDetectionConfiguration;
B _continuousAutoFocusTrackingMetadataSupported;
@"BWNodeOutput" _cinematicVideoMetadataTrackingOutput;
B _deferredPrepareEnabled;
i _inputRotationRelativeToSource;
```

## Instance methods

```
-[FigCaptureMetadataSinkPipelineConfiguration dealloc];
```
