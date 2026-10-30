# `SBFSceneWorkspaceDefaultDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFSceneWorkspaceControllerDelegate`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _scenesActivatedUponClientConnection;
@"NSMutableSet" _scenesKeptActiveWhileForeground;
@"NSMutableSet" _scenesAlwaysKeptActive;
@"NSMutableDictionary" _scenesWithActivationContextGeneratorBlock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFSceneWorkspaceDefaultDelegate sceneDidDeactivate:withContext:];
-[SBFSceneWorkspaceDefaultDelegate workspace:clientDidConnectWithHandshake:];
-[SBFSceneWorkspaceDefaultDelegate init];
-[SBFSceneWorkspaceDefaultDelegate sceneDidActivate:];
-[SBFSceneWorkspaceDefaultDelegate workspace:willRemoveScene:];
-[SBFSceneWorkspaceDefaultDelegate _cleanupTransitionContextGeneratorBlockForSceneIfNeeded:];
-[SBFSceneWorkspaceDefaultDelegate sceneContentStateDidChange:];
-[SBFSceneWorkspaceDefaultDelegate workspace:didAddScene:];
-[SBFSceneWorkspaceDefaultDelegate _setScene:cached:inContainer:withContextGenerator:];
-[SBFSceneWorkspaceDefaultDelegate setScene:shouldActivateUponClientConnection:withContextGenerator:];
-[SBFSceneWorkspaceDefaultDelegate _setScene:activatesWithTransitionContextGeneratorBlock:];
-[SBFSceneWorkspaceDefaultDelegate setScene:shouldAlwaysBeKeptActive:withContextGenerator:];
-[SBFSceneWorkspaceDefaultDelegate _activateScene:];
-[SBFSceneWorkspaceDefaultDelegate setScene:shouldBeKeptActiveWhileForeground:withContextGenerator:];
```
