# `MLFeatureProviderConformer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _usingRank5Mapping;
B _passthroughStateFeatures;
@"NSArray" _featureDescriptions;
@"NSDictionary" _defaultValues;
@"NSDictionary" _optionalInputTypes;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_featureDescriptions) featureDescriptions;
@property (T@"NSDictionary",R,C,N,V_defaultValues) defaultValues;
@property (TB,R,N,V_usingRank5Mapping) usingRank5Mapping;
@property (T@"NSDictionary",R,C,N,V_optionalInputTypes) optionalInputTypes;
@property (TB,R,N,V_passthroughStateFeatures) passthroughStateFeatures;
```

## Instance methods

```
-[MLFeatureProviderConformer conformFeatures:error:];
-[MLFeatureProviderConformer _sequenceConcatConsumesOptionalInputNamed:];
-[MLFeatureProviderConformer optionalInputTypes];
-[MLFeatureProviderConformer defaultValues];
-[MLFeatureProviderConformer _fabricateFeatureForDescription:error:];
-[MLFeatureProviderConformer passthroughStateFeatures];
-[MLFeatureProviderConformer usingRank5Mapping];
-[MLFeatureProviderConformer initWithFeatureDescriptions:defaultValues:usingRank5Mapping:optionalInputTypes:passthroughStateFeatures:];
-[MLFeatureProviderConformer featureDescriptions];
```
