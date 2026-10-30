# `FigCaptureMovieFileSinkTailPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"FigCaptureMovieFileSinkPipelineConfiguration" _movieFileSinkPipelineConfiguration;
@"BWPipelineStage" _movieFilePipelineStage;
@"BWPhotoDecompressorNode" _irisIntermediateJPEGPhotoDecompressorNode;
@"BWNodeOutput" _videoSourceOutput;
@"BWNodeOutput" _audioSourceOutput;
@"BWNodeOutput" _cinematicAudioSourceOutput;
@"NSArray" _metadataSourceOutputs;
@"NSArray" _indexesOfDetectedObjectsInMetadataOutputs;
i _indexOfVideoOrientationInMetadataOutputs;
B _vitalityScoringEnabled;
B _cinematicVideoMetadataEnabled;
B _lowLightVideoNoiseReductionEnabled;
B _delayedCompressorCleanupEnabled;
i _indexOfAudioRemixInMetadataOutputs;
```

## Properties

```
@property (T@"FigCaptureMovieFileSinkPipelineConfiguration",&,N,V_movieFileSinkPipelineConfiguration) movieFileSinkPipelineConfiguration;
@property (T@"BWPipelineStage",&,N,V_movieFilePipelineStage) movieFilePipelineStage;
@property (T@"BWPhotoDecompressorNode",&,N,V_irisIntermediateJPEGPhotoDecompressorNode) irisIntermediateJPEGPhotoDecompressorNode;
@property (T@"BWNodeOutput",&,N,V_videoSourceOutput) videoSourceOutput;
@property (T@"BWNodeOutput",&,N,V_audioSourceOutput) audioSourceOutput;
@property (T@"BWNodeOutput",&,N,V_cinematicAudioSourceOutput) cinematicAudioSourceOutput;
@property (Ti,N,V_indexOfAudioRemixInMetadataOutputs) indexOfAudioRemixInMetadataOutputs;
@property (T@"NSArray",&,N,V_metadataSourceOutputs) metadataSourceOutputs;
@property (T@"NSArray",&,N,V_indexesOfDetectedObjectsInMetadataOutputs) indexesOfDetectedObjectsInMetadataOutputs;
@property (Ti,N,V_indexOfVideoOrientationInMetadataOutputs) indexOfVideoOrientationInMetadataOutputs;
@property (TB,N,V_vitalityScoringEnabled) vitalityScoringEnabled;
@property (TB,N,V_delayedCompressorCleanupEnabled) delayedCompressorCleanupEnabled;
@property (TB,N,V_cinematicVideoMetadataEnabled) cinematicVideoMetadataEnabled;
@property (TB,N,V_lowLightVideoNoiseReductionEnabled) lowLightVideoNoiseReductionEnabled;
```

## Instance methods

```
-[FigCaptureMovieFileSinkTailPipelineConfiguration setCinematicVideoMetadataEnabled:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setIrisIntermediateJPEGPhotoDecompressorNode:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration indexOfVideoOrientationInMetadataOutputs];
-[FigCaptureMovieFileSinkTailPipelineConfiguration init];
-[FigCaptureMovieFileSinkTailPipelineConfiguration dealloc];
-[FigCaptureMovieFileSinkTailPipelineConfiguration indexOfAudioRemixInMetadataOutputs];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setIndexOfVideoOrientationInMetadataOutputs:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration delayedCompressorCleanupEnabled];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setAudioSourceOutput:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setMovieFileSinkPipelineConfiguration:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration videoSourceOutput];
-[FigCaptureMovieFileSinkTailPipelineConfiguration movieFilePipelineStage];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setDelayedCompressorCleanupEnabled:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration audioSourceOutput];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setIndexesOfDetectedObjectsInMetadataOutputs:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration metadataSourceOutputs];
-[FigCaptureMovieFileSinkTailPipelineConfiguration irisIntermediateJPEGPhotoDecompressorNode];
-[FigCaptureMovieFileSinkTailPipelineConfiguration vitalityScoringEnabled];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setVitalityScoringEnabled:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration indexesOfDetectedObjectsInMetadataOutputs];
-[FigCaptureMovieFileSinkTailPipelineConfiguration cinematicAudioSourceOutput];
-[FigCaptureMovieFileSinkTailPipelineConfiguration lowLightVideoNoiseReductionEnabled];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setIndexOfAudioRemixInMetadataOutputs:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration cinematicVideoMetadataEnabled];
-[FigCaptureMovieFileSinkTailPipelineConfiguration movieFileSinkPipelineConfiguration];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setMovieFilePipelineStage:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setCinematicAudioSourceOutput:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setVideoSourceOutput:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setLowLightVideoNoiseReductionEnabled:];
-[FigCaptureMovieFileSinkTailPipelineConfiguration setMetadataSourceOutputs:];
```
