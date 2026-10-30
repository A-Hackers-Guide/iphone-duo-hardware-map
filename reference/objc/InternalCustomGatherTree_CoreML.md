# `InternalCustomGatherTree`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLCustomLayer`
- 1 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
{vector<int, std::allocator<int>>="__begin_"^i"__end_"^i""{?="__cap_"^i}} _shape;
```

## Properties

```
@property (T{vector<int, std::allocator<int>>=^i^i{?=^i}},R,N,V_shape) shape;
```

## Instance methods

```
-[InternalCustomGatherTree shape];
-[InternalCustomGatherTree evaluateOnCPUWithInputs:outputs:error:];
-[InternalCustomGatherTree initWithParameterDictionary:error:];
-[InternalCustomGatherTree outputShapesForInputShapes:error:];
-[InternalCustomGatherTree setWeightData:error:];
```
