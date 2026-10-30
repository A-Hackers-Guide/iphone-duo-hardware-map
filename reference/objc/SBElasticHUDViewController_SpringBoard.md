# `SBElasticHUDViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- Protocols: `UIViewControllerTransitioningDelegate`, `SBElasticValueViewControllerDelegate`, `SBHUDViewControlling`
- 2 instance variables, 8 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<SBElasticHUDViewControllerDelegate>" _delegate;
@"SBElasticValueViewController" _elasticValueViewController;
```

## Properties

```
@property (T@"SBElasticValueViewController",R,N,V_elasticValueViewController) elasticValueViewController;
@property (T@"<SBElasticHUDViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBHUDAttachmentDelegate>",W,D,N) attachmentDelegate;
@property (T@"NSArray",R,C,N) physicalButtonSceneTargets;
```

## Instance methods

```
-[SBElasticHUDViewController animationControllerForDismissedController:];
-[SBElasticHUDViewController animationControllerForPresentedController:presentingController:sourceController:];
-[SBElasticHUDViewController physicalButtonSceneTargets];
-[SBElasticHUDViewController triggerButton];
-[SBElasticHUDViewController supportedInterfaceOrientations];
-[SBElasticHUDViewController initWithFactory:];
-[SBElasticHUDViewController viewDidLoad];
-[SBElasticHUDViewController setPositionOffset:];
-[SBElasticHUDViewController viewDidLayoutSubviews];
-[SBElasticHUDViewController reloadData];
-[SBElasticHUDViewController _canShowWhileLocked];
-[SBElasticHUDViewController definesAnimatedDismissal];
-[SBElasticHUDViewController setDelegate:];
-[SBElasticHUDViewController dismissAnimatedWithCompletion:];
-[SBElasticHUDViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBElasticHUDViewController isHUDAttached];
-[SBElasticHUDViewController delegate];
-[SBElasticHUDViewController attachmentIgnoredOrientations];
-[SBElasticHUDViewController setAttachmentDelegate:];
-[SBElasticHUDViewController attachmentDelegate];
-[SBElasticHUDViewController isEqual:];
-[SBElasticHUDViewController elasticValueViewController];
-[SBElasticHUDViewController elasticValueViewControllerCanBePresented:withReason:];
-[SBElasticHUDViewController elasticValueViewControllerNeedsDismissal:];
-[SBElasticHUDViewController initWithElasticValueContentViewController:];
-[SBElasticHUDViewController noteButtonDownWasHit:];
-[SBElasticHUDViewController noteButtonUpWasHit:];
-[SBElasticHUDViewController noteValueDidChange:];
-[SBElasticHUDViewController noteValueWillDeltaStepToValue:];
-[SBElasticHUDViewController setButtonStepCount:];
```
