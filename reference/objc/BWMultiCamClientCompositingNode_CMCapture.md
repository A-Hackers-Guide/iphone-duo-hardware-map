# `BWMultiCamClientCompositingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 19 instance variables, 1 properties, 13 instance methods, 1 class methods

## Instance variables

```
i _indexOfInputProvidingOutputSampleBuffer;
s _compositingStrategy;
B _gainMapSupported;
@? _clientCompositingCallback;
@"BWStillImageSettings" _stillImageSettings;
@"FigCaptureMovieFileRecordingSettings" _movieSettings;
@"BWPairedBufferSynchronizer" _bufferSynchronizer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stillsInputLock;
^{opaqueCMSampleBuffer=} _primaryStillSampleBuffer;
^{opaqueCMSampleBuffer=} _secondaryStillSampleBuffer;
@"BWNodeError" _receivedNodeError;
@"BWPixelBufferPool" _outputPixelBufferPool;
^{opaqueCMFormatDescription=} _outputSampleBufferFormatDescription;
@"BWPixelBufferPool" _outputGainMapPixelBufferPool;
^{opaqueCMFormatDescription=} _outputGainMapSampleBufferFormatDescription;
@"BWNodeOutput" _compositionPictureInPictureRectMetadataOutput;
^{opaqueCMFormatDescription=} _compositionPictureInPictureRectMetadataFormatDescription;
I _compositionPictureInPictureRectMetadataLocalID;
f _thresholdToRemovePrimaryBufferDetectedFacesObscuredByPIP;
```

## Properties

```
@property (T@"BWNodeOutput",R,V_compositionPictureInPictureRectMetadataOutput) compositionPictureInPictureRectMetadataOutput;
```

## Class methods

```
+[BWMultiCamClientCompositingNode initialize];
```

## Instance methods

```
-[BWMultiCamClientCompositingNode renderSampleBuffer:forInput:];
-[BWMultiCamClientCompositingNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWMultiCamClientCompositingNode dealloc];
-[BWMultiCamClientCompositingNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWMultiCamClientCompositingNode handleDroppedSample:forInput:];
-[BWMultiCamClientCompositingNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWMultiCamClientCompositingNode nodeSubType];
-[BWMultiCamClientCompositingNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWMultiCamClientCompositingNode handleNodeError:forInput:];
-[BWMultiCamClientCompositingNode nodeType];
-[BWMultiCamClientCompositingNode compositionPictureInPictureRectMetadataOutput];
-[BWMultiCamClientCompositingNode didReachEndOfDataForInput:];
-[BWMultiCamClientCompositingNode initWithIndexOfInputProvidingOutputSampleBuffer:compositingStrategy:gainMapSupported:clientCompositingCallback:];
```
