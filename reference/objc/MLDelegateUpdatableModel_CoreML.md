# `MLDelegateUpdatableModel`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLDelegateModel`
- Protocols: `MLUpdatable`
- 0 instance variables, 12 properties, 8 instance methods, 1 class methods

## Properties

```
@property (T@"<MLUpdatable>",R,N) updatableEngine;
@property (T@"MLModelDescription",R,N) modelDescription;
@property (T@"MLModelConfiguration",R,N) configuration;
@property (TB,R,N) supportsConcurrentSubmissions;
@property (TQ,R,N) predictionTypeForKTrace;
@property (TB,R,N) recordsPredictionEvent;
@property (TQ,R,N) signpostID;
@property (T@"MLModelMetadata",R) metadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLDelegateUpdatableModel loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLDelegateUpdatableModel updateModelWithData:];
-[MLDelegateUpdatableModel cancelUpdate];
-[MLDelegateUpdatableModel resumeUpdateWithParameters:];
-[MLDelegateUpdatableModel setUpdateProgressHandlers:dispatchQueue:];
-[MLDelegateUpdatableModel resumeUpdate];
-[MLDelegateUpdatableModel writeToURL:error:];
-[MLDelegateUpdatableModel updatableEngine];
-[MLDelegateUpdatableModel initWithEngine:error:];
```
