# `WiFiAvailabilityEngine`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 34 instance methods, 0 class methods

## Instance variables

```
d _availabilityMatchMaximumAge;
@"NSSet" _providers;
@"NSSet" _sources;
@"NSSet" _availableNetworks;
@? _availabilityChangedCallback;
@"<WiFiScanProvider>" _scanProvider;
@"<WiFiLocationProvider>" _locationProvider;
@"NSObject<OS_dispatch_queue>" _queue;
@"WiFiLexicon" _wifiLexicon;
```

## Properties

```
@property (T@"NSSet",C,N,V_providers) providers;
@property (T@"NSSet",C,N,V_sources) sources;
@property (T@"<WiFiScanProvider>",W,N,V_scanProvider) scanProvider;
@property (T@"<WiFiLocationProvider>",W,N,V_locationProvider) locationProvider;
@property (T@"NSSet",&,N,V_availableNetworks) availableNetworks;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"WiFiLexicon",&,N,V_wifiLexicon) wifiLexicon;
@property (Td,N,V_availabilityMatchMaximumAge) availabilityMatchMaximumAge;
@property (T@?,C,N,V_availabilityChangedCallback) availabilityChangedCallback;
```

## Instance methods

```
-[WiFiAvailabilityEngine providers];
-[WiFiAvailabilityEngine setProviders:];
-[WiFiAvailabilityEngine _setupProviderCallbacks:];
-[WiFiAvailabilityEngine _handleCandidateMatches:];
-[WiFiAvailabilityEngine setLocationProvider:];
-[WiFiAvailabilityEngine setWifiLexicon:];
-[WiFiAvailabilityEngine wifiLexicon];
-[WiFiAvailabilityEngine availableNetworks];
-[WiFiAvailabilityEngine _findRelevantNetworkMatchForScannedNetwork:];
-[WiFiAvailabilityEngine queue];
-[WiFiAvailabilityEngine setAvailabilityMatchMaximumAge:];
-[WiFiAvailabilityEngine _createAvailabilityMatchForCandidate:scannedNetwork:];
-[WiFiAvailabilityEngine _handleWalletRelevancyAdded:removed:];
-[WiFiAvailabilityEngine setScanProvider:];
-[WiFiAvailabilityEngine _setupSourceCallbacks:];
-[WiFiAvailabilityEngine setAvailabilityChangedCallback:];
-[WiFiAvailabilityEngine _findAvailabilityMatchesInSourcesForBSSIDS:];
-[WiFiAvailabilityEngine availabilityMatchMaximumAge];
-[WiFiAvailabilityEngine scanProvider];
-[WiFiAvailabilityEngine _handleWalletRemoval:];
-[WiFiAvailabilityEngine findRecommendationForScannedNetwork:];
-[WiFiAvailabilityEngine _findExistingAvailabilityMatchForScannedNetwork:];
-[WiFiAvailabilityEngine availabilityChangedCallback];
-[WiFiAvailabilityEngine _handleScanResultCallback:error:];
-[WiFiAvailabilityEngine _handle3BarsRelevancyAdded:removed:];
-[WiFiAvailabilityEngine findRecommendationsForScannedNetwork:];
-[WiFiAvailabilityEngine _handleWalletChange:removed:];
-[WiFiAvailabilityEngine setAvailableNetworks:];
-[WiFiAvailabilityEngine sources];
-[WiFiAvailabilityEngine initWithProviders:sources:];
-[WiFiAvailabilityEngine locationProvider];
-[WiFiAvailabilityEngine _removeStaleMatches];
-[WiFiAvailabilityEngine setSources:];
-[WiFiAvailabilityEngine setQueue:];
```
