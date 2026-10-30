# `MLPipelineUpdateEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLPipeline`
- Protocols: `MLUpdatable`
- 3 instance variables, 14 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"MLUpdateProgressHandlers" _progressHandlers;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
{vector<unsigned long long, std::allocator<unsigned long long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _updatableModelIndicies;
```

## Properties

```
@property (T{vector<unsigned long long, std::allocator<unsigned long long>>=^Q^Q{?=^Q}},R,V_updatableModelIndicies) updatableModelIndicies;
@property (T@"MLUpdateProgressHandlers",&,V_progressHandlers) progressHandlers;
@property (T@"NSObject<OS_dispatch_queue>",&,V_dispatchQueue) dispatchQueue;
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
+[MLPipelineUpdateEngine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLPipelineUpdateEngine updateModelWithData:];
-[MLPipelineUpdateEngine cancelUpdate];
-[MLPipelineUpdateEngine resumeUpdateWithParameters:];
-[MLPipelineUpdateEngine setUpdateProgressHandlers:dispatchQueue:];
-[MLPipelineUpdateEngine resumeUpdate];
-[MLPipelineUpdateEngine writeToURL:error:];
-[MLPipelineUpdateEngine parameterValueForKey:error:];
-[MLPipelineUpdateEngine dispatchQueue];
-[MLPipelineUpdateEngine setProgressHandlers:];
-[MLPipelineUpdateEngine setDispatchQueue:];
-[MLPipelineUpdateEngine progressHandlers];
-[MLPipelineUpdateEngine updatableModelIndicies];
-[MLPipelineUpdateEngine initFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```
