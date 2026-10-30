# `MLABInput`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureProvider`
- 4 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"MLMultiArray" _input_x;
@"MLMultiArray" _target_lux;
@"MLMultiArray" _target_nits;
@"MLMultiArray" _target_weight;
```

## Properties

```
@property (T@"MLMultiArray",&,N,V_input_x) input_x;
@property (T@"MLMultiArray",&,N,V_target_lux) target_lux;
@property (T@"MLMultiArray",&,N,V_target_nits) target_nits;
@property (T@"MLMultiArray",&,N,V_target_weight) target_weight;
@property (T@"NSSet",R,N) featureNames;
```

## Instance methods

```
-[MLABInput featureNames];
-[MLABInput featureValueForName:];
-[MLABInput setTarget_nits:];
-[MLABInput input_x];
-[MLABInput initWithInput_x:target_lux:target_nits:target_weight:];
-[MLABInput setInput_x:];
-[MLABInput setTarget_lux:];
-[MLABInput setTarget_weight:];
-[MLABInput target_lux];
-[MLABInput target_nits];
-[MLABInput target_weight];
```
