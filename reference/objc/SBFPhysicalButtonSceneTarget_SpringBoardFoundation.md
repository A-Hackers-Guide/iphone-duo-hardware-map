# `SBFPhysicalButtonSceneTarget`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 3 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _targetsByButton;
@"FBScene" _scene;
@"FBSSceneIdentity" _sceneIdentity;
```

## Properties

```
@property (T@"FBScene",R,W,N,V_scene) scene;
@property (T@"FBSSceneIdentity",R,N,V_sceneIdentity) sceneIdentity;
@property (TQ,R,N) count;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFPhysicalButtonSceneTarget mutableCopyWithZone:];
-[SBFPhysicalButtonSceneTarget count];
-[SBFPhysicalButtonSceneTarget sceneIdentity];
-[SBFPhysicalButtonSceneTarget scene];
-[SBFPhysicalButtonSceneTarget hash];
-[SBFPhysicalButtonSceneTarget description];
-[SBFPhysicalButtonSceneTarget appendDescriptionToStream:];
-[SBFPhysicalButtonSceneTarget copyWithZone:];
-[SBFPhysicalButtonSceneTarget isEqual:];
-[SBFPhysicalButtonSceneTarget buttonTargetForButton:];
```
