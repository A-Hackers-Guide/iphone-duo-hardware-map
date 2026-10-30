# `MTLAccelerationStructurePassDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 1 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"MTLAccelerationStructurePassSampleBufferAttachmentDescriptorArray" _sampleBufferAttachments;
```

## Properties

```
@property (T@"MTLAccelerationStructurePassSampleBufferAttachmentDescriptorArray",R,V_sampleBufferAttachments) sampleBufferAttachments;
```

## Class methods

```
+[MTLAccelerationStructurePassDescriptor allocWithZone:];
+[MTLAccelerationStructurePassDescriptor alloc];
+[MTLAccelerationStructurePassDescriptor accelerationStructurePassDescriptor];
```

## Instance methods

```
-[MTLAccelerationStructurePassDescriptor init];
-[MTLAccelerationStructurePassDescriptor sampleBufferAttachments];
-[MTLAccelerationStructurePassDescriptor dealloc];
-[MTLAccelerationStructurePassDescriptor hash];
-[MTLAccelerationStructurePassDescriptor copyWithZone:];
-[MTLAccelerationStructurePassDescriptor isEqual:];
-[MTLAccelerationStructurePassDescriptor convertToComputePassDescriptor];
-[MTLAccelerationStructurePassDescriptor convertToComputePassDescriptorWithConcurrentDispatch:];
```
