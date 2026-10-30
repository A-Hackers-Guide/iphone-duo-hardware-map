# `UIDestroySceneAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAction`
- 0 instance variables, 5 properties, 13 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) preferredAnimationType;
@property (T@"NSSet",R,N) persistedIdentifiers;
@property (TB,R,N) destroySceneSession;
@property (TB,R,N) appliesToAllScenes;
@property (TB,R,N,GisUserOriginatedRequest) userOriginatedRequest;
```

## Instance methods

```
-[UIDestroySceneAction persistedIdentifiers];
-[UIDestroySceneAction UIActionType];
-[UIDestroySceneAction abortForUsageViolation:];
-[UIDestroySceneAction initWithPersistedIdentifiers:preferredAnimationType:forDestroyingSession:userOriginatedRequest:callbackQueue:completion:];
-[UIDestroySceneAction initWithPreferredAnimationType:callbackQueue:completion:];
-[UIDestroySceneAction destroySceneSession];
-[UIDestroySceneAction initWithPersistedIdentifiers:preferredAnimationType:forDestroyingSession:applyToAllScenes:userOriginatedRequest:callbackQueue:completion:];
-[UIDestroySceneAction isUserOriginatedRequest];
-[UIDestroySceneAction keyDescriptionForSetting:];
-[UIDestroySceneAction appliesToAllScenes];
-[UIDestroySceneAction preferredAnimationType];
-[UIDestroySceneAction initWithPersistedIdentifiers:preferredAnimationType:callbackQueue:completion:];
-[UIDestroySceneAction initWithPersistedIdentifiers:preferredAnimationType:forDestroyingSession:callbackQueue:completion:];
```
