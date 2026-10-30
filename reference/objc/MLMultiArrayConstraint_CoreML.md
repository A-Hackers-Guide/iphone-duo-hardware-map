# `MLMultiArrayConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureValueConstraint`, `NSCopying`, `NSSecureCoding`
- 4 instance variables, 3 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"NSNumber" _defaultOptionalValue;
@"NSArray" _shape;
q _dataType;
@"MLMultiArrayShapeConstraint" _shapeConstraint;
```

## Properties

```
@property (T@"NSArray",R,N,V_shape) shape;
@property (Tq,R,N,V_dataType) dataType;
@property (T@"MLMultiArrayShapeConstraint",R,N,V_shapeConstraint) shapeConstraint;
```

## Class methods

```
+[MLMultiArrayConstraint supportsSecureCoding];
+[MLMultiArrayConstraint constraintWithShape:dataType:];
+[MLMultiArrayConstraint constraintWithShape:dataType:shapeConstraint:];
```

## Instance methods

```
-[MLMultiArrayConstraint isAllowedValue:isNeuralNetworkInputOrOutput:usingRank5Mapping:featureName:error:];
-[MLMultiArrayConstraint shape];
-[MLMultiArrayConstraint shapeConstraint];
-[MLMultiArrayConstraint initWithShape:dataType:shapeConstraint:defaultOptionalValue:];
-[MLMultiArrayConstraint encodeWithCoder:];
-[MLMultiArrayConstraint dataType];
-[MLMultiArrayConstraint initWithShape:dataType:shapeConstraint:];
-[MLMultiArrayConstraint description];
-[MLMultiArrayConstraint initWithCoder:];
-[MLMultiArrayConstraint isAllowedValue:error:];
-[MLMultiArrayConstraint isAllowedShape:error:];
-[MLMultiArrayConstraint copyWithZone:];
-[MLMultiArrayConstraint defaultOptionalValue];
-[MLMultiArrayConstraint isAllowedDataType:error:];
```
