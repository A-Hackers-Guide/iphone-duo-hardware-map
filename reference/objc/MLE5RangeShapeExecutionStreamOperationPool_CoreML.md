# `MLE5RangeShapeExecutionStreamOperationPool`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5ExecutionStreamOperationPool`
- 10 instance variables, 14 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"MLE5ProgramLibrary" _programLibrary;
@"NSString" _milFunctionName;
@"NSString" _milDefaultShapeFunctionName;
@"MLModelDescription" _modelDescription;
@"MLModelConfiguration" _configuration;
@"NSMutableDictionary" _shapeHashToPoolMap;
@"NSMutableSet" _defaultShapePool;
@"NSObject<OS_dispatch_queue>" _serialQueue;
Q _modelSignpostId;
@"MLVersionInfo" _compilerVersionInfo;
```

## Properties

```
@property (T@"MLE5ProgramLibrary",R,N,V_programLibrary) programLibrary;
@property (T@"NSString",R,N,V_milFunctionName) milFunctionName;
@property (T@"NSString",R,N,V_milDefaultShapeFunctionName) milDefaultShapeFunctionName;
@property (T@"MLModelDescription",R,N,V_modelDescription) modelDescription;
@property (T@"MLModelConfiguration",R,N,V_configuration) configuration;
@property (T@"NSMutableDictionary",R,N,V_shapeHashToPoolMap) shapeHashToPoolMap;
@property (T@"NSMutableSet",R,V_defaultShapePool) defaultShapePool;
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
-[MLE5RangeShapeExecutionStreamOperationPool prepareWithInitialPoolSize:error:];
-[MLE5RangeShapeExecutionStreamOperationPool serialQueue];
-[MLE5RangeShapeExecutionStreamOperationPool initWithProgramLibrary:functionName:modelDescription:configuration:modelSignpostId:compilerVersionInfo:];
-[MLE5RangeShapeExecutionStreamOperationPool modelSignpostId];
-[MLE5RangeShapeExecutionStreamOperationPool programLibrary];
-[MLE5RangeShapeExecutionStreamOperationPool configuration];
-[MLE5RangeShapeExecutionStreamOperationPool modelDescription];
-[MLE5RangeShapeExecutionStreamOperationPool _putBack:];
-[MLE5RangeShapeExecutionStreamOperationPool takeOutOperationForFeatures:error:];
-[MLE5RangeShapeExecutionStreamOperationPool compilerVersionInfo];
-[MLE5RangeShapeExecutionStreamOperationPool putBack:];
-[MLE5RangeShapeExecutionStreamOperationPool milFunctionName];
-[MLE5RangeShapeExecutionStreamOperationPool _makeAndPreloadOperationForFunction:error:];
-[MLE5RangeShapeExecutionStreamOperationPool _takeOutAnyOperation];
-[MLE5RangeShapeExecutionStreamOperationPool defaultShapePool];
-[MLE5RangeShapeExecutionStreamOperationPool milDefaultShapeFunctionName];
-[MLE5RangeShapeExecutionStreamOperationPool shapeHashToPoolMap];
```
