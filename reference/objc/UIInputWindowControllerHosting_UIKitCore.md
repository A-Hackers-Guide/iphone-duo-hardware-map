# `UIInputWindowControllerHosting`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _hostingItems;
Q _currentState;
B _requiresConstraintUpdate;
i _extraHostsRequired;
@"UIInputWindowController" _owner;
```

## Properties

```
@property (Ti,N,V_extraHostsRequired) extraHostsRequired;
@property (T@"UIInputWindowController",W,N,V_owner) owner;
@property (T@"NSArray",R,&,N) allHostingItems;
@property (TB,N,V_requiresConstraintUpdate) requiresConstraintUpdate;
```

## Instance methods

```
-[UIInputWindowControllerHosting setNeedsLayout];
-[UIInputWindowControllerHosting removeMatchMoveAnimationIfNeeded];
-[UIInputWindowControllerHosting _updateBackdropViews];
-[UIInputWindowControllerHosting clearInputViewEdgeConstraints];
-[UIInputWindowControllerHosting clearInputAssistantViewEdgeConstraints];
-[UIInputWindowControllerHosting initializeTranslateGestureRecognizerIfNecessary];
-[UIInputWindowControllerHosting removeInputAssistantHostView];
-[UIInputWindowControllerHosting extendKeyboardBackdropHeight:withDuration:];
-[UIInputWindowControllerHosting disableViewSizingConstraints:forNewView:];
-[UIInputWindowControllerHosting unloadForPlacement];
-[UIInputWindowControllerHosting updateEmptyHeightConstraint];
-[UIInputWindowControllerHosting updateViewSizingConstraints];
-[UIInputWindowControllerHosting updateCombinedBackdropViewAnimated:forKeyboardUp:];
-[UIInputWindowControllerHosting resetBackdropHeight];
-[UIInputWindowControllerHosting resetInputViewVisibility];
-[UIInputWindowControllerHosting updateConstraintInsets];
-[UIInputWindowControllerHosting owner];
-[UIInputWindowControllerHosting subPlacementFromPlacement:forHost:];
-[UIInputWindowControllerHosting updateViewConstraints];
-[UIInputWindowControllerHosting visibleFrame];
-[UIInputWindowControllerHosting layoutIfNeeded];
-[UIInputWindowControllerHosting indexOfHost:];
-[UIInputWindowControllerHosting scrollTrackingView];
-[UIInputWindowControllerHosting itemForPurpose:];
-[UIInputWindowControllerHosting allHostingItems];
-[UIInputWindowControllerHosting setRequiresConstraintUpdate:];
-[UIInputWindowControllerHosting initWithHost:];
-[UIInputWindowControllerHosting setOwner:];
-[UIInputWindowControllerHosting reloadForPlacementForInputViewSet:];
-[UIInputWindowControllerHosting setInputSetView:forType:];
-[UIInputWindowControllerHosting requiresConstraintUpdate];
-[UIInputWindowControllerHosting placementForHost:];
-[UIInputWindowControllerHosting _inputViewPadding];
-[UIInputWindowControllerHosting expectedPlacementForHost:];
-[UIInputWindowControllerHosting setExtraHostsRequired:];
-[UIInputWindowControllerHosting removeAllAnimations];
-[UIInputWindowControllerHosting clearInputAccessoryViewEdgeConstraints];
-[UIInputWindowControllerHosting removeCombinedBackdropViewIfNeeded];
-[UIInputWindowControllerHosting performForInputAccessoryBackdropViews:];
-[UIInputWindowControllerHosting extraHostsRequired];
-[UIInputWindowControllerHosting useLayoutHostingItem];
-[UIInputWindowControllerHosting host:isForPurpose:];
-[UIInputWindowControllerHosting item:isForPurpose:];
-[UIInputWindowControllerHosting updateBackdropViewForSplitKeyboard];
```
