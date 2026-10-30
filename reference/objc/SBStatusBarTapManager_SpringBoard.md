# `SBStatusBarTapManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _backgroundActivityIdentifiersToRecentScenes;
@"NSMutableDictionary" _backgroundActivityIdentifiersToRecentSceneResetTimers;
```

## Instance methods

```
-[SBStatusBarTapManager _workspace];
-[SBStatusBarTapManager _addRecentlyTappedApplicationDestinations:forBackgroundActivityWithIdentifier:];
-[SBStatusBarTapManager _allApplicationDestinationsForApplications:windowScene:];
-[SBStatusBarTapManager _appDestinationForNextSceneToVisitForApps:andBackgroundActivityWithIdentifier:windowScene:];
-[SBStatusBarTapManager _foregroundApplicationDestinationsForApplications:windowScene:];
-[SBStatusBarTapManager _handlerForBackgroundActivityWithIdentifier:windowScene:];
-[SBStatusBarTapManager _handlerForBackgroundActivityWithIdentifier:windowScene:orOutApplications:];
-[SBStatusBarTapManager _isUILocked:];
-[SBStatusBarTapManager _performAfterAttemptingUnlockForAppWithBundleIdentifier:windowScene:completion:];
-[SBStatusBarTapManager _recentlyTappedApplicationDestinationsForBackgroundActivityWithIdentifier:];
-[SBStatusBarTapManager _resetRecentlyTappedSceneIdentifiersForBackgroundActivityWithIdentifier:];
-[SBStatusBarTapManager _scheduleResetRecentlyTappedSceneIdentifiersForBackgroundActivityWithIdentifier:];
-[SBStatusBarTapManager canHandleTapForBackgroundActivityWithIdentifier:windowScene:];
-[SBStatusBarTapManager handleTapForBackgroundActivityWithIdentifier:windowScene:];
```
