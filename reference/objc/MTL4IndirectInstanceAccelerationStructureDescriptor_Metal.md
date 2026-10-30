# `MTL4IndirectInstanceAccelerationStructureDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureDescriptor`
- 11 instance variables, 11 properties, 29 instance methods, 0 class methods

## Instance variables

```
Q _maxInstanceCount;
Q _instanceDescriptorType;
Q _instanceDescriptorStride;
Q _maxMotionTransformCount;
q _motionTransformType;
Q _motionTransformStride;
q _instanceTransformationMatrixLayout;
{MTL4BufferRange="bufferAddress"Q"length"Q} _instanceDescriptorBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _instanceCountBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _motionTransformBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _motionTransformCountBuffer;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_instanceDescriptorBuffer) instanceDescriptorBuffer;
@property (TQ,N,V_instanceDescriptorStride) instanceDescriptorStride;
@property (TQ,N,V_maxInstanceCount) maxInstanceCount;
@property (T{MTL4BufferRange=QQ},N,V_instanceCountBuffer) instanceCountBuffer;
@property (TQ,N,V_instanceDescriptorType) instanceDescriptorType;
@property (T{MTL4BufferRange=QQ},N,V_motionTransformBuffer) motionTransformBuffer;
@property (TQ,N,V_maxMotionTransformCount) maxMotionTransformCount;
@property (T{MTL4BufferRange=QQ},N,V_motionTransformCountBuffer) motionTransformCountBuffer;
@property (Tq,N,V_instanceTransformationMatrixLayout) instanceTransformationMatrixLayout;
@property (Tq,N,V_motionTransformType) motionTransformType;
@property (TQ,N,V_motionTransformStride) motionTransformStride;
```

## Instance methods

```
-[MTL4IndirectInstanceAccelerationStructureDescriptor init];
-[MTL4IndirectInstanceAccelerationStructureDescriptor dealloc];
-[MTL4IndirectInstanceAccelerationStructureDescriptor type];
-[MTL4IndirectInstanceAccelerationStructureDescriptor hash];
-[MTL4IndirectInstanceAccelerationStructureDescriptor copyWithZone:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor isEqual:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor instanceCountBuffer];
-[MTL4IndirectInstanceAccelerationStructureDescriptor instanceDescriptorBuffer];
-[MTL4IndirectInstanceAccelerationStructureDescriptor instanceDescriptorStride];
-[MTL4IndirectInstanceAccelerationStructureDescriptor instanceDescriptorType];
-[MTL4IndirectInstanceAccelerationStructureDescriptor instanceTransformationMatrixLayout];
-[MTL4IndirectInstanceAccelerationStructureDescriptor isInstanceDescriptor];
-[MTL4IndirectInstanceAccelerationStructureDescriptor maxInstanceCount];
-[MTL4IndirectInstanceAccelerationStructureDescriptor maxMotionTransformCount];
-[MTL4IndirectInstanceAccelerationStructureDescriptor motionTransformBuffer];
-[MTL4IndirectInstanceAccelerationStructureDescriptor motionTransformCountBuffer];
-[MTL4IndirectInstanceAccelerationStructureDescriptor motionTransformStride];
-[MTL4IndirectInstanceAccelerationStructureDescriptor motionTransformType];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setInstanceCountBuffer:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setInstanceDescriptorBuffer:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setInstanceDescriptorStride:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setInstanceDescriptorType:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setInstanceTransformationMatrixLayout:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setMaxInstanceCount:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setMaxMotionTransformCount:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setMotionTransformBuffer:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setMotionTransformCountBuffer:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setMotionTransformStride:];
-[MTL4IndirectInstanceAccelerationStructureDescriptor setMotionTransformType:];
```
