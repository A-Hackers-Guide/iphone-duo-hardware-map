# `MLSequence`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 5 properties, 8 instance methods, 5 class methods

## Instance variables

```
q _type;
@"NSArray" _values;
```

## Properties

```
@property (T@"NSArray",R,N) featureValues;
@property (T@"NSArray",R,N,V_values) values;
@property (Tq,R,N,V_type) type;
@property (T@"NSArray",R,N) stringValues;
@property (T@"NSArray",R,N) int64Values;
```

## Class methods

```
+[MLSequence supportsSecureCoding];
+[MLSequence emptySequenceWithType:];
+[MLSequence sequenceFromArray:error:];
+[MLSequence sequenceWithInt64Array:];
+[MLSequence sequenceWithStringArray:];
```

## Instance methods

```
-[MLSequence values];
-[MLSequence type];
-[MLSequence encodeWithCoder:];
-[MLSequence initWithCoder:];
-[MLSequence stringValues];
-[MLSequence featureValues];
-[MLSequence initWithArray:type:];
-[MLSequence int64Values];
```
