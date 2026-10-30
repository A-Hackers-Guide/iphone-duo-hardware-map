# `SBContinuityDisplayLayoutPublisher`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayLayoutPublisherObserving`, `FBSDisplayLayoutPublishing`, `BSInvalidatable`
- 14 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SBContinuityDisplayLayoutCoordinator" _coordinator;
@"<BSInvalidatable>" _coordinatorActivation;
@"FBSDisplayLayoutPublisher" _rootPublisher;
@"FBSDisplayLayout" _emptyLayout;
@"NSHashTable" _observers;
@"FBSDisplayConfiguration" _displayConfiguration;
B _activated;
q _pendedInterfaceOrientation;
q _pendedBacklightLevel;
@"NSMutableDictionary" _elementsPendingActivation;
@"NSMutableDictionary" _activeElements;
@"NSMutableDictionary" _transitionsPendingActivation;
@"NSMutableDictionary" _activeTransitions;
B _invalidated;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",C,N) displayConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N) interfaceOrientation;
@property (Tq,N) backlightLevel;
@property (TB,R,N,GisTransitioning) transitioning;
@property (T@"FBSDisplayLayout",R,N) currentLayout;
```

## Instance methods

```
-[SBContinuityDisplayLayoutPublisher interfaceOrientation];
-[SBContinuityDisplayLayoutPublisher setBacklightLevel:];
-[SBContinuityDisplayLayoutPublisher displayConfiguration];
-[SBContinuityDisplayLayoutPublisher addElement:];
-[SBContinuityDisplayLayoutPublisher backlightLevel];
-[SBContinuityDisplayLayoutPublisher setInterfaceOrientation:];
-[SBContinuityDisplayLayoutPublisher removeObserver:];
-[SBContinuityDisplayLayoutPublisher flush];
-[SBContinuityDisplayLayoutPublisher isTransitioning];
-[SBContinuityDisplayLayoutPublisher dealloc];
-[SBContinuityDisplayLayoutPublisher publisher:didUpdateLayout:withTransition:];
-[SBContinuityDisplayLayoutPublisher currentLayout];
-[SBContinuityDisplayLayoutPublisher setDisplayConfiguration:];
-[SBContinuityDisplayLayoutPublisher addObserver:];
-[SBContinuityDisplayLayoutPublisher invalidate];
-[SBContinuityDisplayLayoutPublisher activate];
-[SBContinuityDisplayLayoutPublisher transitionAssertionWithReason:];
-[SBContinuityDisplayLayoutPublisher initWithCoordinator:];
-[SBContinuityDisplayLayoutPublisher _removeElementForKey:];
-[SBContinuityDisplayLayoutPublisher _removeTransitionForKey:];
```
