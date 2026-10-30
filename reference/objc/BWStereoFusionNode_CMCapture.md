# `BWStereoFusionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 18 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
^? _createSampleBufferProcessorFunction;
^{OpaqueFigSampleBufferProcessor=} _sampleBufferProcessor;
@"NSDictionary" _telephotoSensorIDDictionary;
@"NSDictionary" _cameraInfoByPortType;
@"BWStillImageSettings" _currentStillImageSettings;
@"BWNodeInput" _wideInput;
@"BWNodeInput" _telephotoInput;
@"BWNodeOutput" _defaultOutput;
@"BWNodeOutput" _stereoHDROutput;
B _expectsWideFrame;
B _receivedWideFrame;
B _expectsTelephotoFrame;
B _receivedTelephotoFrame;
B _performSBPProcessing;
@"NSDictionary" _sbpZoomRectangleDictionary;
@"BWNodeInput" _masterInput;
@"NSMutableArray" _nodeErrorsForWide;
@"NSMutableArray" _nodeErrorsForTelephoto;
```

## Properties

```
@property (T@"BWNodeInput",R,N,V_wideInput) wideInput;
@property (T@"BWNodeInput",R,N,V_telephotoInput) telephotoInput;
@property (T@"BWNodeOutput",R,N,V_defaultOutput) defaultOutput;
@property (T@"BWNodeOutput",R,N,V_stereoHDROutput) stereoHDROutput;
```

## Class methods

```
+[BWStereoFusionNode initialize];
```

## Instance methods

```
-[BWStereoFusionNode prepareForCurrentConfigurationToBecomeLive];
-[BWStereoFusionNode renderSampleBuffer:forInput:];
-[BWStereoFusionNode dealloc];
-[BWStereoFusionNode nodeSubType];
-[BWStereoFusionNode didSelectFormat:forInput:];
-[BWStereoFusionNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStereoFusionNode handleNodeError:forInput:];
-[BWStereoFusionNode nodeType];
-[BWStereoFusionNode stereoHDROutput];
-[BWStereoFusionNode _initWithTelephotoSensorIDDictionary:cameraInfoByPortType:sbpCreationFunction:treatSoftErrorsAsHardErrors:];
-[BWStereoFusionNode attachesInputBracketToOutputSampleBuffer];
-[BWStereoFusionNode defaultOutput];
-[BWStereoFusionNode didReachEndOfDataForInput:];
-[BWStereoFusionNode initWithTelephotoSensorIDDictionary:cameraInfoByPortType:];
-[BWStereoFusionNode isCaptureRequestStateReset];
-[BWStereoFusionNode sampleBufferProcessor];
-[BWStereoFusionNode setAttachesInputBracketToOutputSampleBuffer:];
-[BWStereoFusionNode telephotoInput];
-[BWStereoFusionNode wideInput];
```
