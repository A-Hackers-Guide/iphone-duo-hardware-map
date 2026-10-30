# `SBContinuitySessionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBContinuitySessionFactory`, `SBContinuitySessionStateObserver`, `BSDescriptionStreaming`
- 10 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"SBContinuitySessionService" _service;
@"<SBContinuitySessionFactory>" _sessionFactory;
@"<BSInvalidatable>" _stateDumpHandle;
@"SBOverridableUserInterfaceStyleProvider" _userInterfaceStyleProvider;
@"NSMutableArray" _waitingWindowScenes;
@"SBContinuityDisplayLayoutCoordinator" _displayLayoutCoordinator;
@"<SBContinuitySessionManagerExternalDependencyProviding>" _externalDependencyProvider;
@"SBApplicationController" _applicationController;
@"SBContinuitySession" _currentSession;
@"SBContinuityDisplayAuthenticationCoordinator" _displayAuthenticationCoordinator;
```

## Properties

```
@property (T@"SBContinuitySession",&,N,V_currentSession) currentSession;
@property (T@"SBOverridableUserInterfaceStyleProvider",R,N) overridableUserInterfaceStyleProvider;
@property (T@"SBContinuityDisplayAuthenticationCoordinator",R,N,V_displayAuthenticationCoordinator) displayAuthenticationCoordinator;
@property (T@"<SBUserInterfaceStyleProvider>",R,N) userInterfaceStyleProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBContinuitySessionManager areContinuitySessionsAllowed];
```

## Instance methods

```
-[SBContinuitySessionManager setCurrentSession:];
-[SBContinuitySessionManager dealloc];
-[SBContinuitySessionManager activate];
-[SBContinuitySessionManager description];
-[SBContinuitySessionManager currentSession];
-[SBContinuitySessionManager appendDescriptionToStream:];
-[SBContinuitySessionManager _initWithService:userInterfaceStyleProvider:displayLayoutCoordinator:sessionFactory:externalDependencyProvider:displayAuthenticationCoordinator:applicationController:];
-[SBContinuitySessionManager _noteSceneOrSessionIsWaiting];
-[SBContinuitySessionManager _registerScene:sessionConnectionCallout:sessionDisconnectionCallout:];
-[SBContinuitySessionManager _setCurrentSession:postNotification:];
-[SBContinuitySessionManager continuitySessionDidUpdateState:];
-[SBContinuitySessionManager displayAuthenticationCoordinator];
-[SBContinuitySessionManager initWithLockScreenCoordinator:keyBag:applicationController:];
-[SBContinuitySessionManager newContinuitySession];
-[SBContinuitySessionManager overridableUserInterfaceStyleProvider];
-[SBContinuitySessionManager registerSystemApertureCurtainWindowScene:];
-[SBContinuitySessionManager registerSystemApertureWindowScene:];
-[SBContinuitySessionManager registerWindowScene:];
-[SBContinuitySessionManager userInterfaceStyleProvider];
```
