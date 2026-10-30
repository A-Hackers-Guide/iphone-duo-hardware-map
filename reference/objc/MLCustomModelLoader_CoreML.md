# `MLCustomModelLoader`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLModelSpecificationLoader`
- 0 instance variables, 4 properties, 0 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLCustomModelLoader customModelWithName:modelDescription:modelConfiguration:parameterDictionary:error:];
+[MLCustomModelLoader loadModelFromSpecification:configuration:error:];
+[MLCustomModelLoader parametersFromCustomModelSpec:error:];
```
