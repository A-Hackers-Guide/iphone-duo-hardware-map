# `CAMeshTransform`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`, `NSMutableCopying`
- 5 instance variables, 6 properties, 30 instance methods, 4 class methods

## Instance variables

```
^v _impl;
Q _normalization;
q _subdivisionSteps;
B _replicatesEdges;
B _preallocatesBounds;
```

## Properties

```
@property (TQ,R) vertexCount;
@property (TQ,R) faceCount;
@property (T@"NSString",R,C) depthNormalization;
@property (Ti,R) subdivisionSteps;
@property (TB,R) replicatesEdges;
@property (TB,R) preallocatesBounds;
```

## Class methods

```
+[CAMeshTransform supportsSecureCoding];
+[CAMeshTransform CAMLParserStartElement:];
+[CAMeshTransform CAMLParserEndElement:content:];
+[CAMeshTransform meshTransformWithVertexCount:vertices:faceCount:faces:depthNormalization:];
```

## Instance methods

```
-[CAMeshTransform replicatesEdges];
-[CAMeshTransform meshTransformForLayer:];
-[CAMeshTransform mutableCopyWithZone:];
-[CAMeshTransform faceCount];
-[CAMeshTransform init];
-[CAMeshTransform inverseMesh];
-[CAMeshTransform dealloc];
-[CAMeshTransform CA_interpolateValues:::interpolator:];
-[CAMeshTransform initWithVertexCount:vertices:faceCount:faces:depthNormalization:];
-[CAMeshTransform vertexCount];
-[CAMeshTransform CA_copyRenderValue];
-[CAMeshTransform subdividedMesh:];
-[CAMeshTransform _init];
-[CAMeshTransform CA_distanceToValue:];
-[CAMeshTransform _initWithMeshTransform:];
-[CAMeshTransform CA_copyNumericValue:];
-[CAMeshTransform encodeWithCAMLWriter:];
-[CAMeshTransform _data];
-[CAMeshTransform _subdivideToDepth:];
-[CAMeshTransform vertexAtIndex:];
-[CAMeshTransform encodeWithCoder:];
-[CAMeshTransform subdivisionSteps];
-[CAMeshTransform depthNormalization];
-[CAMeshTransform preallocatesBounds];
-[CAMeshTransform initWithCoder:];
-[CAMeshTransform copyWithZone:];
-[CAMeshTransform CA_numericValueCount];
-[CAMeshTransform CA_interpolateValue:byFraction:];
-[CAMeshTransform _constructWithData:];
-[CAMeshTransform faceAtIndex:];
```
