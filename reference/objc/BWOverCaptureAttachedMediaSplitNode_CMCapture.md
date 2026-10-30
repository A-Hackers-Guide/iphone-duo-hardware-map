# `BWOverCaptureAttachedMediaSplitNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWAttachedMediaSplitNode`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"BWNodeOutput" _primaryFrameOutput;
@"BWNodeOutput" _synchronizedSlaveFrameOutput;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_primaryFrameOutput) primaryFrameOutput;
@property (T@"BWNodeOutput",R,N,V_synchronizedSlaveFrameOutput) synchronizedSlaveFrameOutput;
```

## Class methods

```
+[BWOverCaptureAttachedMediaSplitNode initialize];
```

## Instance methods

```
-[BWOverCaptureAttachedMediaSplitNode renderSampleBuffer:forInput:];
-[BWOverCaptureAttachedMediaSplitNode primaryFrameOutput];
-[BWOverCaptureAttachedMediaSplitNode dealloc];
-[BWOverCaptureAttachedMediaSplitNode synchronizedSlaveFrameOutput];
-[BWOverCaptureAttachedMediaSplitNode initWithBackPressureExtraRetainBufferCount:];
```
