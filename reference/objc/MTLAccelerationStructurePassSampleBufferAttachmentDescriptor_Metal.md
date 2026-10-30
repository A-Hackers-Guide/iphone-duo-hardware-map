# `MTLAccelerationStructurePassSampleBufferAttachmentDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTLCounterSampleBuffer>" _sampleBuffer;
Q _startOfEncoderSampleIndex;
Q _endOfEncoderSampleIndex;
```

## Properties

```
@property (T@"<MTLCounterSampleBuffer>",&,N,V_sampleBuffer) sampleBuffer;
@property (TQ,N,V_startOfEncoderSampleIndex) startOfEncoderSampleIndex;
@property (TQ,N,V_endOfEncoderSampleIndex) endOfEncoderSampleIndex;
```

## Instance methods

```
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor init];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor dealloc];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor hash];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor copyWithZone:];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor isEqual:];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor endOfEncoderSampleIndex];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor sampleBuffer];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor setEndOfEncoderSampleIndex:];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor setSampleBuffer:];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor setStartOfEncoderSampleIndex:];
-[MTLAccelerationStructurePassSampleBufferAttachmentDescriptor startOfEncoderSampleIndex];
```
