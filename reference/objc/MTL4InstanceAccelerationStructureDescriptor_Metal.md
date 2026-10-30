# `MTL4InstanceAccelerationStructureDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureDescriptor`
- 9 instance variables, 9 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _instanceCount;
Q _motionTransformCount;
q _instanceTransformationMatrixLayout;
q _motionTransformType;
Q _motionTransformStride;
Q _instanceDescriptorType;
Q _instanceDescriptorStride;
{MTL4BufferRange="bufferAddress"Q"length"Q} _instanceDescriptorBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _motionTransformBuffer;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_instanceDescriptorBuffer) instanceDescriptorBuffer;
@property (TQ,N,V_instanceDescriptorStride) instanceDescriptorStride;
@property (TQ,N,V_instanceCount) instanceCount;
@property (TQ,N,V_instanceDescriptorType) instanceDescriptorType;
@property (T{MTL4BufferRange=QQ},N,V_motionTransformBuffer) motionTransformBuffer;
@property (TQ,N,V_motionTransformCount) motionTransformCount;
@property (Tq,N,V_instanceTransformationMatrixLayout) instanceTransformationMatrixLayout;
@property (Tq,N,V_motionTransformType) motionTransformType;
@property (TQ,N,V_motionTransformStride) motionTransformStride;
```

## Instance methods

```
-[MTL4InstanceAccelerationStructureDescriptor setInstanceCount:];
-[MTL4InstanceAccelerationStructureDescriptor init];
-[MTL4InstanceAccelerationStructureDescriptor instanceCount];
-[MTL4InstanceAccelerationStructureDescriptor dealloc];
-[MTL4InstanceAccelerationStructureDescriptor type];
-[MTL4InstanceAccelerationStructureDescriptor hash];
-[MTL4InstanceAccelerationStructureDescriptor copyWithZone:];
-[MTL4InstanceAccelerationStructureDescriptor isEqual:];
-[MTL4InstanceAccelerationStructureDescriptor instanceDescriptorBuffer];
-[MTL4InstanceAccelerationStructureDescriptor instanceDescriptorStride];
-[MTL4InstanceAccelerationStructureDescriptor instanceDescriptorType];
-[MTL4InstanceAccelerationStructureDescriptor instanceTransformationMatrixLayout];
-[MTL4InstanceAccelerationStructureDescriptor isInstanceDescriptor];
-[MTL4InstanceAccelerationStructureDescriptor motionTransformBuffer];
-[MTL4InstanceAccelerationStructureDescriptor motionTransformCount];
-[MTL4InstanceAccelerationStructureDescriptor motionTransformStride];
-[MTL4InstanceAccelerationStructureDescriptor motionTransformType];
-[MTL4InstanceAccelerationStructureDescriptor setInstanceDescriptorBuffer:];
-[MTL4InstanceAccelerationStructureDescriptor setInstanceDescriptorStride:];
-[MTL4InstanceAccelerationStructureDescriptor setInstanceDescriptorType:];
-[MTL4InstanceAccelerationStructureDescriptor setInstanceTransformationMatrixLayout:];
-[MTL4InstanceAccelerationStructureDescriptor setMotionTransformBuffer:];
-[MTL4InstanceAccelerationStructureDescriptor setMotionTransformCount:];
-[MTL4InstanceAccelerationStructureDescriptor setMotionTransformStride:];
-[MTL4InstanceAccelerationStructureDescriptor setMotionTransformType:];
```
