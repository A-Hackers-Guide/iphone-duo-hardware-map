# `_MLVNDetectionPrintCustomModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLCustomModel`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"MLModelDescription" _modelDescription;
Q _detectionPrintRequestRevision;
@"NSDictionary" _expectedOutputShapeV1;
@"MLModelConfiguration" _configuration;
```

## Properties

```
@property (T@"MLModelDescription",R,N,V_modelDescription) modelDescription;
@property (TQ,R,N,V_detectionPrintRequestRevision) detectionPrintRequestRevision;
@property (T@"NSDictionary",R,N,V_expectedOutputShapeV1) expectedOutputShapeV1;
@property (T@"MLModelConfiguration",R,N,V_configuration) configuration;
```

## Instance methods

```
-[_MLVNDetectionPrintCustomModel configuration];
-[_MLVNDetectionPrintCustomModel modelDescription];
-[_MLVNDetectionPrintCustomModel predictionFromFeatures:options:error:];
-[_MLVNDetectionPrintCustomModel detectionPrintRequestRevision];
-[_MLVNDetectionPrintCustomModel expectedOutputShapeV1];
-[_MLVNDetectionPrintCustomModel featureValueFromDetectionPrint:featureName:];
-[_MLVNDetectionPrintCustomModel initWithModelDescription:parameterDictionary:error:];
```
