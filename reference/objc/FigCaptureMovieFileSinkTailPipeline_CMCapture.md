# `FigCaptureMovieFileSinkTailPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCapturePipeline`
- 24 instance variables, 15 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"BWPixelTransferNode" _scalerNode;
@"FigCaptureVISPipeline" _visPipeline;
@"FigCaptureVISPipeline" _stereoVideoCompanionVISPipeline;
@"BWVideoCompressorNode" _videoCompressorNode;
@"BWVideoCompressorNode" _sdofCompressorNode;
@"BWVideoCompressorNode" _depthCompressorNode;
@"NSMutableDictionary" _smartStyleCompressorNodesByAttachedMediaKey;
@"BWBackPressureNode" _irisIntermediateJPEGDecompressionBackPressureNode;
@"BWBackPressureNode" _visBackPressureNode;
@"BWBackPressureNode" _scalerBackPressureNode;
@"BWBackPressureNode" _irisSDOFVISBackPressureNode;
@"BWQuickTimeMovieFileSinkNode" _movieFileSinkNode;
@"<BWNodeBackPressureSource>" _visBackPressureSourceNode;
Q _tailIndex;
i _visBackPressureExtraRetainedBufferCount;
i _videoStabilizationType;
B _offlineVISEnabled;
B _recording;
@"BWSmartCropNode" _smartCropNode;
@"BWBackPressureNode" _secondaryScalerBackPressureNode;
@"BWCinematographyObjectTrackingNode" _cinematographyObjectTrackingNode;
@"BWCinematicVideoMetadataNode" _cinematicVideoMetadataNode;
B _sceneClassifierSuspended;
@"<BWMRCSceneObserver>" _mrcSceneObserver;
```

## Properties

```
@property (T@"<BWMRCSceneObserver>",N,V_mrcSceneObserver) mrcSceneObserver;
@property (T@"BWQuickTimeMovieFileSinkNode",R,N,V_movieFileSinkNode) movieFileSinkNode;
@property (T@"BWPixelTransferNode",R,N,V_scalerNode) scalerNode;
@property (T@"BWVideoCompressorNode",R,N,V_videoCompressorNode) videoCompressorNode;
@property (T@"BWVideoCompressorNode",R,N,V_sdofCompressorNode) sdofCompressorNode;
@property (T@"BWVideoCompressorNode",R,N,V_depthCompressorNode) depthCompressorNode;
@property (T@"NSMutableDictionary",R,N,V_smartStyleCompressorNodesByAttachedMediaKey) smartStyleCompressorNodesByAttachedMediaKey;
@property (T@"FigCaptureVISPipeline",R,N,V_visPipeline) visPipeline;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) irisVISCleanOutputRectForCLAP;
@property (T{?=ii},R,N) offlineVISDimensions;
@property (TB,N,V_recording) recording;
@property (TB,N,V_sceneClassifierSuspended) sceneClassifierSuspended;
@property (T@"BWSmartCropNode",R,N,V_smartCropNode) smartCropNode;
@property (T@"BWCinematographyObjectTrackingNode",R,N,V_cinematographyObjectTrackingNode) cinematographyObjectTrackingNode;
@property (T@"BWCinematicVideoMetadataNode",R,N,V_cinematicVideoMetadataNode) cinematicVideoMetadataNode;
```

## Instance methods

```
-[FigCaptureMovieFileSinkTailPipeline setSceneClassifierSuspended:];
-[FigCaptureMovieFileSinkTailPipeline irisVISCleanOutputRectForCLAP];
-[FigCaptureMovieFileSinkTailPipeline sceneClassifierSuspended];
-[FigCaptureMovieFileSinkTailPipeline cinematographyObjectTrackingNode];
-[FigCaptureMovieFileSinkTailPipeline dealloc];
-[FigCaptureMovieFileSinkTailPipeline cinematicVideoMetadataNode];
-[FigCaptureMovieFileSinkTailPipeline smartCropNode];
-[FigCaptureMovieFileSinkTailPipeline visPipeline];
-[FigCaptureMovieFileSinkTailPipeline setRecording:];
-[FigCaptureMovieFileSinkTailPipeline setTextureStyle:];
-[FigCaptureMovieFileSinkTailPipeline recording];
-[FigCaptureMovieFileSinkTailPipeline depthCompressorNode];
-[FigCaptureMovieFileSinkTailPipeline smartStyleCompressorNodesByAttachedMediaKey];
-[FigCaptureMovieFileSinkTailPipeline offlineVISDimensions];
-[FigCaptureMovieFileSinkTailPipeline sdofCompressorNode];
-[FigCaptureMovieFileSinkTailPipeline mrcSceneObserver];
-[FigCaptureMovieFileSinkTailPipeline setMrcSceneObserver:];
-[FigCaptureMovieFileSinkTailPipeline videoCompressorNode];
-[FigCaptureMovieFileSinkTailPipeline initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:multiCamClientCompositingCallback:workgroup:];
-[FigCaptureMovieFileSinkTailPipeline movieFileSinkNode];
-[FigCaptureMovieFileSinkTailPipeline scalerNode];
```
