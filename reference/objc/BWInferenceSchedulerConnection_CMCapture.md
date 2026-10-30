# `BWInferenceSchedulerConnection`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _identifier;
@"NSString" _engineDescription;
@"BWInferenceSchedulerResourceCoordinator" _coordinator;
@"BWInferenceSchedulerFramebuffer" _framebuffer;
@"NSObject<OS_dispatch_queue>" _inferenceQueue;
@"NSObject<OS_dispatch_queue>" _scalingQueue;
@"NSObject<OS_dispatch_queue>" _submissionQueue;
@"NSObject<OS_dispatch_queue>" _completionQueue;
@"NSObject<OS_dispatch_group>" _coordinationGroup;
```

## Properties

```
@property (TQ,R,N,V_identifier) identifier;
@property (T@"NSString",R,N,V_engineDescription) engineDescription;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_inferenceQueue) inferenceQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_scalingQueue) scalingQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_submissionQueue) submissionQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_completionQueue) completionQueue;
@property (T@"NSObject<OS_dispatch_group>",R,N,V_coordinationGroup) coordinationGroup;
@property (T@"BWInferenceSchedulerResourceCoordinator",R,N,V_coordinator) coordinator;
@property (T@"BWInferenceSchedulerFramebuffer",&,N,V_framebuffer) framebuffer;
```

## Instance methods

```
-[BWInferenceSchedulerConnection identifier];
-[BWInferenceSchedulerConnection completionQueue];
-[BWInferenceSchedulerConnection init];
-[BWInferenceSchedulerConnection dealloc];
-[BWInferenceSchedulerConnection coordinator];
-[BWInferenceSchedulerConnection setFramebuffer:];
-[BWInferenceSchedulerConnection submissionQueue];
-[BWInferenceSchedulerConnection coordinationGroup];
-[BWInferenceSchedulerConnection engineDescription];
-[BWInferenceSchedulerConnection framebuffer];
-[BWInferenceSchedulerConnection inferenceQueue];
-[BWInferenceSchedulerConnection initWithInferenceTargetQueue:scalingTargetQueue:submissionTargetQueue:completionTargetQueue:engineDescription:];
-[BWInferenceSchedulerConnection scalingQueue];
```
