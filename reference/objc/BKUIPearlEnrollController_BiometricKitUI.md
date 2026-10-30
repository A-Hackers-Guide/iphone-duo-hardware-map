# `BKUIPearlEnrollController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSViewController`
- Protocols: `BKUIPearlCoachingControllerDelegate`, `BKUIPearlEnrollViewControllerDelegate`
- 14 instance variables, 19 properties, 69 instance methods, 5 class methods

## Instance variables

```
B _systemRotationAnimating;
q _orientation;
B _inSheet;
B _hasBeenPortrait;
@"<BKUIPearlEnrollControllerDelegate>" _delegate;
@"BKIdentity" _existingIdentity;
@"BKUIPearlEnrollViewController" _enrollViewController;
@"BKUIPearlCoachingController" _coachingController;
@"BKUIFullscreenInstructingViewController" _fullscreenInstructingVC;
@"<NSObject>" _rotationChangeToken;
@"<NSObject>" _rotationLockToken;
@"UINavigationBar" _navbarCopy;
@"BKUIOrientationStateHandler" _orientationStateHandler;
@"BKUIPearlEnrollControllerPreloadedState" _preloadState;
```

## Properties

```
@property (T@"BKUIPearlEnrollViewController",&,N,V_enrollViewController) enrollViewController;
@property (T@"BKUIPearlCoachingController",&,N,V_coachingController) coachingController;
@property (T@"BKUIFullscreenInstructingViewController",&,N,V_fullscreenInstructingVC) fullscreenInstructingVC;
@property (TB,N,V_hasBeenPortrait) hasBeenPortrait;
@property (T@"<NSObject>",&,N,V_rotationChangeToken) rotationChangeToken;
@property (T@"<NSObject>",&,N,V_rotationLockToken) rotationLockToken;
@property (T@"UINavigationBar",R,N,V_navbarCopy) navbarCopy;
@property (T@"BKUIOrientationStateHandler",&,N,V_orientationStateHandler) orientationStateHandler;
@property (T@"BKUIPearlEnrollControllerPreloadedState",&,N,V_preloadState) preloadState;
@property (T@"<BKUIPearlEnrollControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N) inBuddy;
@property (TB,N,V_inSheet) inSheet;
@property (TB,N) collectsFramesForAgeVerification;
@property (TQ,N) enrollmentConfiguration;
@property (T@"BKIdentity",&,N,V_existingIdentity) existingIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKUIPearlEnrollController preloadWithCompletion:];
+[BKUIPearlEnrollController isDisplayZoomEnabled];
+[BKUIPearlEnrollController isPearlAvailable];
+[BKUIPearlEnrollController isPearlInterlocked];
+[BKUIPearlEnrollController preloadCollectingFramesForAgeVerification:completion:];
```

## Instance methods

```
-[BKUIPearlEnrollController isModalInPresentation];
-[BKUIPearlEnrollController init];
-[BKUIPearlEnrollController viewWillDisappear:];
-[BKUIPearlEnrollController dealloc];
-[BKUIPearlEnrollController viewDidLoad];
-[BKUIPearlEnrollController prefersHomeIndicatorAutoHidden];
-[BKUIPearlEnrollController containerView];
-[BKUIPearlEnrollController viewWillAppear:];
-[BKUIPearlEnrollController setDelegate:];
-[BKUIPearlEnrollController delegate];
-[BKUIPearlEnrollController viewWillLayoutSubviews];
-[BKUIPearlEnrollController navigationItem];
-[BKUIPearlEnrollController viewDidDisappear:];
-[BKUIPearlEnrollController preferredContentSize];
-[BKUIPearlEnrollController _startObserving];
-[BKUIPearlEnrollController preferredStatusBarStyle];
-[BKUIPearlEnrollController resetLayout];
-[BKUIPearlEnrollController canBeShownFromSuspendedState];
-[BKUIPearlEnrollController inBuddy];
-[BKUIPearlEnrollController setInBuddy:];
-[BKUIPearlEnrollController deviceOrientationDidChange:];
-[BKUIPearlEnrollController setCoachingHidden:animated:];
-[BKUIPearlEnrollController coachingSkipped];
-[BKUIPearlEnrollController hasBeenPortrait];
-[BKUIPearlEnrollController inSheet];
-[BKUIPearlEnrollController pearlEnrollControllerCompleted:];
-[BKUIPearlEnrollController setCustomDetailString:forState:];
-[BKUIPearlEnrollController _copyAndShowInternalNavBar];
-[BKUIPearlEnrollController coachingController];
-[BKUIPearlEnrollController collectsFramesForAgeVerification];
-[BKUIPearlEnrollController deviceOrientationChanged:];
-[BKUIPearlEnrollController deviceOrientationChanged:duration:];
-[BKUIPearlEnrollController diffSystemAndForcedRotationOrientations];
-[BKUIPearlEnrollController doesNeedFullscreenInstructingView];
-[BKUIPearlEnrollController enrollViewController];
-[BKUIPearlEnrollController enrollmentConfiguration];
-[BKUIPearlEnrollController existingIdentity];
-[BKUIPearlEnrollController fullscreenInstructingVC];
-[BKUIPearlEnrollController initWithPreloadedState:];
-[BKUIPearlEnrollController mustShowFullscreenInstructingView];
-[BKUIPearlEnrollController navbarCopy];
-[BKUIPearlEnrollController orientationStateHandler];
-[BKUIPearlEnrollController pearlEnrollViewController:finishedEnrollWithError:];
-[BKUIPearlEnrollController pearlEnrollViewControllerStateChanged:];
-[BKUIPearlEnrollController preloadState];
-[BKUIPearlEnrollController primeWithExternalizedAuthContext:];
-[BKUIPearlEnrollController primeWithPasscode:];
-[BKUIPearlEnrollController removeFullscreenInstructingViewIfNeeded];
-[BKUIPearlEnrollController rotationChangeToken];
-[BKUIPearlEnrollController rotationLockToken];
-[BKUIPearlEnrollController setCoachingController:];
-[BKUIPearlEnrollController setCoachingHidden:animated:completion:];
-[BKUIPearlEnrollController setCollectsFramesForAgeVerification:];
-[BKUIPearlEnrollController setCustomInstructionString:forState:];
-[BKUIPearlEnrollController setEnrollViewController:];
-[BKUIPearlEnrollController setEnrollmentConfiguration:];
-[BKUIPearlEnrollController setExistingIdentity:];
-[BKUIPearlEnrollController setFullscreenInstructingVC:];
-[BKUIPearlEnrollController setHasBeenPortrait:];
-[BKUIPearlEnrollController setInSheet:];
-[BKUIPearlEnrollController setOrientationStateHandler:];
-[BKUIPearlEnrollController setPreloadState:];
-[BKUIPearlEnrollController setRotationChangeToken:];
-[BKUIPearlEnrollController setRotationLockToken:];
-[BKUIPearlEnrollController setTransparencyForCoachingController];
-[BKUIPearlEnrollController setupFullscreenInstructingViewIfNeeded];
-[BKUIPearlEnrollController showFullscreenInstructingView:];
-[BKUIPearlEnrollController showOrHideFullscreenInstructingViewIfNeeded];
-[BKUIPearlEnrollController startInternalGlassesFlow];
```
