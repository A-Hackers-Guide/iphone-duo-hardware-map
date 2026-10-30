# `FigCaptureMovieFileSinkMiddlePipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCapturePipeline`
- 7 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"FigCaptureVISPipeline" _visPipeline;
@"BWFanOutNode" _videoFanOut;
@"FigCaptureVISPipeline" _overCaptureVISPipeline;
@"BWOverCaptureFanOutNode" _audioFanOut;
@"NSMutableArray" _metadataFanOuts;
@"FigCaptureMovieFileSinkHeadPipeline" _headPipeline;
Q _numberOfTailsToSupport;
```

## Properties

```
@property (T@"FigCaptureVISPipeline",R,N,V_visPipeline) visPipeline;
@property (T@"FigCaptureVISPipeline",R,N,V_overCaptureVISPipeline) overCaptureVISPipeline;
```

## Instance methods

```
-[FigCaptureMovieFileSinkMiddlePipeline dealloc];
-[FigCaptureMovieFileSinkMiddlePipeline visPipeline];
-[FigCaptureMovieFileSinkMiddlePipeline audioOutputForTailIndex:];
-[FigCaptureMovieFileSinkMiddlePipeline initWithConfiguration:graph:parentPipeline:headPipeline:captureDevicesByConnectionID:workgroup:];
-[FigCaptureMovieFileSinkMiddlePipeline metadataOutputsForTailIndex:];
-[FigCaptureMovieFileSinkMiddlePipeline overCaptureVISPipeline];
-[FigCaptureMovieFileSinkMiddlePipeline videoOutputForTailIndex:];
```
