# `BWFaceTrackingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 28 instance variables, 8 properties, 25 instance methods, 1 class methods

## Instance variables

```
^{CVAFaceTracking=} _faceTrackingRef;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _processingLock;
@"NSObject<OS_dispatch_queue>" _processingQueue;
@"NSObject<OS_dispatch_semaphore>" _processingSemaphore;
B _processing;
^{opaqueCMSimpleQueue=} _nextSbufQueue;
B _setupDone;
B _structuredLightOccluded;
B _passthroughInputs;
@"NSString" _depthAttachedMediaKey;
i _preparedRotationDegrees;
i _liveRotationDegrees;
B _mirrored;
i _faceTrackingMachThreadPriority;
i _pearlModuleType;
i _faceTrackingMaxFaces;
B _faceTrackingUsesFaceRecognition;
f _faceTrackingNetworkFailureThresholdMultiplier;
B _faceTrackingPlusEnabled;
f _faceTrackingFailureFieldOfViewModifier;
B _skipProcessing;
@"BWVideoFormat" _uncompressedVideoFormat;
@"BWPixelBufferPool" _uncompressedVideoBufferPool;
^{OpaqueVTPixelTransferSession=} _transferSession;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _decompressionLock;
B _addMesh;
B _addDebugInfo;
@"NSString" _previousPortType;
```

## Properties

```
@property (TB,N,V_mirrored) mirrored;
@property (Ti,N,V_preparedRotationDegrees) rotationDegrees;
@property (Ti,N,V_faceTrackingMaxFaces) maxFaces;
@property (TB,N,V_faceTrackingUsesFaceRecognition) usesFaceRecognition;
@property (TB,N,V_faceTrackingPlusEnabled) faceTrackingPlusEnabled;
@property (Tf,N,V_faceTrackingNetworkFailureThresholdMultiplier) networkFailureThresholdMultiplier;
@property (Tf,N,V_faceTrackingFailureFieldOfViewModifier) trackingFailureFieldOfViewModifier;
@property (TB,N) skipProcessing;
```

## Class methods

```
+[BWFaceTrackingNode initialize];
```

## Instance methods

```
-[BWFaceTrackingNode renderSampleBuffer:forInput:];
-[BWFaceTrackingNode skipProcessing];
-[BWFaceTrackingNode rotationDegrees];
-[BWFaceTrackingNode dealloc];
-[BWFaceTrackingNode setMaxFaces:];
-[BWFaceTrackingNode hasNonLiveConfigurationChanges];
-[BWFaceTrackingNode faceTrackingPlusEnabled];
-[BWFaceTrackingNode setNetworkFailureThresholdMultiplier:];
-[BWFaceTrackingNode mirrored];
-[BWFaceTrackingNode setMirrored:];
-[BWFaceTrackingNode setSkipProcessing:];
-[BWFaceTrackingNode setTrackingFailureFieldOfViewModifier:];
-[BWFaceTrackingNode maxFaces];
-[BWFaceTrackingNode setRotationDegrees:];
-[BWFaceTrackingNode didReachEndOfDataForConfigurationID:input:];
-[BWFaceTrackingNode initWithFigThreadPriority:pearlModuleType:useUnfilteredDepth:queueDepth:passthroughInputs:allowPixelTransfer:];
-[BWFaceTrackingNode setFaceTrackingPlusEnabled:];
-[BWFaceTrackingNode trackingFailureFieldOfViewModifier];
-[BWFaceTrackingNode usesFaceRecognition];
-[BWFaceTrackingNode nodeSubType];
-[BWFaceTrackingNode didSelectFormat:forInput:];
-[BWFaceTrackingNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWFaceTrackingNode setUsesFaceRecognition:];
-[BWFaceTrackingNode networkFailureThresholdMultiplier];
-[BWFaceTrackingNode nodeType];
```
