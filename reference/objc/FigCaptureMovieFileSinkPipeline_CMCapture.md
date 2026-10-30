# `FigCaptureMovieFileSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkPipeline`
- 18 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"BWFigVideoCaptureDevice" _primaryCaptureDevice;
@"FigCaptureMovieFileSinkHeadPipeline" _headPipeline;
@"FigCaptureMovieFileSinkMiddlePipeline" _middlePipeline;
@"NSMutableArray" _tailPipelines;
@"NSMutableArray" _movieFileSinkNodes;
@"NSMutableArray" _videoCompressorNodes;
@"NSMutableArray" _sdofCompressorNodes;
@"FigVideoCaptureConnectionConfiguration" _primaryMovieFileVideoCaptureConnectionConfiguration;
B _momentCaptureMovieRecordingEnabled;
B _overCaptureTailPipelineRenderingEnabled;
B _overCaptureEnabled;
B _stereoVideoCaptureEnabled;
i _videoStabilizationStrength;
B _smartStyleReversibilityEnabled;
@"OS_os_workgroup" _workgroup;
@"BWCinematographyObjectTrackingNode" _cinematographyObjectTrackingNode;
@"BWCinematicVideoMetadataNode" _cinematicVideoMetadataNode;
i _movieRecordingEndOfDataBehavior;
```

## Class methods

```
+[FigCaptureMovieFileSinkPipeline initialize];
```

## Instance methods

```
-[FigCaptureMovieFileSinkPipeline dealloc];
-[FigCaptureMovieFileSinkPipeline headPipeline];
-[FigCaptureMovieFileSinkPipeline middlePipeline];
```
