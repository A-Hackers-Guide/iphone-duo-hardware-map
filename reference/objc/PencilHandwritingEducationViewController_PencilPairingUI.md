# `PencilHandwritingEducationViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PencilHandwritingEducationElementViewControllerDelegate`
- 9 instance variables, 14 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _setupComplete;
B _didDisappear;
B _didRunInitialAppearActions;
@"<PencilHandwritingEducationViewControllerDelegate>" _delegate;
@"UISegmentedControl" _segmentedControl;
@"UIView" _containerView;
@"PencilHandwritingEducationElementViewController" _displayedController;
@"NSMutableArray" _viewControllers;
@"NSDate" _appearDate;
```

## Properties

```
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"PencilHandwritingEducationElementViewController",&,N,V_displayedController) displayedController;
@property (T@"NSMutableArray",&,N,V_viewControllers) viewControllers;
@property (TB,N,V_setupComplete) setupComplete;
@property (T@"NSDate",&,N,V_appearDate) appearDate;
@property (TB,N,V_didDisappear) didDisappear;
@property (TB,N,V_didRunInitialAppearActions) didRunInitialAppearActions;
@property (T@"<PencilHandwritingEducationViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) isAnimating;
@property (T@"UISegmentedControl",R,N,V_segmentedControl) segmentedControl;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PencilHandwritingEducationViewController localizedTitle];
```

## Instance methods

```
-[PencilHandwritingEducationViewController setContainerView:];
-[PencilHandwritingEducationViewController traitCollection];
-[PencilHandwritingEducationViewController setSetupComplete:];
-[PencilHandwritingEducationViewController dealloc];
-[PencilHandwritingEducationViewController viewDidLoad];
-[PencilHandwritingEducationViewController containerView];
-[PencilHandwritingEducationViewController _canShowWhileLocked];
-[PencilHandwritingEducationViewController setDelegate:];
-[PencilHandwritingEducationViewController viewDidAppear:];
-[PencilHandwritingEducationViewController setViewControllers:];
-[PencilHandwritingEducationViewController delegate];
-[PencilHandwritingEducationViewController viewDidDisappear:];
-[PencilHandwritingEducationViewController viewControllers];
-[PencilHandwritingEducationViewController setupComplete];
-[PencilHandwritingEducationViewController isAnimating];
-[PencilHandwritingEducationViewController segmentedControl];
-[PencilHandwritingEducationViewController displayedController];
-[PencilHandwritingEducationViewController setDisplayedController:];
-[PencilHandwritingEducationViewController didDisappear];
-[PencilHandwritingEducationViewController doneButtonPressed:];
-[PencilHandwritingEducationViewController setDidDisappear:];
-[PencilHandwritingEducationViewController elementControllerShouldDismiss:];
-[PencilHandwritingEducationViewController _configureViewControllersIfNecessary];
-[PencilHandwritingEducationViewController addControllerToContainer:];
-[PencilHandwritingEducationViewController appearDate];
-[PencilHandwritingEducationViewController beginAnimationIfNecessaryForElementController:delay:];
-[PencilHandwritingEducationViewController calculateFittingHeightByTemporarilyAdjustingFrameForWidth:];
-[PencilHandwritingEducationViewController cancelScheduledAnimations];
-[PencilHandwritingEducationViewController didRunInitialAppearActions];
-[PencilHandwritingEducationViewController elementControllerDidAppear:];
-[PencilHandwritingEducationViewController setAppearDate:];
-[PencilHandwritingEducationViewController setDidRunInitialAppearActions:];
-[PencilHandwritingEducationViewController shouldBeginAnimationForElementController:];
-[PencilHandwritingEducationViewController updateButtonTray:];
```
