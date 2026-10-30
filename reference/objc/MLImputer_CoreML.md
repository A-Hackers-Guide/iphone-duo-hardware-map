# `MLImputer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`
- 2 instance variables, 6 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"MLFeatureValue" _imputeValue;
@"MLFeatureValue" _replaceValue;
```

## Properties

```
@property (T@"MLFeatureValue",R,N,V_imputeValue) imputeValue;
@property (T@"MLFeatureValue",R,N,V_replaceValue) replaceValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLImputer imputeValueFrom:replaceValue:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:error:];
+[MLImputer imputeValueFrom:replaceValue:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:error:];
+[MLImputer loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLImputer predictionTypeForKTrace];
-[MLImputer predictionFromFeatures:options:error:];
-[MLImputer imputeValue];
-[MLImputer initWith:imputeValue:replaceValue:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:error:];
-[MLImputer replaceValue];
```
