# `BWStereoDisparityProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _portTypesWithDepthSegmentationPortraitParameters;
{?="width"i"height"i} _inputDimensions;
{?="width"i"height"i} _disparityOutputDimensions;
B _zoomingDisparityAllowed;
B _shouldComputeDisparityWhenCalibrationFails;
i _stillImageDepthDataType;
```

## Properties

```
@property (T@"NSArray",&,N,V_portTypesWithDepthSegmentationPortraitParameters) portTypesWithDepthSegmentationPortraitParameters;
@property (T{?=ii},N,V_inputDimensions) inputDimensions;
@property (T{?=ii},N,V_disparityOutputDimensions) disparityOutputDimensions;
@property (Ti,N,V_stillImageDepthDataType) stillImageDepthDataType;
@property (TB,N,V_zoomingDisparityAllowed) zoomingDisparityAllowed;
@property (TB,N,V_shouldComputeDisparityWhenCalibrationFails) shouldComputeDisparityWhenCalibrationFails;
```

## Instance methods

```
-[BWStereoDisparityProcessorControllerConfiguration stillImageDepthDataType];
-[BWStereoDisparityProcessorControllerConfiguration zoomingDisparityAllowed];
-[BWStereoDisparityProcessorControllerConfiguration dealloc];
-[BWStereoDisparityProcessorControllerConfiguration portTypesWithDepthSegmentationPortraitParameters];
-[BWStereoDisparityProcessorControllerConfiguration inputDimensions];
-[BWStereoDisparityProcessorControllerConfiguration setPortTypesWithDepthSegmentationPortraitParameters:];
-[BWStereoDisparityProcessorControllerConfiguration setShouldComputeDisparityWhenCalibrationFails:];
-[BWStereoDisparityProcessorControllerConfiguration description];
-[BWStereoDisparityProcessorControllerConfiguration setDisparityOutputDimensions:];
-[BWStereoDisparityProcessorControllerConfiguration setStillImageDepthDataType:];
-[BWStereoDisparityProcessorControllerConfiguration disparityOutputDimensions];
-[BWStereoDisparityProcessorControllerConfiguration setInputDimensions:];
-[BWStereoDisparityProcessorControllerConfiguration shouldComputeDisparityWhenCalibrationFails];
-[BWStereoDisparityProcessorControllerConfiguration setZoomingDisparityAllowed:];
```
