# `BWFocusSegmentationMaskConverterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWFigVideoCaptureDeviceContinuousAutoFocusTrackingChangedDelegate`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"BWNodeOutput" _focusTrackedObjectsOutput;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rectOfInterest;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _configurationLock;
B _subjectAcquired;
i _subjectNotAcquiredFrameCount;
@? _subjectAcquiredChangedHandler;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_focusTrackedObjectsOutput) focusTrackedObjectsOutput;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) rectOfInterest;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWFocusSegmentationMaskConverterNode initialize];
```

## Instance methods

```
-[BWFocusSegmentationMaskConverterNode renderSampleBuffer:forInput:];
-[BWFocusSegmentationMaskConverterNode dealloc];
-[BWFocusSegmentationMaskConverterNode setRectOfInterest:];
-[BWFocusSegmentationMaskConverterNode didReachEndOfDataForConfigurationID:input:];
-[BWFocusSegmentationMaskConverterNode rectOfInterest];
-[BWFocusSegmentationMaskConverterNode nodeSubType];
-[BWFocusSegmentationMaskConverterNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWFocusSegmentationMaskConverterNode nodeType];
-[BWFocusSegmentationMaskConverterNode _correctRectangleInFocusTrackedObject:fromFocusSegmentationMaskSampleBuffer:];
-[BWFocusSegmentationMaskConverterNode _createFocusTrackedObjectsSampleBufferFromSourceSampleBuffer:];
-[BWFocusSegmentationMaskConverterNode _createOutputSampleBufferForSourceSampleBuffer:focusTrackedObject:focusSegmentationMask:];
-[BWFocusSegmentationMaskConverterNode _updateSubjectAcquiredState:];
-[BWFocusSegmentationMaskConverterNode didStopContinuousAutoFocusTracking];
-[BWFocusSegmentationMaskConverterNode focusTrackedObjectsOutput];
-[BWFocusSegmentationMaskConverterNode initWithSubjectAcquiredChangedHandler:];
```
