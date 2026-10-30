# `MLAppleSoundAnalysisPreprocessing`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 3 instance variables, 4 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"NSString" _inputFeatureName;
@"NSString" _outputFeatureName;
@"<MLCustomModel>" _frontendProcessingModel;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLAppleSoundAnalysisPreprocessing loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLAppleSoundAnalysisPreprocessing predictionFromFeatures:options:error:];
-[MLAppleSoundAnalysisPreprocessing initWithDescription:configuration:error:];
```
