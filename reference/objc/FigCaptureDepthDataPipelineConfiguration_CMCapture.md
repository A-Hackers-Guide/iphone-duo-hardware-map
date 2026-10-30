# `FigCaptureDepthDataPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"FigDepthDataCaptureConnectionConfiguration" _depthDataConnectionConfiguration;
@"FigVideoCaptureConnectionConfiguration" _videoDataConnectionConfiguration;
@"FigMetadataObjectCaptureConnectionConfiguration" _metadataObjectConnectionConfiguration;
B _depthConvertedUpstream;
{FigCaptureVideoTransform="mirrored"B"rotationDegrees"i"dimensions"{?="width"i"height"i}} _previousTransform;
B _hardwareDepthFilteringEnabled;
B _videoAndConvertedDepthDataOutputEnabled;
@"BWPipelineStage" _pipelineStage;
{?="val"[8I]} _clientAuditToken;
i _depthDataBaseRotationDegrees;
@"NSDictionary" _cameraInfoByPortType;
@"FigCaptureSourceVideoFormat" _requiredFormat;
i _pearlModuleType;
```

## Instance methods

```
-[FigCaptureDepthDataPipelineConfiguration init];
-[FigCaptureDepthDataPipelineConfiguration dealloc];
```
