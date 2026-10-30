# `SBBacklightEnvironmentSessionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightInactiveEnvironmentSessionObserving`, `BLSHBacklightEnvironmentSessionProviding`
- 8 instance variables, 5 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _globalBacklightEnvironmentSceneProviders;
@"NSMapTable" _backlightEnvironmentSceneProvidersByWindowScene;
@"NSMapTable" _backlightSceneHostEnvironmentProvidersByWindowScene;
@"NSHashTable" _observers;
@"NSMutableDictionary" _scenelessSessions;
@"NSMapTable" _currentSessionsByWindowScene;
@"<BSInvalidatable>" _presentationUpdateLiveRenderAssertion;
B _springBoardBootCompleted;
```

## Properties

```
@property (T@"NSSet",R,C,N) currentPresentationBundleIdentifiers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBacklightEnvironmentSessionProvider didEndInactiveEnvironmentSession:];
-[SBBacklightEnvironmentSessionProvider registerBacklightSceneHostEnvironmentProvider:windowScene:];
-[SBBacklightEnvironmentSessionProvider _setCurrentSession:forWindowScene:];
-[SBBacklightEnvironmentSessionProvider _buildPresentationForWindowScene:];
-[SBBacklightEnvironmentSessionProvider _windowSceneForBLSDisplay:];
-[SBBacklightEnvironmentSessionProvider removeObserver:];
-[SBBacklightEnvironmentSessionProvider init];
-[SBBacklightEnvironmentSessionProvider _rebuildPresentation];
-[SBBacklightEnvironmentSessionProvider _windowSceneForSession:];
-[SBBacklightEnvironmentSessionProvider _currentSessionForWindowScene:];
-[SBBacklightEnvironmentSessionProvider invalidateBacklightScenesForProvider:];
-[SBBacklightEnvironmentSessionProvider createInactiveEnvironmentSession];
-[SBBacklightEnvironmentSessionProvider unregisterBacklightSceneHostEnvironmentProvider:windowScene:];
-[SBBacklightEnvironmentSessionProvider addObserver:];
-[SBBacklightEnvironmentSessionProvider _backlightPresentationEntriesForWindowScene:];
-[SBBacklightEnvironmentSessionProvider _currentPresentationBundleIdentifiersForSession:];
-[SBBacklightEnvironmentSessionProvider _createInactiveEnvironmentSessionForWindowScene:];
-[SBBacklightEnvironmentSessionProvider invalidateBacklightSceneHostEnvironmentsForProvider:];
-[SBBacklightEnvironmentSessionProvider registerGlobalBacklightEnvironmentSceneProvider:];
-[SBBacklightEnvironmentSessionProvider createInactiveEnvironmentSessionForDisplay:];
-[SBBacklightEnvironmentSessionProvider currentPresentationBundleIdentifiers];
-[SBBacklightEnvironmentSessionProvider inactiveEnvironmentSession:didUpdateToPresentation:];
-[SBBacklightEnvironmentSessionProvider _rebuildPresentationForWindowScene:];
-[SBBacklightEnvironmentSessionProvider _windowSceneForBLSDisplayReferenceId:];
-[SBBacklightEnvironmentSessionProvider unregisterBacklightEnvironmentSceneProvider:windowScene:];
-[SBBacklightEnvironmentSessionProvider _notifyObserversOfPresentation];
-[SBBacklightEnvironmentSessionProvider registerBacklightEnvironmentSceneProvider:windowScene:];
```
