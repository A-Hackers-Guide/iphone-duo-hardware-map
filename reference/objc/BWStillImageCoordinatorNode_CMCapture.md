# `BWStillImageCoordinatorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWFigVideoCaptureStreamStillImageCaptureDelegate`, `FigCaptureOSStateDataProvider`, `BWStillImageProcessingStatusDelegate`
- 76 instance variables, 7 properties, 58 instance methods, 10 class methods

## Instance variables

```
B _active;
B _liveReconfiguring;
@"BWStillImageNodeConfiguration" _nodeConfiguration;
@"BWFigVideoCaptureDevice" _captureDevice;
@"NSDictionary" _portTypeToInput;
@"NSDictionary" _portTypeToOutput;
@"NSDictionary" _portTypeToSensorRawInput;
@"NSDictionary" _portTypeToSensorRawOutput;
@"NSArray" _highResStillImageDimensions;
@"<BWStillImageCaptureStatusDelegate>" _stillImageCaptureStatusDelegate;
@"<BWStillImageProcessingSupportProvider>" _stillImageProcessingSupportProvider;
i _stillImageCapturePipeliningMode;
I _numberOfBurstCapturesInFlight;
I _maxNumberOfBurstCapturesAllowedInFlight;
@"NSMutableArray" _requestQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _requestQueueLock;
i _captureRequestCount;
i _prepareRequestCount;
@"NSObject<OS_dispatch_queue>" _stillImageDispatchQueue;
@"NSObject<OS_dispatch_group>" _stillImageDispatchGroup;
Ai _stillImageDispatchGroupEnterCount;
@"NSObject<OS_dispatch_group>" _stillImageGraphStopDispatchGroup;
Ai _stillImageGraphStopDispatchGroupEnterCount;
@"FigStateMachine" _stateMachine;
@"NSMutableDictionary" _receivedImagesOrErrorsForRequestByPortType;
@"NSMutableDictionary" _receivedUltraHighResImagesOrErrorsForRequestByPortType;
i _clientExpectedImagesOrErrorsForRequest;
i _clientReceivedImagesOrErrorsForRequest;
@"BWStillImageCoordinatorRequest" _currentRequest;
@"FigCaptureStillImageSettings" _currentRequestedStillImageCaptureSettings;
@"BWStillImageCaptureSettings" _currentResolvedStillImageCaptureSettings;
@"BWStillImageProcessingSettings" _currentResolvedStillImageProcessingSettings;
I _firedDelegateCallbackFlags;
@"NSString" _flushedCaptureRequestIdentifier;
B _isMomentCaptureCapturingBeforeCommitted;
B _isMomentCaptureProcessingBeforeCommitted;
@"NSMutableArray" _momentCaptureUnfiredCallbacks;
@"NSMutableArray" _momentCaptureBuffersByInputIndex;
i _momentCaptureUncommittedStillImageCaptureError;
q _momentCaptureUnfiredWillBeginCaptureBeforeResolvingSettingsCallbackSettingsID;
q _momentCaptureLastCancelledSettingsID;
q _momentCaptureLastComittedSettingsID;
{?="value"q"timescale"i"flags"I"epoch"q} _streamingDisruptionEndPTS;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferTrackingLock;
i _inUseBufferCount;
i _inUseZoomBasedBufferCount;
i _inUseUltraHighResBufferCount;
i _ultraHighResFrameCountExpansionFactor;
B _responsiveShutterEnabled;
B _responsiveShutterEnabledViaAPI;
B _fastCapturePrioritizationEnabled;
@"<BWCompressedShotBuffer>" _compressedShotBuffer;
i _extraUncompressedShotBufferCapacityForThermalSystemPressureLevelSerious;
i _extraUncompressedShotBufferCapacityForThermalSystemPressureLevelCritical;
i _normalResolutionOverlapCapacityForSoQ;
B _shotBufferEnabled;
i _allocatedShotBufferCapacity;
i _defaultShotBufferCapacity;
i _numberOfZoomBasedBufferIncludedInShotBuffer;
i _numberOfUltraHighResBufferIncludedInShotBuffer;
@"NSObject<OS_dispatch_group>" _shotBufferWaitGroup;
i _shotBufferWaitFreeBufferCount;
B _shotPacerEnabled;
f _shotPacerMaxFPS;
q _lastStillImageCaptureStartTime;
q _lastStillImageCaptureCompleteTime;
B _dynamicShotQualityEnabled;
i _minFullQualityShots;
f _timeSinceLastCaptureEnterThreshold;
f _timeSinceLastCaptureExitThreshold;
i _numCapturesInShotSequence;
@"FigCaptureOSStateHandle" _osStateHandle;
@"BWDeviceOrientationMonitor" _deviceOrientationMonitor;
@"NSObject<OS_dispatch_source>" _calibrationTimer;
i _calibrationSettingsIDCounter;
B _cinematicFramingWarpingRequired;
```

## Properties

```
@property (T@"<BWStillImageCaptureStatusDelegate>",W,N,V_stillImageCaptureStatusDelegate) stillImageCaptureStatusDelegate;
@property (T@"<BWStillImageProcessingSupportProvider>",W,N,V_stillImageProcessingSupportProvider) stillImageProcessingSupportProvider;
@property (TB,N,V_cinematicFramingWarpingRequired) cinematicFramingWarpingRequired;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWStillImageCoordinatorNode initialize];
+[BWStillImageCoordinatorNode currentAllocatedShotBufferCapacity];
+[BWStillImageCoordinatorNode maxShotBufferCapacity];
+[BWStillImageCoordinatorNode numberOfUltraHighResBufferIncludedInShotBuffer];
+[BWStillImageCoordinatorNode numberOfZoomBasedBufferIncludedInShotBuffer];
+[BWStillImageCoordinatorNode setCurrentAllocatedShotBufferCapacity:];
+[BWStillImageCoordinatorNode setMaxShotBufferCapacity:];
+[BWStillImageCoordinatorNode setNumberOfUltraHighResBufferIncludedInShotBuffer:];
+[BWStillImageCoordinatorNode setNumberOfZoomBasedBufferIncludedInShotBuffer:];
+[BWStillImageCoordinatorNode worstCaseMaxBracketedCaptureBufferCountForPreparedSettings:stillImageCaptureSettings:captureDevice:];
```

