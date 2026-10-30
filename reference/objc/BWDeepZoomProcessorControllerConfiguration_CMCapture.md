# `BWDeepZoomProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 6 instance variables, 6 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"BWVideoFormat" _inputFormat;
@"BWVideoFormat" _outputFormat;
i _version;
i _type;
i _mode;
{?="width"i"height"i} _stereoPhotoOutputDimensions;
```

## Properties

```
@property (T@"BWVideoFormat",&,N,V_inputFormat) inputFormat;
@property (T@"BWVideoFormat",&,N,V_outputFormat) outputFormat;
@property (Ti,N,V_version) version;
@property (Ti,N,V_type) type;
@property (Ti,N,V_mode) mode;
@property (T{?=ii},N,V_stereoPhotoOutputDimensions) stereoPhotoOutputDimensions;
```

## Class methods

```
+[BWDeepZoomProcessorControllerConfiguration deepZoomProcessingModeForType:sensorConfiguration:captureType:];
+[BWDeepZoomProcessorControllerConfiguration doDeepZoomStandardOrLiteForSampleBuffer:type:sensorConfiguration:intermediateZoomSrcRectOut:intermediateZoomDstRectOut:];
+[BWDeepZoomProcessorControllerConfiguration doDeepZoomStandardOrLiteForType:sensorConfiguration:dimensions:metadata:stillImageSettings:intermediateZoomSrcRectOut:intermediateZoomDstRectOut:];
+[BWDeepZoomProcessorControllerConfiguration doDeepZoomTransferForSampleBuffer:sensorConfiguration:intermediateZoomSrcRectOut:];
```

## Instance methods

```
-[BWDeepZoomProcessorControllerConfiguration setStereoPhotoOutputDimensions:];
-[BWDeepZoomProcessorControllerConfiguration setOutputFormat:];
-[BWDeepZoomProcessorControllerConfiguration stereoPhotoOutputDimensions];
-[BWDeepZoomProcessorControllerConfiguration inputFormat];
-[BWDeepZoomProcessorControllerConfiguration dealloc];
-[BWDeepZoomProcessorControllerConfiguration version];
-[BWDeepZoomProcessorControllerConfiguration setMode:];
-[BWDeepZoomProcessorControllerConfiguration setInputFormat:];
-[BWDeepZoomProcessorControllerConfiguration setType:];
-[BWDeepZoomProcessorControllerConfiguration type];
-[BWDeepZoomProcessorControllerConfiguration mode];
-[BWDeepZoomProcessorControllerConfiguration setVersion:];
-[BWDeepZoomProcessorControllerConfiguration outputFormat];
```
