# `SBPPTOperation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOperation`
- 7 instance variables, 1 properties, 9 instance methods, 85 class methods

## Instance variables

```
@? _finishTestBlock;
@? _startTestBlock;
@? _finishSubTestBlock;
@? _startSubTestBlock;
d _operationStartTime;
d _operationEndTime;
@"NSString" _operationName;
```

## Properties

```
@property (T@"NSString",C,N,V_operationName) operationName;
```

## Class methods

```
+[SBPPTOperation operationToSaveAppSwitcherState];
+[SBPPTOperation operationToWaitForTimeInterval:];
+[SBPPTOperation _appLibrarySupport__performPanGesturesOnScreenFromPage:toPage:completion:];
+[SBPPTOperation _appLibrarySupport_performDragFromPoint:andDragTo:duration:fromView:withCompletion:];
+[SBPPTOperation _appLibrarySupport_performLeftToRightPanGestureOnScreenWithDuration:completion:];
+[SBPPTOperation _appLibrarySupport_performPanGestureAwayFromUserInterfaceLayoutDirectionOnScreenWithDuration:completion:];
+[SBPPTOperation _appLibrarySupport_performPanGestureTowardsUserInterfaceLayoutDirectionOnScreenWithDuration:completion:];
+[SBPPTOperation _appLibrarySupport_performPanGesturesOnScreenUntilOnDefaultHomeScreenIconPageWithCompletion:];
+[SBPPTOperation _appLibrarySupport_performPanGesturesOnScreenUntilOnDeweyOverlayWithCompletion:];
+[SBPPTOperation _appLibrarySupport_performPanGesturesOnScreenUntilOnPage:withCompletion:];
+[SBPPTOperation _appLibrarySupport_performPanWithComposer:startLocation:endLocation:duration:];
+[SBPPTOperation _appLibrarySupport_performRightToLeftPanGestureOnScreenWithDuration:completion:];
+[SBPPTOperation _appLibrarySupport_performTapAtPoint:fromView:withCompletion:];
+[SBPPTOperation _dismissOverlaysAndResetHomeScreenToPage:animated:operation:completion:];
+[SBPPTOperation _homeScreenController];
+[SBPPTOperation _isLibraryDismissalAllowedWithCompletion:];
+[SBPPTOperation _isLibraryPresentationAllowedWithCompletion:];
+[SBPPTOperation _libraryViewController];
+[SBPPTOperation _mainDisplayWindowScene];
+[SBPPTOperation _mainDisplayWindowScene];
+[SBPPTOperation appLibraryDismissExpandedPod];
+[SBPPTOperation appLibraryExpandFirstPod];
+[SBPPTOperation configureAppLibraryForAllAppsInOnePod];
+[SBPPTOperation configureAppLibraryForEachAppHavingOwnPod];
+[SBPPTOperation dismissAppLibraryOverlay];
+[SBPPTOperation dismissAppLibraryPad:forTestWithName:];
+[SBPPTOperation dismissAppLibrarySearch];
+[SBPPTOperation dismissOverlaysAndResetHomeScreenToFirstIconPageAnimated:];
+[SBPPTOperation dismissOverlaysAndResetHomeScreenToLastIconPageAnimated:];
+[SBPPTOperation dismissOverlaysAndResetHomeScreenToPage:animated:completion:];
+[SBPPTOperation embeddedWindowScene];
+[SBPPTOperation embeddedWindowScene];
+[SBPPTOperation enqueueOperations:];
+[SBPPTOperation isLibraryPresented];
+[SBPPTOperation operationToActivateApplicationWithBundleIdentifier:];
+[SBPPTOperation operationToActivateNullOffscreenApp];
+[SBPPTOperation operationToCreateFolderWithName:containingIconsForBundleIdentifiers:];
+[SBPPTOperation operationToDismissAppSwitcherAndReturnToSource];
+[SBPPTOperation operationToDismissBannerNotification];
+[SBPPTOperation operationToDismissCoverSheet];
+[SBPPTOperation operationToDismissFloatingDock];
+[SBPPTOperation operationToDismissPageManagementForTestWithName:];
+[SBPPTOperation operationToFinishTest:];
+[SBPPTOperation operationToLoadPPTAppSwitcherState];
+[SBPPTOperation operationToLockInterface];
+[SBPPTOperation operationToMonitorCoverSheetTransitionWithTestName:execute:];
+[SBPPTOperation operationToOpenFolderWithName:];
+[SBPPTOperation operationToPresentAppSwitcher];
+[SBPPTOperation operationToPresentBannerNotification];
+[SBPPTOperation operationToPresentCoverSheet];
+[SBPPTOperation operationToPresentFloatingDock];
+[SBPPTOperation operationToPresentPageManagementForTestWithName:];
+[SBPPTOperation operationToPreventSystemIdle];
+[SBPPTOperation operationToPublishExampleNotificationsWithNotificationCount:threadCount:];
+[SBPPTOperation operationToRemoveExampleNotifications];
+[SBPPTOperation operationToRestoreAppSwitcherState];
+[SBPPTOperation operationToRestoreHomeScreenState];
+[SBPPTOperation operationToResumeSystemIdle];
+[SBPPTOperation operationToSaveHomeScreenState];
+[SBPPTOperation operationToSetAllApplicationsBlockedForScreenTime:];
+[SBPPTOperation operationToSetApplicationWithBundleIdentifier:blockedForScreenTime:];
+[SBPPTOperation operationToSetInterfaceOrientation:];
+[SBPPTOperation operationToStartTest:];
+[SBPPTOperation operationToSwipeDownInMiddleOfInterface];
+[SBPPTOperation operationToSwipeLeftInMiddleOfInterface];
+[SBPPTOperation operationToSwipeRightInMiddleOfInterface];
+[SBPPTOperation operationToSwipeUpInMiddleOfInterface];
+[SBPPTOperation operationToSynthesizeEventsForCommandString:];
+[SBPPTOperation operationToSynthesizeEventsForEventActions:];
+[SBPPTOperation operationToSynthesizeEventsForEventStream:];
+[SBPPTOperation operationToTerminateApplicationWithBundleIdentifier:];
+[SBPPTOperation operationToTerminateNullOffscreenApp];
+[SBPPTOperation operationToTransitionToHomeScreen];
+[SBPPTOperation operationToUnlockInterface];
+[SBPPTOperation operationToUnlockInterfaceFinishingUIUnlock:];
+[SBPPTOperation operationToUpdateHomeScreenPagesForActiveFocusModeForTestWithName:];
+[SBPPTOperation operationToWaitForNotificationName:object:timeout:];
+[SBPPTOperation performTapAtPointWithBlock:];
+[SBPPTOperation presentAppLibrary:forTestWithName:];
+[SBPPTOperation presentAppLibraryForTestWithName:];
+[SBPPTOperation presentAppLibraryPhone];
+[SBPPTOperation presentAppLibrarySearchByTappingSearchField];
+[SBPPTOperation pullToAppLibrarySearch];
+[SBPPTOperation resetAndPrepareforNextTest];
+[SBPPTOperation resetAppLibraryToTop];
```

## Instance methods

```
-[SBPPTOperation init];
-[SBPPTOperation operationName];
-[SBPPTOperation setOperationName:];
-[SBPPTOperation operationWillStart];
-[SBPPTOperation markFinishedSubTest:forTestName:];
-[SBPPTOperation markFinishedTest:];
-[SBPPTOperation markStartSubTest:forTestName:];
-[SBPPTOperation markStartedTest:];
-[SBPPTOperation operationDidFinish];
```
