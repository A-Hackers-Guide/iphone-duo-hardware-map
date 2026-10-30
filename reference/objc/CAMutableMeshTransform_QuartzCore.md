# `CAMutableMeshTransform`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMeshTransform`
- 0 instance variables, 4 properties, 16 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",C) depthNormalization;
@property (Ti) subdivisionSteps;
@property (TB) replicatesEdges;
@property (TB) preallocatesBounds;
```

## Class methods

```
+[CAMutableMeshTransform meshTransform];
```

## Instance methods

```
-[CAMutableMeshTransform replaceVertexAtIndex:withVertex:];
-[CAMutableMeshTransform replicatesEdges];
-[CAMutableMeshTransform setDepthNormalization:];
-[CAMutableMeshTransform setPreallocatesBounds:];
-[CAMutableMeshTransform init];
-[CAMutableMeshTransform setReplicatesEdges:];
-[CAMutableMeshTransform removeFaceAtIndex:];
-[CAMutableMeshTransform addVertex:];
-[CAMutableMeshTransform subdivisionSteps];
-[CAMutableMeshTransform depthNormalization];
-[CAMutableMeshTransform removeVertexAtIndex:];
-[CAMutableMeshTransform preallocatesBounds];
-[CAMutableMeshTransform addFace:];
-[CAMutableMeshTransform copyWithZone:];
-[CAMutableMeshTransform replaceFaceAtIndex:withFace:];
-[CAMutableMeshTransform setSubdivisionSteps:];
```
