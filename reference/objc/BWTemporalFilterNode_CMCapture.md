# `BWTemporalFilterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 22 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _maxLossyCompressionLevel;
@"BWNodeInput" _videoInput;
^{OpaqueVTTemporalFilterSession=} _mctfSession;
^{opaqueCMSimpleQueue=} _inputSampleBufferQueue;
@"BWNodeOutput" _videoOutput;
B _dumpInputVideo;
B _dumpOutputVideo;
B _forceBypassTemporalFilter;
B _forceEnableTemporalFilter;
^{OpaqueVTPixelTransferSession=} _pixelTransferSession;
{?="framesReceivedCount"Q"framesWithMLVNRAppliedCount"Q"framesWithMCTFAppliedCount"Q"framesDispatchedCount"Q"framesDroppedCount"Q"droppedInFilterSessionCallback"Q"lastFrameWasMLVNRAppliedFrame"B} _frameStats;
B _logMLVNRMetadata;
B _mctfUsesMLVNRPixelBufferAttachments;
@"NSDictionary" _filterSessionConfigurationsByPortType;
@"NSObject<OS_dispatch_queue>" _sampleBufferSerialQueue;
@"NSMutableSet" _enqueueFailedInputSbufPTSValuesList;
B _didReachEODForVideoInput;
B _lowLightBandingMitigationEnabled;
I _liveSessionInputPixelFormat;
I _liveSessionOutputPixelFormat;
i _liveSessionWidth;
i _liveSessionHeight;
```

## Class methods

```
+[BWTemporalFilterNode initialize];
```

## Instance methods

```
-[BWTemporalFilterNode prepareForCurrentConfigurationToBecomeLive];
-[BWTemporalFilterNode renderSampleBuffer:forInput:];
-[BWTemporalFilterNode dealloc];
-[BWTemporalFilterNode hasNonLiveConfigurationChanges];
-[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:];
-[BWTemporalFilterNode nodeSubType];
-[BWTemporalFilterNode didSelectFormat:forInput:];
-[BWTemporalFilterNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWTemporalFilterNode nodeType];
```
