# `FigCaptureLiDARDepthPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCapturePipeline`
- 13 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"BWFigVideoCaptureDevice" _captureDevice;
@"NSDictionary" _cameraInfoByPortType;
@"NSDictionary" _sensorIDStringsByPortType;
@"FigDepthDataCaptureConnectionConfiguration" _depthDataCaptureConnectionConfiguration;
i _rgbCameraHorizontalSensorBinningFactor;
i _rgbCameraVerticalSensorBinningFactor;
I _depthPixelFormat;
B _depthDataFilteringEnabled;
{?="width"i"height"i} _depthOutputDimensions;
@"NSString" _rgbCameraSourceID;
@"BWVideoPointCloudSynchronizerNode" _synchronizerNode;
@"BWPointCloudDensificationNode" _pointCloudDensificationNode;
@"BWDepthRotatorNode" _depthRotatorNode;
```

## Properties

```
@property (T@"BWNodeOutput",R,N) depthDataSinkOutput;
@property (T@"NSString",R,N,V_rgbCameraSourceID) rgbCameraSourceID;
```

## Class methods

```
+[FigCaptureLiDARDepthPipeline initialize];
```

## Instance methods

```
-[FigCaptureLiDARDepthPipeline dealloc];
-[FigCaptureLiDARDepthPipeline _buildLiDARDepthPipelineWithVideoSourceCaptureOutput:pointCloudOutput:graph:timeOfFlightCameraType:];
-[FigCaptureLiDARDepthPipeline depthDataSinkOutput];
-[FigCaptureLiDARDepthPipeline initWithCaptureDevice:cameraInfoByPortType:sensorIDStringsByPortType:timeOfFlightCameraType:depthDataCaptureConnectionConfiguration:videoSourceCaptureOutput:pointCloudOutput:graph:name:rgbCameraSourceID:errorOut:];
-[FigCaptureLiDARDepthPipeline rgbCameraSourceID];
```
