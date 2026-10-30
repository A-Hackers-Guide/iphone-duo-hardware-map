# `SBHomeGestureDismissableCoverSheetViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSCoverSheetViewControllerBase`
- Protocols: `SBSystemGestureRecognizerDelegate`, `SBFZStackParticipantDelegate`
- 4 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _wantsHomeGestureOwnership;
B _hasHomeGestureOwnership;
@"SBHomeGesturePanGestureRecognizer" _bottomEdgeRecognizer;
@"SBFZStackParticipant" _zStackParticipant;
```

## Properties

```
@property (T@"SBHomeGesturePanGestureRecognizer",&,N,V_bottomEdgeRecognizer) bottomEdgeRecognizer;
@property (TB,N,V_wantsHomeGestureOwnership) wantsHomeGestureOwnership;
@property (TB,N,V_hasHomeGestureOwnership) hasHomeGestureOwnership;
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (Tq,R,N) zStackParticipantIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHomeGestureDismissableCoverSheetViewController zStackParticipant];
-[SBHomeGestureDismissableCoverSheetViewController setZStackParticipant:];
-[SBHomeGestureDismissableCoverSheetViewController _handleBottomEdgeGestureChanged:];
-[SBHomeGestureDismissableCoverSheetViewController _relinquishHomeGestureOwnership];
-[SBHomeGestureDismissableCoverSheetViewController gestureRecognizer:shouldReceiveTouch:];
-[SBHomeGestureDismissableCoverSheetViewController zStackParticipant:updatePreferences:];
-[SBHomeGestureDismissableCoverSheetViewController viewWillDisappear:];
-[SBHomeGestureDismissableCoverSheetViewController _handleBottomEdgeGestureBegan:];
-[SBHomeGestureDismissableCoverSheetViewController zStackParticipantDidChange:];
-[SBHomeGestureDismissableCoverSheetViewController zStackParticipant:updateZOrderPreferences:];
-[SBHomeGestureDismissableCoverSheetViewController _requestHomeGestureOwnership];
-[SBHomeGestureDismissableCoverSheetViewController setWantsHomeGestureOwnership:];
-[SBHomeGestureDismissableCoverSheetViewController viewForSystemGestureRecognizer:];
-[SBHomeGestureDismissableCoverSheetViewController viewDidAppear:];
-[SBHomeGestureDismissableCoverSheetViewController gestureRecognizerShouldBegin:];
-[SBHomeGestureDismissableCoverSheetViewController _addOrRemoveGestureForCurrentSettings];
-[SBHomeGestureDismissableCoverSheetViewController _handleBottomEdgeGestureEnded:];
-[SBHomeGestureDismissableCoverSheetViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBHomeGestureDismissableCoverSheetViewController wantsHomeGestureOwnership];
-[SBHomeGestureDismissableCoverSheetViewController _handleBottomEdgeGesture:];
-[SBHomeGestureDismissableCoverSheetViewController bottomEdgeRecognizer];
-[SBHomeGestureDismissableCoverSheetViewController hasHomeGestureOwnership];
-[SBHomeGestureDismissableCoverSheetViewController setBottomEdgeRecognizer:];
-[SBHomeGestureDismissableCoverSheetViewController setHasHomeGestureOwnership:];
-[SBHomeGestureDismissableCoverSheetViewController shouldDismissForHomeGestureRecognizer:];
-[SBHomeGestureDismissableCoverSheetViewController zStackParticipantIdentifier];
```
