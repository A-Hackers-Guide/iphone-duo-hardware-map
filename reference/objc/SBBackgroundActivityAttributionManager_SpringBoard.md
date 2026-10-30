# `SBBackgroundActivityAttributionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneStatusBarAssertionManagerObserver`, `SBBackgroundActivityAssertionServiceManagerDelegate`, `BSDescriptionProviding`, `SBWindowSceneAttachmentObserving`
- 14 instance variables, 13 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"STBackgroundActivitiesStatusDomain" _backgroundActivitiesDomain;
@"STBackgroundActivitiesStatusDomainData" _queue_processedData;
@"STStatusBarOverridesStatusDomain" _overridesDomain;
@"STStatusBarOverridesStatusDomainData" _queue_processedOverrides;
@"NSMapTable" _statusBarAssertionManagersByWindowScene;
@"NSMapTable" _attributionsByBackgroundActivityIdentifier;
@"NSMapTable" _suspendedAttributionsByBackgroundActivityIdentifier;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"FBWorkspaceEventQueue" _eventQueue;
@"NSMutableSet" _backgroundActivityIdentifiers;
@"NSMutableSet" _suspendedBackgroundActivityIdentifiers;
@"SBStatusBarTapManager" _statusBarTapManager;
@"SBBackgroundActivityAssertionServiceManager" _assertionServiceManager;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_statusBarAssertionManagersByWindowScene) statusBarAssertionManagersByWindowScene;
@property (T@"NSMapTable",&,N,V_attributionsByBackgroundActivityIdentifier) attributionsByBackgroundActivityIdentifier;
@property (T@"NSMapTable",&,N,V_suspendedAttributionsByBackgroundActivityIdentifier) suspendedAttributionsByBackgroundActivityIdentifier;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
@property (T@"FBWorkspaceEventQueue",&,N,V_eventQueue) eventQueue;
@property (T@"NSMutableSet",C,N,V_backgroundActivityIdentifiers) backgroundActivityIdentifiers;
@property (T@"NSMutableSet",C,N,V_suspendedBackgroundActivityIdentifiers) suspendedBackgroundActivityIdentifiers;
@property (T@"SBStatusBarTapManager",R,N,V_statusBarTapManager) statusBarTapManager;
@property (T@"SBBackgroundActivityAssertionServiceManager",R,N,V_assertionServiceManager) assertionServiceManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBackgroundActivityAttributionManager eventQueue];
-[SBBackgroundActivityAttributionManager setEventQueue:];
-[SBBackgroundActivityAttributionManager succinctDescriptionBuilder];
-[SBBackgroundActivityAttributionManager windowSceneDidDisconnect:];
-[SBBackgroundActivityAttributionManager dealloc];
-[SBBackgroundActivityAttributionManager descriptionWithMultilinePrefix:];
-[SBBackgroundActivityAttributionManager setBackgroundActivityIdentifiers:];
-[SBBackgroundActivityAttributionManager succinctDescription];
-[SBBackgroundActivityAttributionManager statusBarAssertionManager:statusBarSettingsDidChange:];
-[SBBackgroundActivityAttributionManager description];
-[SBBackgroundActivityAttributionManager backgroundActivityIdentifiers];
-[SBBackgroundActivityAttributionManager setInternalQueue:];
-[SBBackgroundActivityAttributionManager windowSceneDidConnect:];
-[SBBackgroundActivityAttributionManager internalQueue];
-[SBBackgroundActivityAttributionManager descriptionBuilderWithMultilinePrefix:];
-[SBBackgroundActivityAttributionManager _postStatusStringsByIdentifier:];
-[SBBackgroundActivityAttributionManager updateForegroundApplicationSceneHandles:withOptions:completion:];
-[SBBackgroundActivityAttributionManager _applicationForBackgroundActivityAttribution:];
-[SBBackgroundActivityAttributionManager _mainQueue_getBackgroundActivityIdentifiersToSuppressAndStatusStringsByIdentifierForForegroundApplicationSceneHandles:withHandler:];
-[SBBackgroundActivityAttributionManager _queue_updateWithData:andOverrides:];
-[SBBackgroundActivityAttributionManager _registerHandlerAndHandleExistingState];
-[SBBackgroundActivityAttributionManager _statusStringsByIdentifierForActiveAttributionsByBackgroundActivityIdentifier:inactiveAttributionsByBackgroundActivityIdentifier:];
-[SBBackgroundActivityAttributionManager _updateAppSceneSettingsForForegroundAppsAndPostAddedBackgroundActivityIdentifiers:removedBackgroundActivityIdentifiers:];
-[SBBackgroundActivityAttributionManager _updateForegroundApplicationSceneHandlesForAssertionManagerChange];
-[SBBackgroundActivityAttributionManager assertionServiceDidChangeStatusStringsForAForegroundApp];
-[SBBackgroundActivityAttributionManager assertionServiceManager];
-[SBBackgroundActivityAttributionManager attributionsByBackgroundActivityIdentifier];
-[SBBackgroundActivityAttributionManager handleTapForBackgroundActivityWithIdentifier:windowScene:];
-[SBBackgroundActivityAttributionManager initWithSystemStatusServerHandle:applicationController:];
-[SBBackgroundActivityAttributionManager invalidateBackgroundActivityAttributions:];
-[SBBackgroundActivityAttributionManager setAttributionsByBackgroundActivityIdentifier:];
-[SBBackgroundActivityAttributionManager setStatusBarAssertionManagersByWindowScene:];
-[SBBackgroundActivityAttributionManager setSuspendedAttributionsByBackgroundActivityIdentifier:];
-[SBBackgroundActivityAttributionManager setSuspendedBackgroundActivityIdentifiers:];
-[SBBackgroundActivityAttributionManager statusBarAssertionManagersByWindowScene];
-[SBBackgroundActivityAttributionManager statusBarTapManager];
-[SBBackgroundActivityAttributionManager suspendedAttributionsByBackgroundActivityIdentifier];
-[SBBackgroundActivityAttributionManager suspendedBackgroundActivityIdentifiers];
```
