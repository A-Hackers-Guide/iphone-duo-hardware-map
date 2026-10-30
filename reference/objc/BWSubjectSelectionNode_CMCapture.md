# `BWSubjectSelectionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWFigVideoCaptureDeviceSubjectSelectionDelegate`
- 19 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _videoCaptureInputsByPortType;
@"NSMutableDictionary" _videoCaptureOutputsByPortType;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
@"NSDictionary" _cameraInfoByPortType;
{?="width"i"height"i} _outputDimensions;
@"SubjectSelectionSession" _subjectSelectionSession;
@"NSObject<OS_dispatch_queue>" _subjectSelectionSessionCreatorQueue;
I _subjectSelectionSessionCreationToken;
@"BWDeviceOrientationMonitor" _deviceOrientationMonitor;
I _minLuxLevelNeeded;
B _deviceOrientationCorrectionEnabled;
@"NSArray" _portTypes;
i _endOfDataInputsCount;
B _cameraHasDistortionCoefficients;
B _cameraHasCalibrationValidMaxRadius;
i _centerStageFramingMode;
B _gazeSelectionEnabled;
```

## Properties

```
@property (T@"NSDictionary",R,N) videoCaptureInputsByPortType;
@property (T@"NSDictionary",R,N) videoCaptureOutputsByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSubjectSelectionNode initialize];
```

## Instance methods

```
-[BWSubjectSelectionNode prepareForCurrentConfigurationToBecomeLive];
-[BWSubjectSelectionNode renderSampleBuffer:forInput:];
-[BWSubjectSelectionNode dealloc];
-[BWSubjectSelectionNode didChangeCenterStageFramingMode:];
-[BWSubjectSelectionNode nodeSubType];
-[BWSubjectSelectionNode didSelectFormat:forInput:];
-[BWSubjectSelectionNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWSubjectSelectionNode nodeType];
-[BWSubjectSelectionNode didReachEndOfDataForInput:];
-[BWSubjectSelectionNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:portTypes:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageFramingMode:gazeSelectionEnabled:];
-[BWSubjectSelectionNode videoCaptureInputsByPortType];
-[BWSubjectSelectionNode videoCaptureOutputsByPortType];
```
