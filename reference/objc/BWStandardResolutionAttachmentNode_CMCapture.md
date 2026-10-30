# `BWStandardResolutionAttachmentNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 5 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _formatDescription;
^{OpaqueVTPixelTransferSession=} _transferSession;
@"<BWPixelBufferProvider>" _pixelBufferProvider;
{?="width"i"height"i} _standardResolutionDimensions;
@"NSString" _standardResAttachedMediaKey;
```

## Class methods

```
+[BWStandardResolutionAttachmentNode initialize];
```

## Instance methods

```
-[BWStandardResolutionAttachmentNode prepareForCurrentConfigurationToBecomeLive];
-[BWStandardResolutionAttachmentNode renderSampleBuffer:forInput:];
-[BWStandardResolutionAttachmentNode dealloc];
-[BWStandardResolutionAttachmentNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWStandardResolutionAttachmentNode didReachEndOfDataForConfigurationID:input:];
-[BWStandardResolutionAttachmentNode nodeSubType];
-[BWStandardResolutionAttachmentNode handleNodeError:forInput:];
-[BWStandardResolutionAttachmentNode nodeType];
-[BWStandardResolutionAttachmentNode initWithStandardResolutionAttachedMediaKey:];
```
