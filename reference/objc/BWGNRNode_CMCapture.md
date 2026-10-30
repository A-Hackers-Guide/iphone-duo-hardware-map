# `BWGNRNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 32 instance variables, 0 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _sisEnabled;
B _oisEnabled;
B _hdrEnabled;
B _processingLTMHDRFusion;
@"BWNodeOutput" _bravoHDRDisparityOutput;
^? _createSampleBufferProcessorFunction;
^{OpaqueFigSampleBufferProcessor=} _sampleBufferProcessor;
@"NSString" _portType;
@"NSString" _sensorID;
@"NSDictionary" _sensorIDDictionary;
@"NSString" _telephotoPortType;
@"NSString" _telephotoSensorID;
@"NSDictionary" _telephotoSensorIDDictionary;
@"BWStillImageSettings" _currentStillImageSettings;
i _processingType;
B _clientExpectsPreBracketFrame;
B _expectsPreBracketFrame;
B _receivedPreBracketFrame;
I _expectedFrameCount;
I _receivedFrameCount;
B _receivedAllFrames;
i _receivedReferenceFrameBracketedCaptureSequenceNumber;
i _gnrFusionReferenceFrameBracketedCaptureSequenceNumber;
B _processingHDREV0BracketFrame;
i _hdrEV0BracketCaptureIdentifier;
i _hdrDisparityBracketedCaptureSequenceNumber;
@"NSMutableDictionary" _inputAttachedMedia;
^{opaqueCMSampleBuffer=} _collectedUnprocessedPreBracketHDR;
@"FigCapturePixelConverter" _stereoFusedGNRHDRPixelConverter;
q _previouslyCompletedFusionSettingsID;
B _usesHDRPreBracketFrameForErrorRecoveryDownstream;
B _allowedToModifyInputBuffers;
```

## Class methods

```
+[BWGNRNode initialize];
```

## Instance methods

```
-[BWGNRNode prepareForCurrentConfigurationToBecomeLive];
-[BWGNRNode renderSampleBuffer:forInput:];
-[BWGNRNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWGNRNode dealloc];
-[BWGNRNode nodeSubType];
-[BWGNRNode didSelectFormat:forInput:];
-[BWGNRNode handleNodeError:forInput:];
-[BWGNRNode nodeType];
-[BWGNRNode setAllowedToModifyInputBuffers:];
-[BWGNRNode _initWithSISEnabled:OISEnabled:LTMHDREnabled:processingLTMHDRFusion:portType:sensorID:sensorIDDictionary:telephotoPortType:telephotoSensorID:telephotoSensorIDDictionary:sbpCreationFunction:treatSoftErrorsAsHardErrors:];
-[BWGNRNode allowedToModifyInputBuffers];
-[BWGNRNode attachesInputBracketToOutputSampleBuffer];
-[BWGNRNode initWithSISEnabled:OISEnabled:LTMHDREnabled:processingLTMHDRFusion:portType:sensorID:sensorIDDictionary:telephotoPortType:telephotoSensorID:telephotoSensorIDDictionary:];
-[BWGNRNode setAttachesInputBracketToOutputSampleBuffer:];
-[BWGNRNode setUsesHDRPreBracketFrameForErrorRecoveryDownstream:];
-[BWGNRNode usesHDRPreBracketFrameForErrorRecoveryDownstream];
```
