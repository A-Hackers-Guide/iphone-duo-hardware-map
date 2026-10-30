# `MLKNearestNeighborsClassifier`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLSpecificationCompiler`, `MLCompiledModelLoader`, `MLUpdatable`, `NSSecureCoding`
- 15 instance variables, 26 properties, 46 instance methods, 4 class methods

## Instance variables

```
B _continueWithUpdate;
@"MLUpdateProgressHandlers" _progressHandlers;
@"NSObject<OS_dispatch_queue>" _progressHandlersDispatchQueue;
@"NSDictionary" _updateParameters;
@"MLParameterContainer" _parameterContainer;
Q _numberOfDimensions;
q _indexType;
@"<MLNearestNeighborsIndex>" _index;
q _labelType;
@"NSArray" _labelsForDataPoints;
@"NSOrderedSet" _labelsSet;
@"NSObject" _defaultLabel;
q _weightingScheme;
@"NSString" _nearestLabelsFeatureName;
@"NSString" _nearestDistancesFeatureName;
```

## Properties

```
@property (T@"MLUpdateProgressHandlers",&,N,V_progressHandlers) progressHandlers;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_progressHandlersDispatchQueue) progressHandlersDispatchQueue;
@property (T@"NSDictionary",&,N,V_updateParameters) updateParameters;
@property (TB,N,V_continueWithUpdate) continueWithUpdate;
@property (T@"MLParameterContainer",&,N,V_parameterContainer) parameterContainer;
@property (TQ,N,V_numberOfDimensions) numberOfDimensions;
@property (Tq,N,V_indexType) indexType;
@property (T@"<MLNearestNeighborsIndex>",&,N,V_index) index;
@property (Tq,N,V_labelType) labelType;
@property (T@"NSArray",&,N,V_labelsForDataPoints) labelsForDataPoints;
@property (T@"NSOrderedSet",&,N,V_labelsSet) labelsSet;
@property (T@"NSObject",&,N,V_defaultLabel) defaultLabel;
@property (Tq,N,V_weightingScheme) weightingScheme;
@property (T@"NSString",&,N,V_nearestLabelsFeatureName) nearestLabelsFeatureName;
@property (T@"NSString",&,N,V_nearestDistancesFeatureName) nearestDistancesFeatureName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"MLModelDescription",R,N) modelDescription;
@property (T@"MLModelConfiguration",R,N) configuration;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (TQ,R,N) signpostID;
@property (T@"MLModelMetadata",R) metadata;
```

## Class methods

```
+[MLKNearestNeighborsClassifier supportsSecureCoding];
+[MLKNearestNeighborsClassifier compileSpecification:toArchive:options:error:];
+[MLKNearestNeighborsClassifier compiledVersionForSpecification:options:error:];
+[MLKNearestNeighborsClassifier loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLKNearestNeighborsClassifier updateModelWithData:];
-[MLKNearestNeighborsClassifier indexType];
-[MLKNearestNeighborsClassifier cancelUpdate];
-[MLKNearestNeighborsClassifier resumeUpdateWithParameters:];
-[MLKNearestNeighborsClassifier setUpdateProgressHandlers:dispatchQueue:];
-[MLKNearestNeighborsClassifier resumeUpdate];
-[MLKNearestNeighborsClassifier writeToURL:error:];
-[MLKNearestNeighborsClassifier parameterValueForKey:error:];
-[MLKNearestNeighborsClassifier updateParameters];
-[MLKNearestNeighborsClassifier parameterContainer];
-[MLKNearestNeighborsClassifier setProgressHandlers:];
-[MLKNearestNeighborsClassifier setIndexType:];
-[MLKNearestNeighborsClassifier progressHandlersDispatchQueue];
-[MLKNearestNeighborsClassifier continueWithUpdate];
-[MLKNearestNeighborsClassifier setWeightingScheme:];
-[MLKNearestNeighborsClassifier index];
-[MLKNearestNeighborsClassifier setProgressHandlersDispatchQueue:];
-[MLKNearestNeighborsClassifier setIndex:];
-[MLKNearestNeighborsClassifier weightingScheme];
-[MLKNearestNeighborsClassifier setParameterContainer:];
-[MLKNearestNeighborsClassifier encodeWithCoder:];
-[MLKNearestNeighborsClassifier setContinueWithUpdate:];
-[MLKNearestNeighborsClassifier initWithCoder:];
-[MLKNearestNeighborsClassifier progressHandlers];
-[MLKNearestNeighborsClassifier predictionFromFeatures:options:error:];
-[MLKNearestNeighborsClassifier labelType];
-[MLKNearestNeighborsClassifier setLabelType:];
-[MLKNearestNeighborsClassifier setNearestDistancesFeatureName:];
-[MLKNearestNeighborsClassifier computeClassProbabilities:from:];
-[MLKNearestNeighborsClassifier computeKClosestLabels:];
-[MLKNearestNeighborsClassifier defaultLabel];
-[MLKNearestNeighborsClassifier extractNearestNeighborLabels:distances:indices:from:];
-[MLKNearestNeighborsClassifier initWithDescription:configuration:parameters:dataPoints:labels:error:];
-[MLKNearestNeighborsClassifier inputMultiArray:error:];
-[MLKNearestNeighborsClassifier labelsForDataPoints];
-[MLKNearestNeighborsClassifier labelsSet];
-[MLKNearestNeighborsClassifier nearestDistancesFeatureName];
-[MLKNearestNeighborsClassifier nearestLabelsFeatureName];
-[MLKNearestNeighborsClassifier numberOfDimensions];
-[MLKNearestNeighborsClassifier packageOutputWithPredictedLabel:classProbabilities:nearestLabels:nearestDistances:nearestFeatureIndices:];
-[MLKNearestNeighborsClassifier setDefaultLabel:];
-[MLKNearestNeighborsClassifier setLabelsForDataPoints:];
-[MLKNearestNeighborsClassifier setLabelsSet:];
-[MLKNearestNeighborsClassifier setNearestLabelsFeatureName:];
-[MLKNearestNeighborsClassifier setNumberOfDimensions:];
-[MLKNearestNeighborsClassifier setUpdateParameters:];
```
