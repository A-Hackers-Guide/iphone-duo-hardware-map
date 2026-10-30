# `MLLinkedModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 3 instance variables, 7 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"MLModel" _linkedModel;
@"NSString" _modelFileName;
@"NSString" _modelSearchPath;
```

## Properties

```
@property (T@"MLModel",&,V_linkedModel) linkedModel;
@property (T@"NSString",&,V_modelFileName) modelFileName;
@property (T@"NSString",&,V_modelSearchPath) modelSearchPath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLLinkedModel findFile:inSearchPath:basePath:];
+[MLLinkedModel areFeaturesIn:modelNamed:aSubsetOf:error:];
+[MLLinkedModel loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLLinkedModel predictionsFromBatch:options:error:];
-[MLLinkedModel parameterValueForKey:error:];
-[MLLinkedModel predictionFromFeatures:options:error:];
-[MLLinkedModel modelSearchPath];
-[MLLinkedModel setLinkedModel:];
-[MLLinkedModel initWithLinkedModel:modelFileName:modelSearchPath:configuration:];
-[MLLinkedModel linkedModel];
-[MLLinkedModel modelFileName];
-[MLLinkedModel setModelFileName:];
-[MLLinkedModel setModelSearchPath:];
-[MLLinkedModel updateParameterDescriptionsByUnarchivingSpecification:];
```
