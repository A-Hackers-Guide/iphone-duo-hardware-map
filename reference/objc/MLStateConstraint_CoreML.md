# `MLStateConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureValueConstraint`, `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _bufferShape;
q _dataType;
```

## Properties

```
@property (T@"NSArray",R,N,V_bufferShape) bufferShape;
@property (Tq,R,N,V_dataType) dataType;
```

## Class methods

```
+[MLStateConstraint supportsSecureCoding];
+[MLStateConstraint constraintWithBufferShape:dataType:];
```

## Instance methods

```
-[MLStateConstraint shape];
-[MLStateConstraint initWithShape:dataType:shapeConstraint:defaultOptionalValue:];
-[MLStateConstraint encodeWithCoder:];
-[MLStateConstraint dataType];
-[MLStateConstraint description];
-[MLStateConstraint initWithCoder:];
-[MLStateConstraint isAllowedValue:error:];
-[MLStateConstraint isAllowedShape:error:];
-[MLStateConstraint copyWithZone:];
-[MLStateConstraint isAllowedDataType:error:];
-[MLStateConstraint bufferShape];
```
