# `FBSystemShell`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 9 instance variables, 6 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"FBSystemShellInitializationContext" _initializationContext;
Q _state;
@"RBSAssertion" _runningAssertion;
@"BKSSystemShellService" _systemShellService;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"RBSAssertion" _lock_preventSleepAssertion;
@"NSMutableSet" _lock_preventIdleSleepReasons;
@"NSMutableArray" _lock_blocksToRunWhenReady;
@"BSCompoundAssertion" _lock_temporaryWatchdogAssertion;
```

## Properties

```
@property (TQ,R,N,V_state) _state;
@property (T@"FBSystemShellInitializationContext",R,N,V_initializationContext) initializationContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSystemShell sharedInstance];
+[FBSystemShell _createSingletonWithOptions:];
```

## Instance methods

```
-[FBSystemShell _state];
-[FBSystemShell _initWithOptions:];
-[FBSystemShell _setState:];
-[FBSystemShell succinctDescriptionBuilder];
-[FBSystemShell descriptionWithMultilinePrefix:];
-[FBSystemShell succinctDescription];
-[FBSystemShell description];
-[FBSystemShell descriptionBuilderWithMultilinePrefix:];
-[FBSystemShell readyForInteraction];
-[FBSystemShell initializationContext];
-[FBSystemShell _addBlockToExecuteWhenReady:];
-[FBSystemShell _informSystemShellServiceDidFinishLaunching];
-[FBSystemShell _initializationComplete];
-[FBSystemShell _setSystemIdleSleepDisabled:forReason:];
-[FBSystemShell _startSystemShellService];
-[FBSystemShell assertWatchdogEnabledForLimitedDurationForReason:];
-[FBSystemShell sendActionsToBackBoard:];
```
