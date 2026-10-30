# `MLDictionaryConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureValueConstraint`, `NSCopying`, `NSSecureCoding`
- 1 instance variables, 1 properties, 7 instance methods, 3 class methods

## Instance variables

```
q _keyType;
```

## Properties

```
@property (Tq,R,N,V_keyType) keyType;
```

## Class methods

```
+[MLDictionaryConstraint supportsSecureCoding];
+[MLDictionaryConstraint constraintWithInt64Keys];
+[MLDictionaryConstraint constraintWithStringKeys];
```

## Instance methods

```
-[MLDictionaryConstraint encodeWithCoder:];
-[MLDictionaryConstraint description];
-[MLDictionaryConstraint initWithCoder:];
-[MLDictionaryConstraint isAllowedValue:error:];
-[MLDictionaryConstraint copyWithZone:];
-[MLDictionaryConstraint keyType];
-[MLDictionaryConstraint initWithKeyType:];
```
