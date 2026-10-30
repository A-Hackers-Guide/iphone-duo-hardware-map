# `MLModelDescription`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 18 instance variables, 19 properties, 56 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _functionDescriptions;
@"NSString" _defaultFunctionName;
@"NSString" _functionName;
B _isUpdatable;
@"NSDictionary" _inputDescriptionsByName;
@"NSDictionary" _outputDescriptionsByName;
@"NSDictionary" _stateDescriptionsByName;
@"NSString" _predictedFeatureName;
@"NSString" _predictedProbabilitiesName;
@"NSDictionary" _metadata;
@"NSArray" _classLabels;
@"NSURL" _modelURL;
@"NSDictionary" _trainingInputDescriptionsByName;
@"NSDictionary" _parameterDescriptionsByKey;
@"MLLayerPath" _modelPath;
@"NSOrderedSet" _inputFeatureNames;
@"NSOrderedSet" _outputFeatureNames;
@"NSOrderedSet" _stateFeatureNames;
```

## Properties

```
@property (T@"NSArray",C,N,V_classLabels) classLabels;
@property (T@"NSString",R,C,N) functionName;
@property (T@"NSURL",&,N,V_modelURL) modelURL;
@property (TB,N,V_isUpdatable) isUpdatable;
@property (T@"NSDictionary",&,N,V_trainingInputDescriptionsByName) trainingInputDescriptionsByName;
@property (T@"NSDictionary",&,N,V_parameterDescriptionsByKey) parameterDescriptionsByKey;
@property (T@"MLLayerPath",&,N,V_modelPath) modelPath;
@property (T@"MLFeatureDescription",R,C,N) predictedValueFeatureDescription;
@property (T@"MLFeatureDescription",R) predictedClassFeatureDescription;
@property (T@"MLFeatureDescription",R) classProbabilityFeatureDescription;
@property (T@"NSOrderedSet",R,V_inputFeatureNames) inputFeatureNames;
@property (T@"NSOrderedSet",R,V_outputFeatureNames) outputFeatureNames;
@property (T@"NSOrderedSet",R,V_stateFeatureNames) stateFeatureNames;
@property (T@"NSDictionary",R,N,V_inputDescriptionsByName) inputDescriptionsByName;
@property (T@"NSDictionary",R,N,V_outputDescriptionsByName) outputDescriptionsByName;
@property (T@"NSDictionary",R,N,V_stateDescriptionsByName) stateDescriptionsByName;
@property (T@"NSString",R,C,N,V_predictedFeatureName) predictedFeatureName;
@property (T@"NSString",R,C,N,V_predictedProbabilitiesName) predictedProbabilitiesName;
@property (T@"NSDictionary",R,N,V_metadata) metadata;
```

## Class methods

```
+[MLModelDescription supportsSecureCoding];
+[MLModelDescription metadataWithFormat:];
+[MLModelDescription metadataWithSpecification:];
```

## Instance methods

```
-[MLModelDescription classLabels];
-[MLModelDescription outputFeatureNames];
-[MLModelDescription defaultFunctionName];
-[MLModelDescription stateDescriptionsByName];
-[MLModelDescription hasEnumeratedShapeInputs];
-[MLModelDescription functionName];
-[MLModelDescription setTrainingInputDescriptionsByName:];
-[MLModelDescription setParameterDescriptionsByKey:];
-[MLModelDescription trainingInputDescriptionsByName];
-[MLModelDescription hasRangeShapeInputs];
-[MLModelDescription modelDescriptionBySettingMetadata:];
-[MLModelDescription initFromRawModelSpecification:];
-[MLModelDescription debugQuickLookObject];
-[MLModelDescription initWithModelSpecification:error:];
-[MLModelDescription setIsUpdatable:];
-[MLModelDescription verifyInput:error:];
-[MLModelDescription initFromRawModelDescriptionSpecification:];
-[MLModelDescription initWithInputDescriptions:outputDescriptions:predictedFeatureName:predictedProbabilitiesName:functionDescriptions:isUpdatable:trainingInputDescriptions:parameterDescriptions:orderedInputFeatureNames:orderedOutputFeatureNames:metadata:defaultFunctionName:functionName:classLabels:modelURL:modelPath:];
-[MLModelDescription isUpdatable];
-[MLModelDescription modelPath];
-[MLModelDescription predictedFeatureName];
-[MLModelDescription initFromSingleFunctionModelDescriptionSpecification:];
-[MLModelDescription metadata];
-[MLModelDescription initFromRawCompiledModelArchive:error:];
-[MLModelDescription initWithInputDescriptions:outputDescriptions:stateDescriptions:predictedFeatureName:predictedProbabilitiesName:functionDescriptions:isUpdatable:trainingInputDescriptions:parameterDescriptions:orderedInputFeatureNames:orderedOutputFeatureNames:orderedStateFeatureNames:metadata:defaultFunctionName:functionName:classLabels:modelURL:modelPath:];
-[MLModelDescription outputDescriptionsByName];
-[MLModelDescription initWithInputDescriptions:outputDescriptions:predictedFeatureName:predictedProbabilitiesName:trainingInputDescriptions:metadata:];
-[MLModelDescription parameterDescriptionsByKey];
-[MLModelDescription functionDescriptions];
-[MLModelDescription validateAsClassifierDescriptionAndReturnError:];
-[MLModelDescription initWithInputDescriptions:outputDescriptions:predictedFeatureName:predictedProbabilitiesName:metadata:];
-[MLModelDescription validateAsRegressorDescriptionAndReturnError:];
-[MLModelDescription initWithInputDescriptions:outputDescriptions:stateDescriptions:predictedFeatureName:predictedProbabilitiesName:functionName:];
-[MLModelDescription encodeWithCoder:];
-[MLModelDescription inputDescriptionsByName];
-[MLModelDescription inputFeatureNames];
-[MLModelDescription predictedProbabilitiesName];
-[MLModelDescription hash];
-[MLModelDescription setModelPath:];
-[MLModelDescription initFromModelDescriptionSpecification:];
-[MLModelDescription initWithModelDescriptionSpecification:error:];
-[MLModelDescription description];
-[MLModelDescription initWithCoder:];
-[MLModelDescription classProbabilityFeatureDescription];
-[MLModelDescription initFromSingleFunctionCompiledModelArchive:error:];
-[MLModelDescription initFromSingleFunctionModelSpecification:];
-[MLModelDescription copyWithZone:];
-[MLModelDescription stateFeatureNames];
-[MLModelDescription modelURL];
-[MLModelDescription predictedValueFeatureDescription];
-[MLModelDescription isEqual:];
-[MLModelDescription isEqualToDescription:];
-[MLModelDescription initWithInputDescriptions:outputDescriptions:predictedFeatureName:predictedProbabilitiesName:trainingInputDescriptions:orderedInputFeatureNames:orderedOutputFeatureNames:metadata:];
-[MLModelDescription setModelURL:];
-[MLModelDescription predictedClassFeatureDescription];
-[MLModelDescription setClassLabels:];
```
