# `SBSystemNotesPositionHyperregionComposer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPIPPositionHyperregionComposing`
- 7 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBPIPPositionHyperregionLibrary" _regionsLibrary;
Q _state;
{CGSize="width"d"height"d} _dismissToSize;
Q _offscreenCorners;
i _animationState;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"<SBPIPPositionHyperregionComposerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBPIPPositionHyperregionComposerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",?,C,N) connectedWindowScenes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemNotesPositionHyperregionComposer init];
-[SBSystemNotesPositionHyperregionComposer dealloc];
-[SBSystemNotesPositionHyperregionComposer invalidate];
-[SBSystemNotesPositionHyperregionComposer setDelegate:];
-[SBSystemNotesPositionHyperregionComposer delegate];
-[SBSystemNotesPositionHyperregionComposer _setupStateCapture];
-[SBSystemNotesPositionHyperregionComposer description];
-[SBSystemNotesPositionHyperregionComposer _addOffscreenCornersToRegions:geometry:];
-[SBSystemNotesPositionHyperregionComposer canonicalPositionForPoint:proposedPosition:geometry:interaction:];
-[SBSystemNotesPositionHyperregionComposer defaultCornerPositionForLayoutSettingsPosition:proposedCenter:geometry:interaction:];
-[SBSystemNotesPositionHyperregionComposer performActionsWithTransientStateChange:];
-[SBSystemNotesPositionHyperregionComposer positionRegionsForRegions:geometry:interaction:];
-[SBSystemNotesPositionHyperregionComposer setupForEdgeProtectCornerSwipe];
-[SBSystemNotesPositionHyperregionComposer setupForInteractiveCornerGesture];
-[SBSystemNotesPositionHyperregionComposer setupForInteractiveCornerGestureEnd];
-[SBSystemNotesPositionHyperregionComposer setupForInteractiveDismissalToSize:];
-[SBSystemNotesPositionHyperregionComposer setupForStandardBehavior];
-[SBSystemNotesPositionHyperregionComposer setupForSwipesFromCorners:animated:];
```
