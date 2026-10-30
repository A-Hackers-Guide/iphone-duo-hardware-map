# `MLNormalizer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`
- 1 instance variables, 5 properties, 4 instance methods, 4 class methods

## Instance variables

```
i _norm;
```

## Properties

```
@property (Ti,R,N,V_norm) norm;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLNormalizer inputDescriptionFrom:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:];
+[MLNormalizer loadModelFromSpecification:configuration:error:];
+[MLNormalizer normFrom:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:];
+[MLNormalizer normFrom:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:];
```

## Instance methods

```
-[MLNormalizer predictionTypeForKTrace];
-[MLNormalizer predictionFromFeatures:options:error:];
-[MLNormalizer initWith:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:];
-[MLNormalizer norm];
```
