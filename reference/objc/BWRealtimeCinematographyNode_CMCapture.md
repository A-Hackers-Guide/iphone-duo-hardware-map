# `BWRealtimeCinematographyNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `PTCinematographyStreamDelegate`, `BWCinematicVideoFocusDetectionProvider`, `BWFigVideoCaptureDeviceStreamingFilterDelegate`
- 44 instance variables, 12 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"PTCinematographyStream" _cinematographyStream;
@"NSDictionary" _latestDetections;
@"BWNodeOutput" _movieFileOutput;
@"BWNodeOutput" _previewOutput;
@"BWNodeOutput" _detectedObjectsOutput;
@"BWFigVideoCaptureDevice" _captureDevice;
@"BWCinematographyLowLightMonitor" _lowLightMonitor;
f _networkBias;
B _usePTSToSyncPreviewAndCaptureFrames;
B _hasAutoFocus;
i _framesSinceAutoFocusUpdate;
i _autoFocusUpdateFrameDelay;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastFixedFocusRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastFixedFocusFinalCropRect;
i focusMode;
B _hasSeenDepth;
B _highResolutionInputEnabled;
f _simulatedAperture;
^{opaqueCMSampleBuffer=} _previousSampleBuffer;
^{opaqueCMFormatDescription=} _depthFormatDescription;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
@"NSMutableArray" _videoCaptureSampleBufferQueue;
@"NSMutableArray" _previewSampleBufferQueue;
i _numEODMessagesReceived;
@"BWNodeInput" _captureInput;
@"PTGlobalCinematographyMetadataVersion1" _globalCinematographyMetadata;
@"PTGlobalRenderingMetadata" _globalRenderingMetadata;
@"PTGlobalVideoHeaderMetadataVersion1" _globalVideoHeaderMetadata;
@"PTGlobalVideoMetadata" _globalMetadata;
B _globalsWereSet;
q _globalRenderingMetadataVersion;
q _latestFocusDetectionTrackID;
B _smartStyleLearningEnabled;
I _frameCount;
{?="value"q"timescale"i"flags"I"epoch"q} _firstFramePTS;
d _halfRatePreviewTimeThresholdSeconds;
@"FigCaptureThermalMonitor" _thermalMonitor;
B _thermalConstraintActive;
@"NSMutableArray" _focusDetections;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _focusDetectionsLock;
B _focusDetectionProviderEnabled;
B _transformCinematographyDetectionsForMovieFileOutput;
B _depthInputProvided;
@"<BWCinematicVideoDisparityProvider>" _cinematicVideoDisparityProvider;
```

## Properties

```
@property (T@"BWNodeOutput",R,N) detectedObjectsOutput;
@property (Tf,N) simulatedAperture;
@property (T@"NSString",R,N) cinematographyModelVersionString;
@property (T@"BWNodeOutput",R,N,V_movieFileOutput) movieFileOutput;
@property (T@"BWNodeOutput",R,N,V_previewOutput) previewOutput;
@property (T@"NSData",R,N) globalMetadata;
@property (TB,R,N,V_transformCinematographyDetectionsForMovieFileOutput) transformCinematographyDetectionsForMovieFileOutput;
@property (T@"<BWCinematicVideoDisparityProvider>",N,V_cinematicVideoDisparityProvider) cinematicVideoDisparityProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWRealtimeCinematographyNode initialize];
```

## Instance methods

```
-[BWRealtimeCinematographyNode renderSampleBuffer:forInput:];
-[BWRealtimeCinematographyNode dealloc];
-[BWRealtimeCinematographyNode hasNonLiveConfigurationChanges];
-[BWRealtimeCinematographyNode setSimulatedAperture:];
-[BWRealtimeCinematographyNode previewOutput];
-[BWRealtimeCinematographyNode handleDroppedSample:forInput:];
-[BWRealtimeCinematographyNode didReachEndOfDataForConfigurationID:input:];
-[BWRealtimeCinematographyNode simulatedAperture];
-[BWRealtimeCinematographyNode nodeSubType];
-[BWRealtimeCinematographyNode didSelectFormat:forInput:];
-[BWRealtimeCinematographyNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWRealtimeCinematographyNode nodeType];
-[BWRealtimeCinematographyNode movieFileOutput];
-[BWRealtimeCinematographyNode cinematicVideoDisparityProvider];
-[BWRealtimeCinematographyNode cinematographyModelVersionString];
-[BWRealtimeCinematographyNode copyCinematicVideoFocusDetections];
-[BWRealtimeCinematographyNode detectedObjectsOutput];
-[BWRealtimeCinematographyNode focusDetectionProviderEnabled];
-[BWRealtimeCinematographyNode globalMetadata];
-[BWRealtimeCinematographyNode initWithObjectMetadataIdentifiers:cachedSimulatedAperture:captureDevice:tuningParameters:videoDepthConfiguration:smartStyleLearningEnabled:highResolutionInputEnabled:transformCinematographyDetectionsForMovieFileOutput:depthInputProvided:];
-[BWRealtimeCinematographyNode setCinematicVideoDisparityProvider:];
-[BWRealtimeCinematographyNode setFocusDetectionProviderEnabled:];
-[BWRealtimeCinematographyNode transformCinematographyDetectionsForMovieFileOutput];
```
