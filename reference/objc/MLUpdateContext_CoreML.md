# `MLUpdateContext`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"MLUpdateTask" _task;
@"MLModel<MLWritable>" _model;
q _event;
@"NSDictionary" _metrics;
@"NSDictionary" _parameters;
@"NSError" _error;
```

## Properties

```
@property (T@"MLUpdateTask",&,N,V_task) task;
@property (T@"MLModel<MLWritable>",&,N,V_model) model;
@property (Tq,N,V_event) event;
@property (T@"NSDictionary",&,N,V_metrics) metrics;
@property (T@"NSDictionary",&,N,V_parameters) parameters;
@property (T@"NSError",&,N,V_error) error;
```

## Class methods

```
+[MLUpdateContext updateContextForEvent:metrics:parameters:error:];
+[MLUpdateContext updateContextWithTask:model:event:metrics:parameters:];
```

## Instance methods

```
-[MLUpdateContext setEvent:];
-[MLUpdateContext model];
-[MLUpdateContext setMetrics:];
-[MLUpdateContext setError:];
-[MLUpdateContext setModel:];
-[MLUpdateContext parameters];
-[MLUpdateContext setParameters:];
-[MLUpdateContext event];
-[MLUpdateContext error];
-[MLUpdateContext setTask:];
-[MLUpdateContext description];
-[MLUpdateContext task];
-[MLUpdateContext metrics];
```
