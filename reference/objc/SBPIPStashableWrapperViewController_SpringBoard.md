# `SBPIPStashableWrapperViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PTSettingsKeyPathObserver`
- 21 instance variables, 10 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"SBPIPStashVisualSettings" _settings;
@"SBPIPShadowSettings" _shadowSettings;
@"UIView" _containerView;
@"UIView" _shadowView;
@"SBPIPStashView" _stashView;
@"UIView" _tabShadowView;
@"SBPIPStashedMaskView" _stashMaskView;
@"SBPortalView" _leftSideContentPortalView;
@"SBPortalView" _rightSideContentPortalView;
B _interactivelyResizing;
B _stashTabHidden;
B _stashTabShownLeft;
Q _inFlightStashTabAnimationIdentifier;
Q _inFlightStashProgressAnimationIdentifier;
@"UITapGestureRecognizer" _stashedTapGestureRecognizer;
@"UIViewController" _contentViewController;
@"UIView" _contentView;
d _cornerRadiusMetric;
B _stashed;
@"<SBPIPStashableWrapperViewControllerDelegate>" _delegate;
{CGSize="width"d"height"d} _minimumStashTabSize;
```

## Properties

```
@property (T@"<SBPIPStashableWrapperViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",R,N) contentContainerView;
@property (TB,N,GisInteractivelyResizing,V_interactivelyResizing) interactivelyResizing;
@property (T{CGSize=dd},N,V_minimumStashTabSize) minimumStashTabSize;
@property (TB,N,V_stashed) stashed;
@property (TB,R,N) isStashTabHidden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPStashableWrapperViewController preferredInterfaceOrientationForPresentation];
-[SBPIPStashableWrapperViewController isInteractivelyResizing];
-[SBPIPStashableWrapperViewController dealloc];
-[SBPIPStashableWrapperViewController viewDidLoad];
-[SBPIPStashableWrapperViewController _continuousCornerRadius];
-[SBPIPStashableWrapperViewController setDelegate:];
-[SBPIPStashableWrapperViewController loadView];
-[SBPIPStashableWrapperViewController delegate];
-[SBPIPStashableWrapperViewController viewWillLayoutSubviews];
-[SBPIPStashableWrapperViewController contentContainerView];
-[SBPIPStashableWrapperViewController preferredContentSize];
-[SBPIPStashableWrapperViewController settings:changedValueForKeyPath:];
-[SBPIPStashableWrapperViewController stashed];
-[SBPIPStashableWrapperViewController _addMaskViewSubviewIfNeeded];
-[SBPIPStashableWrapperViewController _handleTapWhileStashedGestureRecognizer:];
-[SBPIPStashableWrapperViewController _layoutStashTabViewsIfNeeded];
-[SBPIPStashableWrapperViewController _resetStashTabViewsIfPossible];
-[SBPIPStashableWrapperViewController _setPortalActive:left:];
-[SBPIPStashableWrapperViewController _setStashMaskActive:];
-[SBPIPStashableWrapperViewController _setStashedTabHidden:left:];
-[SBPIPStashableWrapperViewController _updateContentCornerRadiusForMaskActive:];
-[SBPIPStashableWrapperViewController isStashTabHidden];
-[SBPIPStashableWrapperViewController minimumStashTabSize];
-[SBPIPStashableWrapperViewController setInteractivelyResizing:];
-[SBPIPStashableWrapperViewController setMinimumStashTabSize:];
-[SBPIPStashableWrapperViewController setStashProgress:];
-[SBPIPStashableWrapperViewController setStashed:];
-[SBPIPStashableWrapperViewController _applyDropShadowSettings:toView:];
-[SBPIPStashableWrapperViewController _newShadowViewWithSettings:];
-[SBPIPStashableWrapperViewController _setStashProgress:animated:];
-[SBPIPStashableWrapperViewController initWithContentViewController:cornerRadius:stashVisualSettings:shadowSettings:];
-[SBPIPStashableWrapperViewController setStashTabHidden:left:withSpringBehavior:completion:];
-[SBPIPStashableWrapperViewController setStashed:animated:];
```
