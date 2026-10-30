# `MLArrayFeatureExtractor`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 3 instance variables, 7 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"NSString" _arrayColumnName;
@"NSArray" _extractIndices;
q _outputType;
```

## Properties

```
@property (T@"NSString",R,N,V_arrayColumnName) arrayColumnName;
@property (T@"NSArray",R,N,V_extractIndices) extractIndices;
@property (Tq,R,N,V_outputType) outputType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLArrayFeatureExtractor extractArrayElement:indices:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:];
+[MLArrayFeatureExtractor extractArrayElement:indices:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:];
+[MLArrayFeatureExtractor loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLArrayFeatureExtractor outputType];
-[MLArrayFeatureExtractor predictionFromFeatures:options:error:];
-[MLArrayFeatureExtractor arrayColumnName];
-[MLArrayFeatureExtractor extractIndices];
-[MLArrayFeatureExtractor initWith:indices:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:];
```
