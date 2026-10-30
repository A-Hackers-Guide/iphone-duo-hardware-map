# `MTL4PrimitiveAccelerationStructureDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureDescriptor`
- 6 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
I _motionStartBorderMode;
I _motionEndBorderMode;
f _motionStartTime;
f _motionEndTime;
@"NSArray" _geometryDescriptors;
Q _motionKeyframeCount;
```

## Properties

```
@property (T@"NSArray",&,N,V_geometryDescriptors) geometryDescriptors;
@property (TI,N,V_motionStartBorderMode) motionStartBorderMode;
@property (TI,N,V_motionEndBorderMode) motionEndBorderMode;
@property (Tf,N,V_motionStartTime) motionStartTime;
@property (Tf,N,V_motionEndTime) motionEndTime;
@property (TQ,N,V_motionKeyframeCount) motionKeyframeCount;
```

## Instance methods

```
-[MTL4PrimitiveAccelerationStructureDescriptor init];
-[MTL4PrimitiveAccelerationStructureDescriptor dealloc];
-[MTL4PrimitiveAccelerationStructureDescriptor type];
-[MTL4PrimitiveAccelerationStructureDescriptor hash];
-[MTL4PrimitiveAccelerationStructureDescriptor copyWithZone:];
-[MTL4PrimitiveAccelerationStructureDescriptor isEqual:];
-[MTL4PrimitiveAccelerationStructureDescriptor motionStartTime];
-[MTL4PrimitiveAccelerationStructureDescriptor geometryDescriptors];
-[MTL4PrimitiveAccelerationStructureDescriptor motionEndBorderMode];
-[MTL4PrimitiveAccelerationStructureDescriptor motionEndTime];
-[MTL4PrimitiveAccelerationStructureDescriptor motionKeyframeCount];
-[MTL4PrimitiveAccelerationStructureDescriptor motionStartBorderMode];
-[MTL4PrimitiveAccelerationStructureDescriptor setGeometryDescriptors:];
-[MTL4PrimitiveAccelerationStructureDescriptor setMotionEndBorderMode:];
-[MTL4PrimitiveAccelerationStructureDescriptor setMotionEndTime:];
-[MTL4PrimitiveAccelerationStructureDescriptor setMotionKeyframeCount:];
-[MTL4PrimitiveAccelerationStructureDescriptor setMotionStartBorderMode:];
-[MTL4PrimitiveAccelerationStructureDescriptor setMotionStartTime:];
```
