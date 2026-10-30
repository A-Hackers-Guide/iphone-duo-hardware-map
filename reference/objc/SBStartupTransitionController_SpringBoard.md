# `SBStartupTransitionController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSTransactionObserver`, `BSDescriptionProviding`, `BSTransactionObserver`
- 7 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBInitialRestartState" _initialRestartState;
@"SBStartupTransitionContextPersistence" _transitionContextPersistence;
@"SBStartupTransitionFactory" _transitionFactory;
@"BSTransaction<SBStartupTransition>" _transition;
@"BSTransactionBlockObserver" _transitionObserver;
B _ranOnce;
@"NSSet" _renderOverlayDismissActions;
```

## Properties

```
@property (T@"BSTransaction<SBStartupTransition>",R,N,V_transition) startupTransition;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStartupTransitionController transactionDidComplete:];
-[SBStartupTransitionController succinctDescriptionBuilder];
-[SBStartupTransitionController descriptionWithMultilinePrefix:];
-[SBStartupTransitionController succinctDescription];
-[SBStartupTransitionController description];
-[SBStartupTransitionController descriptionBuilderWithMultilinePrefix:];
-[SBStartupTransitionController transactionDidBegin:];
-[SBStartupTransitionController _readTransitionContext];
-[SBStartupTransitionController _saveContextFromTransitionContext:];
-[SBStartupTransitionController _transitionForContext:outDestination:];
-[SBStartupTransitionController runStartupTransitionWithInitialRestartState:callbackBlock:];
-[SBStartupTransitionController startupTransition];
```
