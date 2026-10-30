# `MLLazyUnionFeatureProvider`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureProvider`
- 2 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<MLFeatureProvider>" _first;
@"<MLFeatureProvider>" _second;
```

## Properties

```
@property (T@"<MLFeatureProvider>",&,N,V_first) first;
@property (T@"<MLFeatureProvider>",&,N,V_second) second;
@property (T@"NSSet",R,N) featureNames;
```

## Instance methods

```
-[MLLazyUnionFeatureProvider second];
-[MLLazyUnionFeatureProvider first];
-[MLLazyUnionFeatureProvider setFirst:];
-[MLLazyUnionFeatureProvider setSecond:];
-[MLLazyUnionFeatureProvider featureNames];
-[MLLazyUnionFeatureProvider featureValueForName:];
-[MLLazyUnionFeatureProvider initWithFeaturesFrom:addedToFeaturesFrom:];
-[MLLazyUnionFeatureProvider unionFeatureProvider];
```
