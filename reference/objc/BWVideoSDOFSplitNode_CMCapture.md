# `BWVideoSDOFSplitNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFanOutNode`
- 3 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _originalVideoFormatDescription;
@"BWNodeOutput" _originalOutput;
@"BWNodeOutput" _sdofOutput;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_originalOutput) originalOutput;
@property (T@"BWNodeOutput",R,N,V_sdofOutput) sdofOutput;
```

## Class methods

```
+[BWVideoSDOFSplitNode initialize];
```

## Instance methods

```
-[BWVideoSDOFSplitNode renderSampleBuffer:forInput:];
-[BWVideoSDOFSplitNode originalOutput];
-[BWVideoSDOFSplitNode init];
-[BWVideoSDOFSplitNode dealloc];
-[BWVideoSDOFSplitNode sdofOutput];
-[BWVideoSDOFSplitNode nodeSubType];
```
