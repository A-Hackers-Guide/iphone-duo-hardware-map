# `MLNumericConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSNumber" _minNumber;
@"NSNumber" _maxNumber;
@"NSSet" _enumeratedNumbers;
```

## Properties

```
@property (T@"NSNumber",&,N,V_minNumber) minNumber;
@property (T@"NSNumber",&,N,V_maxNumber) maxNumber;
@property (T@"NSSet",&,N,V_enumeratedNumbers) enumeratedNumbers;
```

## Class methods

```
+[MLNumericConstraint supportsSecureCoding];
+[MLNumericConstraint numericConstraintWithEnumeratedNumbers:];
+[MLNumericConstraint numericConstraintWithMinNumber:maxNumber:];
```

## Instance methods

```
-[MLNumericConstraint encodeWithCoder:];
-[MLNumericConstraint description];
-[MLNumericConstraint initWithCoder:];
-[MLNumericConstraint enumeratedNumbers];
-[MLNumericConstraint maxNumber];
-[MLNumericConstraint minNumber];
-[MLNumericConstraint setEnumeratedNumbers:];
-[MLNumericConstraint setMaxNumber:];
-[MLNumericConstraint setMinNumber:];
```
