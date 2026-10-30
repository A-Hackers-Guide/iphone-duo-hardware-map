# `_MLVNScenePrintCustomModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLCustomModel`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"MLModelDescription" _modelDescription;
Q _scenePrintRequestRevision;
@"MLModelConfiguration" _configuration;
```

## Properties

```
@property (T@"MLModelDescription",R,N,V_modelDescription) modelDescription;
@property (TQ,R,N,V_scenePrintRequestRevision) scenePrintRequestRevision;
@property (T@"MLModelConfiguration",R,N,V_configuration) configuration;
```

## Instance methods

```
-[_MLVNScenePrintCustomModel configuration];
-[_MLVNScenePrintCustomModel modelDescription];
-[_MLVNScenePrintCustomModel predictionFromFeatures:options:error:];
-[_MLVNScenePrintCustomModel featureValueFromScenePrint:elementSize:];
-[_MLVNScenePrintCustomModel initWithModelDescription:parameterDictionary:error:];
-[_MLVNScenePrintCustomModel scenePrintRequestRevision];
```
