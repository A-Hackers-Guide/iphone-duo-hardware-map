# `SBInsertionDodgingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDodgingModifier`
- 4 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
Q _phase;
{CGPoint="x"d"y"d} _initialCenter;
{CGSize="width"d"height"d} _initialSize;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T{CGPoint=dd},N,V_initialCenter) initialCenter;
@property (T{CGSize=dd},N,V_initialSize) initialSize;
@property (TQ,N,V_phase) phase;
```

## Instance methods

```
-[SBInsertionDodgingModifier phase];
-[SBInsertionDodgingModifier identifier];
-[SBInsertionDodgingModifier setIdentifier:];
-[SBInsertionDodgingModifier setPhase:];
-[SBInsertionDodgingModifier setInitialSize:];
-[SBInsertionDodgingModifier initialSize];
-[SBInsertionDodgingModifier handleAnimationCompletionEvent:];
-[SBInsertionDodgingModifier _animationDidCompleteEventName];
-[SBInsertionDodgingModifier _modelDidUpdateEventName];
-[SBInsertionDodgingModifier animationBehaviorModeForIdentifier:];
-[SBInsertionDodgingModifier framesForIdentifiers];
-[SBInsertionDodgingModifier handleCustomEvent:];
-[SBInsertionDodgingModifier handleInsertionEvent:];
-[SBInsertionDodgingModifier initWithIdentifier:initialCenter:initialSize:];
-[SBInsertionDodgingModifier initialCenter];
-[SBInsertionDodgingModifier modelForInvalidatedModel:];
-[SBInsertionDodgingModifier setInitialCenter:];
```
