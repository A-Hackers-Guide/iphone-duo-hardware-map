# `BWAttachedMediaSwapNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 4 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _primaryFormatToAttachedMediaKey;
@"NSString" _attachedMediaKeyToPrimaryFormat;
@"NSArray" _sampleBufferAttachmentsToTransfer;
B _generatesDroppedSampleMarkerBuffers;
```

## Class methods

```
+[BWAttachedMediaSwapNode initialize];
```

## Instance methods

```
-[BWAttachedMediaSwapNode renderSampleBuffer:forInput:];
-[BWAttachedMediaSwapNode dealloc];
-[BWAttachedMediaSwapNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWAttachedMediaSwapNode nodeSubType];
-[BWAttachedMediaSwapNode initWithPrimaryFormatToAttachedMediaKey:attachedMediaKeyToPrimaryFormat:sampleBufferAttachmentsToTransfer:generatesDroppedSampleMarkerBuffers:];
```
