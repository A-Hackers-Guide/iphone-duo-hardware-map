# `BWMetadataSynchronizerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _syncMetadataByPortType;
@"NSArray" _propagateSampleBufferAttachmentKeys;
@"NSArray" _propagateSampleBufferMetadataDictKeys;
@"NSArray" _syncOnlyIfMetadataEnabledForKeys;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
^{?=@B^{opaqueCMSimpleQueue}{?=qiIq}} _inputsStorage;
```

## Class methods

```
+[BWMetadataSynchronizerNode initialize];
```

## Instance methods

```
-[BWMetadataSynchronizerNode renderSampleBuffer:forInput:];
-[BWMetadataSynchronizerNode dealloc];
-[BWMetadataSynchronizerNode initWithArraysOfMetadataInputs:propagateSampleBufferAttachmentKeys:propagateSampleBufferMetadataDictKeys:syncMetadataByPortType:syncOnlyIfMetadataEnabledForKeys:];
-[BWMetadataSynchronizerNode handleDroppedSample:forInput:];
-[BWMetadataSynchronizerNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWMetadataSynchronizerNode didReachEndOfDataForConfigurationID:input:];
-[BWMetadataSynchronizerNode nodeSubType];
-[BWMetadataSynchronizerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWMetadataSynchronizerNode handleNodeError:forInput:];
-[BWMetadataSynchronizerNode nodeType];
```
