# `SBSceneDisconnectionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _isExecuting;
Q _numberOfRecentScenesExcludedFromDisconnection;
```

## Properties

```
@property (TQ,N,V_numberOfRecentScenesExcludedFromDisconnection) numberOfRecentScenesExcludedFromDisconnection;
@property (TB,N,V_isExecuting) isExecuting;
```

## Class methods

```
+[SBSceneDisconnectionManager sharedManager];
```

## Instance methods

```
-[SBSceneDisconnectionManager init];
-[SBSceneDisconnectionManager isExecuting];
-[SBSceneDisconnectionManager setIsExecuting:];
-[SBSceneDisconnectionManager _beginSceneCleanupWithBackgroundedSceneEntities:];
-[SBSceneDisconnectionManager disconnectScenes:completion:];
-[SBSceneDisconnectionManager liveScenesForApplication:];
-[SBSceneDisconnectionManager numberOfRecentScenesExcludedFromDisconnection];
-[SBSceneDisconnectionManager positionOf:inSwitcher:];
-[SBSceneDisconnectionManager setNumberOfRecentScenesExcludedFromDisconnection:];
-[SBSceneDisconnectionManager shouldDisconnectScene:inSwitcher:];
```
