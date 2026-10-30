# `BWAttachedMediaSplitNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFanOutNode`
- 7 instance variables, 0 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _attachedMediaKeys;
@"NSMutableDictionary" _attachedMediaFormatDescriptions;
@"NSArray" _attachedMediaToPropagateToPrimaryOutput;
@"NSMutableSet" _disabledAttachedMediaKeys;
i _numOutputs;
B _emitsNodeErrorsForMissingAttachedMedia;
B _emitsDroppedSampleForMissingAttachedMedia;
```

## Class methods

```
+[BWAttachedMediaSplitNode initialize];
```

## Instance methods

```
-[BWAttachedMediaSplitNode renderSampleBuffer:forInput:];
-[BWAttachedMediaSplitNode setEmitsNodeErrorsForMissingAttachedMedia:];
-[BWAttachedMediaSplitNode initWithAttachedMediaKeys:attachedMediaToPropagateToPrimaryOutput:];
-[BWAttachedMediaSplitNode dealloc];
-[BWAttachedMediaSplitNode setOutputRenderingEnabled:forAttachedMediaKey:];
-[BWAttachedMediaSplitNode isOutputRenderingEnabledForAttachedMediaKey:];
-[BWAttachedMediaSplitNode setEmitsDroppedSampleForMissingAttachedMedia:];
-[BWAttachedMediaSplitNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWAttachedMediaSplitNode emitsDroppedSampleForMissingAttachedMedia];
-[BWAttachedMediaSplitNode nodeSubType];
-[BWAttachedMediaSplitNode initWithAttachedMediaKeys:];
-[BWAttachedMediaSplitNode didSelectFormat:forInput:];
-[BWAttachedMediaSplitNode emitsNodeErrorsForMissingAttachedMedia];
```
