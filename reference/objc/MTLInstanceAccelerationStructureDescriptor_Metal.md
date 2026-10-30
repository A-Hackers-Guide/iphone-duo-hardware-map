# `MTLInstanceAccelerationStructureDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureDescriptor`
- 13 instance variables, 12 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _overriddenInstanceDescriptorStride;
Q _instanceDescriptorStride;
@"<MTLBuffer>" _instanceDescriptorBuffer;
Q _instanceDescriptorBufferOffset;
Q _instanceCount;
@"NSArray" _instancedAccelerationStructures;
@"<MTLBuffer>" _motionTransformBuffer;
Q _motionTransformBufferOffset;
Q _motionTransformCount;
q _instanceTransformationMatrixLayout;
q _motionTransformType;
Q _motionTransformStride;
Q _instanceDescriptorType;
```

## Properties

```
@property (T@"<MTLBuffer>",&,N,V_instanceDescriptorBuffer) instanceDescriptorBuffer;
@property (TQ,N,V_instanceDescriptorBufferOffset) instanceDescriptorBufferOffset;
@property (TQ,N) instanceDescriptorStride;
@property (TQ,N,V_instanceCount) instanceCount;
@property (T@"NSArray",&,N,V_instancedAccelerationStructures) instancedAccelerationStructures;
@property (TQ,N,V_instanceDescriptorType) instanceDescriptorType;
@property (T@"<MTLBuffer>",&,N,V_motionTransformBuffer) motionTransformBuffer;
@property (TQ,N,V_motionTransformBufferOffset) motionTransformBufferOffset;
@property (TQ,N,V_motionTransformCount) motionTransformCount;
@property (Tq,N,V_instanceTransformationMatrixLayout) instanceTransformationMatrixLayout;
@property (Tq,N,V_motionTransformType) motionTransformType;
@property (TQ,N,V_motionTransformStride) motionTransformStride;
```

## Class methods

```
+[MTLInstanceAccelerationStructureDescriptor descriptor];
```

## Instance methods

```
-[MTLInstanceAccelerationStructureDescriptor setInstanceCount:];
-[MTLInstanceAccelerationStructureDescriptor init];
-[MTLInstanceAccelerationStructureDescriptor instanceCount];
-[MTLInstanceAccelerationStructureDescriptor dealloc];
-[MTLInstanceAccelerationStructureDescriptor type];
-[MTLInstanceAccelerationStructureDescriptor hash];
-[MTLInstanceAccelerationStructureDescriptor copyWithZone:];
-[MTLInstanceAccelerationStructureDescriptor isEqual:];
-[MTLInstanceAccelerationStructureDescriptor setMotionTransformBufferOffset:];
-[MTLInstanceAccelerationStructureDescriptor instancedAccelerationStructures];
-[MTLInstanceAccelerationStructureDescriptor instanceDescriptorBuffer];
-[MTLInstanceAccelerationStructureDescriptor instanceDescriptorBufferOffset];
-[MTLInstanceAccelerationStructureDescriptor instanceDescriptorStride];
-[MTLInstanceAccelerationStructureDescriptor instanceDescriptorType];
-[MTLInstanceAccelerationStructureDescriptor instanceTransformationMatrixLayout];
-[MTLInstanceAccelerationStructureDescriptor isInstanceDescriptor];
-[MTLInstanceAccelerationStructureDescriptor motionTransformBuffer];
-[MTLInstanceAccelerationStructureDescriptor motionTransformBufferOffset];
-[MTLInstanceAccelerationStructureDescriptor motionTransformCount];
-[MTLInstanceAccelerationStructureDescriptor motionTransformStride];
-[MTLInstanceAccelerationStructureDescriptor motionTransformType];
-[MTLInstanceAccelerationStructureDescriptor setInstanceDescriptorBuffer:];
-[MTLInstanceAccelerationStructureDescriptor setInstanceDescriptorBufferOffset:];
-[MTLInstanceAccelerationStructureDescriptor setInstanceDescriptorStride:];
-[MTLInstanceAccelerationStructureDescriptor setInstanceDescriptorType:];
-[MTLInstanceAccelerationStructureDescriptor setInstanceTransformationMatrixLayout:];
-[MTLInstanceAccelerationStructureDescriptor setInstancedAccelerationStructures:];
-[MTLInstanceAccelerationStructureDescriptor setMotionTransformBuffer:];
-[MTLInstanceAccelerationStructureDescriptor setMotionTransformCount:];
-[MTLInstanceAccelerationStructureDescriptor setMotionTransformStride:];
-[MTLInstanceAccelerationStructureDescriptor setMotionTransformType:];
```
