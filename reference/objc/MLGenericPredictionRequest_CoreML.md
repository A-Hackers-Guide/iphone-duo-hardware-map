# `MLGenericPredictionRequest`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLPredictionRequest`
- 5 instance variables, 8 properties, 7 instance methods, 0 class methods

## Instance variables

```
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _used;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _cancelled;
@"<MLFeatureProvider>" _inputFeatures;
@"MLPredictionOptions" _predictionOptions;
@"MLModel" _model;
```

## Properties

```
@property (T@"MLModel",R,N,V_model) model;
@property (T@"<MLFeatureProvider>",R,N,V_inputFeatures) inputFeatures;
@property (T@"MLPredictionOptions",R,N,V_predictionOptions) predictionOptions;
@property (TB,R,N) isCancelled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLGenericPredictionRequest model];
-[MLGenericPredictionRequest isCancelled];
-[MLGenericPredictionRequest submitWithCompletionHandler:];
-[MLGenericPredictionRequest cancel];
-[MLGenericPredictionRequest initForModel:inputFeatures:options:];
-[MLGenericPredictionRequest inputFeatures];
-[MLGenericPredictionRequest predictionOptions];
```
