# `MLPredictionRequest` (protocol)

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"<MLFeatureProvider>",R,N) inputFeatures;
@property (T@"MLPredictionOptions",R,N) predictionOptions;
@property (TB,R,N) isCancelled;
```

## Instance methods

```
-[MLPredictionRequest isCancelled];
-[MLPredictionRequest submitWithCompletionHandler:];
-[MLPredictionRequest cancel];
-[MLPredictionRequest inputFeatures];
-[MLPredictionRequest predictionOptions];
```
