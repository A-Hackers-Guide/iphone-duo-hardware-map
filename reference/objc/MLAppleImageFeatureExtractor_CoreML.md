# `MLAppleImageFeatureExtractor`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 5 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSString" _inputFeatureName;
@"NSArray" _outputFeatureName;
q _outputDataType;
i _extractorType;
@"MLAppleImageFeatureExtractorParameters" _parameters;
```

## Properties

```
@property (T@"MLAppleImageFeatureExtractorParameters",R,V_parameters) parameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLAppleImageFeatureExtractor loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLAppleImageFeatureExtractor parameters];
-[MLAppleImageFeatureExtractor predictionFromFeatures:options:error:];
-[MLAppleImageFeatureExtractor computeScenePrintFeatures:handle:useCPUOnly:error:];
-[MLAppleImageFeatureExtractor featureValueFromObjectPrint:key:shape:];
-[MLAppleImageFeatureExtractor featureValueFromScenePrint:elementSize:];
-[MLAppleImageFeatureExtractor initWithParameters:modelDescription:featureExtractorType:configuration:error:];
```
