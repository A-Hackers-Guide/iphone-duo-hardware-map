# `_ANEProcedureData`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"NSString" _procedureSymbol;
@"NSArray" _weightArray;
Q _mutableWeightsBufferID;
Q _mutableWeightsBufferSize;
```

## Properties

```
@property (T@"NSString",R,C,N,V_procedureSymbol) procedureSymbol;
@property (T@"NSArray",R,N,V_weightArray) weightArray;
@property (TQ,N,V_mutableWeightsBufferID) mutableWeightsBufferID;
@property (TQ,N,V_mutableWeightsBufferSize) mutableWeightsBufferSize;
```

## Class methods

```
+[_ANEProcedureData supportsSecureCoding];
+[_ANEProcedureData new];
+[_ANEProcedureData procedureDataWithSymbol:weightArray:];
```

## Instance methods

```
-[_ANEProcedureData setMutableWeightsBufferID:];
-[_ANEProcedureData procedureSymbol];
-[_ANEProcedureData initWithProcedure:weightArray:];
-[_ANEProcedureData init];
-[_ANEProcedureData weightArray];
-[_ANEProcedureData mutableWeightsBufferSize];
-[_ANEProcedureData setMutableWeightsBufferSize:];
-[_ANEProcedureData encodeWithCoder:];
-[_ANEProcedureData description];
-[_ANEProcedureData initWithCoder:];
-[_ANEProcedureData copyWithZone:];
-[_ANEProcedureData mutableWeightsBufferID];
```
