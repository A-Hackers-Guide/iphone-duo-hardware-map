# `DSAlternateDeviceAccessManager`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 10 properties, 31 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _providerLock;
Ai _fetchState;
B _hasMultipleFaceIDs;
B _hasMultipleTouchIDs;
@"DSContinuityStore" _continuityStore;
@"<DSPairedComputerStoreProtocol>" _pairedComputerStore;
@"DSAlternateDeviceAccessDelegate" _delegate;
@"NSArray" _continuityDevices;
@"NSArray" _pairedComputers;
Q _fetchCompletedTime;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"LAContext" _authContext;
```

## Properties

```
@property (T@"DSContinuityStore",&,N,V_continuityStore) continuityStore;
@property (T@"<DSPairedComputerStoreProtocol>",&,N,V_pairedComputerStore) pairedComputerStore;
@property (T@"DSAlternateDeviceAccessDelegate",&,N,V_delegate) delegate;
@property (T@"NSArray",&,N,V_continuityDevices) continuityDevices;
@property (T@"NSArray",&,N,V_pairedComputers) pairedComputers;
@property (TB,N,V_hasMultipleFaceIDs) hasMultipleFaceIDs;
@property (TB,N,V_hasMultipleTouchIDs) hasMultipleTouchIDs;
@property (TQ,V_fetchCompletedTime) fetchCompletedTime;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"LAContext",&,N,V_authContext) authContext;
```

## Class methods

```
+[DSAlternateDeviceAccessManager sharedManager];
```

## Instance methods

```
-[DSAlternateDeviceAccessManager setWorkQueue:];
-[DSAlternateDeviceAccessManager init];
-[DSAlternateDeviceAccessManager workQueue];
-[DSAlternateDeviceAccessManager authContext];
-[DSAlternateDeviceAccessManager setDelegate:];
-[DSAlternateDeviceAccessManager delegate];
-[DSAlternateDeviceAccessManager setAuthContext:];
-[DSAlternateDeviceAccessManager fetchCompletedTime];
-[DSAlternateDeviceAccessManager setFetchCompletedTime:];
-[DSAlternateDeviceAccessManager continuityStore];
-[DSAlternateDeviceAccessManager pairedComputers];
-[DSAlternateDeviceAccessManager continuityDevices];
-[DSAlternateDeviceAccessManager fetchAccessMethodsWithCompletion:];
-[DSAlternateDeviceAccessManager hasAlternateAccess];
-[DSAlternateDeviceAccessManager hasAlternateFaceID];
-[DSAlternateDeviceAccessManager hasAlternateTouchID];
-[DSAlternateDeviceAccessManager hasMultipleFaceIDs];
-[DSAlternateDeviceAccessManager hasMultipleTouchIDs];
-[DSAlternateDeviceAccessManager mirroringDevices];
-[DSAlternateDeviceAccessManager pairedComputerStore];
-[DSAlternateDeviceAccessManager performFetchWithCompletion:];
-[DSAlternateDeviceAccessManager resetAllAccessMethodsWithCompletion:];
-[DSAlternateDeviceAccessManager sendSummaryAnalyticsWithReviewAction:resetAction:exit:];
-[DSAlternateDeviceAccessManager setContinuityDevices:];
-[DSAlternateDeviceAccessManager setContinuityStore:];
-[DSAlternateDeviceAccessManager setHasMultipleFaceIDs:];
-[DSAlternateDeviceAccessManager setHasMultipleTouchIDs:];
-[DSAlternateDeviceAccessManager setPairedComputerStore:];
-[DSAlternateDeviceAccessManager setPairedComputers:];
-[DSAlternateDeviceAccessManager startPresentationWithNavigationController:];
-[DSAlternateDeviceAccessManager syncingDevices];
```
