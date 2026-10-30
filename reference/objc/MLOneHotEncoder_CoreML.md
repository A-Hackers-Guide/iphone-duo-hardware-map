# `MLOneHotEncoder`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`, `MLModeling`
- 3 instance variables, 14 properties, 9 instance methods, 4 class methods

## Instance variables

```
B _ouputSparse;
B _handleUnknown;
@"NSOrderedSet" _featureEncoding;
```

## Properties

```
@property (T@"NSOrderedSet",R,N,V_featureEncoding) featureEncoding;
@property (TB,R,N,V_ouputSparse) ouputSparse;
@property (TB,R,N,V_handleUnknown) handleUnknown;
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
+[MLOneHotEncoder featureEncoderFrom:dataTransformerName:ouputSparse:handleUnknown:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:];
+[MLOneHotEncoder featureEncoderFrom:inputDescription:orderedInputFeatureNames:];
+[MLOneHotEncoder featureEncoderFrom:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:];
+[MLOneHotEncoder loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLOneHotEncoder predictionTypeForKTrace];
-[MLOneHotEncoder predictionFromFeatures:options:error:];
-[MLOneHotEncoder featureEncoding];
-[MLOneHotEncoder encodeFeatureValue:];
-[MLOneHotEncoder encodeFeatureValueIntString:];
-[MLOneHotEncoder handleUnknown];
-[MLOneHotEncoder initWith:dataTransformerName:ouputSparse:handleUnknown:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:];
-[MLOneHotEncoder ouputSparse];
-[MLOneHotEncoder unknownDenseVector];
```
