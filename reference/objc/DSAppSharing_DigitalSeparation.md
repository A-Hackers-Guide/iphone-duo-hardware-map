# `DSAppSharing`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"<DSTCCStore>" _tccStore;
@"HKHealthStore" _healthKitStore;
@"HKAuthorizationStore" _authorizationStore;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"<DSTCCStore>",&,N,V_tccStore) tccStore;
@property (T@"HKHealthStore",&,N,V_healthKitStore) healthKitStore;
@property (T@"HKAuthorizationStore",&,N,V_authorizationStore) authorizationStore;
```

## Instance methods

```
-[DSAppSharing setWorkQueue:];
-[DSAppSharing workQueue];
-[DSAppSharing authorizationStore];
-[DSAppSharing setTccStore:];
-[DSAppSharing tccStore];
-[DSAppSharing resetPermission:forApp:handler:];
-[DSAppSharing addApp:toMap:withLocationAuthorization:];
-[DSAppSharing addApp:toMap:withService:];
-[DSAppSharing addFileAccessPermissionsToAppMap:handler:];
-[DSAppSharing addHealthPermissionsToAppMap:handler:];
-[DSAppSharing addLocalNetworkPermissionsToAppMap:handler:];
-[DSAppSharing addLocationPermissions:];
-[DSAppSharing addTCCPermissionsToAppMap:handler:];
-[DSAppSharing approvedBundleIdForKappa:handler:];
-[DSAppSharing collectAppsWithAccessToService:appMap:completionHandler:];
-[DSAppSharing collectPermissionsForApps:queue:handler:];
-[DSAppSharing deleteApp:forTest:];
-[DSAppSharing healthKitStore];
-[DSAppSharing initWithTCCStore:];
-[DSAppSharing newDictionaryWithApps:];
-[DSAppSharing removeAppsWithNoPermissions:];
-[DSAppSharing resetBackgroundAppRefresh:queue:handler:];
-[DSAppSharing resetFileAccessPermissionsForApp:withCompletionHandler:];
-[DSAppSharing resetHealthPermissionsForApp:withCompletionHandler:];
-[DSAppSharing resetPermission:forApps:handler:];
-[DSAppSharing resetPermissions:forApps:queue:handler:];
-[DSAppSharing resetShortcutsAutomationTimer:handler:];
-[DSAppSharing setAuthorizationStore:];
-[DSAppSharing setHealthKitStore:];
```
