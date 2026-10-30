# `MLClassifierResult`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 5 class methods

## Instance variables

```
@"MLFeatureValue" _predictedClass;
@"NSDictionary" _classProbability;
q _predictedClassFeatureType;
@"<MLFeatureProvider>" _additionalFeatures;
```

## Properties

```
@property (T@"MLFeatureValue",R,V_predictedClass) predictedClass;
@property (T@"NSDictionary",R,V_classProbability) classProbability;
@property (Tq,R,V_predictedClassFeatureType) predictedClassFeatureType;
@property (T@"<MLFeatureProvider>",R,V_additionalFeatures) additionalFeatures;
```

## Class methods

```
+[MLClassifierResult resultWithClassProbability:additionalFeatures:classLabelOfMaxProbability:];
+[MLClassifierResult resultWithIntClassProbability:];
+[MLClassifierResult resultWithIntClassProbability:additionalFeatures:];
+[MLClassifierResult resultWithStringClassProbability:];
+[MLClassifierResult resultWithStringClassProbability:additionalFeatures:];
```

## Instance methods

```
-[MLClassifierResult additionalFeatures];
-[MLClassifierResult asFeatureDictionaryWithPredictedClassDescription:classProbabilityDescription:];
-[MLClassifierResult classProbability];
-[MLClassifierResult initWithClassProbability:additionalFeatures:classLabelOfMaxProbability:];
-[MLClassifierResult initWithIntClassProbability:classFeatureType:additionalFeatures:];
-[MLClassifierResult initWithStringClassProbability:classFeatureType:additionalFeatures:];
-[MLClassifierResult predictedClass];
-[MLClassifierResult predictedClassFeatureType];
```
