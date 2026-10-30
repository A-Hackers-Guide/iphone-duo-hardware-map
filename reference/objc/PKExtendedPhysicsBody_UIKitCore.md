# `PKExtendedPhysicsBody`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPhysicsBody`
- 2 instance variables, 1 properties, 7 instance methods, 9 class methods

## Instance variables

```
q _associations;
d _areaFactor;
```

## Properties

```
@property (Td,N) normalizedDensity;
```

## Class methods

```
+[PKExtendedPhysicsBody bodyWithRectangleOfSize:center:];
+[PKExtendedPhysicsBody bodyWithBodies:];
+[PKExtendedPhysicsBody bodyWithCircleOfRadius:];
+[PKExtendedPhysicsBody bodyWithEdgeChainFromPath:];
+[PKExtendedPhysicsBody bodyWithEdgeFromPoint:toPoint:];
+[PKExtendedPhysicsBody bodyWithEdgeLoopFromPath:];
+[PKExtendedPhysicsBody bodyWithEllipseInRect:];
+[PKExtendedPhysicsBody bodyWithPolygonFromPath:];
+[PKExtendedPhysicsBody bodyWithRectangleOfSize:];
```

## Instance methods

```
-[PKExtendedPhysicsBody init];
-[PKExtendedPhysicsBody description];
-[PKExtendedPhysicsBody associate];
-[PKExtendedPhysicsBody dissociate];
-[PKExtendedPhysicsBody initWithRectangleOfSize:];
-[PKExtendedPhysicsBody normalizedDensity];
-[PKExtendedPhysicsBody setNormalizedDensity:];
```
