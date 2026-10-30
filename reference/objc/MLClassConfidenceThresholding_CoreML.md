# `MLClassConfidenceThresholding`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 2 instance variables, 6 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"MLParameterContainer" _parameterContainer;
@"MLFeatureProviderConformer" _inputFeatureConformer;
```

## Properties

```
@property (T@"MLParameterContainer",&,N,V_parameterContainer) parameterContainer;
@property (T@"MLFeatureProviderConformer",R,N,V_inputFeatureConformer) inputFeatureConformer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLClassConfidenceThresholding loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLClassConfidenceThresholding parameterValueForKey:error:];
-[MLClassConfidenceThresholding parameterContainer];
-[MLClassConfidenceThresholding setParameterContainer:];
-[MLClassConfidenceThresholding predictionFromFeatures:options:error:];
-[MLClassConfidenceThresholding inputFeatureConformer];
-[MLClassConfidenceThresholding initWithDescription:configuration:precisionRecallCurves:error:];
```
