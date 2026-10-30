# `MLE5ExecutionStreamPool`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"MLModelConfiguration" _modelConfiguration;
@"NSMutableSet" _pool;
@"NSMutableSet" _allStreams;
@"NSObject<OS_dispatch_queue>" _serialQueue;
Q _modelSignpostId;
```

## Properties

```
@property (T@"MLModelConfiguration",R,C,N,V_modelConfiguration) modelConfiguration;
@property (T@"NSMutableSet",R,N,V_pool) pool;
@property (T@"NSMutableSet",R,N,V_allStreams) allStreams;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_serialQueue) serialQueue;
@property (TQ,R,N,V_modelSignpostId) modelSignpostId;
```

## Instance methods

```
-[MLE5ExecutionStreamPool pool];
-[MLE5ExecutionStreamPool enableInstrumentsTracing];
-[MLE5ExecutionStreamPool takeOut];
-[MLE5ExecutionStreamPool serialQueue];
-[MLE5ExecutionStreamPool allStreams];
-[MLE5ExecutionStreamPool modelSignpostId];
-[MLE5ExecutionStreamPool initWithModelConfiguration:modelSignpostId:];
-[MLE5ExecutionStreamPool modelConfiguration];
-[MLE5ExecutionStreamPool _emitMappingTracepointForStream:];
-[MLE5ExecutionStreamPool putBack:];
```
