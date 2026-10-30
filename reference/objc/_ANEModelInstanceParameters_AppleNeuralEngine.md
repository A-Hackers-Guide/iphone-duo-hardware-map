# `_ANEModelInstanceParameters`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"NSString" _instanceName;
@"NSArray" _procedureArray;
```

## Properties

```
@property (T@"NSString",R,C,N,V_instanceName) instanceName;
@property (T@"NSArray",R,N,V_procedureArray) procedureArray;
```

## Class methods

```
+[_ANEModelInstanceParameters supportsSecureCoding];
+[_ANEModelInstanceParameters new];
+[_ANEModelInstanceParameters withProcedureData:procedureArray:];
```

## Instance methods

```
-[_ANEModelInstanceParameters init];
-[_ANEModelInstanceParameters encodeWithCoder:];
-[_ANEModelInstanceParameters procedureArray];
-[_ANEModelInstanceParameters description];
-[_ANEModelInstanceParameters initWithCoder:];
-[_ANEModelInstanceParameters initWithProcedureData:procedureArray:];
-[_ANEModelInstanceParameters copyWithZone:];
-[_ANEModelInstanceParameters instanceName];
```
