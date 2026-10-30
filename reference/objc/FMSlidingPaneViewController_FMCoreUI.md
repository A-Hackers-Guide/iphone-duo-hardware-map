# `FMSlidingPaneViewController`

- Image: [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](../userland/System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FMViewController`
- 11 instance variables, 15 properties, 56 instance methods, 0 class methods

## Instance variables

```
B _didHideToolbar;
@"UIVisualEffect" _paneVisualEffect;
@"<FMSlidingPaneViewControllerDelegate>" _delegate;
d _animationDuration;
d _animationSpringDamping;
d _animationInitialVelocity;
Q _animationOptions;
@"SlidingPaneViewState" _paneState;
@"NSMutableArray" _actionFutures;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _paneInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _paneContentInsets;
```

## Properties

```
@property (T@"SlidingPaneViewState",&,N,V_paneState) paneState;
@property (TB,N,V_didHideToolbar) didHideToolbar;
@property (T@"NSMutableArray",&,N,V_actionFutures) actionFutures;
@property (T@"FMFuture",R,N) currentFuture;
@property (T@"<FMSlidingPaneViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIViewController",R,N) paneViewController;
@property (T@"UIView",R,N) paneView;
@property (T{UIEdgeInsets=dddd},N,V_paneInsets) paneInsets;
@property (T{UIEdgeInsets=dddd},N,V_paneContentInsets) paneContentInsets;
@property (Td,N,V_animationDuration) animationDuration;
@property (Td,N,V_animationSpringDamping) animationSpringDamping;
@property (Td,N,V_animationInitialVelocity) animationInitialVelocity;
@property (TQ,N,V_animationOptions) animationOptions;
@property (T@"UIVisualEffect",&,N,V_paneVisualEffect) paneVisualEffect;
@property (TB,R,N,GisPaneShowing) paneShowing;
```

## Instance methods

```
-[FMSlidingPaneViewController animationOptions];
-[FMSlidingPaneViewController setAnimationOptions:];
-[FMSlidingPaneViewController setAnimationDuration:];
-[FMSlidingPaneViewController animationDuration];
-[FMSlidingPaneViewController initWithNibName:bundle:];
-[FMSlidingPaneViewController viewWillAppear:];
-[FMSlidingPaneViewController setDelegate:];
-[FMSlidingPaneViewController delegate];
-[FMSlidingPaneViewController awakeFromNib];
-[FMSlidingPaneViewController traitCollectionForChildViewController:];
-[FMSlidingPaneViewController dismiss:];
-[FMSlidingPaneViewController paneViewController];
-[FMSlidingPaneViewController animationSpringDamping];
-[FMSlidingPaneViewController _paneParentView];
-[FMSlidingPaneViewController completeFuture:];
-[FMSlidingPaneViewController didPresentPane:inRect:animated:];
-[FMSlidingPaneViewController newActionFuture];
-[FMSlidingPaneViewController _normalizeSize:];
-[FMSlidingPaneViewController _createPaneContentConstraintsForState:];
-[FMSlidingPaneViewController _createPaneViewForState:];
-[FMSlidingPaneViewController _crossDissolveOldPaneState:newPaneState:animated:completion:];
-[FMSlidingPaneViewController _dismissPaneState:animated:completion:];
-[FMSlidingPaneViewController _metricsFromEdgeInsets:];
-[FMSlidingPaneViewController _paneFrameChanged:];
-[FMSlidingPaneViewController _preferredSizeForPaneState:];
-[FMSlidingPaneViewController _presentPaneState:animated:interactive:completion:];
-[FMSlidingPaneViewController _removeChildViewControllerForState:];
-[FMSlidingPaneViewController actionFutures];
-[FMSlidingPaneViewController animationInitialVelocity];
-[FMSlidingPaneViewController commonConfiguration];
-[FMSlidingPaneViewController currentFuture];
-[FMSlidingPaneViewController didDismissPane:animated:];
-[FMSlidingPaneViewController didHideToolbar];
-[FMSlidingPaneViewController dismiss:forEvent:];
-[FMSlidingPaneViewController dismissPaneViewControllerAnimated:completion:];
-[FMSlidingPaneViewController dismissSegue:];
-[FMSlidingPaneViewController isPaneShowing];
-[FMSlidingPaneViewController paneContentInsets];
-[FMSlidingPaneViewController paneInsets];
-[FMSlidingPaneViewController paneSizeChanged:forViewController:];
-[FMSlidingPaneViewController paneState];
-[FMSlidingPaneViewController paneView];
-[FMSlidingPaneViewController paneVisualEffect];
-[FMSlidingPaneViewController presentPaneViewController:fromEdge:animated:completion:];
-[FMSlidingPaneViewController presentPaneViewController:fromEdge:withPercent:completion:];
-[FMSlidingPaneViewController setActionFutures:];
-[FMSlidingPaneViewController setAnimationInitialVelocity:];
-[FMSlidingPaneViewController setAnimationSpringDamping:];
-[FMSlidingPaneViewController setDidHideToolbar:];
-[FMSlidingPaneViewController setPaneContentInsets:];
-[FMSlidingPaneViewController setPaneInsets:];
-[FMSlidingPaneViewController setPaneState:];
-[FMSlidingPaneViewController setPaneVisualEffect:];
-[FMSlidingPaneViewController setPresentingConstraintConstant:];
-[FMSlidingPaneViewController willDismissPane:animated:];
-[FMSlidingPaneViewController willPresentPane:inRect:animated:];
```
