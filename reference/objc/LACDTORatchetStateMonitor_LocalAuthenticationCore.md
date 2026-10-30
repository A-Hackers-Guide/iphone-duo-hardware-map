# `LACDTORatchetStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTORatchetStateProvider`, `LACDTOEventProducer`, `LACDTOEventHandler`, `LACDTOPolicyEvaluationControllerObserver`
- 5 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<LACDTORatchetStateProvider>" _ratchetStateProvider;
@"LACTimer" _timer;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"<LACDTOEventBus>" eventBus;
@"LACDTORatchetState" _ratchetState;
```

## Properties

```
@property (T@"LACDTORatchetState",R,N,V_ratchetState) ratchetState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACDTOEventBus>",&,N,VeventBus) eventBus;
```

## Instance methods

```
-[LACDTORatchetStateMonitor setRatchetState:];
-[LACDTORatchetStateMonitor ratchetState];
-[LACDTORatchetStateMonitor _scheduleNextStatusCheck];
-[LACDTORatchetStateMonitor eventBus];
-[LACDTORatchetStateMonitor handleEvent:sender:];
-[LACDTORatchetStateMonitor initWithRatchetStateProvider:workQueue:];
-[LACDTORatchetStateMonitor policyController:didFinishPolicyEvaluation:result:];
-[LACDTORatchetStateMonitor policyController:willStartPolicyEvaluation:];
-[LACDTORatchetStateMonitor ratchetStateCompositeWithCompletion:];
-[LACDTORatchetStateMonitor ratchetStateWithCompletion:];
-[LACDTORatchetStateMonitor setEventBus:];
```
