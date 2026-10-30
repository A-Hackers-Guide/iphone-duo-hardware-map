# `SBPPTRunner`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NCNotificationViewControllerObserving`, `CCUIPPTHostDelegate`
- 0 instance variables, 8 properties, 53 instance methods, 8 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBPPTRunner sharedInstance];
+[SBPPTRunner _operationToRestoreVideoFromPIP];
+[SBPPTRunner _operationToPutVideoInPIP];
+[SBPPTRunner _operationToStashPIP];
+[SBPPTRunner _operationToUnstashStashedPIP];
+[SBPPTRunner isAppLibraryTest:];
+[SBPPTRunner isFocusModeTest:];
+[SBPPTRunner isPageManagementTest:];
```

## Instance methods

```
-[SBPPTRunner longLookDidPresentForNotificationViewController:];
-[SBPPTRunner longLookWillPresentForNotificationViewController:];
-[SBPPTRunner assistantDidAppear:windowScene:];
-[SBPPTRunner longLookDidDismissForNotificationViewController:];
-[SBPPTRunner longLookWillDismissForNotificationViewController:];
-[SBPPTRunner assistantWillAppear:windowScene:];
-[SBPPTRunner runTestWithName:options:];
-[SBPPTRunner prepareForControlCenterPPTHostState:completionHandler:];
-[SBPPTRunner _configureParams:forScrollView:];
-[SBPPTRunner _runScrollDeweyTestWithOptions:];
-[SBPPTRunner _cs_mainDisplayWindowScene];
-[SBPPTRunner _libraryViewController];
-[SBPPTRunner _mainDisplayWindowScene];
-[SBPPTRunner _mainDisplayWindowScene];
-[SBPPTRunner _operationToDismissCoverSheetForTestWithName:];
-[SBPPTRunner _operationToDismissDashBoardForTestWithName:];
-[SBPPTRunner _operationToPresentCoverSheetForTestWithName:];
-[SBPPTRunner _runAppLibraryPadPresentTestWithOptions:];
-[SBPPTRunner _runAppLibraryTestWithName:options:];
-[SBPPTRunner _runCoverSheetDismissTestWithOptions:];
-[SBPPTRunner _runCoverSheetDismissToSafariTestWithOptions:];
-[SBPPTRunner _runCoverSheetPresentOverSafariTestWithOptions:];
-[SBPPTRunner _runCoverSheetPresentTestWithOptions:];
-[SBPPTRunner _runCoverSheetTestWithName:options:];
-[SBPPTRunner _runDashBoardDismissTestWithOptions:];
-[SBPPTRunner _runDashBoardTestWithName:options:];
-[SBPPTRunner _runFloatingDockBringupTestWithOptions:];
-[SBPPTRunner _runFloatingDockDismissTestWithOptions:];
-[SBPPTRunner _runFocusModePresentTestWithName:options:];
-[SBPPTRunner _runFocusModeTestWithName:options:];
-[SBPPTRunner _runLibrarySearchTestWithOptions:];
-[SBPPTRunner _runNotificationBannerTransitionTestWithOptions:];
-[SBPPTRunner _runNotificationClearLongLookTransitionTestWithOptions:];
-[SBPPTRunner _runNotificationReParkLongLookTransitionTestWithOptions:];
-[SBPPTRunner _runNotificationShortToLongLookTransitionTestWithOptions:];
-[SBPPTRunner _runPIPAutoStashByEnteringSwitcherTestWithOptions:];
-[SBPPTRunner _runPIPAutoUnstashAndRestoreByExitingSwitcherBackToAppTestWithOptions:];
-[SBPPTRunner _runPIPBasicRestoreTestWithOptions:];
-[SBPPTRunner _runPIPManualStashTestWithOptions:];
-[SBPPTRunner _runPIPManualUnstashTestWithOptions:];
-[SBPPTRunner _runPageManagementPresentTestWithName:options:];
-[SBPPTRunner _runPageManagementTestWithName:options:];
-[SBPPTRunner _runPiPAutoStashByEnteringSwitcherTestWithOptions:];
-[SBPPTRunner _runPiPAutoUnstashAndRestoreByExitingSwitcherBackToAppTestWithOptions:];
-[SBPPTRunner _runPiPBasicRestoreTestWithOptions:];
-[SBPPTRunner _runPiPManualStashTestWithOptions:];
-[SBPPTRunner _runPiPManualUnstashTestWithOptions:];
-[SBPPTRunner _runPullToAppLibrarySearchTestWithOptions:];
-[SBPPTRunner _runScrollWithinExpandedPodTestWithOptions:];
-[SBPPTRunner _runSiriTestWithName:options:];
-[SBPPTRunner _runSwipeFromDeweyTestWithOptions:];
-[SBPPTRunner _runSwipeToDeweyTestWithOptions:];
-[SBPPTRunner _setCoverSheetPresentationManagerTransitionCallbacksForTestName:operation:];
```
