# `MTLComputePassDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLComputePassDescriptor`
- 1 instance variables, 3 properties, 15 instance methods, 1 class methods

## Instance variables

```
{MTLComputePassDescriptorPrivate="dispatchType"Q"sampleBufferAttachments"@"MTLComputePassSampleBufferAttachmentDescriptorArrayInternal""substreamCount"I"allowCommandEncoderCoalescing"B"usedForRaytracingEmulation"B} _private;
```

## Properties

```
@property (TI,N) substreamCount;
@property (TB,N) allowCommandEncoderCoalescing;
@property (TB,N) usedForRaytracingEmulation;
```

## Class methods

```
+[MTLComputePassDescriptorInternal computePassDescriptor];
```

## Instance methods

```
-[MTLComputePassDescriptorInternal init];
-[MTLComputePassDescriptorInternal sampleBufferAttachments];
-[MTLComputePassDescriptorInternal dealloc];
-[MTLComputePassDescriptorInternal _descriptorPrivate];
-[MTLComputePassDescriptorInternal dispatchType];
-[MTLComputePassDescriptorInternal hash];
-[MTLComputePassDescriptorInternal copyWithZone:];
-[MTLComputePassDescriptorInternal isEqual:];
-[MTLComputePassDescriptorInternal allowCommandEncoderCoalescing];
-[MTLComputePassDescriptorInternal setAllowCommandEncoderCoalescing:];
-[MTLComputePassDescriptorInternal setDispatchType:];
-[MTLComputePassDescriptorInternal setSubstreamCount:];
-[MTLComputePassDescriptorInternal setUsedForRaytracingEmulation:];
-[MTLComputePassDescriptorInternal substreamCount];
-[MTLComputePassDescriptorInternal usedForRaytracingEmulation];
```
