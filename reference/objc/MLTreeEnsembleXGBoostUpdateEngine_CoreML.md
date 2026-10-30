# `MLTreeEnsembleXGBoostUpdateEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLTreeEnsembleXGBoostClassifier`
- Protocols: `MLUpdatable`
- 10 instance variables, 21 properties, 32 instance methods, 1 class methods

## Instance variables

```
B _continueWithUpdate;
B _personalization;
@"MLUpdateProgressHandlers" _progressHandlers;
@"NSObject<OS_dispatch_queue>" _progressHandlersDispatchQueue;
@"MLParameterContainer" _parameterContainer;
Q _numDimensions;
{shared_ptr<Archiver::MMappedFile>="__ptr_"^{MMappedFile}"__cntrl_"^{__shared_weak_count}} _mmappedModel;
{vector<std::string, std::allocator<std::string>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _classesByString;
{vector<long long, std::allocator<long long>>="__begin_"^q"__end_"^q""{?="__cap_"^q}} _classesByInt;
{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}} _cachedModel;
```

## Properties

```
@property (T@"MLUpdateProgressHandlers",&,N,V_progressHandlers) progressHandlers;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_progressHandlersDispatchQueue) progressHandlersDispatchQueue;
@property (TB,N,V_continueWithUpdate) continueWithUpdate;
@property (TB,N,V_personalization) personalization;
@property (T@"MLParameterContainer",&,N,V_parameterContainer) parameterContainer;
@property (T{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}},N,V_classesByString) classesByString;
@property (T{vector<long long, std::allocator<long long>>=^q^q{?=^q}},N,V_classesByInt) classesByInt;
@property (TQ,N,V_numDimensions) numDimensions;
@property (T{shared_ptr<Archiver::MMappedFile>=^{MMappedFile}^{__shared_weak_count}},N,V_mmappedModel) mmappedModel;
@property (T{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}},N,V_cachedModel) cachedModel;
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
+[MLTreeEnsembleXGBoostUpdateEngine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
```

## Instance methods

```
-[MLTreeEnsembleXGBoostUpdateEngine updateModelWithData:];
-[MLTreeEnsembleXGBoostUpdateEngine cancelUpdate];
-[MLTreeEnsembleXGBoostUpdateEngine resumeUpdateWithParameters:];
-[MLTreeEnsembleXGBoostUpdateEngine setUpdateProgressHandlers:dispatchQueue:];
-[MLTreeEnsembleXGBoostUpdateEngine resumeUpdate];
-[MLTreeEnsembleXGBoostUpdateEngine writeToURL:error:];
-[MLTreeEnsembleXGBoostUpdateEngine parameterValueForKey:error:];
-[MLTreeEnsembleXGBoostUpdateEngine personalization];
-[MLTreeEnsembleXGBoostUpdateEngine updateParameters];
-[MLTreeEnsembleXGBoostUpdateEngine parameterContainer];
-[MLTreeEnsembleXGBoostUpdateEngine setProgressHandlers:];
-[MLTreeEnsembleXGBoostUpdateEngine progressHandlersDispatchQueue];
-[MLTreeEnsembleXGBoostUpdateEngine cachedModel];
-[MLTreeEnsembleXGBoostUpdateEngine continueWithUpdate];
-[MLTreeEnsembleXGBoostUpdateEngine setProgressHandlersDispatchQueue:];
-[MLTreeEnsembleXGBoostUpdateEngine setParameterContainer:];
-[MLTreeEnsembleXGBoostUpdateEngine parameterValueForKey:];
-[MLTreeEnsembleXGBoostUpdateEngine setContinueWithUpdate:];
-[MLTreeEnsembleXGBoostUpdateEngine setPersonalization:];
-[MLTreeEnsembleXGBoostUpdateEngine setCachedModel:];
-[MLTreeEnsembleXGBoostUpdateEngine progressHandlers];
-[MLTreeEnsembleXGBoostUpdateEngine classesByString];
-[MLTreeEnsembleXGBoostUpdateEngine classesByInt];
-[MLTreeEnsembleXGBoostUpdateEngine initWithCompiledArchive:configuration:error:];
-[MLTreeEnsembleXGBoostUpdateEngine loadParameterDescriptionsAndContainerFromConfiguration:modelDescription:error:];
-[MLTreeEnsembleXGBoostUpdateEngine mmappedModel];
-[MLTreeEnsembleXGBoostUpdateEngine numDimensions];
-[MLTreeEnsembleXGBoostUpdateEngine setBoosterParameters:error:];
-[MLTreeEnsembleXGBoostUpdateEngine setClassesByInt:];
-[MLTreeEnsembleXGBoostUpdateEngine setClassesByString:];
-[MLTreeEnsembleXGBoostUpdateEngine setMmappedModel:];
-[MLTreeEnsembleXGBoostUpdateEngine setNumDimensions:];
```
