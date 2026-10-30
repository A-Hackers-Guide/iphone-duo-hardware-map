# `FBSApplicationLibrary`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LSApplicationWorkspaceObserverProtocol`, `BSInvalidatable`, `FBSApplicationInfoProvider`
- 17 instance variables, 5 properties, 55 instance methods, 0 class methods

## Instance variables

```
@"FBSApplicationLibraryConfiguration" _configuration;
@"LSApplicationWorkspace" _applicationWorkspace;
@"NSObject<OS_dispatch_queue>" _observerQueue;
@"NSMapTable" _observerQueue_tokensToBlocks;
@"NSObject<OS_dispatch_queue>" _workQueue;
B _workQueue_usingNetwork;
@"NSMutableDictionary" _workQueue_identitiesByBundleID;
@"NSMutableDictionary" _workQueue_installedApplicationsByIdentity;
@"NSMutableDictionary" _workQueue_placeholdersByIdentity;
@"NSMutableSet" _workQueue_injectedAppIdentifiers;
Q _workQueue_synchronizationActionCount;
@"NSMutableArray" _workQueue_pendingSynchronizationExecutionBlocks;
@"NSObject<OS_dispatch_queue>" _callOutQueue;
@"NSObject<OS_dispatch_queue>" _completionQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BSInvalidatable>" _stateCaptureAssertion;
B _lock_invalidated;
```

## Properties

```
@property (TB,R,N,GisUsingNetwork) usingNetwork;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSApplicationLibrary applicationsDidUninstall:];
-[FBSApplicationLibrary applicationsDidChangePersonas:];
-[FBSApplicationLibrary applicationsDidInstall:];
-[FBSApplicationLibrary placeholdersForBundleIdentifier:];
-[FBSApplicationLibrary removeObserverForToken:];
-[FBSApplicationLibrary applicationStateDidChange:];
-[FBSApplicationLibrary observeDidChangeNetworkUsageWithBlock:];
-[FBSApplicationLibrary applicationsWillInstall:];
-[FBSApplicationLibrary placeholderForIdentityString:];
-[FBSApplicationLibrary addApplicationProxy:withOverrideURL:];
-[FBSApplicationLibrary installedApplicationsForBundleIdentifier:];
-[FBSApplicationLibrary applicationsDidFailToInstall:];
-[FBSApplicationLibrary uninstallApplication:withOptions:completion:];
-[FBSApplicationLibrary init];
-[FBSApplicationLibrary applicationInstallsDidStart:];
-[FBSApplicationLibrary placeholderWithBundleIdentifier:];
-[FBSApplicationLibrary dealloc];
-[FBSApplicationLibrary uninstallApplicationIdentity:withOptions:completion:];
-[FBSApplicationLibrary observeDidRemoveApplicationsWithBlock:];
-[FBSApplicationLibrary observeDidReplaceApplicationsWithBlock:];
-[FBSApplicationLibrary isUsingNetwork];
-[FBSApplicationLibrary uninstallApplication:completion:];
-[FBSApplicationLibrary observeDidAddApplicationsWithBlock:];
-[FBSApplicationLibrary observeDidDemoteApplicationsWithBlock:];
-[FBSApplicationLibrary applicationsDidFailToUninstall:];
-[FBSApplicationLibrary initWithConfiguration:];
-[FBSApplicationLibrary installedApplicationForIdentity:];
-[FBSApplicationLibrary _initWithApplicationWorkspace:configuration:];
-[FBSApplicationLibrary installedApplicationWithBundleIdentifier:completionHandler:];
-[FBSApplicationLibrary observeDidAddPlaceholdersWithBlock:];
-[FBSApplicationLibrary invalidate];
-[FBSApplicationLibrary applicationInstallsDidResume:];
-[FBSApplicationLibrary observeDidUpdateApplicationsWithBlock:];
-[FBSApplicationLibrary applicationInfoForBundleIdentifier:];
-[FBSApplicationLibrary _reloadPlaceholdersNotificationFired];
-[FBSApplicationLibrary _synchronizationQueue];
-[FBSApplicationLibrary synchronize:];
-[FBSApplicationLibrary applicationInstallsDidUpdateIcon:];
-[FBSApplicationLibrary applicationInstallsDidPause:];
-[FBSApplicationLibrary placeholderForIdentity:];
-[FBSApplicationLibrary description];
-[FBSApplicationLibrary deviceManagementPolicyDidChange:];
-[FBSApplicationLibrary addApplicationRecord:];
-[FBSApplicationLibrary applicationsWillUninstall:];
-[FBSApplicationLibrary allInstalledApplications];
-[FBSApplicationLibrary installedApplicationWithBundleIdentifier:];
-[FBSApplicationLibrary applicationInfoForAuditToken:];
-[FBSApplicationLibrary installedApplicationForIdentityString:];
-[FBSApplicationLibrary allPlaceholders];
-[FBSApplicationLibrary observeDidCancelPlaceholdersWithBlock:];
-[FBSApplicationLibrary applicationInstallsDidPrioritize:];
-[FBSApplicationLibrary networkUsageChanged:];
-[FBSApplicationLibrary applicationInstallsDidCancel:];
-[FBSApplicationLibrary applicationInstallsArePrioritized:arePaused:];
-[FBSApplicationLibrary applicationInstallsDidChange:];
```
