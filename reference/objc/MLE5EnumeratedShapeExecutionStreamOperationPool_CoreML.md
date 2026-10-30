# `MLE5EnumeratedShapeExecutionStreamOperationPool`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5ExecutionStreamOperationPool`
- 9 instance variables, 13 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"MLE5ProgramLibrary" _programLibrary;
@"MLModelConfiguration" _configuration;
@"NSString" _milEntryFunctionName;
@"NSSet" _milFunctionNames;
@"MLModelDescription" _modelDescription;
@"NSMutableDictionary" _functionNameToPoolMap;
@"NSObject<OS_dispatch_queue>" _serialQueue;
Q _modelSignpostId;
@"MLVersionInfo" _compilerVersionInfo;
```

## Properties

```
@property (T@"MLE5ProgramLibrary",R,N,V_programLibrary) programLibrary;
@property (T@"MLModelConfiguration",R,N,V_configuration) configuration;
@property (T@"NSString",R,N,V_milEntryFunctionName) milEntryFunctionName;
@property (T@"NSSet",R,N,V_milFunctionNames) milFunctionNames;
@property (T@"MLModelDescription",R,N,V_modelDescription) modelDescription;
@property (T@"NSMutableDictionary",R,N,V_functionNameToPoolMap) functionNameToPoolMap;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_serialQueue) serialQueue;
@property (TQ,R,N,V_modelSignpostId) modelSignpostId;
@property (T@"MLVersionInfo",R,N,V_compilerVersionInfo) compilerVersionInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLE5EnumeratedShapeExecutionStreamOperationPool prepareWithInitialPoolSize:error:];
-[MLE5EnumeratedShapeExecutionStreamOperationPool serialQueue];
-[MLE5EnumeratedShapeExecutionStreamOperationPool initWithProgramLibrary:functionName:modelDescription:configuration:modelSignpostId:compilerVersionInfo:];
-[MLE5EnumeratedShapeExecutionStreamOperationPool modelSignpostId];
-[MLE5EnumeratedShapeExecutionStreamOperationPool programLibrary];
-[MLE5EnumeratedShapeExecutionStreamOperationPool configuration];
-[MLE5EnumeratedShapeExecutionStreamOperationPool modelDescription];
-[MLE5EnumeratedShapeExecutionStreamOperationPool _putBack:];
-[MLE5EnumeratedShapeExecutionStreamOperationPool takeOutOperationForFeatures:error:];
-[MLE5EnumeratedShapeExecutionStreamOperationPool compilerVersionInfo];
-[MLE5EnumeratedShapeExecutionStreamOperationPool putBack:];
-[MLE5EnumeratedShapeExecutionStreamOperationPool _takeOutOperationForFunctionName:error:];
-[MLE5EnumeratedShapeExecutionStreamOperationPool _takeOutOperationFromAnyProgramFunction];
-[MLE5EnumeratedShapeExecutionStreamOperationPool functionNameToPoolMap];
-[MLE5EnumeratedShapeExecutionStreamOperationPool milEntryFunctionName];
-[MLE5EnumeratedShapeExecutionStreamOperationPool milFunctionNames];
```
