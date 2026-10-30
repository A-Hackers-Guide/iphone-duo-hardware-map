# `MTLIndirectInstanceAccelerationStructureDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureDescriptor`
- 16 instance variables, 15 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _overriddenInstanceDescriptorStride;
Q _instanceDescriptorStride;
@"<MTLBuffer>" _instanceDescriptorBuffer;
Q _instanceDescriptorBufferOffset;
Q _maxInstanceCount;
@"<MTLBuffer>" _instanceCountBuffer;
Q _instanceCountBufferOffset;
Q _instanceDescriptorType;
@"<MTLBuffer>" _motionTransformBuffer;
Q _motionTransformBufferOffset;
Q _maxMotionTransformCount;
q _motionTransformType;
Q _motionTransformStride;
@"<MTLBuffer>" _motionTransformCountBuffer;
Q _motionTransformCountBufferOffset;
q _instanceTransformationMatrixLayout;
```

## Properties

```
@property (T@"<MTLBuffer>",&,N,V_instanceDescriptorBuffer) instanceDescriptorBuffer;
@property (TQ,N,V_instanceDescriptorBufferOffset) instanceDescriptorBufferOffset;
@property (TQ,N) instanceDescriptorStride;
@property (TQ,N,V_maxInstanceCount) maxInstanceCount;
@property (T@"<MTLBuffer>",&,N,V_instanceCountBuffer) instanceCountBuffer;
@property (TQ,N,V_instanceCountBufferOffset) instanceCountBufferOffset;
@property (TQ,N,V_instanceDescriptorType) instanceDescriptorType;
@property (T@"<MTLBuffer>",&,N,V_motionTransformBuffer) motionTransformBuffer;
@property (TQ,N,V_motionTransformBufferOffset) motionTransformBufferOffset;
@property (TQ,N,V_maxMotionTransformCount) maxMotionTransformCount;
@property (T@"<MTLBuffer>",&,N,V_motionTransformCountBuffer) motionTransformCountBuffer;
@property (TQ,N,V_motionTransformCountBufferOffset) motionTransformCountBufferOffset;
@property (Tq,N,V_instanceTransformationMatrixLayout) instanceTransformationMatrixLayout;
@property (Tq,N,V_motionTransformType) motionTransformType;
@property (TQ,N,V_motionTransformStride) motionTransformStride;
```

## Class methods

```
+[MTLIndirectInstanceAccelerationStructureDescriptor descriptor];
```

## Instance methods

```
-[MTLIndirectInstanceAccelerationStructureDescriptor init];
-[MTLIndirectInstanceAccelerationStructureDescriptor dealloc];
-[MTLIndirectInstanceAccelerationStructureDescriptor type];
-[MTLIndirectInstanceAccelerationStructureDescriptor hash];
-[MTLIndirectInstanceAccelerationStructureDescriptor copyWithZone:];
-[MTLIndirectInstanceAccelerationStructureDescriptor isEqual:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMotionTransformBufferOffset:];
-[MTLIndirectInstanceAccelerationStructureDescriptor instanceCountBuffer];
-[MTLIndirectInstanceAccelerationStructureDescriptor instanceCountBufferOffset];
-[MTLIndirectInstanceAccelerationStructureDescriptor instanceDescriptorBuffer];
-[MTLIndirectInstanceAccelerationStructureDescriptor instanceDescriptorBufferOffset];
-[MTLIndirectInstanceAccelerationStructureDescriptor instanceDescriptorStride];
-[MTLIndirectInstanceAccelerationStructureDescriptor instanceDescriptorType];
-[MTLIndirectInstanceAccelerationStructureDescriptor instanceTransformationMatrixLayout];
-[MTLIndirectInstanceAccelerationStructureDescriptor isInstanceDescriptor];
-[MTLIndirectInstanceAccelerationStructureDescriptor maxInstanceCount];
-[MTLIndirectInstanceAccelerationStructureDescriptor maxMotionTransformCount];
-[MTLIndirectInstanceAccelerationStructureDescriptor motionTransformBuffer];
-[MTLIndirectInstanceAccelerationStructureDescriptor motionTransformBufferOffset];
-[MTLIndirectInstanceAccelerationStructureDescriptor motionTransformCountBuffer];
-[MTLIndirectInstanceAccelerationStructureDescriptor motionTransformCountBufferOffset];
-[MTLIndirectInstanceAccelerationStructureDescriptor motionTransformStride];
-[MTLIndirectInstanceAccelerationStructureDescriptor motionTransformType];
-[MTLIndirectInstanceAccelerationStructureDescriptor setInstanceCountBuffer:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setInstanceCountBufferOffset:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setInstanceDescriptorBuffer:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setInstanceDescriptorBufferOffset:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setInstanceDescriptorStride:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setInstanceDescriptorType:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setInstanceTransformationMatrixLayout:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMaxInstanceCount:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMaxMotionTransformCount:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMotionTransformBuffer:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMotionTransformCountBuffer:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMotionTransformCountBufferOffset:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMotionTransformStride:];
-[MTLIndirectInstanceAccelerationStructureDescriptor setMotionTransformType:];
```
