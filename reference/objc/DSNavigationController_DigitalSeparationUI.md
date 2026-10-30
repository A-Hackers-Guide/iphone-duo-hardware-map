# `DSNavigationController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBNavigationController`
- Protocols: `DSNavigationDelegate`, `UINavigationControllerDelegate`, `UIAdaptivePresentationControllerDelegate`, `LARatchetObserver`, `AKEmbeddedBioRatchetUIStateDelegate`
- 29 instance variables, 33 properties, 117 instance methods, 1 class methods

## Instance variables

```
B _requiresAuthForEntry;
B _isShowingNetworkError;
B _isReachable;
@"DSSharingPermissions" fetchedSharingPermissions;
@"LAContext" _authContext;
@"NSString" _entryMethod;
@"DSNavigationManager" _navigationManager;
@"NSDictionary" _navigationChapters;
@"NSArray" _navigationOrder;
@"DSRemoteUILoader" _remoteUILoader;
q _currentFlowType;
# _startingPaneType;
q _currentChapter;
q _currentChapterForAnalytics;
@"UIViewController" _networkErrorController;
@"UINavigationController" _connectionErrorNavigation;
@"NSDictionary" _cachedPanes;
@"UIWindow" _obfuscationWindow;
@"NSObject<OS_nw_path_monitor>" _pathMonitor;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"DSDaemonProxy" _daemonProxy;
@"DSDeepLinkRepresentation" _deepLink;
@"NSMutableDictionary" _unsharedResourcesBySource;
@"NSMutableSet" _unsharedPeople;
@"NSMutableSet" _unsharedApps;
@"NSMutableSet" _unsharedPermissions;
@"NSMutableSet" _unpairedComputers;
@"NSMutableSet" _reviewedComputers;
# _deepLinkPaneType;
```

## Properties

```
@property (T@"DSNavigationManager",&,N,V_navigationManager) navigationManager;
@property (T@"NSDictionary",&,N,V_navigationChapters) navigationChapters;
@property (T@"NSArray",&,N,V_navigationOrder) navigationOrder;
@property (T@"DSRemoteUILoader",&,N,V_remoteUILoader) remoteUILoader;
@property (Tq,N,V_currentFlowType) currentFlowType;
@property (T#,N,V_startingPaneType) startingPaneType;
@property (Tq,N,V_currentChapter) currentChapter;
@property (Tq,N,V_currentChapterForAnalytics) currentChapterForAnalytics;
@property (T@"UIViewController",&,N,V_networkErrorController) networkErrorController;
@property (TB,N,V_isShowingNetworkError) isShowingNetworkError;
@property (T@"UINavigationController",&,N,V_connectionErrorNavigation) connectionErrorNavigation;
@property (T@"NSDictionary",&,N,V_cachedPanes) cachedPanes;
@property (T@"UIWindow",&,N,V_obfuscationWindow) obfuscationWindow;
@property (T@"NSObject<OS_nw_path_monitor>",R,N,V_pathMonitor) pathMonitor;
@property (TB,V_isReachable) isReachable;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"DSDaemonProxy",&,N,V_daemonProxy) daemonProxy;
@property (T@"DSDeepLinkRepresentation",&,N,V_deepLink) deepLink;
@property (T@"NSMutableDictionary",&,N,V_unsharedResourcesBySource) unsharedResourcesBySource;
@property (T@"NSMutableSet",&,N,V_unsharedPeople) unsharedPeople;
@property (T@"NSMutableSet",&,N,V_unsharedApps) unsharedApps;
@property (T@"NSMutableSet",&,N,V_unsharedPermissions) unsharedPermissions;
@property (T@"NSMutableSet",&,N,V_unpairedComputers) unpairedComputers;
@property (T@"NSMutableSet",&,N,V_reviewedComputers) reviewedComputers;
@property (T#,&,N,V_deepLinkPaneType) deepLinkPaneType;
@property (T@"LAContext",&,N,V_authContext) authContext;
@property (T@"NSString",&,N,V_entryMethod) entryMethod;
@property (TB,N,V_requiresAuthForEntry) requiresAuthForEntry;
@property (T@"DSSharingPermissions",?,&,N,VfetchedSharingPermissions) fetchedSharingPermissions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSNavigationController initialize];
```

## Instance methods

