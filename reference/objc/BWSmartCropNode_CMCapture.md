# `BWSmartCropNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWSmartCropHomographyProvider`, `BWFigVideoCaptureDeviceCenterStageDelegate`
- 29 instance variables, 17 properties, 52 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _cameraInfoByPortType;
f _teleNondisruptiveSwitchingZoomFactor;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
i _maxLossyCompressionLevel;
{?="columns"[3]} _cameraExtrinsicMatrix;
{?="columns"[3]} _pendingCameraExtrinsicMatrix;
{?="width"i"height"i} _outputDimensions;
{?="width"i"height"i} _previousOutputDimensions;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"NSArray" _portTypes;
@"<RTSCProcessor>" _rtscProcessor;
B _videoOutputFormatIsLive;
i _processingMode;
@"BWFigVideoCaptureDevice" _captureDevice;
i _activeOmahaConstituentDeviceType;
B _stillCaptureEnabled;
@"NSMutableArray" _stillPTSQueue;
@"NSMutableDictionary" _stillHomographyByPTS;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stillHomographyQueueLock;
@"BWNodeInput" _detectionMetadataInput;
@"BWNodeOutput" _detectionMetadataOutput;
B _detectionMetadataIsLive;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
@"NSObject<OS_dispatch_queue>" _rtscProcessorInitQueue;
q _singleFaceDetectedCumulativeTime;
q _multipleFacesDetectedCumulativeTime;
q _faceDetectionStartTime;
I _numFacesDetected;
```

## Properties

```
@property (T{?=ii},N,V_outputDimensions) outputDimensions;
@property (T{?=[3]},N,V_pendingCameraExtrinsicMatrix) cameraExtrinsicMatrix;
@property (Ti,R,N,V_processingMode) processingMode;
@property (T@,&,N,V_rtscProcessor) rtscProcessor;
@property (T@"BWNodeInput",R,N,V_detectionMetadataInput) detectionMetadataInput;
@property (T@"BWNodeOutput",R,N,V_detectionMetadataOutput) detectionMetadataOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) regionOfInterestForCameraControls;
@property (T@?,N) regionOfInterestForCameraControlsChangedHandler;
@property (TB,N,GisRegionOfInterestForCameraControlsFeedbackEnabled) regionOfInterestForCameraControlsFeedbackEnabled;
@property (T{?=BBB{CGRect={CGPoint=dd}{CGSize=dd}}ifffdfff},N) cinematicFramingControls;
@property (TB,N) cinematicFramingControlsSuspended;
@property (Tq,R,N,V_singleFaceDetectedCumulativeTime) singleFaceDetectedCumulativeTime;
@property (Tq,R,N,V_multipleFacesDetectedCumulativeTime) multipleFacesDetectedCumulativeTime;
```

## Class methods

```
+[BWSmartCropNode initialize];
```

## Instance methods

```
-[BWSmartCropNode prepareForCurrentConfigurationToBecomeLive];
-[BWSmartCropNode processingMode];
-[BWSmartCropNode cameraExtrinsicMatrix];
-[BWSmartCropNode _supportedInputPixelFormats];
-[BWSmartCropNode setRegionOfInterestForCameraControlsFeedbackEnabled:];
-[BWSmartCropNode renderSampleBuffer:forInput:];
-[BWSmartCropNode setRtscProcessor:];
-[BWSmartCropNode _pushHomography:pts:];
-[BWSmartCropNode setOutputDimensions:];
-[BWSmartCropNode _addVideoCaptureInputAndOutput];
-[BWSmartCropNode setRegionOfInterestForCameraControlsChangedHandler:];
-[BWSmartCropNode _updateOutputRequirements];
-[BWSmartCropNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxLossyCompressionLevel:cameraExtrinsicMatrix:processingMode:stillCaptureEnabled:objectMetadataIdentifiers:captureDevice:];
-[BWSmartCropNode _renderMetadataSampleBuffer:forInput:];
-[BWSmartCropNode cinematicFramingControlsSuspended];
-[BWSmartCropNode didChangeCenterStageMetadataDeliveryEnabled:];
-[BWSmartCropNode dealloc];
-[BWSmartCropNode _supportedOutputPixelFormats];
-[BWSmartCropNode outputDimensions];
-[BWSmartCropNode _updateDetectedFacesArray:];
-[BWSmartCropNode didChangeCenterStageFramingMode:];
-[BWSmartCropNode setCinematicFramingControlsSuspended:];
-[BWSmartCropNode detectionMetadataOutput];
-[BWSmartCropNode setCinematicFramingControls:];
-[BWSmartCropNode _updateSampleBufferMetadataAfterWarping:];
-[BWSmartCropNode _updateDetectedObjectsInfo:];
-[BWSmartCropNode isRegionOfInterestForCameraControlsFeedbackEnabled];
-[BWSmartCropNode _startFaceDetectionTimeAnalytics];
-[BWSmartCropNode cinematicFramingControls];
-[BWSmartCropNode didChangeCenterStageRectOfInterest:];
-[BWSmartCropNode regionOfInterestForCameraControlsChangedHandler];
-[BWSmartCropNode _updateFaceDetectionTimeAnalytics];
-[BWSmartCropNode detectionMetadataInput];
-[BWSmartCropNode _processFaceDetectionTimeAnalytics:];
-[BWSmartCropNode _renderVideoSampleBuffer:forInput:];
-[BWSmartCropNode didReachEndOfDataForConfigurationID:input:];
-[BWSmartCropNode _createCalibrationDictionaryFromSampleBuffer:];
-[BWSmartCropNode _isSampleBufferFromPrimaryStream:metadataDict:];
-[BWSmartCropNode multipleFacesDetectedCumulativeTime];
-[BWSmartCropNode nodeSubType];
-[BWSmartCropNode regionOfInterestForCameraControls];
-[BWSmartCropNode singleFaceDetectedCumulativeTime];
-[BWSmartCropNode _popHomography];
-[BWSmartCropNode restrictCenterStageFieldOfViewToWide:];
-[BWSmartCropNode didSelectFormat:forInput:];
-[BWSmartCropNode _addMetadataInputsAndOutputsWithMetadataIdentifiers:];
-[BWSmartCropNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWSmartCropNode _initRTSCProcessor];
-[BWSmartCropNode setCameraExtrinsicMatrix:];
-[BWSmartCropNode nodeType];
-[BWSmartCropNode rtscProcessor];
-[BWSmartCropNode smartCropHomographyDataForPTS:];
```
