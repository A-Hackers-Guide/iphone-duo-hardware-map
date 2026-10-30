# `BWPipelineStage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 7 properties, 12 instance methods, 7 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _executionQueue;
@"NSObject<OS_dispatch_group>" _executionGroup;
@"NSObject<OS_dispatch_semaphore>" _inflightMessagesSemaphore;
@"NSMutableArray" _queuedMessages;
@"NSMutableArray" _inputsForQueuedMessages;
AQ _activeInput;
@"NSString" _name;
I _priority;
i _workIntervalType;
B _stillImagePipelineStage;
@"OS_os_workgroup" _workgroup;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (TI,R,N,V_priority) priority;
@property (T@"NSObject<OS_dispatch_queue>",R,&,N,V_executionQueue) queue;
@property (TB,R,N,V_stillImagePipelineStage) stillImagePipelineStage;
@property (Ti,N,V_workIntervalType) workIntervalType;
@property (T@"OS_os_workgroup",R,N,V_workgroup) workgroup;
@property (TQ,R) activeInput;
```

## Class methods

```
+[BWPipelineStage initialize];
+[BWPipelineStage pipelineStageWithName:priority:];
+[BWPipelineStage pipelineStageWithName:priority:discardsLateSampleData:];
+[BWPipelineStage pipelineStageWithName:priority:workIntervalType:];
+[BWPipelineStage pipelineStageWithName:priority:workgroup:];
+[BWPipelineStage pipelineStageWithName:priority:workgroup:discardsLateSampleData:];
+[BWPipelineStage pipelineStageWithName:priority:workgroup:maxQueuedSampleDataMessages:];
```

## Instance methods

```
-[BWPipelineStage priority];
-[BWPipelineStage dealloc];
-[BWPipelineStage queue];
-[BWPipelineStage description];
-[BWPipelineStage name];
-[BWPipelineStage activeInput];
-[BWPipelineStage sendMessage:toInput:];
-[BWPipelineStage sendMessagesToInput:messageProvider:];
-[BWPipelineStage setWorkIntervalType:];
-[BWPipelineStage stillImagePipelineStage];
-[BWPipelineStage workIntervalType];
-[BWPipelineStage workgroup];
```
