# `AMPOnboardingViewController`

- Image: [`/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI`](../userland/System__Library__PrivateFrameworks__AMPCoreUI.framework__AMPCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIScrollViewDelegate`
- 11 instance variables, 18 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _viewHasAppeared;
@"NSString" _titleText;
@"NSString" _descriptionText;
@"NSString" _primaryButtonText;
@"OBPrivacyLinkController" _privacyLinkController;
@? _primaryButtonCallback;
@"AMSUIOnboardingViewController" _onboardingController;
@"UIImage" _image;
@"UIVisualEffectView" _statusBarVisualEffectView;
@"_UIBackdropView" _backdropView;
@"NSObject<OS_dispatch_queue>" _metricsQueue;
```

## Properties

```
@property (T@"AMSUIOnboardingViewController",&,N,V_onboardingController) onboardingController;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"NSString",&,N,V_titleText) titleText;
@property (T@"NSString",&,N,V_descriptionText) descriptionText;
@property (T@"NSString",&,N,V_primaryButtonText) primaryButtonText;
@property (TB,R,N) isPresentedInFormSheet;
@property (T@"UIVisualEffectView",&,N,V_statusBarVisualEffectView) statusBarVisualEffectView;
@property (T@"_UIBackdropView",&,N,V_backdropView) backdropView;
@property (T@"UITraitCollection",R,N) cappedTraitCollection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_metricsQueue) metricsQueue;
@property (TB,N,V_viewHasAppeared) viewHasAppeared;
@property (T@"UIImage",R,N) headerImage;
@property (T@"OBPrivacyLinkController",R,N,V_privacyLinkController) privacyLinkController;
@property (T@?,C,N,V_primaryButtonCallback) primaryButtonCallback;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AMPOnboardingViewController setBackdropView:];
-[AMPOnboardingViewController onboardingController];
-[AMPOnboardingViewController descriptionText];
-[AMPOnboardingViewController setOnboardingController:];
-[AMPOnboardingViewController backdropView];
-[AMPOnboardingViewController isModalInPresentation];
-[AMPOnboardingViewController setMetricsQueue:];
-[AMPOnboardingViewController supportedInterfaceOrientations];
-[AMPOnboardingViewController setDescriptionText:];
-[AMPOnboardingViewController setTitleText:];
-[AMPOnboardingViewController viewDidLoad];
-[AMPOnboardingViewController viewDidLayoutSubviews];
-[AMPOnboardingViewController titleText];
-[AMPOnboardingViewController viewWillAppear:];
-[AMPOnboardingViewController viewDidAppear:];
-[AMPOnboardingViewController metricsQueue];
-[AMPOnboardingViewController traitCollectionDidChange:];
-[AMPOnboardingViewController image];
-[AMPOnboardingViewController setImage:];
-[AMPOnboardingViewController headerImage];
-[AMPOnboardingViewController privacyLinkController];
-[AMPOnboardingViewController primaryButtonText];
-[AMPOnboardingViewController viewHasAppeared];
-[AMPOnboardingViewController cappedTraitCollection];
-[AMPOnboardingViewController childTraitCollectionForViewController:];
-[AMPOnboardingViewController didTapPrimaryButton:];
-[AMPOnboardingViewController initWithHeaderImage:titleText:descriptionText:primaryButtonText:privacyLinkController:];
-[AMPOnboardingViewController initWithTitleText:features:primaryButtonText:privacyLinkController:];
-[AMPOnboardingViewController isPresentedInFormSheet];
-[AMPOnboardingViewController primaryButtonCallback];
-[AMPOnboardingViewController setPrimaryButtonCallback:];
-[AMPOnboardingViewController setPrimaryButtonText:];
-[AMPOnboardingViewController setViewHasAppeared:];
-[AMPOnboardingViewController updateOverrideTraits];
-[AMPOnboardingViewController setStatusBarVisualEffectView:];
-[AMPOnboardingViewController statusBarVisualEffectView];
```