## Instance methods

```
-[BWStillImageCoordinatorNode setResponsiveShutterEnabled:];
-[BWStillImageCoordinatorNode prepareForCurrentConfigurationToBecomeLive];
-[BWStillImageCoordinatorNode osStatePropertyList];
-[BWStillImageCoordinatorNode stillImageCapturePipeliningMode];
-[BWStillImageCoordinatorNode stillImageProcessingSupportProvider];
-[BWStillImageCoordinatorNode setStillImageProcessingSupportProvider:];
-[BWStillImageCoordinatorNode _stillImageDispatchQueue];
-[BWStillImageCoordinatorNode responsiveShutterEnabled];
-[BWStillImageCoordinatorNode setFastCapturePrioritizationEnabled:];
-[BWStillImageCoordinatorNode fastCapturePrioritizationEnabled];
-[BWStillImageCoordinatorNode sensorRawInputForPortType:];
-[BWStillImageCoordinatorNode captureStreamWillWaitForTimeMachineToFill:];
-[BWStillImageCoordinatorNode renderSampleBuffer:forInput:];
-[BWStillImageCoordinatorNode _configureCurrentCaptureRequestStateForFigCaptureStillImageSettings];
-[BWStillImageCoordinatorNode shouldGraphLiveReconfigurationWait];
-[BWStillImageCoordinatorNode commitStillImageMomentCaptureWithSettings:];
-[BWStillImageCoordinatorNode inputForPortType:];
-[BWStillImageCoordinatorNode setStillImageCaptureStatusDelegate:];
-[BWStillImageCoordinatorNode sensorRawOutputForPortType:];
-[BWStillImageCoordinatorNode setCinematicFramingWarpingRequired:];
-[BWStillImageCoordinatorNode dealloc];
-[BWStillImageCoordinatorNode outputForPortType:];
-[BWStillImageCoordinatorNode initWithNodeConfiguration:captureDevice:inputPortTypes:sensorRawInputPortTypes:highResStillImageDimensions:];
-[BWStillImageCoordinatorNode compressedShotBuffer];
-[BWStillImageCoordinatorNode setMaxNumberOfBurstCapturesAllowedInFlight:];
-[BWStillImageCoordinatorNode cancelStillImageMomentCaptureWithSettingsID:];
-[BWStillImageCoordinatorNode setResponsiveShutterEnabledViaAPI:];
-[BWStillImageCoordinatorNode stillImageCaptureStatusDelegate];
-[BWStillImageCoordinatorNode willLiveReconfigureGraph];
-[BWStillImageCoordinatorNode prepareStillImageCaptureNowWithSettings:];
-[BWStillImageCoordinatorNode _unpackNextRequest];
-[BWStillImageCoordinatorNode _enqueueRequest:serviceRequestsIfNecessary:];
-[BWStillImageCoordinatorNode captureStream:didCaptureReferenceFrameWithPTS:referenceFrameBracketedCaptureSequenceNumber:];
-[BWStillImageCoordinatorNode captureStream:stillImageCaptureError:];
-[BWStillImageCoordinatorNode _initWithNodeConfiguration:captureDevice:inputPortTypes:sensorRawInputPortTypes:highResStillImageDimensions:allStateTransitionsHandler:];
-[BWStillImageCoordinatorNode setStillImageCapturePipeliningMode:];
-[BWStillImageCoordinatorNode cinematicFramingWarpingRequired];
-[BWStillImageCoordinatorNode captureStillImageNowWithSettings:];
-[BWStillImageCoordinatorNode captureStreamWillBeginStillImageCapture:];
-[BWStillImageCoordinatorNode didReachEndOfDataForConfigurationID:input:];
-[BWStillImageCoordinatorNode _stillImageDispatchGroup];
-[BWStillImageCoordinatorNode processStillImageNowWithAssetBundle:];
-[BWStillImageCoordinatorNode captureStream:didCapturePreBracketedEV0ImageWithPTS:];
-[BWStillImageCoordinatorNode beginStillImageMomentCaptureWithSettings:];
-[BWStillImageCoordinatorNode captureStreamDidCompleteStillImageCapture:];
-[BWStillImageCoordinatorNode _stateMachine];
-[BWStillImageCoordinatorNode nodeSubType];
-[BWStillImageCoordinatorNode node:didSelectNewReferenceFrameWithPTS:transform:forSettings:];
-[BWStillImageCoordinatorNode node:didSelectVitalityMode:forSettings:];
-[BWStillImageCoordinatorNode willStopGraph:];
-[BWStillImageCoordinatorNode didSelectFormat:forInput:];
-[BWStillImageCoordinatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageCoordinatorNode clientReceivedPayloadForSettings:status:clientIsMidStillImageGraph:];
-[BWStillImageCoordinatorNode handleNodeError:forInput:];
-[BWStillImageCoordinatorNode maxNumberOfBurstCapturesAllowedInFlight];
-[BWStillImageCoordinatorNode nodeType];
-[BWStillImageCoordinatorNode initiateStillImageCaptureNowWithSettings:];
-[BWStillImageCoordinatorNode setCompressedShotBuffer:];
```
