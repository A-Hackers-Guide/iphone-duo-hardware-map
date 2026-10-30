# `SBSystemApertureSceneHoster`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSSystemApertureScenePresentationSessionServerDelegate`, `BSInvalidatable`
- 4 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _activeElements;
@"NSMutableSet" _pendingElements;
@"<SBSystemApertureBackgroundActivitiesSuppressing><SAElementRegistering>" _backgroundSuppressingRegistrar;
@"SBSSystemApertureScenePresentationSessionServer" _server;
```

## Properties

```
@property (T@"<SBSystemApertureBackgroundActivitiesSuppressing><SAElementRegistering>",W,N,V_backgroundSuppressingRegistrar) backgroundSuppressingRegistrar;
@property (T@"SBSSystemApertureScenePresentationSessionServer",&,N,V_server) server;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureSceneHoster setServer:];
-[SBSystemApertureSceneHoster server];
-[SBSystemApertureSceneHoster _registerElement:];
-[SBSystemApertureSceneHoster invalidate];
-[SBSystemApertureSceneHoster sceneCreationRequestServer:didReceiveRequestForSystemApertureSceneWithClientIdentity:];
-[SBSystemApertureSceneHoster sceneCreationRequestServer:invalidateSceneElement:];
-[SBSystemApertureSceneHoster _removeElement:];
-[SBSystemApertureSceneHoster _addPendingElement:];
-[SBSystemApertureSceneHoster _enumerateElementsUsingBlock:];
-[SBSystemApertureSceneHoster _invalidateElement:];
-[SBSystemApertureSceneHoster _removePendingElement:];
-[SBSystemApertureSceneHoster backgroundSuppressingRegistrar];
-[SBSystemApertureSceneHoster initWithBackgroundSuppressingRegistrar:];
-[SBSystemApertureSceneHoster setBackgroundSuppressingRegistrar:];
```
