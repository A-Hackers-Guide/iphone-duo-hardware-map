# `MLPipeline`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLPipeline`
- 2 instance variables, 6 properties, 17 instance methods, 5 class methods

## Instance variables

```
@"NSArray" _models;
@"NSArray" _modelNames;
```

## Properties

```
@property (T@"NSArray",&,V_models) models;
@property (T@"NSArray",&,V_modelNames) modelNames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLPipeline classLabelsForPipelineFromSubModelArray:predictedFeatureName:];
+[MLPipeline classLabelsForPipelineFromSubModelDescriptionArray:predictedFeatureName:];
+[MLPipeline extractSubModelNamesFromArchive:numModels:];
+[MLPipeline loadModelAssetDescriptionFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLPipeline parseModelArchive:subModelNames:subModelArchiveNames:error:];
```

## Instance methods

```
-[MLPipeline predictionTypeForKTrace];
-[MLPipeline predictionsFromBatch:options:error:];
-[MLPipeline submitPredictionRequest:completionHandler:];
-[MLPipeline executionSchedule];
-[MLPipeline writeToURL:error:];
-[MLPipeline parameterValueForKey:error:];
-[MLPipeline replaceModelAtIndex:with:];
-[MLPipeline initWithModels:modelNames:description:configuration:];
-[MLPipeline modelNames];
-[MLPipeline setModels:];
-[MLPipeline models];
-[MLPipeline updateParameterDescriptionsByKeyBasedOnSubModel];
-[MLPipeline supportsConcurrentSubmissions];
-[MLPipeline initModelFromMetadataAndArchive:versionInfo:description:configuration:error:];
-[MLPipeline _submitPredictionRequestToSubmodel:input:options:completionHandler:];
-[MLPipeline predictionFromFeatures:options:error:];
-[MLPipeline setModelNames:];
```
