# `WiFiWalletSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAvailabilitySource`
- 7 instance variables, 11 properties, 35 instance methods, 0 class methods

## Instance variables

```
@? changeHandler;
@? relevancyHandler;
@? removalHandler;
@"PKPassLibrary" _passLibrary;
@"NSMutableDictionary" _networks;
@"NSMutableSet" _relevantPassIdentifiers;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"PKPassLibrary",&,N,V_passLibrary) passLibrary;
@property (T@"NSMutableDictionary",&,N,V_networks) networks;
@property (T@"NSMutableSet",&,N,V_relevantPassIdentifiers) relevantPassIdentifiers;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@?,C,N,VchangeHandler) changeHandler;
@property (T@?,C,N,VrelevancyHandler) relevancyHandler;
@property (T@?,C,N,VremovalHandler) removalHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiWalletSource setNetworks:];
-[WiFiWalletSource init];
-[WiFiWalletSource networks];
-[WiFiWalletSource dealloc];
-[WiFiWalletSource queue];
-[WiFiWalletSource setChangeHandler:];
-[WiFiWalletSource changeHandler];
-[WiFiWalletSource setQueue:];
-[WiFiWalletSource initWithChangeHandler:];
-[WiFiWalletSource _passLibraryDidChange:];
-[WiFiWalletSource passLibrary];
-[WiFiWalletSource setPassLibrary:];
-[WiFiWalletSource _addPass:];
-[WiFiWalletSource _createWiFiWalletPassFromPass:];
-[WiFiWalletSource _handlePassLibraryChange:];
-[WiFiWalletSource _handleRelevantPassUpdate:];
-[WiFiWalletSource _initializeWiFiPasses];
-[WiFiWalletSource _issueChangeCallbackWithPass:removedNetworks:];
-[WiFiWalletSource _issueRelevancyCallbackWithRelevantNetworks:notRelevantNetworks:];
-[WiFiWalletSource _issueRemovalCallbackWithPass:];
-[WiFiWalletSource _networksWithIdentifier:];
-[WiFiWalletSource _passDidBecomeRelevant:];
-[WiFiWalletSource _passLibraryDidBecomeRelevantNotification:];
-[WiFiWalletSource _removePass:withSerialNumber:];
-[WiFiWalletSource _removeRelevantPasses];
-[WiFiWalletSource _replacePass:];
-[WiFiWalletSource candidateNetworks];
-[WiFiWalletSource expiredWalletIDs];
-[WiFiWalletSource relevancyHandler];
-[WiFiWalletSource relevantNetworks];
-[WiFiWalletSource relevantPassIdentifiers];
-[WiFiWalletSource removalHandler];
-[WiFiWalletSource setRelevancyHandler:];
-[WiFiWalletSource setRelevantPassIdentifiers:];
-[WiFiWalletSource setRemovalHandler:];
```
