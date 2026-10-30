# `DSNavigationDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"LAContext",&,N) authContext;
@property (T@"NSMutableDictionary",?,R,N) unsharedResourcesBySource;
@property (T@"NSMutableSet",?,R,N) unsharedPeople;
@property (T@"NSMutableSet",?,R,N) unsharedApps;
@property (T@"NSMutableSet",?,R,N) unsharedPermissions;
@property (T@"NSMutableSet",?,R,N) unpairedComputers;
@property (T@"DSSharingPermissions",?,&,N) fetchedSharingPermissions;
@property (T@"NSMutableSet",?,R,N) reviewedComputers;
```

## Instance methods

```
-[DSNavigationDelegate isNetworkReachable];
-[DSNavigationDelegate authContext];
-[DSNavigationDelegate setAuthContext:];
-[DSNavigationDelegate deepLinkForCurrentFlowAndPane];
-[DSNavigationDelegate displayNetworkError];
-[DSNavigationDelegate exitFlowForRatchetWait];
-[DSNavigationDelegate goToCustomizeSharing];
-[DSNavigationDelegate learnMorePressedForController:withURL:];
-[DSNavigationDelegate pushNextPane];
-[DSNavigationDelegate quickExit];
-[DSNavigationDelegate sendSummaryAnalyticsWithEventName:];
-[DSNavigationDelegate startFlowWithType:];
-[DSNavigationDelegate fetchedSharingPermissions];
-[DSNavigationDelegate pushPaneAfterPaneType:];
-[DSNavigationDelegate pushPaneType:loadRemoteUI:];
-[DSNavigationDelegate reviewedComputers];
-[DSNavigationDelegate setFetchedSharingPermissions:];
-[DSNavigationDelegate unpairedComputers];
-[DSNavigationDelegate unsharedApps];
-[DSNavigationDelegate unsharedPeople];
-[DSNavigationDelegate unsharedPermissions];
-[DSNavigationDelegate unsharedResourcesBySource];
```
