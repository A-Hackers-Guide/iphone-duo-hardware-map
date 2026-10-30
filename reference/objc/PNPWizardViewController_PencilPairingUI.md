# `PNPWizardViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- Protocols: `FMUIAccessoryOnboardingCoordinatorDelegate`, `_TtP15PencilPairingUI28PNPWelcomeControllerDelegate_`, `UINavigationControllerDelegate`
- 17 instance variables, 4 properties, 27 instance methods, 0 class methods

## Instance variables

```
? wizardDelegate;
B usesExtraContentInsets;
B showsIcon;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 deviceType;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 deviceState;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 controllerFlow;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 watchdogTimer;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 controllerQueue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 onboardingStyle;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pairingEducationController;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 onDidTapStartTour;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pendingInitialPairingMode;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 controllerIndex;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 hasScribbleKeyboard;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 didCreateFindMyCoordinator;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 findMyCoordinator;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 controllersToRemove;
```

## Properties

```
@property (T@"<PNPWizardViewDelegate>",N,W,VwizardDelegate) wizardDelegate;
@property (TB,N,VusesExtraContentInsets) usesExtraContentInsets;
@property (TB,N,VshowsIcon) showsIcon;
@property (TQ,N,R) supportedInterfaceOrientations;
```

## Instance methods

```
-[PNPWizardViewController navigationController:didShowViewController:animated:];
-[PNPWizardViewController navigationController:willShowViewController:animated:];
-[PNPWizardViewController initWithNavigationBarClass:toolbarClass:];
-[PNPWizardViewController supportedInterfaceOrientations];
-[PNPWizardViewController prepareForPresentation];
-[PNPWizardViewController viewDidLoad];
-[PNPWizardViewController initWithNibName:bundle:];
-[PNPWizardViewController _canShowWhileLocked];
-[PNPWizardViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[PNPWizardViewController initWithCoder:];
-[PNPWizardViewController initWithRootViewController:];
-[PNPWizardViewController setShowsIcon:];
-[PNPWizardViewController showsIcon];
-[PNPWizardViewController didCompleteAccessoryOnboarding:pairingSuccessful:];
-[PNPWizardViewController findMyNewPencilPairingSucceeded];
-[PNPWizardViewController controllerFor:buttonType:];
-[PNPWizardViewController currentOnboardingStyle];
-[PNPWizardViewController deviceStateDidChange];
-[PNPWizardViewController isShowingPairingEducationPane];
-[PNPWizardViewController setUsesExtraContentInsets:];
-[PNPWizardViewController setWizardDelegate:];
-[PNPWizardViewController transitionToEducationFlowIfNecessary:];
-[PNPWizardViewController transitionToPairingMode:];
-[PNPWizardViewController usesExtraContentInsets];
-[PNPWizardViewController welcomeControllerButtonDidPress:intent:];
-[PNPWizardViewController welcomeControllerWith:buttonType:deviceType:];
-[PNPWizardViewController wizardDelegate];
```
