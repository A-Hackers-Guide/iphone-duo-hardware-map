# `MTLPrimitiveAccelerationStructureDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureDescriptor`
- 6 instance variables, 6 properties, 18 instance methods, 1 class methods

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

## Class methods

```
+[MTLPrimitiveAccelerationStructureDescriptor descriptor];
```

## Instance methods

```
-[MTLPrimitiveAccelerationStructureDescriptor init];
-[MTLPrimitiveAccelerationStructureDescriptor dealloc];
-[MTLPrimitiveAccelerationStructureDescriptor type];
-[MTLPrimitiveAccelerationStructureDescriptor hash];
-[MTLPrimitiveAccelerationStructureDescriptor copyWithZone:];
-[MTLPrimitiveAccelerationStructureDescriptor isEqual:];
-[MTLPrimitiveAccelerationStructureDescriptor motionStartTime];
-[MTLPrimitiveAccelerationStructureDescriptor geometryDescriptors];
-[MTLPrimitiveAccelerationStructureDescriptor motionEndBorderMode];
-[MTLPrimitiveAccelerationStructureDescriptor motionEndTime];
-[MTLPrimitiveAccelerationStructureDescriptor motionKeyframeCount];
-[MTLPrimitiveAccelerationStructureDescriptor motionStartBorderMode];
-[MTLPrimitiveAccelerationStructureDescriptor setGeometryDescriptors:];
-[MTLPrimitiveAccelerationStructureDescriptor setMotionEndBorderMode:];
-[MTLPrimitiveAccelerationStructureDescriptor setMotionEndTime:];
-[MTLPrimitiveAccelerationStructureDescriptor setMotionKeyframeCount:];
-[MTLPrimitiveAccelerationStructureDescriptor setMotionStartBorderMode:];
-[MTLPrimitiveAccelerationStructureDescriptor setMotionStartTime:];
```
