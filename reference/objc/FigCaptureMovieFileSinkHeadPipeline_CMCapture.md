# `FigCaptureMovieFileSinkHeadPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCapturePipeline`
- 23 instance variables, 20 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"BWIrisStagingNode" _irisStagingNode;
@"BWFileCoordinatorNode" _fileCoordinatorNode;
@"BWPhotoDecompressorNode" _irisIntermediateJPEGPhotoDecompressorNode;
@"BWVideoDefringingNode" _videoDefringingNode;
@"BWSceneClassifierSinkNode" _sceneClassifierSinkNode;
@"BWAudioConverterNode" _audioConverterNode;
@"BWAudioConverterNode" _cinematicAudioConverterNode;
@"BWAudioRemixAnalysisMetadataNode" _audioRemixMetadataNode;
@"BWVideoOrientationMetadataNode" _videoOrientationMetadataNode;
@"BWNodeOutput" _sceneClassifierPipelineUpstreamOutput;
@"NSMutableArray" _inferenceConnections;
@"NSString" _videoConnectionID;
@"NSString" _videoSourceID;
i _sourceDeviceType;
@"BWNodeOutput" _videoOutput;
@"BWNodeOutput" _audioOutput;
@"BWNodeOutput" _cinematicAudioOutput;
@"NSMutableArray" _metadataOutputs;
@"NSArray" _indexesOfDetectedObjectsInMetadataOutputs;
i _indexOfVideoOrientationInMetadataOutputs;
@"<BWPersonalPhotographerDelegate>" _personalPhotographerDelegate;
i _videoSourceDeviceType;
i _indexOfAudioRemixInMetadataOutputs;
```

## Properties

```
@property (T@"<BWMRCSceneObserver>",N) mrcSceneObserver;
@property (T@"<BWSemanticStyleSceneObserver>",N) semanticStyleSceneObserver;
@property (T@"NSString",R,N,V_videoConnectionID) videoConnectionID;
@property (T@"NSString",R,N,V_videoSourceID) videoSourceID;
@property (Ti,R,N,V_videoSourceDeviceType) videoSourceDeviceType;
@property (T@"BWIrisStagingNode",R,N,V_irisStagingNode) irisStagingNode;
@property (T@"BWFileCoordinatorNode",R,N,V_fileCoordinatorNode) fileCoordinatorNode;
@property (T@"BWVideoOrientationMetadataNode",R,N,V_videoOrientationMetadataNode) videoOrientationMetadataNode;
@property (T@"BWPhotoDecompressorNode",R,N,V_irisIntermediateJPEGPhotoDecompressorNode) irisIntermediateJPEGPhotoDecompressorNode;
@property (T@"BWVideoDefringingNode",R,N,V_videoDefringingNode) videoDefringingNode;
@property (T@"BWNodeOutput",R,N,V_videoOutput) videoOutput;
@property (T@"BWNodeOutput",R,N,V_audioOutput) audioOutput;
@property (T@"BWNodeOutput",R,N,V_cinematicAudioOutput) cinematicAudioOutput;
@property (Ti,R,N,V_indexOfAudioRemixInMetadataOutputs) indexOfAudioRemixInMetadataOutputs;
@property (T@"NSArray",R,N,V_metadataOutputs) metadataOutputs;
@property (T@"NSArray",R,N,V_indexesOfDetectedObjectsInMetadataOutputs) indexesOfDetectedObjectsInMetadataOutputs;
@property (Ti,R,N,V_indexOfVideoOrientationInMetadataOutputs) indexOfVideoOrientationInMetadataOutputs;
@property (T@"NSArray",R,N,V_inferenceConnections) inferenceConnections;
@property (TB,N) sceneClassifierSuspended;
@property (T@"<BWPersonalPhotographerDelegate>",R,N,V_personalPhotographerDelegate) personalPhotographerDelegate;
```

## Instance methods

```
-[FigCaptureMovieFileSinkHeadPipeline setSceneClassifierSuspended:];
-[FigCaptureMovieFileSinkHeadPipeline sceneClassifierSuspended];
-[FigCaptureMovieFileSinkHeadPipeline semanticStyleSceneObserver];
-[FigCaptureMovieFileSinkHeadPipeline videoOrientationMetadataNode];
-[FigCaptureMovieFileSinkHeadPipeline indexOfVideoOrientationInMetadataOutputs];
-[FigCaptureMovieFileSinkHeadPipeline dealloc];
-[FigCaptureMovieFileSinkHeadPipeline inferenceConnections];
-[FigCaptureMovieFileSinkHeadPipeline indexOfAudioRemixInMetadataOutputs];
-[FigCaptureMovieFileSinkHeadPipeline cinematicAudioOutput];
-[FigCaptureMovieFileSinkHeadPipeline videoSourceID];
-[FigCaptureMovieFileSinkHeadPipeline metadataOutputs];
-[FigCaptureMovieFileSinkHeadPipeline audioOutput];
-[FigCaptureMovieFileSinkHeadPipeline videoOutput];
-[FigCaptureMovieFileSinkHeadPipeline videoDefringingNode];
-[FigCaptureMovieFileSinkHeadPipeline irisIntermediateJPEGPhotoDecompressorNode];
-[FigCaptureMovieFileSinkHeadPipeline videoSourceDeviceType];
-[FigCaptureMovieFileSinkHeadPipeline setSemanticStyleSceneObserver:];
-[FigCaptureMovieFileSinkHeadPipeline indexesOfDetectedObjectsInMetadataOutputs];
-[FigCaptureMovieFileSinkHeadPipeline mrcSceneObserver];
-[FigCaptureMovieFileSinkHeadPipeline fileCoordinatorNode];
-[FigCaptureMovieFileSinkHeadPipeline setMrcSceneObserver:];
-[FigCaptureMovieFileSinkHeadPipeline irisStagingNode];
-[FigCaptureMovieFileSinkHeadPipeline initWithConfiguration:videoSourceCaptureOutputsByConnectionID:sourceStreamingSensorRawOutput:sourceStreamingHueMapOutput:sourceStreamingSemanticMasksOutput:audioSourceCaptureOutput:audioSourceCinematicAudioCaptureOutput:smartCameraInferenceOutput:detectedObjectBoxedMetadataOutputs:objectDetectionSourceOutput:metadataSourcePipelineOutputs:graph:parentPipeline:inferenceScheduler:captureDevicesByConnectionID:audioSourceDelegate:fileCoordinatorStatusDelegate:irisRequestDelegate:personalPhotographerCaptureDelegate:masterClock:workgroup:videoGreenGhostMitigationEnabled:];
-[FigCaptureMovieFileSinkHeadPipeline videoConnectionID];
-[FigCaptureMovieFileSinkHeadPipeline personalPhotographerDelegate];
```
