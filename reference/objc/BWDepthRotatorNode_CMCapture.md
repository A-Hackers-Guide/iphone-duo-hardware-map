# `BWDepthRotatorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 8 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _outputDepthFormatDescription;
^{opaqueCMFormatDescription=} _outputDYFormatDescription;
I _inputDepthFormat;
{?="width"i"height"i} _inputDepthDimensions;
i _rotationDegrees;
q _bufferSerialNumber;
B _separateDepthComponentsEnabled;
B _depthProvidedAsAttachedMedia;
```

## Class methods

```
+[BWDepthRotatorNode initialize];
```

## Instance methods

```
-[BWDepthRotatorNode renderSampleBuffer:forInput:];
-[BWDepthRotatorNode dealloc];
-[BWDepthRotatorNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWDepthRotatorNode nodeSubType];
-[BWDepthRotatorNode nodeType];
-[BWDepthRotatorNode didReachEndOfDataForInput:];
-[BWDepthRotatorNode initWithRotationDegrees:separateDepthComponentsEnabled:depthProvidedAsAttachedMedia:];
```
