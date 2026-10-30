# `BWStillImageStandardResolutionAttachmentTransferNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageNodeConfiguration" _nodeConfiguration;
@"NSMutableDictionary" _inferencesFromStandardResBuffer;
@"NSMutableDictionary" _attachedMediasFromStandardResBuffer;
@"NSMutableDictionary" _attachmentsFromStandardResBuffer;
B _hasAttachmentsFromStandardResBuffer;
^{opaqueCMSampleBuffer=} _enhancedResolutionBuffer;
@"NSString" _lastCaptureRequestIdentifier;
q _lastSettingsID;
{?="width"i"height"i} _standardResBufferDimensions;
```

## Class methods

```
+[BWStillImageStandardResolutionAttachmentTransferNode initialize];
```

## Instance methods

```
-[BWStillImageStandardResolutionAttachmentTransferNode renderSampleBuffer:forInput:];
-[BWStillImageStandardResolutionAttachmentTransferNode dealloc];
-[BWStillImageStandardResolutionAttachmentTransferNode nodeSubType];
-[BWStillImageStandardResolutionAttachmentTransferNode initWithNodeConfiguration:];
-[BWStillImageStandardResolutionAttachmentTransferNode didSelectFormat:forInput:];
-[BWStillImageStandardResolutionAttachmentTransferNode handleNodeError:forInput:];
-[BWStillImageStandardResolutionAttachmentTransferNode nodeType];
```
