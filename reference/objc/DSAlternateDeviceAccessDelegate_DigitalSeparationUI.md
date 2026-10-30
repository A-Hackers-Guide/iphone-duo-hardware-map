# `DSAlternateDeviceAccessDelegate`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSNavigationDelegate`
- 3 instance variables, 14 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"LAContext" authContext;
@"UINavigationController" _navigationController;
@"NSArray" _navigationOrder;
```

## Properties

```
@property (T@"UINavigationController",&,N,V_navigationController) navigationController;
@property (T@"NSArray",&,N,V_navigationOrder) navigationOrder;
@property (T@"LAContext",&,N,VauthContext) authContext;
@property (T@"NSMutableDictionary",?,R,N) unsharedResourcesBySource;
@property (T@"NSMutableSet",?,R,N) unsharedPeople;
@property (T@"NSMutableSet",?,R,N) unsharedApps;
@property (T@"NSMutableSet",?,R,N) unsharedPermissions;
@property (T@"NSMutableSet",?,R,N) unpairedComputers;
@property (T@"DSSharingPermissions",?,&,N) fetchedSharingPermissions;
@property (T@"NSMutableSet",?,R,N) reviewedComputers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSAlternateDeviceAccessDelegate tearDown];
-[DSAlternateDeviceAccessDelegate isNetworkReachable];
-[DSAlternateDeviceAccessDelegate authContext];
-[DSAlternateDeviceAccessDelegate initWithPresentingViewController:];
-[DSAlternateDeviceAccessDelegate setAuthContext:];
-[DSAlternateDeviceAccessDelegate setNavigationController:];
-[DSAlternateDeviceAccessDelegate navigationController];
-[DSAlternateDeviceAccessDelegate finishFlow];
-[DSAlternateDeviceAccessDelegate navigationOrder];
-[DSAlternateDeviceAccessDelegate setUpNavigation];
-[DSAlternateDeviceAccessDelegate deepLinkForCurrentFlowAndPane];
-[DSAlternateDeviceAccessDelegate displayNetworkError];
-[DSAlternateDeviceAccessDelegate exitFlowForRatchetWait];
-[DSAlternateDeviceAccessDelegate goToCustomizeSharing];
-[DSAlternateDeviceAccessDelegate learnMorePressedForController:withURL:];
-[DSAlternateDeviceAccessDelegate pushNextPane];
-[DSAlternateDeviceAccessDelegate pushPaneAfterPaneType:];
-[DSAlternateDeviceAccessDelegate pushPaneType:];
-[DSAlternateDeviceAccessDelegate quickExit];
-[DSAlternateDeviceAccessDelegate sendSummaryAnalyticsWithEventName:];
-[DSAlternateDeviceAccessDelegate setNavigationOrder:];
-[DSAlternateDeviceAccessDelegate startFlowWithType:];
```
