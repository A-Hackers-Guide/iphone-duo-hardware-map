# `MLE5StaticShapeExecutionStreamOperationPool`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5ExecutionStreamOperationPool`
- 9 instance variables, 13 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"MLE5ProgramLibrary" _programLibrary;
@"NSString" _functionName;
@"MLModelDescription" _modelDescription;
@"MLModelConfiguration" _modelConfiguration;
@"NSMutableSet" _pool;
@"NSObject<OS_dispatch_queue>" _serialQueue;
Q _modelSignpostId;
@"MLPixelBufferPool" _pixelBufferPool;
q _numberOfOperationsInUse;
```

## Properties

```
@property (T@"MLE5ProgramLibrary",R,V_programLibrary) programLibrary;
@property (T@"NSString",R,V_functionName) functionName;
@property (T@"MLModelDescription",R,V_modelDescription) modelDescription;
@property (T@"MLModelConfiguration",R,V_modelConfiguration) modelConfiguration;
@property (T@"NSMutableSet",R,V_pool) pool;
@property (T@"NSObject<OS_dispatch_queue>",R,V_serialQueue) serialQueue;
@property (TQ,R,V_modelSignpostId) modelSignpostId;
@property (T@"MLPixelBufferPool",R,N,V_pixelBufferPool) pixelBufferPool;
@property (Tq,V_numberOfOperationsInUse) numberOfOperationsInUse;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLE5StaticShapeExecutionStreamOperationPool pool];
-[MLE5StaticShapeExecutionStreamOperationPool prepareWithInitialPoolSize:error:];
-[MLE5StaticShapeExecutionStreamOperationPool functionName];
-[MLE5StaticShapeExecutionStreamOperationPool serialQueue];
-[MLE5StaticShapeExecutionStreamOperationPool initWithProgramLibrary:functionName:modelDescription:configuration:modelSignpostId:compilerVersionInfo:];
-[MLE5StaticShapeExecutionStreamOperationPool pixelBufferPool];
-[MLE5StaticShapeExecutionStreamOperationPool modelSignpostId];
-[MLE5StaticShapeExecutionStreamOperationPool programLibrary];
-[MLE5StaticShapeExecutionStreamOperationPool modelConfiguration];
-[MLE5StaticShapeExecutionStreamOperationPool modelDescription];
-[MLE5StaticShapeExecutionStreamOperationPool _putBack:];
-[MLE5StaticShapeExecutionStreamOperationPool setNumberOfOperationsInUse:];
-[MLE5StaticShapeExecutionStreamOperationPool takeOutOperationForFeatures:error:];
-[MLE5StaticShapeExecutionStreamOperationPool _takeOut];
-[MLE5StaticShapeExecutionStreamOperationPool numberOfOperationsInUse];
-[MLE5StaticShapeExecutionStreamOperationPool putBack:];
```
