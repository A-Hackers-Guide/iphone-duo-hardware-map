# `MLMultiArrayShapeConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
q _type;
@"NSArray" _sizeRangeForDimension;
@"NSOrderedSet" _shapeSet;
```

## Properties

```
@property (T@"NSOrderedSet",R,N,V_shapeSet) shapeSet;
@property (Tq,R,N,V_type) type;
@property (T@"NSArray",R,N,V_sizeRangeForDimension) sizeRangeForDimension;
@property (T@"NSArray",R,N) enumeratedShapes;
```

## Class methods

```
+[MLMultiArrayShapeConstraint supportsSecureCoding];
```

## Instance methods

```
-[MLMultiArrayShapeConstraint initWithSizeRangeForDimension:];
-[MLMultiArrayShapeConstraint initUnspecified];
-[MLMultiArrayShapeConstraint shapeSet];
-[MLMultiArrayShapeConstraint findAvailableShape:];
-[MLMultiArrayShapeConstraint type];
-[MLMultiArrayShapeConstraint sizeRangeForDimension];
-[MLMultiArrayShapeConstraint encodeWithCoder:];
-[MLMultiArrayShapeConstraint initWithEnumeratedShapes:];
-[MLMultiArrayShapeConstraint initWithCoder:];
-[MLMultiArrayShapeConstraint isAllowedShape:error:];
-[MLMultiArrayShapeConstraint enumeratedShapes];
```
