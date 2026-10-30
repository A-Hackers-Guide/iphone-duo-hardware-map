# `_ANEIntermediateTensor`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSString" _tensorName;
Q _tensorIndex;
```

## Properties

```
@property (T@"NSString",R,C,N,V_tensorName) tensorName;
@property (TQ,R,N,V_tensorIndex) tensorIndex;
```

## Class methods

```
+[_ANEIntermediateTensor supportsSecureCoding];
+[_ANEIntermediateTensor descriptorWithName:index:];
```

## Instance methods

```
-[_ANEIntermediateTensor encodeWithCoder:];
-[_ANEIntermediateTensor initWithCoder:];
-[_ANEIntermediateTensor copyWithZone:];
-[_ANEIntermediateTensor initWithName:index:];
-[_ANEIntermediateTensor tensorIndex];
-[_ANEIntermediateTensor tensorName];
```