```
-[DSNavigationController setWorkQueue:];
-[DSNavigationController setNavigationManager:];
-[DSNavigationController popViewControllerAnimated:];
-[DSNavigationController navigationManager];
-[DSNavigationController presentViewController:animated:completion:];
-[DSNavigationController navigationController:willShowViewController:animated:];
-[DSNavigationController presentationControllerDidDismiss:];
-[DSNavigationController init];
-[DSNavigationController isReachable];
-[DSNavigationController isNetworkReachable];
-[DSNavigationController workQueue];
-[DSNavigationController dealloc];
-[DSNavigationController currentChapter];
-[DSNavigationController viewDidLoad];
-[DSNavigationController willResignActive:];
-[DSNavigationController pathMonitor];
-[DSNavigationController viewWillAppear:];
-[DSNavigationController authContext];
-[DSNavigationController didEnterBackground:];
-[DSNavigationController setAuthContext:];
-[DSNavigationController cancel];
-[DSNavigationController willEnterForeground:];
-[DSNavigationController deepLink];
-[DSNavigationController setDeepLink:];
-[DSNavigationController finishFlow];
-[DSNavigationController daemonProxy];
-[DSNavigationController ratchetStateDidChange:];
-[DSNavigationController setIsReachable:];
-[DSNavigationController rightNavButtonTapped];
-[DSNavigationController setDaemonProxy:];
-[DSNavigationController currentFlowType];
-[DSNavigationController navigationOrder];
-[DSNavigationController setCachedPanes:];
-[DSNavigationController setEntryMethod:];
-[DSNavigationController startWithPanes:];
-[DSNavigationController _pushWelcomeControllerAsTopView];
-[DSNavigationController paneBeforePane:];
-[DSNavigationController updateDaemonModelForCurrentPane];
-[DSNavigationController _setupRatchetObserver];
-[DSNavigationController authToReturnToSafetyCheck];
-[DSNavigationController cachedPanes];
-[DSNavigationController connectionErrorNavigation];
-[DSNavigationController currentChapterForAnalytics];
-[DSNavigationController deepLinkForCurrentFlowAndPane];
-[DSNavigationController deepLinkPaneType];
-[DSNavigationController destroyConnectedWindowScene];
-[DSNavigationController displayNetworkError];
-[DSNavigationController entryMethod];
-[DSNavigationController exitFlowForRatchetWait];
-[DSNavigationController fetchedSharingPermissions];
-[DSNavigationController flowTypeForAnalytics];
-[DSNavigationController goToCustomizeSharing];
-[DSNavigationController hideNetworkError];
-[DSNavigationController initStartingWithBlockingPanes:];
-[DSNavigationController initStartingWithDeviceAccess];
-[DSNavigationController initStartingWithEmergencyReset];
-[DSNavigationController initStartingWithMangeSharing];
-[DSNavigationController initStartingWithURL:];
-[DSNavigationController isDetailControllerClass:];
-[DSNavigationController isInFamiliarLocation];
-[DSNavigationController isShowingNetworkError];
-[DSNavigationController isStandardFlow];
-[DSNavigationController learnMorePressedForController:withURL:];
-[DSNavigationController navigationChapters];
-[DSNavigationController networkErrorController];
-[DSNavigationController obfuscationWindow];
-[DSNavigationController paneInstanceForType:];
-[DSNavigationController popToPreviousPane:];
-[DSNavigationController pushNextPane];
-[DSNavigationController pushPaneAfterPaneType:];
-[DSNavigationController pushPaneType:];
-[DSNavigationController pushPaneType:loadRemoteUI:];
-[DSNavigationController pushPaneWithController:paneType:shouldShow:];
-[DSNavigationController quickExit];
-[DSNavigationController remoteUILoader];
-[DSNavigationController requiresAuthForEntry];
-[DSNavigationController resetRemoteUI];
-[DSNavigationController reviewedComputers];
-[DSNavigationController sendSummaryAnalyticsWithEventName:];
-[DSNavigationController sendSummaryAnalyticsWithQuickExit:finalScreen:];
-[DSNavigationController setConnectionErrorNavigation:];
-[DSNavigationController setCurrentChapter:];
-[DSNavigationController setCurrentChapterForAnalytics:];
-[DSNavigationController setCurrentFlowType:];
-[DSNavigationController setDeepLinkPaneType:];
-[DSNavigationController setFetchedSharingPermissions:];
-[DSNavigationController setIsShowingNetworkError:];
-[DSNavigationController setNavigationChapters:];
-[DSNavigationController setNavigationOrder:];
-[DSNavigationController setNavigationOrderAndChapters];
-[DSNavigationController setNetworkErrorController:];
-[DSNavigationController setObfuscationWindow:];
-[DSNavigationController setRemoteUILoader:];
-[DSNavigationController setRequiresAuthForEntry:];
-[DSNavigationController setReviewedComputers:];
-[DSNavigationController setStartingPaneType:];
-[DSNavigationController setUnpairedComputers:];
-[DSNavigationController setUnsharedApps:];
-[DSNavigationController setUnsharedPeople:];
-[DSNavigationController setUnsharedPermissions:];
-[DSNavigationController setUnsharedResourcesBySource:];
-[DSNavigationController setupCancelButtonWithController:];
-[DSNavigationController setupChapterIndicatorWithController:];
-[DSNavigationController setupConnectionError];
-[DSNavigationController setupQuickExitButtonWithController:];
-[DSNavigationController shouldFinishFlow];
-[DSNavigationController startFlowWithType:];
-[DSNavigationController startWithURL:];
-[DSNavigationController startingPaneType];
-[DSNavigationController topViewControllerType];
-[DSNavigationController unpairedComputers];
-[DSNavigationController unsharedApps];
-[DSNavigationController unsharedPeople];
-[DSNavigationController unsharedPermissions];
-[DSNavigationController unsharedResourcesBySource];
-[DSNavigationController updateCurrentChapterWithPaneType:];
-[DSNavigationController updateReachabilityState:];
```
