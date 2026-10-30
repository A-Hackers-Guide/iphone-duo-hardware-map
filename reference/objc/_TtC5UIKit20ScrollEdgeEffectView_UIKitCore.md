# `_TtC5UIKit20ScrollEdgeEffectView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyObserver`
- 15 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
UIKit.ScrollEdgeEffectView.BackdropView backgroundCapture;
UIKit.ScrollEdgeEffectView.DebugView ? debugOverlay;
Swift.Bool debugOverlayEnabled;
_$sSo18UIScrollEdgeEffectC effect;
UIKit.ScrollEdgeEffectView.v8.ScrollPocket pocket;
Swift.Bool shouldHideAtTop;
Swift.Bool hasPalette;
UIKit.PocketElectionState.Ballot ? pocketBallot;
__C.UIRectEdge edge;
Swift.Bool reducedTransparency;
Swift.Bool isOwningViewEffectivelyHidden;
_$sSo6UIViewCSgXw owningView;
UIKit.ScrollEdgeEffectView.PocketElementModel elementModel;
UIKit.ScrollEdgeEffectView.ObservableState observableState;
UIKit._PocketDebugInputValues ? _debugSnapshot;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},N,R) alignmentRectInsets;
@property (TB,N,R) _shouldInformFocusAboutBecomingVisible;
@property (TB,N,R) isTransparentFocusItem;
@property (TB,N,R) eligibleForFocusOcclusion;
@property (TB,N,R) eligibleForFocusInteraction;
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) _debugElection;
@property (T@"NSString",N,R) _debugBallot;
@property (T@"_TtC5UIKit23_PocketDebugInputValues",N,&,V_debugSnapshot) _debugSnapshot;
```

## Class methods

```
+[_TtC5UIKit20ScrollEdgeEffectView _supportsInvalidatingFocusCache];
```

## Instance methods

```
-[_TtC5UIKit20ScrollEdgeEffectView _isEligibleForFocusInteraction];
-[_TtC5UIKit20ScrollEdgeEffectView focusItemsInRect:];
-[_TtC5UIKit20ScrollEdgeEffectView alignmentRectInsets];
-[_TtC5UIKit20ScrollEdgeEffectView layoutSubviews];
-[_TtC5UIKit20ScrollEdgeEffectView hitTest:withEvent:];
-[_TtC5UIKit20ScrollEdgeEffectView _didMoveFromWindow:toWindow:];
-[_TtC5UIKit20ScrollEdgeEffectView _debugBallot];
-[_TtC5UIKit20ScrollEdgeEffectView _debugSnapshot];
-[_TtC5UIKit20ScrollEdgeEffectView settings:changedValueForKey:];
-[_TtC5UIKit20ScrollEdgeEffectView updateDebugView];
-[_TtC5UIKit20ScrollEdgeEffectView _debugElection];
-[_TtC5UIKit20ScrollEdgeEffectView _isEligibleForFocusOcclusion];
-[_TtC5UIKit20ScrollEdgeEffectView _shouldInformFocusAboutBecomingVisible];
-[_TtC5UIKit20ScrollEdgeEffectView description];
-[_TtC5UIKit20ScrollEdgeEffectView initWithCoder:];
-[_TtC5UIKit20ScrollEdgeEffectView isTransparentFocusItem];
-[_TtC5UIKit20ScrollEdgeEffectView didMoveToSuperview];
-[_TtC5UIKit20ScrollEdgeEffectView set_debugSnapshot:];
-[_TtC5UIKit20ScrollEdgeEffectView initWithFrame:];
```
