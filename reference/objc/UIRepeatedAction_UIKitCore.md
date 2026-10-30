# `UIRepeatedAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 9 properties, 33 instance methods, 2 class methods

## Instance variables

```
B _didCompletePreInvocationDelay;
B _didCompleteInvocationDelay;
B _disableRepeat;
B _skipInitialFire;
d _preInvocationDelay;
d _invocationDelay;
d _repeatedDelay;
@"NSInvocation" _invocation;
@ _invocationArgument;
@"NSTimer" _timer;
@"NSObject<UIRepeatedActionDelegate>" _delegate;
```

## Properties

```
@property (T@"NSInvocation",&,N,V_invocation) invocation;
@property (T@,&,N,V_invocationArgument) invocationArgument;
@property (T@"NSTimer",&,N,V_timer) timer;
@property (Td,N,V_preInvocationDelay) preInvocationDelay;
@property (Td,N,V_invocationDelay) invocationDelay;
@property (Td,N,V_repeatedDelay) repeatedDelay;
@property (TB,N,V_disableRepeat) disableRepeat;
@property (TB,N,V_skipInitialFire) skipInitialFire;
@property (T@"NSObject<UIRepeatedActionDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[UIRepeatedAction _invocationForTarget:selector:object:];
+[UIRepeatedAction actionWithTarget:selector:object:];
```

## Instance methods

```
-[UIRepeatedAction setInvocationArgument:];
-[UIRepeatedAction invocationDelay];
-[UIRepeatedAction disableRepeat];
-[UIRepeatedAction invoke];
-[UIRepeatedAction setTimer:];
-[UIRepeatedAction _shouldInvokeRepeatedAction];
-[UIRepeatedAction timer];
-[UIRepeatedAction dealloc];
-[UIRepeatedAction setInvocation:];
-[UIRepeatedAction reset];
-[UIRepeatedAction initWithInvocation:];
-[UIRepeatedAction _invocationTimerFire];
-[UIRepeatedAction _adjustInvocationForPhase:];
-[UIRepeatedAction skipInitialFire];
-[UIRepeatedAction setDisableRepeat:];
-[UIRepeatedAction invalidate];
-[UIRepeatedAction setDelegate:];
-[UIRepeatedAction repeatedDelay];
-[UIRepeatedAction invocationArgument];
-[UIRepeatedAction invocation];
-[UIRepeatedAction setInvocationDelay:];
-[UIRepeatedAction _shouldBeginCurrentRepetitionForPhase:];
-[UIRepeatedAction setRepeatedDelay:];
-[UIRepeatedAction _repeatedTimerFire];
-[UIRepeatedAction delegate];
-[UIRepeatedAction scheduleWithTarget:selector:object:];
-[UIRepeatedAction setPreInvocationDelay:];
-[UIRepeatedAction setSkipInitialFire:];
-[UIRepeatedAction _resetInternalState];
-[UIRepeatedAction preInvocationDelay];
-[UIRepeatedAction _preInvocationTimerFire];
-[UIRepeatedAction initWithTarget:selector:object:];
-[UIRepeatedAction schedule];
```
