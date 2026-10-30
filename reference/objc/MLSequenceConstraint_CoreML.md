# `MLSequenceConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureValueConstraint`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"MLFeatureDescription" _valueDescription;
{_NSRange="location"Q"length"Q} _countRange;
```

## Properties

```
@property (T@"MLFeatureDescription",R,N,V_valueDescription) valueDescription;
@property (T{_NSRange=QQ},R,N,V_countRange) countRange;
```

## Class methods

```
+[MLSequenceConstraint supportsSecureCoding];
```

## Instance methods

```
-[MLSequenceConstraint encodeWithCoder:];
-[MLSequenceConstraint initWithCoder:];
-[MLSequenceConstraint isAllowedValue:error:];
-[MLSequenceConstraint copyWithZone:];
-[MLSequenceConstraint valueDescription];
-[MLSequenceConstraint countRange];
-[MLSequenceConstraint initWithValueDescription:countRange:];
```
