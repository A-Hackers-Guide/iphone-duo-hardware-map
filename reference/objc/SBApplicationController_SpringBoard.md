# `SBApplicationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationRestrictionDataSource`, `XBApplicationProviding`, `SBApplicationLifecycleObserver`, `SBApplicationDelegate`
- 14 instance variables, 4 properties, 66 instance methods, 5 class methods

## Instance variables

```
@"NSMutableDictionary" _applicationsByBundleIdentifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _applicationsLock;
@"NSMutableDictionary" _systemAppsVisibilityOverrides;
@"NSSet" _cachedSystemAppsWithVisibilityOverrideHidden;
@"SBApplicationRestrictionController" _restrictionController;
@"SBApplicationLibraryObserver" _appLibraryObserver;
@"FBSApplicationLibrary" _appLibrary;
@"SBApplicationInfo" _systemAppInfo;
@"SBSplashBoardController" _splashBoardController;
@"SBAppProtectionCoordinator" _appProtectionCoordinator;
@"SBReverseCountedSemaphore" _uninstallationReverseSemaphore;
@"NSSet" _preventLaunchBundleIDs;
@"RBSProcessMonitor" _processMonitor;
@"SBApplicationRestrictionMonitoringServer" _restrictionMonitoringServer;
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
+[SBApplicationController sharedInstance];
+[SBApplicationController sharedInstanceIfExists];
+[SBApplicationController _setClearAllLegacySnapshotsWhenLoaded:];
+[SBApplicationController _setClearSystemAppSnapshotsWhenLoaded:];
+[SBApplicationController _sharedInstanceCreateIfNecessary:];
```

## Instance methods

```
-[SBApplicationController applicationWithBundleIdentifier:];
-[SBApplicationController applicationsAdded:];
-[SBApplicationController faceTimeApp];
-[SBApplicationController _finishDeferredMajorVersionMigrationTasks_FlushSystemSnapshots];
-[SBApplicationController applicationsDemoted:];
-[SBApplicationController _sendInstalledAppsDidChangeNotification:removed:replaced:updated:];
-[SBApplicationController applicationsRemoved:];
-[SBApplicationController _informRestrictionsMayHaveChanged];
-[SBApplicationController allApplications];
-[SBApplicationController initWithTelephonyStateProvider:];
-[SBApplicationController applicationRestrictionsMayHaveChanged];
-[SBApplicationController _applicationRestrictionMonitoringServer];
-[SBApplicationController allBundleIdentifiers];
-[SBApplicationController _allApplicationsFilteredBySystem:];
-[SBApplicationController dealloc];
-[SBApplicationController applicationWithPid:];
-[SBApplicationController applicationsReplaced:];
-[SBApplicationController _loadApplications:remove:];
-[SBApplicationController runningApplications];
-[SBApplicationController _updateVisibilityOverrides];
-[SBApplicationController splashBoardSystemApplications];
-[SBApplicationController iPodOutApplication];
-[SBApplicationController applicationForDisplayItem:];
-[SBApplicationController _loadApplicationFromApplicationInfo:informVisibilityOverridesDidChange:];
-[SBApplicationController _appLibrary];
-[SBApplicationController testFlightApplication];
-[SBApplicationController inCallServiceApp];
-[SBApplicationController isApplicationAlwaysAvailableForProxy:];
-[SBApplicationController cameraApplication];
-[SBApplicationController webApplication];
-[SBApplicationController _appProtectionCoordinator];
-[SBApplicationController loginApplication];
-[SBApplicationController setupApplication];
-[SBApplicationController applicationsUpdated:];
-[SBApplicationController representedApplicationWithBundleIdentifier:];
-[SBApplicationController uninstallApplication:];
-[SBApplicationController _informVisibilityOverridesDidChange];
-[SBApplicationController dataActivationApplication];
-[SBApplicationController _appClassForInfo:];
-[SBApplicationController notesApplication];
-[SBApplicationController musicApplication];
-[SBApplicationController isApplicationAlwaysAvailableForInfo:];
-[SBApplicationController waitForUninstallsToComplete:];
-[SBApplicationController _finishDeferredMajorVersionMigrationTasks_FlushLegacySnapshots];
-[SBApplicationController mapsApplication];
-[SBApplicationController allSplashBoardApplications];
-[SBApplicationController _appLayoutContainsOnlyResizableApps:];
-[SBApplicationController applicationRequestedUninstall:];
-[SBApplicationController applicationVisibilityMayHaveChanged];
-[SBApplicationController _removeApplicationsFromModelWithBundleIdentifier:forInstall:withReason:informVisibilityOverridesDidChange:];
-[SBApplicationController restrictionController];
-[SBApplicationController _appInfosToBundleIDs:];
-[SBApplicationController mobilePhone];
-[SBApplicationController allInstalledApplications];
-[SBApplicationController alwaysAvailableApplicationBundleIdentifiers];
-[SBApplicationController _lock_applicationWithBundleIdentifier:];
-[SBApplicationController recentlyUsedBundleIDs];
-[SBApplicationController clockApplication];
-[SBApplicationController requestUninstallApplication:options:withCompletion:];
-[SBApplicationController _splashBoardController];
-[SBApplicationController _memoryWarningReceived];
-[SBApplicationController _preLoadApplications];
-[SBApplicationController _updateVisibilityOverridesInBackground];
-[SBApplicationController requestUninstallApplicationWithBundleIdentifier:options:withCompletion:];
-[SBApplicationController bundleIdentifiersWithVisibilityOverrideHidden];
-[SBApplicationController _appLibraryObserver];
```
