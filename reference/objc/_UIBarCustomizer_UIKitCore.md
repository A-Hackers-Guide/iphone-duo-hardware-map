# `_UIBarCustomizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragInteractionDelegate`, `UIDropInteractionDelegate`
- 17 instance variables, 21 properties, 60 instance methods, 0 class methods

## Instance variables

```
B _isActive;
B _wasReset;
@"<_UIBarCustomizerDelegate>" _delegate;
@"NSMutableArray" __visibleItems;
@"_UIBarCustomizationSession" __activeSession;
@ _keyboardSuppressionAssertion;
@"UIDragInteraction" _dragInteraction;
@"_UIBarCustomizationContainerView" _containerView;
@"UIView" _dimmingView;
@"UIScrollView" _visibleItemScrollView;
@"UIView" _reservoirContainerView;
@"_UIBarCustomizationItemReservoirView" _reservoir;
Q __dropIndex;
@"NSMutableArray" _ellipsisDotViews;
Q _overflowItemCount;
{CGPoint="x"d"y"d} _lastDragLocation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialSourceFrame;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V__visibleItems) _visibleItems;
@property (T@"_UIBarCustomizationSession",&,N,V__activeSession) _activeSession;
@property (T@,&,N,V_keyboardSuppressionAssertion) keyboardSuppressionAssertion;
@property (T@"UIDragInteraction",&,N,V_dragInteraction) dragInteraction;
@property (T@"_UIBarCustomizationContainerView",&,N,V_containerView) containerView;
@property (T@"UIView",&,N,V_dimmingView) dimmingView;
@property (T@"UIScrollView",&,N,V_visibleItemScrollView) visibleItemScrollView;
@property (T@"UIView",&,N,V_reservoirContainerView) reservoirContainerView;
@property (T@"_UIBarCustomizationItemReservoirView",&,N,V_reservoir) reservoir;
@property (TQ,N,V__dropIndex) _dropIndex;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_initialSourceFrame) initialSourceFrame;
@property (T{CGPoint=dd},N,V_lastDragLocation) lastDragLocation;
@property (TB,N,V_wasReset) wasReset;
@property (T@"NSMutableArray",&,N,V_ellipsisDotViews) ellipsisDotViews;
@property (TQ,N,V_overflowItemCount) overflowItemCount;
@property (T@"<_UIBarCustomizerDelegate>",R,W,N,V_delegate) delegate;
@property (TB,R,N,V_isActive) isActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIBarCustomizer dragInteraction:previewForLiftingItem:session:];
-[_UIBarCustomizer dragInteraction:itemsForBeginningSession:];
-[_UIBarCustomizer dragInteraction:previewForCancellingItem:withDefault:];
-[_UIBarCustomizer dragInteraction:item:willAnimateCancelWithAnimator:];
-[_UIBarCustomizer dropInteraction:sessionDidUpdate:];
-[_UIBarCustomizer dragInteraction:sessionWillBegin:];
-[_UIBarCustomizer dragInteraction:prefersFullSizePreviewsForSession:];
-[_UIBarCustomizer setContainerView:];
-[_UIBarCustomizer dimmingView];
-[_UIBarCustomizer initWithDelegate:];
-[_UIBarCustomizer dragInteraction:session:willEndWithOperation:];
-[_UIBarCustomizer dropInteraction:performDrop:];
-[_UIBarCustomizer dragInteraction];
-[_UIBarCustomizer dropInteraction:canHandleSession:];
-[_UIBarCustomizer dragInteraction:sessionIsRestrictedToDraggingApplication:];
-[_UIBarCustomizer dragInteraction:session:willAddItems:forInteraction:];
-[_UIBarCustomizer _setActive:];
-[_UIBarCustomizer end];
-[_UIBarCustomizer dropInteraction:item:willAnimateDropWithAnimator:];
-[_UIBarCustomizer setDimmingView:];
-[_UIBarCustomizer containerView];
-[_UIBarCustomizer keyboardSuppressionAssertion];
-[_UIBarCustomizer setKeyboardSuppressionAssertion:];
-[_UIBarCustomizer _handleDimmingViewTap:];
-[_UIBarCustomizer delegate];
-[_UIBarCustomizer dragInteraction:itemsForAddingToSession:withTouchAtPoint:];
-[_UIBarCustomizer invalidateLayout];
-[_UIBarCustomizer isActive];
-[_UIBarCustomizer setDragInteraction:];
-[_UIBarCustomizer dropInteraction:previewForDroppingItem:withDefault:];
-[_UIBarCustomizer _reflow];
-[_UIBarCustomizer _activeSession];
-[_UIBarCustomizer _animateDropOrCancelForItem:animator:isCancel:];
-[_UIBarCustomizer _dragInteraction:delayForLiftBeginningAtLocation:];
-[_UIBarCustomizer _dragItemsAtLocation:];
-[_UIBarCustomizer _dropIndex];
-[_UIBarCustomizer _overflowItemBucketSize];
-[_UIBarCustomizer _reflowAnimatedWithAlongsideActions:];
-[_UIBarCustomizer _updateDebugUI];
-[_UIBarCustomizer _visibleItems];
-[_UIBarCustomizer beginWithSession:];
-[_UIBarCustomizer ellipsisDotViews];
-[_UIBarCustomizer initialSourceFrame];
-[_UIBarCustomizer lastDragLocation];
-[_UIBarCustomizer overflowItemCount];
-[_UIBarCustomizer reservoir];
-[_UIBarCustomizer reservoirContainerView];
-[_UIBarCustomizer setEllipsisDotViews:];
-[_UIBarCustomizer setInitialSourceFrame:];
-[_UIBarCustomizer setLastDragLocation:];
-[_UIBarCustomizer setOverflowItemCount:];
-[_UIBarCustomizer setReservoir:];
-[_UIBarCustomizer setReservoirContainerView:];
-[_UIBarCustomizer setVisibleItemScrollView:];
-[_UIBarCustomizer setWasReset:];
-[_UIBarCustomizer set_activeSession:];
-[_UIBarCustomizer set_dropIndex:];
-[_UIBarCustomizer set_visibleItems:];
-[_UIBarCustomizer visibleItemScrollView];
-[_UIBarCustomizer wasReset];
```
