# `BWNodeConnection`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWNodeOutputConsumer`
- 20 instance variables, 13 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"BWNodeInput" _input;
@"BWNodeOutput" _output;
@"BWNodeInput" _bypassInput;
@"BWPipelineStage" _pipelineStage;
@"BWNodeConnection" _bypassConnection;
B _waitingForDeferredAttach;
B _waitingForDeferredResume;
B _waitingForDeferredResumeForEventsOnly;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _suspensionLock;
AB _suspended;
Ai _messageTypeToWaitForBeforeSuspension;
B _resuming;
B _bypassed;
B _wantsMessageCachingWhileSuspended;
B _messageCachingEnabled;
B _resumedForEventsOnly;
@"NSMutableArray" _messagesToPropagate;
Aq _allowedLiveConfigurationID;
@"NSObject<OS_dispatch_queue>" _messageDispatchQueue;
B _allowsSuspensionWithoutPipelineStage;
```

## Properties

```
@property (T@"BWNodeInput",R,W) input;
@property (T@"BWNodeOutput",R,W) output;
@property (T@"BWPipelineStage",R) pipelineStage;
@property (T@"NSObject<OS_dispatch_queue>",R) messageDispatchQueue;
@property (TB,R) bypassed;
@property (TB,R) suspended;
@property (TB,R) resuming;
@property (TB,N,V_allowsSuspensionWithoutPipelineStage) allowsSuspensionWithoutPipelineStage;
@property (TB,N,V_wantsMessageCachingWhileSuspended) wantsMessageCachingWhileSuspended;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWNodeConnection initialize];
```

## Instance methods

```
-[BWNodeConnection suspended];
-[BWNodeConnection logGraphTimeoutState];
-[BWNodeConnection connectBypassInput];
-[BWNodeConnection resumeForEventsOnly:];
-[BWNodeConnection input];
-[BWNodeConnection initWithOutput:input:pipelineStage:];
-[BWNodeConnection dealloc];
-[BWNodeConnection detach];
-[BWNodeConnection pipelineStage];
-[BWNodeConnection attachNow];
-[BWNodeConnection allowsSuspensionWithoutPipelineStage];
-[BWNodeConnection consumeMessage:fromOutput:];
-[BWNodeConnection discardMessagesBeforeLiveConfigurationID:];
-[BWNodeConnection setWantsMessageCachingWhileSuspended:];
-[BWNodeConnection pipelineStageExecutingOnConnectedInput];
-[BWNodeConnection resolveCommonBufferFormat];
-[BWNodeConnection attach];
-[BWNodeConnection bypassed];
-[BWNodeConnection suspendWithMessageCachingAllowed:overrideCachingEnabled:bypassed:afterHandlingMessageWithType:];
-[BWNodeConnection wantsMessageCachingWhileSuspended];
-[BWNodeConnection description];
-[BWNodeConnection setAllowsSuspensionWithoutPipelineStage:];
-[BWNodeConnection messageDispatchQueue];
-[BWNodeConnection output];
-[BWNodeConnection resuming];
-[BWNodeConnection deferredAttach];
```
