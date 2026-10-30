# `PencilEducationViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PKScribbleInteractionDelegate`, `PencilEducationElementViewControllerDelegate`
- 16 instance variables, 19 properties, 47 instance methods, 1 class methods

## Instance variables

```
@"NSLayoutConstraint" _segmentedControlWidthConstraint;
@"NSLayoutConstraint" _containerViewWidthConstraint;
B _alternateLayout;
B _setupComplete;
B _didDisappear;
B _didRunInitialAppearActions;
B _inhibitAnimation;
@"<PencilEducationViewControllerDelegate>" _delegate;
@"UISegmentedControl" _segmentedControl;
q _deviceType;
@"UIView" _containerView;
@"PencilEducationElementViewController" _displayedController;
@"NSMutableArray" _viewControllers;
Q _pendingTransitionIndex;
Q _animationBeginRequestIndex;
@"NSDate" _appearDate;
```

## Properties

```
@property (T@"UISegmentedControl",&,N,V_segmentedControl) segmentedControl;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"PencilEducationElementViewController",&,N,V_displayedController) displayedController;
@property (T@"NSMutableArray",&,N,V_viewControllers) viewControllers;
@property (TQ,N,V_pendingTransitionIndex) pendingTransitionIndex;
@property (TQ,N,V_animationBeginRequestIndex) animationBeginRequestIndex;
@property (TB,N,V_setupComplete) setupComplete;
@property (T@"NSDate",&,N,V_appearDate) appearDate;
@property (TB,N,V_didDisappear) didDisappear;
@property (TB,N,V_didRunInitialAppearActions) didRunInitialAppearActions;
@property (TB,N,V_inhibitAnimation) inhibitAnimation;
@property (T@"<PencilEducationViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) isAnimating;
@property (Tq,R,N,V_deviceType) deviceType;
@property (TB,N,V_alternateLayout) alternateLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PencilEducationViewController localizedTitle];
```

## Instance methods

```
-[PencilEducationViewController setContainerView:];
-[PencilEducationViewController observeValueForKeyPath:ofObject:change:context:];
-[PencilEducationViewController traitCollection];
-[PencilEducationViewController setSetupComplete:];
-[PencilEducationViewController deviceType];
-[PencilEducationViewController dealloc];
-[PencilEducationViewController viewDidLoad];
-[PencilEducationViewController viewDidLayoutSubviews];
-[PencilEducationViewController containerView];
-[PencilEducationViewController _canShowWhileLocked];
-[PencilEducationViewController setDelegate:];
-[PencilEducationViewController viewDidAppear:];
-[PencilEducationViewController setViewControllers:];
-[PencilEducationViewController initWithDeviceType:];
-[PencilEducationViewController setAlternateLayout:];
-[PencilEducationViewController delegate];
-[PencilEducationViewController viewDidDisappear:];
-[PencilEducationViewController viewControllers];
-[PencilEducationViewController setupComplete];
-[PencilEducationViewController isAnimating];
-[PencilEducationViewController alternateLayout];
-[PencilEducationViewController segmentedControl];
-[PencilEducationViewController setSegmentedControl:];
-[PencilEducationViewController displayedController];
-[PencilEducationViewController setDisplayedController:];
-[PencilEducationViewController didDisappear];
-[PencilEducationViewController segmentedControlDidChange:];
-[PencilEducationViewController doneButtonPressed:];
-[PencilEducationViewController setDidDisappear:];
-[PencilEducationViewController _configureViewControllersIfNecessary];
-[PencilEducationViewController addControllerToContainer:];
-[PencilEducationViewController animationBeginRequestIndex];
-[PencilEducationViewController appearDate];
-[PencilEducationViewController beginAnimationIfNecessaryForElementController:delay:];
-[PencilEducationViewController calculateFittingHeightByTemporarilyAdjustingFrameForWidth:];
-[PencilEducationViewController cancelScheduledAnimations];
-[PencilEducationViewController didRunInitialAppearActions];
-[PencilEducationViewController elementControllerDidAppear:];
-[PencilEducationViewController elementControllerWillReplay:];
-[PencilEducationViewController inhibitAnimation];
-[PencilEducationViewController pendingTransitionIndex];
-[PencilEducationViewController setAnimationBeginRequestIndex:];
-[PencilEducationViewController setAppearDate:];
-[PencilEducationViewController setDidRunInitialAppearActions:];
-[PencilEducationViewController setInhibitAnimation:];
-[PencilEducationViewController setPendingTransitionIndex:];
-[PencilEducationViewController shouldBeginAnimationForElementController:];
```
