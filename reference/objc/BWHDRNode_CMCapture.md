# `BWHDRNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 18 instance variables, 0 properties, 15 instance methods, 1 class methods

## Instance variables

```
^? _createSampleBufferProcessorFunction;
i _clientPID;
@"NSDictionary" _sensorIDDictionary;
^{OpaqueFigSampleBufferProcessor=} _sampleBufferProcessor;
i _bracketCount;
@"NSArray" _exposureValues;
@"BWStillImageSettings" _currentStillImageSettings;
[3^{opaqueCMSampleBuffer}] _pendingBracketBuffers;
B _preBracketedFrameExpected;
B _preBracketedFrameReceived;
@"NSMutableArray" _receivedNodeErrors;
I _emittedFrameOrErrorCount;
B _alwaysRequestsPreBracketedEV0;
B _supportsStereoFusionCaptures;
@"FigCapturePixelConverter" _stereoFusionPixelConverter;
@"BWPixelBufferPool" _telephotoHDREV0DisparityBufferPool;
^{opaqueCMFormatDescription=} _telephotoHDREV0DisparityFormatDescription;
^{OpaqueVTPixelTransferSession=} _telephotoHDREV0DisparityCopySession;
```

## Class methods

```
+[BWHDRNode initialize];
```

## Instance methods

```
-[BWHDRNode prepareForCurrentConfigurationToBecomeLive];
-[BWHDRNode renderSampleBuffer:forInput:];
-[BWHDRNode dealloc];
-[BWHDRNode nodeSubType];
-[BWHDRNode didSelectFormat:forInput:];
-[BWHDRNode handleNodeError:forInput:];
-[BWHDRNode nodeType];
-[BWHDRNode _initWithClientPID:sensorIDDictionary:sbpCreationFunction:];
-[BWHDRNode alwaysRequestsPreBracketedEV0];
-[BWHDRNode attachesInputBracketToOutputSampleBuffer];
-[BWHDRNode initWithClientPID:sensorIDDictionary:];
-[BWHDRNode setAlwaysRequestsPreBracketedEV0:];
-[BWHDRNode setAttachesInputBracketToOutputSampleBuffer:];
-[BWHDRNode setSupportsStereoFusionCaptures:];
-[BWHDRNode supportsStereoFusionCaptures];
```
