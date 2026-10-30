# `_UISimplex`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `NSSecureCoding`, `NSCopying`
- 14 instance variables, 17 properties, 23 instance methods, 2 class methods

## Instance variables

```
^d __points;
{?="metadata"b1} _clean;
i __cggetriWorkspaceSize;
Q __dimensions;
Q __pointCount;
^d __projection;
Q __missingNormalCount;
^d __missingNormals;
^d __facetNormals;
^d __facetNormalOffsets;
^d __incenter;
@"NSArray" __facets;
^d __cggetriWorkspace;
^d __temp;
```

## Properties

```
@property (T^d,R,N,V__projection) _projection;
@property (TQ,R,N,V__missingNormalCount) _missingNormalCount;
@property (T^d,R,N,V__missingNormals) _missingNormals;
@property (T^d,R,N,V__facetNormals) _facetNormals;
@property (T^d,R,N,V__facetNormalOffsets) _facetNormalOffsets;
@property (T^d,R,N,V__incenter) _incenter;
@property (T@"NSArray",R,N,V__facets) _facets;
@property (Ti,R,N,V__cggetriWorkspaceSize) _cggetriWorkspaceSize;
@property (T^d,R,N,V__cggetriWorkspace) _cggetriWorkspace;
@property (T^d,R,N,V__temp) _temp;
@property (TQ,R,N,V__pointCount) _pointCount;
@property (Tr^d,R,N) _points;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISimplex supportsSecureCoding];
+[_UISimplex keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UISimplex dealloc];
-[_UISimplex _temp];
-[_UISimplex encodeWithCoder:];
-[_UISimplex description];
-[_UISimplex initWithCoder:];
-[_UISimplex _dimensions];
-[_UISimplex copyWithZone:];
-[_UISimplex isEqual:];
-[_UISimplex _closestPoint:toPoint:];
-[_UISimplex _missingNormals];
-[_UISimplex _facets];
-[_UISimplex _points];
-[_UISimplex _cggetriWorkspace];
-[_UISimplex _cggetriWorkspaceSize];
-[_UISimplex _facetNormalOffsets];
-[_UISimplex _facetNormals];
-[_UISimplex _incenter];
-[_UISimplex _missingNormalCount];
-[_UISimplex _mutatePoints:];
-[_UISimplex _pointCount];
-[_UISimplex _projection];
-[_UISimplex _recomputeMetadata];
-[_UISimplex initWithDimensions:pointCount:];
```
