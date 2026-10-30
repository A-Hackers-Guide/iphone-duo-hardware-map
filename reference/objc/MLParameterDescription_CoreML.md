# `MLParameterDescription`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 6 class methods

## Instance variables

```
@"MLParameterKey" _key;
@ _defaultValue;
@"MLNumericConstraint" _numericConstraint;
```

## Properties

```
@property (T@"MLParameterKey",&,N,V_key) key;
@property (T@,&,N,V_defaultValue) defaultValue;
@property (T@"MLNumericConstraint",&,N,V_numericConstraint) numericConstraint;
```

## Class methods

```
+[MLParameterDescription supportsSecureCoding];
+[MLParameterDescription parameterDescriptionForKey:boolParameterSpec:];
+[MLParameterDescription parameterDescriptionForKey:defaultValue:numericConstraint:];
+[MLParameterDescription parameterDescriptionForKey:doubleParameterSpec:];
+[MLParameterDescription parameterDescriptionForKey:int64ParameterSpec:];
+[MLParameterDescription parameterDescriptionForKey:stringParameterSpec:];
```

## Instance methods

```
-[MLParameterDescription setDefaultValue:];
-[MLParameterDescription defaultValue];
-[MLParameterDescription setKey:];
-[MLParameterDescription encodeWithCoder:];
-[MLParameterDescription description];
-[MLParameterDescription initWithCoder:];
-[MLParameterDescription key];
-[MLParameterDescription numericConstraint];
-[MLParameterDescription setNumericConstraint:];
```
