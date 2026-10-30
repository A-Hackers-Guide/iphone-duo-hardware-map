# `FBProcessExitContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 8 instance variables, 12 properties, 28 instance methods, 1 class methods

## Instance variables

```
Q _exitReason;
@"RBSProcessExitContext" _underlyingContext;
@"NSError" _launchError;
@"NSError" _terminationError;
@"FBSProcessTerminationRequest" _terminationRequest;
@"FBProcessWatchdogEventContext" _watchdogContext;
@"FBProcessState" _stateBeforeExiting;
q _terminationReason;
```

## Properties

```
@property (T@"FBSProcessTerminationRequest",&,N,V_terminationRequest) terminationRequest;
@property (T@"FBProcessWatchdogEventContext",&,N,V_watchdogContext) watchdogContext;
@property (T@"FBProcessState",C,N,V_stateBeforeExiting) stateBeforeExiting;
@property (Tq,N,V_terminationReason) terminationReason;
@property (TQ,R,N,V_exitReason) exitReason;
@property (T@"NSError",R,N,V_launchError) launchError;
@property (T@"NSError",R,N,V_terminationError) terminationError;
@property (T@"RBSProcessExitContext",R,N,V_underlyingContext) underlyingContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBProcessExitContext descriptionForExitReason:];
```

## Instance methods

```
-[FBProcessExitContext exitCode];
-[FBProcessExitContext setTerminationRequest:];
-[FBProcessExitContext debugDescription];
-[FBProcessExitContext initWithLaunchError:];
-[FBProcessExitContext succinctDescriptionBuilder];
-[FBProcessExitContext watchdogContext];
-[FBProcessExitContext exitReason];
-[FBProcessExitContext initWithTerminationError:];
-[FBProcessExitContext descriptionWithMultilinePrefix:];
-[FBProcessExitContext fairPlayFailure];
-[FBProcessExitContext succinctDescription];
-[FBProcessExitContext exitStatus];
-[FBProcessExitContext setTerminationReason:];
-[FBProcessExitContext consideredJetsam];
-[FBProcessExitContext launchError];
-[FBProcessExitContext terminationError];
-[FBProcessExitContext description];
-[FBProcessExitContext terminationRequest];
-[FBProcessExitContext setStateBeforeExiting:];
-[FBProcessExitContext underlyingContext];
-[FBProcessExitContext terminationSignal];
-[FBProcessExitContext stateBeforeExiting];
-[FBProcessExitContext initWithUnderlyingContext:];
-[FBProcessExitContext terminationReason];
-[FBProcessExitContext exitedNormally];
-[FBProcessExitContext setWatchdogContext:];
-[FBProcessExitContext createError];
-[FBProcessExitContext descriptionBuilderWithMultilinePrefix:];
```
