# `FBSApplicationPlaceholderProgress`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSApplicationPlaceholderProgress`, `BSInvalidatable`, `BSDescriptionProviding`
- 10 instance variables, 10 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSProgress" _progress;
i _invalidated;
q _cancellationAllowed;
q _state;
d _percentComplete;
Q _installPhase;
Q _installState;
Q _expectedFinalInstallPhase;
@"FBSApplicationPlaceholder" _placeholder;
```

## Properties

```
@property (T@"FBSApplicationPlaceholder",R,W,N,V_placeholder) placeholder;
@property (TQ,R,N,V_installState) installState;
@property (TQ,R,N,V_installPhase) installPhase;
@property (TQ,R,N,V_expectedFinalInstallPhase) expectedFinalInstallPhase;
@property (Tq,R,N,V_state) state;
@property (Td,R,N,V_percentComplete) percentComplete;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSApplicationPlaceholderProgress placeholder];
-[FBSApplicationPlaceholderProgress initWithPlaceholder:queue:];
-[FBSApplicationPlaceholderProgress percentComplete];
-[FBSApplicationPlaceholderProgress observeValueForKeyPath:ofObject:change:context:];
-[FBSApplicationPlaceholderProgress succinctDescriptionBuilder];
-[FBSApplicationPlaceholderProgress installPhase];
-[FBSApplicationPlaceholderProgress _queue_updateFromProgress];
-[FBSApplicationPlaceholderProgress dealloc];
-[FBSApplicationPlaceholderProgress descriptionWithMultilinePrefix:];
-[FBSApplicationPlaceholderProgress _stopObservingProgress:withContext:];
-[FBSApplicationPlaceholderProgress succinctDescription];
-[FBSApplicationPlaceholderProgress invalidate];
-[FBSApplicationPlaceholderProgress queue_isValid];
-[FBSApplicationPlaceholderProgress expectedFinalInstallPhase];
-[FBSApplicationPlaceholderProgress queue_canPerformAction:];
-[FBSApplicationPlaceholderProgress _startObservingProgress:withContext:];
-[FBSApplicationPlaceholderProgress installState];
-[FBSApplicationPlaceholderProgress description];
-[FBSApplicationPlaceholderProgress queue_supportedActions];
-[FBSApplicationPlaceholderProgress queue_updateProxy:];
-[FBSApplicationPlaceholderProgress state];
-[FBSApplicationPlaceholderProgress descriptionBuilderWithMultilinePrefix:];
-[FBSApplicationPlaceholderProgress queue_isCancellationAllowed];
```
