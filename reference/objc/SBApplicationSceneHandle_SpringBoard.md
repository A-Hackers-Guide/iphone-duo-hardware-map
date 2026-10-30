# `SBApplicationSceneHandle`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSceneHandle`
- 9 instance variables, 5 properties, 35 instance methods, 1 class methods

## Instance variables

```
@"SBApplication" _application;
@"NSString" _persistenceIdentifier;
B _isSecure;
@"NSHashTable" _sceneUpdateContributers;
Q _userLaunchSignpostID;
@"NSObject<OS_xpc_object>" _launchMetricsPayload;
d _userLaunchEventTime;
B _sceneUpdateInProgress;
q _layoutRole;
```

## Properties

```
@property (TB,N,GisSceneUpdateInProgress,V_sceneUpdateInProgress) sceneUpdateInProgress;
@property (T@"SBApplication",R,N,V_application) application;
@property (T@"NSString",R,N,V_persistenceIdentifier) persistenceIdentifier;
@property (TB,R,N,GisSecure,V_isSecure) secure;
@property (Tq,N,V_layoutRole) layoutRole;
```

## Class methods

```
+[SBApplicationSceneHandle lookupOrCreatePersistenceIDFromApplication:sceneID:];
```

## Instance methods

```
-[SBApplicationSceneHandle _commonInit];
-[SBApplicationSceneHandle isSecure];
-[SBApplicationSceneHandle _initWithScene:];
-[SBApplicationSceneHandle layoutRole];
-[SBApplicationSceneHandle application];
-[SBApplicationSceneHandle _commonInitWithApplication:sceneIdentifier:displayIdentity:];
-[SBApplicationSceneHandle setLayoutRole:];
-[SBApplicationSceneHandle _modifyApplicationTransitionContext:fromRequestContext:entity:];
-[SBApplicationSceneHandle dealloc];
-[SBApplicationSceneHandle _modifyProcessExecutionContext:fromRequestContext:entity:];
-[SBApplicationSceneHandle _modifyApplicationSceneAndSceneSettings:fromRequestContext:entity:];
-[SBApplicationSceneHandle newSceneViewController];
-[SBApplicationSceneHandle _applicationsDidChange:];
-[SBApplicationSceneHandle displayItemRepresentation];
-[SBApplicationSceneHandle newScenePlaceholderContentContextWithActivationSettings:];
-[SBApplicationSceneHandle persistenceIdentifier];
-[SBApplicationSceneHandle newSceneViewWithReferenceSize:contentOrientation:containerOrientation:hostRequester:];
-[SBApplicationSceneHandle _modifyApplicationSceneClientSettings:fromRequestContext:entity:initialSceneSettings:];
-[SBApplicationSceneHandle _stopObserving];
-[SBApplicationSceneHandle _persistenceIdentifier];
-[SBApplicationSceneHandle _initWithDefinition:];
-[SBApplicationSceneHandle _createApplicationSceneClientSettingsFromContext:entity:initialSceneSettings:];
-[SBApplicationSceneHandle _createApplicationSceneSettingsFromContext:entity:];
-[SBApplicationSceneHandle _createApplicationSceneTransitionContextFromContext:entity:];
-[SBApplicationSceneHandle _createParametersFromTransitionContext:entity:];
-[SBApplicationSceneHandle _createProcessExecutionContextFromContext:entity:];
-[SBApplicationSceneHandle _finalizeLaunchSignpostState];
-[SBApplicationSceneHandle _initWithApplication:scene:displayIdentity:secure:];
-[SBApplicationSceneHandle _initWithApplication:sceneDefinition:displayIdentity:secure:];
-[SBApplicationSceneHandle _updateApplicationSceneAndSceneSettings:fromContext:entity:];
-[SBApplicationSceneHandle _updateSceneTransitionContext:fromRequestContext:entity:];
-[SBApplicationSceneHandle addSceneUpdateContributer:];
-[SBApplicationSceneHandle isSceneUpdateInProgress];
-[SBApplicationSceneHandle removeSceneUpdateContributer:];
-[SBApplicationSceneHandle setSceneUpdateInProgress:];
```
