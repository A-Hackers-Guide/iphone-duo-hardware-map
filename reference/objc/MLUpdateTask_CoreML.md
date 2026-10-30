# `MLUpdateTask`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLTask`
- Protocols: `MLTaskStateTransitionDelegate`
- 6 instance variables, 10 properties, 18 instance methods, 5 class methods

## Instance variables

```
B _updateHasStarted;
@"MLModel<MLUpdatable>" _updatableModel;
@"<MLBatchProvider>" _trainingData;
@"MLUpdateProgressHandlers" _progressHandlers;
@"NSObject<OS_dispatch_queue>" _updateQueue;
@"NSURL" _updatableModelURL;
```

## Properties

```
@property (T@"MLModel<MLUpdatable>",R,N,V_updatableModel) updatableModel;
@property (T@"<MLBatchProvider>",R,N,V_trainingData) trainingData;
@property (T@"MLUpdateProgressHandlers",R,N,V_progressHandlers) progressHandlers;
@property (TB,N,V_updateHasStarted) updateHasStarted;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_updateQueue) updateQueue;
@property (T@"NSURL",R,N,V_updatableModelURL) updatableModelURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLUpdateTask updateModelAtURL:trainingData:configuration:writeToURL:error:];
+[MLUpdateTask updateTaskForModelAtURL:trainingData:completionHandler:error:];
+[MLUpdateTask updateTaskForModelAtURL:trainingData:configuration:completionHandler:error:];
+[MLUpdateTask updateTaskForModelAtURL:trainingData:configuration:progressHandlers:error:];
+[MLUpdateTask updateTaskForModelAtURL:trainingData:progressHandlers:error:];
```

## Instance methods

```
-[MLUpdateTask updateQueue];
-[MLUpdateTask description];
-[MLUpdateTask progressHandlers];
-[MLUpdateTask _completionHandlerBlock];
-[MLUpdateTask _invokeProgressHandlerForContext:];
-[MLUpdateTask _progressHandlerBlock];
-[MLUpdateTask initWithModelAtURL:trainingData:configuration:progressHandlers:error:];
-[MLUpdateTask onCancellation];
-[MLUpdateTask onCompletionWithTaskContext:];
-[MLUpdateTask onFailureWithTaskContext:];
-[MLUpdateTask onResumptionWithTaskContext:];
-[MLUpdateTask onSuspensionWithTaskContext:];
-[MLUpdateTask resumeWithParameters:];
-[MLUpdateTask setUpdateHasStarted:];
-[MLUpdateTask trainingData];
-[MLUpdateTask updatableModel];
-[MLUpdateTask updatableModelURL];
-[MLUpdateTask updateHasStarted];
```
