# `SBTransientUIInteractionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemGestureRecognizerDelegate`
- 8 instance variables, 13 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"SBFailingSystemGestureRecognizer" _dismissGestureRecognizer;
@"UITapGestureRecognizer" _unhideTapRecognizer;
@"UITapGestureRecognizer" _unhideDoubleTapRecognizer;
@"UIPanGestureRecognizer" _indirectPanRecognizer;
@"NSHashTable" _tapToDismissParticipants;
@"NSHashTable" _tapToUnhideParticipants;
@"NSHashTable" _indirectPanToParticipants;
@"SBSystemGestureManager" _systemGestureManager;
```

## Properties

```
@property (T@"SBFailingSystemGestureRecognizer",&,N,V_dismissGestureRecognizer) dismissGestureRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_unhideTapRecognizer) unhideTapRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_unhideDoubleTapRecognizer) unhideDoubleTapRecognizer;
@property (T@"UIPanGestureRecognizer",&,N,V_indirectPanRecognizer) indirectPanRecognizer;
@property (T@"NSHashTable",&,N,V_tapToDismissParticipants) tapToDismissParticipants;
@property (T@"NSHashTable",&,N,V_tapToUnhideParticipants) tapToUnhideParticipants;
@property (T@"NSHashTable",&,N,V_indirectPanToParticipants) indirectPanToParticipants;
@property (T@"SBSystemGestureManager",W,N,V_systemGestureManager) systemGestureManager;
@property (T@"UIWindow",R,N) window;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTransientUIInteractionManager setSystemGestureManager:];
-[SBTransientUIInteractionManager setUnhideTapRecognizer:];
-[SBTransientUIInteractionManager gestureRecognizer:shouldReceiveTouch:];
-[SBTransientUIInteractionManager dismissGestureRecognizer];
-[SBTransientUIInteractionManager indirectPanToParticipants];
-[SBTransientUIInteractionManager unregisterParticipantForTapToUnhide:];
-[SBTransientUIInteractionManager window];
-[SBTransientUIInteractionManager setIndirectPanRecognizer:];
-[SBTransientUIInteractionManager viewForSystemGestureRecognizer:];
-[SBTransientUIInteractionManager _screenWasIndirectPannedToDismiss:];
-[SBTransientUIInteractionManager unregisterParticipantForTapToDismiss:];
-[SBTransientUIInteractionManager setIndirectPanToParticipants:];
-[SBTransientUIInteractionManager systemGestureManager];
-[SBTransientUIInteractionManager registerParticipantForTapToDismiss:];
-[SBTransientUIInteractionManager unregisterParticipantForIndirectPanToDismiss:];
-[SBTransientUIInteractionManager setTapToUnhideParticipants:];
-[SBTransientUIInteractionManager initWithSystemGestureManager:];
-[SBTransientUIInteractionManager gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBTransientUIInteractionManager setTapToDismissParticipants:];
-[SBTransientUIInteractionManager indirectPanRecognizer];
-[SBTransientUIInteractionManager tapToDismissParticipants];
-[SBTransientUIInteractionManager unhideDoubleTapRecognizer];
-[SBTransientUIInteractionManager registerParticipantForTapToUnhide:];
-[SBTransientUIInteractionManager tapToUnhideParticipants];
-[SBTransientUIInteractionManager registerParticipantForIndirectPanToDismiss:];
-[SBTransientUIInteractionManager setUnhideDoubleTapRecognizer:];
-[SBTransientUIInteractionManager setDismissGestureRecognizer:];
-[SBTransientUIInteractionManager unhideTapRecognizer];
-[SBTransientUIInteractionManager _screenWasTappedToUnhide:];
```
