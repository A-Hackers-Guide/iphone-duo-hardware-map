# `MLCategoricalMapping`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`
- 2 instance variables, 6 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _mapping;
@"MLFeatureValue" _valueOnUnknown;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_mapping) mapping;
@property (T@"MLFeatureValue",R,N,V_valueOnUnknown) valueOnUnknown;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLCategoricalMapping loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLCategoricalMapping predictionTypeForKTrace];
-[MLCategoricalMapping mapping];
-[MLCategoricalMapping predictionFromFeatures:options:error:];
-[MLCategoricalMapping initWithMapping:valueOnUnknown:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:];
-[MLCategoricalMapping mapFeature:error:];
-[MLCategoricalMapping valueOnUnknown];
```
