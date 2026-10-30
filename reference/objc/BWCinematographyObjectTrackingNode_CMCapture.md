# `BWCinematographyObjectTrackingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWInferenceFormatProvider`, `PTCinematographyStreamDelegate`
- 39 instance variables, 8 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"PTCinematographyStream" _cinematographyStream;
@"PTCinematographyFrame" _previousCinematographyFrame;
i _cinematographyProcessingCadence;
i _framesSinceCinematographyProcessing;
{CGSize="width"d"height"d} _focusTapWindowSize;
@"NSDictionary" _cinematicVideoParameters;
@"NSString" _portTypeProvidingSDOFRenderingParameters;
Q _framesSinceLastDDR;
Q _humanPoseCadence;
@"NSDictionary" _latestDetections;
@"NSDictionary" _cameraInfoByPortType;
@"PTGlobalCinematographyMetadataVersion1" _globalCinematographyMetadata;
@"PTGlobalRenderingMetadata" _globalRenderingMetadata;
@"PTGlobalVideoHeaderMetadataVersion1" _globalVideoHeaderMetadata;
@"PTGlobalVideoMetadata" _globalMetadata;
q _globalRenderingMetadataVersion;
@"BWCinematographyLowLightMonitor" _lowLightMonitor;
q _latestFocusDetectionTrackID;
B _focusTrackedObjectTrackAcquired;
q _focusTrackedObjectLastID;
@"NSSet" _humanPosePreventionSet;
@"BWInferenceEngine" _inferenceEngine;
@"BWInferenceScheduler" _inferenceScheduler;
@"BWFigVideoCaptureDevice" _captureDevice;
@"NSMutableArray" _cinematicVideoMetadata;
q _framesSinceLastMetadataOutput;
q _metadataCollectionSize;
B _reportCinematicMetadataStatistics;
B _cinematicConversionDisabledOnModuleGating;
{?="value"q"timescale"i"flags"I"epoch"q} _cinematicMetadataRecordingStartPTS;
I _cinematicMetadataTotalFrameCount;
I _cinematicMetadataFramesOnWideCount;
I _cinematicMetadataFirstTwoSecondsFrameCount;
I _cinematicMetadataFirstTwoSecondsFramesOnWideCount;
I _cinematicMetadataFirstTenSecondsFrameCount;
I _cinematicMetadataFirstTenSecondsFramesOnWideCount;
B _inferenceEnginePrepared;
B _prepareCinematographyOnInit;
B _disabled;
```

## Properties

```
@property (T@"NSString",R,N) cinematographyModelVersionString;
@property (TB,N,V_disabled) disabled;
@property (T@"NSData",R,N) globalMetadata;
@property (Tq,N,V_metadataCollectionSize) metadataCollectionSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWCinematographyObjectTrackingNode initialize];
```

## Instance methods

```
-[BWCinematographyObjectTrackingNode prepareForCurrentConfigurationToBecomeLive];
-[BWCinematographyObjectTrackingNode disabled];
-[BWCinematographyObjectTrackingNode renderSampleBuffer:forInput:];
-[BWCinematographyObjectTrackingNode outputFormatForAttachedMediaKey:];
-[BWCinematographyObjectTrackingNode intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWCinematographyObjectTrackingNode inputVideoFormatForAttachedMediaKey:];
-[BWCinematographyObjectTrackingNode dealloc];
-[BWCinematographyObjectTrackingNode inputInferenceVideoFormatForAttachedMediaKey:];
-[BWCinematographyObjectTrackingNode outputVideoFormatForAttachedMediaKey:];
-[BWCinematographyObjectTrackingNode inputFormatForAttachedMediaKey:];
-[BWCinematographyObjectTrackingNode handleDroppedSample:forInput:];
-[BWCinematographyObjectTrackingNode didReachEndOfDataForConfigurationID:input:];
-[BWCinematographyObjectTrackingNode nodeSubType];
-[BWCinematographyObjectTrackingNode didSelectFormat:forInput:];
-[BWCinematographyObjectTrackingNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWCinematographyObjectTrackingNode setDisabled:];
-[BWCinematographyObjectTrackingNode nodeType];
-[BWCinematographyObjectTrackingNode cinematographyModelVersionString];
-[BWCinematographyObjectTrackingNode globalMetadata];
-[BWCinematographyObjectTrackingNode initWithCaptureDevice:tuningParameters:inferenceScheduler:frameRate:prepareCinematographyOnInit:];
-[BWCinematographyObjectTrackingNode metadataCollectionSize];
-[BWCinematographyObjectTrackingNode setMetadataCollectionSize:];
```
