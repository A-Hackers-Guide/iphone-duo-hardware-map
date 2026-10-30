# `SBIdleTimerCoordinatorHelper`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<SBIdleTimerProviding>" _sourceProvider;
@"<SBIdleTimerCoordinating>" _targetCoordinator;
@"NSMapTable" _idleTimerCache;
```

## Properties

```
@property (T@"<SBIdleTimerProviding>",W,N,V_sourceProvider) sourceProvider;
@property (T@"NSMapTable",R,N,V_idleTimerCache) idleTimerCache;
@property (T@"<SBIdleTimerCoordinating>",W,N,V_targetCoordinator) targetCoordinator;
```

## Instance methods

```
-[SBIdleTimerCoordinatorHelper init];
-[SBIdleTimerCoordinatorHelper removeProvider:];
-[SBIdleTimerCoordinatorHelper initWithSourceProvider:];
-[SBIdleTimerCoordinatorHelper sourceProvider];
-[SBIdleTimerCoordinatorHelper updateProvider:behavior:reason:];
-[SBIdleTimerCoordinatorHelper _updateProvider:behavior:reason:];
-[SBIdleTimerCoordinatorHelper _updateProviderInfo:behavior:reason:];
-[SBIdleTimerCoordinatorHelper bindProvider:toSourceTimer:behavior:forReason:];
-[SBIdleTimerCoordinatorHelper hasProvider:];
-[SBIdleTimerCoordinatorHelper idleTimerCache];
-[SBIdleTimerCoordinatorHelper idleTimerProxyForProvider:];
-[SBIdleTimerCoordinatorHelper proposeIdleTimerBehavior:fromProvider:reason:];
-[SBIdleTimerCoordinatorHelper proposeProvider:byCoordinator:reason:];
-[SBIdleTimerCoordinatorHelper setSourceProvider:];
-[SBIdleTimerCoordinatorHelper setTargetCoordinator:];
-[SBIdleTimerCoordinatorHelper targetCoordinator];
```
