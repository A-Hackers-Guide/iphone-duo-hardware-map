# `MLNonMaximumSuppression`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`
- 1 instance variables, 5 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"MLNonMaximumSuppressionParameters" _parameters;
```

## Properties

```
@property (T@"MLNonMaximumSuppressionParameters",R,V_parameters) parameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLNonMaximumSuppression loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLNonMaximumSuppression predictionTypeForKTrace];
-[MLNonMaximumSuppression parameters];
-[MLNonMaximumSuppression predictionFromFeatures:options:error:];
-[MLNonMaximumSuppression initWithParameters:modelDescription:configuration:error:];
```
