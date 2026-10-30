# `MLRegressorResult`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"MLMultiArray" _predictedValue;
@"<MLFeatureProvider>" _additionalFeatures;
```

## Properties

```
@property (T@"MLMultiArray",R,V_predictedValue) predictedValue;
@property (T@"<MLFeatureProvider>",R,V_additionalFeatures) additionalFeatures;
```

## Class methods

```
+[MLRegressorResult resultWithValue:];
+[MLRegressorResult resultWithValue:additionalFeatures:];
```

## Instance methods

```
-[MLRegressorResult predictedValue];
-[MLRegressorResult asFeatureDictionaryWithPredictedValueDescription:];
-[MLRegressorResult initWithValue:additionalFeatures:];
-[MLRegressorResult additionalFeatures];
```
