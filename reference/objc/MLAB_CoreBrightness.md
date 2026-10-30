# `MLAB`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"MLModel" _model;
```

## Properties

```
@property (T@"MLModel",R,N,V_model) model;
```

## Class methods

```
+[MLAB loadContentsOfURL:configuration:completionHandler:];
+[MLAB URLOfModelInThisBundle];
+[MLAB loadWithConfiguration:completionHandler:];
```

## Instance methods

```
-[MLAB model];
-[MLAB predictionFromFeatures:error:];
-[MLAB init];
-[MLAB initWithContentsOfURL:error:];
-[MLAB initWithConfiguration:error:];
-[MLAB predictionFromFeatures:options:error:];
-[MLAB initWithMLModel:];
-[MLAB initWithContentsOfURL:configuration:error:];
-[MLAB predictionsFromInputs:options:error:];
-[MLAB predictionFromInput_x:target_lux:target_nits:target_weight:error:];
```
