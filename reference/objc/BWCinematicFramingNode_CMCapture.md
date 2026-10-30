# `BWCinematicFramingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWFigVideoCaptureDeviceCenterStageDelegate`, `BWFigVideoCaptureDeviceManualCinematicFramingDelegate`, `BWCinematicFramingStatesProvider`
- 39 instance variables, 18 properties, 40 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _videoCaptureInputsByPortType;
@"BWNodeOutput" _videoCaptureOutput;
@"NSMutableDictionary" _detectionMetadataInputsByPortType;
@"BWNodeOutput" _detectionMetadataOutput;
^{opaqueCMFormatDescription=} _outputFormatDescription;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
@"NSDictionary" _cameraInfoByPortType;
{?="width"i"height"i} _outputDimensions;
[2{?="inputCamera"@"VCCamera""outputCamera"@"VCCamera""pts"{?="value"q"timescale"i"flags"I"epoch"q}"outputROI"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}}] _stillCaptureQueue;
I _stillCaptureEnqueueIndex;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stillCaptureQueueLock;
@"VCProcessor" _vcProcessor;
{?="autoFramingEnabled"B"fisheyeEffectEnabled"B"fieldOfViewRestrictedToWide"B"outputFramingRectOfInterest"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"centerStageFramingMode"i"videoZoomFactor"f"panningAngleX"f"panningAngleY"f"manualFramingDefaultZoomFactor"d"defaultVirtualCameraRotationAngleX"f"defaultVirtualCameraRotationAngleY"f"defaultVirtualCameraRotationAngleZ"f} _cinematicFramingControls;
@"BWDeviceOrientationMonitor" _deviceOrientationMonitor;
I _maxPeopleDetected;
@"NSString" _clientApplicationID;
I _cinematicFramingControlMode;
I _minLuxLevelNeeded;
B _stillImageCaptureEnabled;
B _deviceOrientationCorrectionEnabled;
B _outputCameraResetInFlight;
B _oneShotFramingInFlight;
i _maxLossyCompressionLevel;
@"NSArray" _portTypes;
i _endOfDataVideoInputsCount;
i _endOfDataMetadataInputsCount;
B _videoOutputFormatIsLive;
B _metadataOutputFormatIsLive;
B _cameraHasDistoritionCoefficients;
B _cameraHasCalibrationValidMaxRadius;
B _cinematicFramingControlsSuspended;
B _regionOfInterestForCameraControlsEnabled;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _regionOfInterestForCameraControls;
@? _regionOfInterestForCameraControlsChangedHandler;
Q _pipelineType;
B _centerStageMetadataDeliveryEnabled;
B _downstreamRequires10BitPixelFormat;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_videoCaptureInputsByPortType) videoCaptureInputsByPortType;
@property (T@"BWNodeOutput",R,N,V_videoCaptureOutput) videoCaptureOutput;
@property (T@"NSDictionary",R,N,V_detectionMetadataInputsByPortType) detectionMetadataInputsByPortType;
@property (T@"BWNodeOutput",R,N,V_detectionMetadataOutput) detectionMetadataOutput;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (TI,N,V_cinematicFramingControlMode) cinematicFramingControlMode;
@property (Td,N) manualFramingVideoZoomFactor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_regionOfInterestForCameraControls) regionOfInterestForCameraControls;
@property (T@?,N) regionOfInterestForCameraControlsChangedHandler;
@property (TB,N,GisRegionOfInterestForCameraControlsFeedbackEnabled) regionOfInterestForCameraControlsFeedbackEnabled;
@property (T{?=BBB{CGRect={CGPoint=dd}{CGSize=dd}}ifffdfff},N) cinematicFramingControls;
@property (TB,N) cinematicFramingControlsSuspended;
@property (Tq,R,N) singleFaceDetectedCumulativeTime;
@property (Tq,R,N) multipleFacesDetectedCumulativeTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWCinematicFramingNode initialize];
```

## Instance methods

```
-[BWCinematicFramingNode prepareForCurrentConfigurationToBecomeLive];
-[BWCinematicFramingNode setRegionOfInterestForCameraControlsFeedbackEnabled:];
-[BWCinematicFramingNode renderSampleBuffer:forInput:];
-[BWCinematicFramingNode startPanningAtPoint:];
-[BWCinematicFramingNode setRegionOfInterestForCameraControlsChangedHandler:];
-[BWCinematicFramingNode cinematicFramingControlsSuspended];
-[BWCinematicFramingNode didChangeCenterStageMetadataDeliveryEnabled:];
-[BWCinematicFramingNode dealloc];
-[BWCinematicFramingNode didChangeCenterStageFramingMode:];
-[BWCinematicFramingNode setCinematicFramingControlsSuspended:];
-[BWCinematicFramingNode detectionMetadataOutput];
-[BWCinematicFramingNode setCinematicFramingControls:];
-[BWCinematicFramingNode setClientApplicationID:];
-[BWCinematicFramingNode isRegionOfInterestForCameraControlsFeedbackEnabled];
-[BWCinematicFramingNode cinematicFramingControls];
-[BWCinematicFramingNode didChangeCenterStageRectOfInterest:];
-[BWCinematicFramingNode regionOfInterestForCameraControlsChangedHandler];
-[BWCinematicFramingNode handleDroppedSample:forInput:];
-[BWCinematicFramingNode performOneShotFraming];
-[BWCinematicFramingNode cinematicFramingControlMode];
-[BWCinematicFramingNode resetFraming];
-[BWCinematicFramingNode panWithTranslation:];
-[BWCinematicFramingNode videoCaptureOutput];
-[BWCinematicFramingNode multipleFacesDetectedCumulativeTime];
-[BWCinematicFramingNode nodeSubType];
-[BWCinematicFramingNode setCinematicFramingControlMode:];
-[BWCinematicFramingNode regionOfInterestForCameraControls];
-[BWCinematicFramingNode singleFaceDetectedCumulativeTime];
-[BWCinematicFramingNode restrictCenterStageFieldOfViewToWide:];
-[BWCinematicFramingNode didSelectFormat:forInput:];
-[BWCinematicFramingNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWCinematicFramingNode nodeType];
-[BWCinematicFramingNode clientApplicationID];
-[BWCinematicFramingNode copyCameraStatesForPTS:];
-[BWCinematicFramingNode detectionMetadataInputsByPortType];
-[BWCinematicFramingNode didReachEndOfDataForInput:];
-[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:downStreamRequires10BitPixelFormat:];
-[BWCinematicFramingNode manualFramingVideoZoomFactor];
-[BWCinematicFramingNode setManualFramingVideoZoomFactor:];
-[BWCinematicFramingNode videoCaptureInputsByPortType];
```
