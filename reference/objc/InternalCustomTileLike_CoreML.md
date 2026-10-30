# `InternalCustomTileLike`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLCustomLayer`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _inputRank;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _multiples;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _inputShape;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _outputShape;
```

## Properties

```
@property (TQ,R,N,V_inputRank) inputRank;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,N,V_multiples) multiples;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,N,V_inputShape) inputShape;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,N,V_outputShape) outputShape;
```

## Instance methods

```
-[InternalCustomTileLike evaluateOnCPUWithInputs:outputs:error:];
-[InternalCustomTileLike initWithParameterDictionary:error:];
-[InternalCustomTileLike inputRank];
-[InternalCustomTileLike inputShape];
-[InternalCustomTileLike multiples];
-[InternalCustomTileLike outputShape];
-[InternalCustomTileLike outputShapesForInputShapes:error:];
-[InternalCustomTileLike setWeightData:error:];
```
