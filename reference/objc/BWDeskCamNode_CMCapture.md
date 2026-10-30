# `BWDeskCamNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `DeskCamSessionDelegate`, `BWFigVideoCaptureDeviceOverheadCameraModeChangedDelegate`
- 28 instance variables, 11 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"BWNodeInput" _videoCaptureInput;
@"BWNodeOutput" _videoCaptureOutput;
@"BWNodeInput" _stillImageInput;
@"BWNodeOutput" _stillImageOutput;
@"BWNodeInput" _detectionMetadataInput;
@"BWNodeOutput" _detectionMetadataOutput;
^{opaqueCMFormatDescription=} _outputFormatDescription;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
@"NSDictionary" _cameraInfoByPortType;
{?="width"i"height"i} _outputDimensions;
[2{?="pixelBuffer"^{__CVBuffer}"pts"{?="value"q"timescale"i"flags"I"epoch"q}}] _stillCaptureQueue;
I _stillCaptureEnqueueIndex;
@"DeskCamSession" _deskCamSession;
@"BWDeviceOrientationMonitor" _deviceOrientationMonitor;
@"NSString" _clientApplicationID;
I _minLuxLevelNeeded;
B _stillImageCaptureEnabled;
^{OpaqueVTPixelTransferSession=} _stillImagePixelTransferSession;
i _maxLossyCompressionLevel;
@"NSString" _portType;
i _overheadCameraMode;
@"BWFigVideoCaptureDevice" _captureDevice;
S _numberOfFramesReceivedBeforeFocusUpdate;
S _numberOfFramesReceivedSinceLastFocusUpdate;
f _deskViewCameraZoomFactor;
B _downstreamRequires10BitPixelFormat;
```

## Properties

```
@property (T@"BWNodeInput",R,N,V_videoCaptureInput) videoCaptureInput;
@property (T@"BWNodeOutput",R,N,V_videoCaptureOutput) videoCaptureOutput;
@property (T@"BWNodeInput",R,N,V_stillImageInput) stillImageInput;
@property (T@"BWNodeOutput",R,N,V_stillImageOutput) stillImageOutput;
@property (T@"BWNodeInput",R,N,V_detectionMetadataInput) detectionMetadataInput;
@property (T@"BWNodeOutput",R,N,V_detectionMetadataOutput) detectionMetadataOutput;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWDeskCamNode initialize];
```

## Instance methods

```
-[BWDeskCamNode prepareForCurrentConfigurationToBecomeLive];
-[BWDeskCamNode renderSampleBuffer:forInput:];
-[BWDeskCamNode dealloc];
-[BWDeskCamNode detectionMetadataOutput];
-[BWDeskCamNode setClientApplicationID:];
-[BWDeskCamNode detectionMetadataInput];
-[BWDeskCamNode videoCaptureOutput];
-[BWDeskCamNode nodeSubType];
-[BWDeskCamNode didSelectFormat:forInput:];
-[BWDeskCamNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWDeskCamNode setDeskViewCameraZoomFactor:];
-[BWDeskCamNode stillImageOutput];
-[BWDeskCamNode nodeType];
-[BWDeskCamNode clientApplicationID];
-[BWDeskCamNode stillImageInput];
-[BWDeskCamNode deskViewTrapezoidDidUpdate];
-[BWDeskCamNode didChangeOverheadCameraMode:];
-[BWDeskCamNode didReachEndOfDataForInput:];
-[BWDeskCamNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:downStreamRequires10BitPixelFormat:];
-[BWDeskCamNode videoCaptureInput];
```
