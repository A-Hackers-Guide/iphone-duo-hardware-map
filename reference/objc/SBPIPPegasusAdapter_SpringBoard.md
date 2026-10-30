# `SBPIPPegasusAdapter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PGPictureInPictureControllerDelegate`, `SBPIPContainerViewControllerObserver`, `SBBannerManagerTransitionObserver`, `SBPIPControllerAdapter`
- 9 instance variables, 4 properties, 49 instance methods, 2 class methods

## Instance variables

```
@"SBPIPController<SBPIPControllerAdapterContextProviding>" _pipController;
@"NSMutableSet" _presentedExpanseBanners;
@"PGPictureInPictureController" _pegasusController;
@"SBPIPAnalytics" _analyticsHelper;
@"BSAbsoluteMachTimer" _pipDefaultContentSizeResetTimer;
@"SBWindowSceneStatusBarSettingsAssertion" _appStatusBarSettingsAssertion;
B _isReducingResourcesUsage;
@"<BSInvalidatable>" _hideFaceTimePIPFromSharePlayScreenSharingAssertion;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBPIPPegasusAdapter isSupported];
+[SBPIPPegasusAdapter _isAutoPictureInPictureSupported];
```

## Instance methods

```
-[SBPIPPegasusAdapter bannerManager:presentable:willTransitionToSize:withTransitionCoordinator:];
-[SBPIPPegasusAdapter pictureInPictureController:didHidePictureInPictureViewController:];
-[SBPIPPegasusAdapter pipController:morphAnimatorDataSourceForMorphAnimatorController:];
-[SBPIPPegasusAdapter setPIPController:];
-[SBPIPPegasusAdapter observeValueForKeyPath:ofObject:change:context:];
-[SBPIPPegasusAdapter pictureInPictureController:willHidePictureInPictureViewController:];
-[SBPIPPegasusAdapter containerViewControllerStopReducingResourcesUsage:];
-[SBPIPPegasusAdapter containerViewControllerStartReducingResourcesUsage:];
-[SBPIPPegasusAdapter _updateAppStatusBarSettingsAssertion];
-[SBPIPPegasusAdapter pictureInPictureController:didRequestStopForPictureInPictureViewController:sourceSceneSessionIdentifier:animated:];
-[SBPIPPegasusAdapter _layoutStateContainsSceneForSourceSceneSessionIdentifier:bundleIdentifier:windowScene:];
-[SBPIPPegasusAdapter _updateHasIdleTimerBehaviors];
-[SBPIPPegasusAdapter initWithApplicationController:];
-[SBPIPPegasusAdapter contentTypeForPIPController:];
-[SBPIPPegasusAdapter pictureInPictureController:requestActivationOfSceneWithPersistenceIdentier:pictureInPictureViewController:completion:];
-[SBPIPPegasusAdapter dealloc];
-[SBPIPPegasusAdapter pictureInPictureControllerCanBackgroundStartForFaceTimeVideoCall:];
-[SBPIPPegasusAdapter pictureInPictureController:shouldDenyNewConnection:];
-[SBPIPPegasusAdapter preventStashAssertionsForPIPController:];
-[SBPIPPegasusAdapter pictureInPictureController:displayConfigurationForApplication:];
-[SBPIPPegasusAdapter pictureInPictureController:shouldAuthorizeBackgroundPIPForAppWithBundleIdentifier:];
-[SBPIPPegasusAdapter pipController:willBeginPIPInterruptionForAssertion:];
-[SBPIPPegasusAdapter _postEnsuredInSwitcher_pictureInPictureController:didRequestStopForPictureInPictureViewController:sourceSceneSessionIdentifier:forDisplayContentModeSwap:];
-[SBPIPPegasusAdapter isStartingStoppingOrCancellingPictureInPictureForPIPController:];
-[SBPIPPegasusAdapter pipController:didStartPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:animated:completionHandler:];
-[SBPIPPegasusAdapter _enumerateContainerViewControllersForApplication:scenePersistenceIdentifier:usingBlock:];
-[SBPIPPegasusAdapter _actuallyUpdateBannerInsetsForExpanseBanner:isSizeChanging:isFullScreen:];
-[SBPIPPegasusAdapter pipController:willRestorePictureInPictureForTestForApplicationWithBundleIdentifier:];
-[SBPIPPegasusAdapter pipController:didCancelPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:];
-[SBPIPPegasusAdapter pictureInPictureController:didCreatePictureInPictureViewController:];
-[SBPIPPegasusAdapter restorePictureInPictureForPIPController:applicationBundleIdentifier:forDisplayContentModeSwap:];
-[SBPIPPegasusAdapter pictureInPictureController:willDestroyPictureInPictureViewController:];
-[SBPIPPegasusAdapter _presentableIsDodgeableAndStatusBarSuppressing:];
-[SBPIPPegasusAdapter _updateHideFromClonedDisplaysAssertion];
-[SBPIPPegasusAdapter _reasonForAssertion:];
-[SBPIPPegasusAdapter isStoppingOrCancellingPictureForPIPController:applicationWithBundleIdentifier:scenePersistenceIdentifier:];
-[SBPIPPegasusAdapter _bannerPresentableWillAnimateTransition:isPresentation:isDismissal:isFullScreen:withTransitionCoordinator:];
-[SBPIPPegasusAdapter bannerManager:willDismissPresentable:withTransitionCoordinator:userInfo:];
-[SBPIPPegasusAdapter _activateSceneWithPersistenceIdentifier:pictureInPictureViewController:completion:];
-[SBPIPPegasusAdapter shouldStartPictureInPictureForPIPController:applicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:];
-[SBPIPPegasusAdapter bannerManager:willPresentPresentable:withTransitionCoordinator:userInfo:];
-[SBPIPPegasusAdapter pipController:willEndPIPInterruptionForAssertion:];
-[SBPIPPegasusAdapter containerViewControllerDidUpdatePrefersHiddenFromClonedDisplays:];
-[SBPIPPegasusAdapter pipController:willStartPictureInPictureTestActionForApplicationWithBundleIdentifier:];
-[SBPIPPegasusAdapter isPresentingPictureInPictureForPIPController:applicationBundleIdentifier:];
-[SBPIPPegasusAdapter tetheringModeForScenePersistenceIdentifier:];
-[SBPIPPegasusAdapter bannerManager:containerWillTransitionToSize:withTransitionCoordinator:];
-[SBPIPPegasusAdapter pictureInPictureController:didRequestStopForPictureInPictureViewController:sourceSceneSessionIdentifier:forDisplayContentModeSwap:];
-[SBPIPPegasusAdapter _updateBannerInsetsForExpanseBanner:isSizeChanging:isFullScreen:];
```
