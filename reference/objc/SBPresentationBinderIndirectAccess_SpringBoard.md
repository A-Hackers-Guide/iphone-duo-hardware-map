# `SBPresentationBinderIndirectAccess`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneObserver`, `BSInvalidatable`
- 2 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayIdentity" _displayIdentity;
@"NSMapTable" _presentedScenesToPresentationBinderWindowScenes;
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
-[SBPresentationBinderIndirectAccess initWithDisplayIdentity:];
-[SBPresentationBinderIndirectAccess dealloc];
-[SBPresentationBinderIndirectAccess invalidate];
-[SBPresentationBinderIndirectAccess sceneWillInvalidate:];
-[SBPresentationBinderIndirectAccess scene:didUpdateClientSettings:];
-[SBPresentationBinderIndirectAccess _createPresentationBinderWindowSceneForScene:traitsRole:];
-[SBPresentationBinderIndirectAccess _invalidateAllPresentationBinderWindowScenes];
-[SBPresentationBinderIndirectAccess addSceneToPresentationBinder:traitsRole:presentingBlock:];
-[SBPresentationBinderIndirectAccess presentationBinderWindowSceneForScene:];
-[SBPresentationBinderIndirectAccess removeSceneFromPresentationBinder:dismissingBlock:];
```
