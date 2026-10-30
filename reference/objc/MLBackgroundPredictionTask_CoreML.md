# `MLBackgroundPredictionTask`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLBackgroundTask`
- 3 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSURL" _modelURL;
@"MLModelConfiguration" _modelConfiguration;
@"MLPredictionOptions" _predictionOptions;
```

## Properties

```
@property (T@"NSURL",C,N,V_modelURL) modelURL;
@property (T@"MLModelConfiguration",C,N,V_modelConfiguration) modelConfiguration;
@property (T@"MLPredictionOptions",C,N,V_predictionOptions) predictionOptions;
```

## Class methods

```
+[MLBackgroundPredictionTask supportsSecureCoding];
+[MLBackgroundPredictionTask taskRunnerClass];
```

## Instance methods

```
-[MLBackgroundPredictionTask setModelConfiguration:];
-[MLBackgroundPredictionTask modelConfiguration];
-[MLBackgroundPredictionTask encodeWithCoder:];
-[MLBackgroundPredictionTask initWithCoder:];
-[MLBackgroundPredictionTask copyWithZone:];
-[MLBackgroundPredictionTask modelURL];
-[MLBackgroundPredictionTask setModelURL:];
-[MLBackgroundPredictionTask predictionOptions];
-[MLBackgroundPredictionTask setPredictionOptions:];
```
