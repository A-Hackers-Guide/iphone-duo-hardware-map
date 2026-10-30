# `MLAppleAudioFeatureExtractor`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 4 instance variables, 5 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSString" _inputFeatureName;
@"NSString" _outputFeatureName;
@"<MLCustomModel>" _featureEmbeddingModel;
@"MLAppleAudioFeatureExtractorParameters" _parameters;
```

## Properties

```
@property (T@"MLAppleAudioFeatureExtractorParameters",R,V_parameters) parameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLAppleAudioFeatureExtractor loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLAppleAudioFeatureExtractor parameters];
-[MLAppleAudioFeatureExtractor predictionFromFeatures:options:error:];
-[MLAppleAudioFeatureExtractor initWithParameters:modelDescription:configuration:error:];
```
