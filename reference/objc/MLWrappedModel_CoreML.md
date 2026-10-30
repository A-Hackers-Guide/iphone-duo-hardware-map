# `MLWrappedModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"MLModel" _innerModel;
@"NSString" _reason;
```

## Properties

```
@property (T@"MLModel",&,V_innerModel) innerModel;
@property (T@"NSString",&,N,V_reason) reason;
```

## Instance methods

```
-[MLWrappedModel predictionsFromBatch:options:error:];
-[MLWrappedModel parameterValueForKey:error:];
-[MLWrappedModel predictionFromFeatures:error:];
-[MLWrappedModel setReason:];
-[MLWrappedModel predictionsFromBatch:error:];
-[MLWrappedModel reason];
-[MLWrappedModel predictionFromFeatures:options:error:];
-[MLWrappedModel clearInnerModelWithReason:];
-[MLWrappedModel initWithInnerModel:];
-[MLWrappedModel innerModel];
-[MLWrappedModel setInnerModel:];
```
