# `MLScaler`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`
- 2 instance variables, 6 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"MLFeatureValue" _shiftValue;
@"MLFeatureValue" _scaleValue;
```

## Properties

```
@property (T@"MLFeatureValue",R,N,V_shiftValue) shiftValue;
@property (T@"MLFeatureValue",R,N,V_scaleValue) scaleValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLScaler loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLScaler predictionTypeForKTrace];
-[MLScaler scaleValue];
-[MLScaler predictionFromFeatures:options:error:];
-[MLScaler initWithShiftValue:scaleValue:description:configuration:];
-[MLScaler shiftValue];
```
