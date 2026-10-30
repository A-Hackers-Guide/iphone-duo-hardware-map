# `BWStillImageDisparitySplitterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 2 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
^@ _outputs;
Q _numberOfOutputs;
```

## Properties

```
@property (T@"BWNodeOutput",R,N) disparityOutput;
@property (T@"BWNodeOutput",R,N) processedOutput;
```

## Class methods

```
+[BWStillImageDisparitySplitterNode initialize];
```

## Instance methods

```
-[BWStillImageDisparitySplitterNode renderSampleBuffer:forInput:];
-[BWStillImageDisparitySplitterNode init];
-[BWStillImageDisparitySplitterNode dealloc];
-[BWStillImageDisparitySplitterNode handleDroppedSample:forInput:];
-[BWStillImageDisparitySplitterNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWStillImageDisparitySplitterNode nodeSubType];
-[BWStillImageDisparitySplitterNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageDisparitySplitterNode handleNodeError:forInput:];
-[BWStillImageDisparitySplitterNode nodeType];
-[BWStillImageDisparitySplitterNode processedOutput];
-[BWStillImageDisparitySplitterNode disparityOutput];
-[BWStillImageDisparitySplitterNode didReachEndOfDataForInput:];
```
