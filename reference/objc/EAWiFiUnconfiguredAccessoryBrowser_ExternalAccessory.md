# `EAWiFiUnconfiguredAccessoryBrowser`

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
B __debugLog;
@"<EAWiFiUnconfiguredAccessoryBrowserDelegate>" _delegate;
@"NSSet" _unconfiguredAccessories;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"NSPredicate" _accessorySearchPredicate;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_delegateQueue) delegateQueue;
@property (T@"NSPredicate",&,V_accessorySearchPredicate) accessorySearchPredicate;
@property (T@"<EAWiFiUnconfiguredAccessoryBrowserDelegate>",W,N,V_delegate) delegate;
@property (T@"NSSet",R,C,V_unconfiguredAccessories) unconfiguredAccessories;
```

## Instance methods

```
-[EAWiFiUnconfiguredAccessoryBrowser init];
-[EAWiFiUnconfiguredAccessoryBrowser initWithDelegate:queue:];
-[EAWiFiUnconfiguredAccessoryBrowser dealloc];
-[EAWiFiUnconfiguredAccessoryBrowser setDelegate:];
-[EAWiFiUnconfiguredAccessoryBrowser setDelegateQueue:];
-[EAWiFiUnconfiguredAccessoryBrowser delegate];
-[EAWiFiUnconfiguredAccessoryBrowser delegateQueue];
-[EAWiFiUnconfiguredAccessoryBrowser _handleBrowserDidUpdateState:];
-[EAWiFiUnconfiguredAccessoryBrowser _handleBrowserFinishedConfiguring:];
-[EAWiFiUnconfiguredAccessoryBrowser _handleNewAccessoriesNotification:];
-[EAWiFiUnconfiguredAccessoryBrowser _handlePurgeAccessoriesSetNotification:];
-[EAWiFiUnconfiguredAccessoryBrowser _handleRemovedAccessoriesNotification:];
-[EAWiFiUnconfiguredAccessoryBrowser accessorySearchPredicate];
-[EAWiFiUnconfiguredAccessoryBrowser configureAccessory:withConfigurationUIOnViewController:];
-[EAWiFiUnconfiguredAccessoryBrowser setAccessorySearchPredicate:];
-[EAWiFiUnconfiguredAccessoryBrowser startSearchingForUnconfiguredAccessoriesMatchingPredicate:];
-[EAWiFiUnconfiguredAccessoryBrowser stopSearchingForUnconfiguredAccessories];
-[EAWiFiUnconfiguredAccessoryBrowser unconfiguredAccessories];
```
