# `SBCompanionSceneViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTraitsOrientedContentViewController`
- Protocols: `BSInvalidatable`
- 3 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<UIScenePresenter>" _scenePresenter;
@"FBScene" _companionScene;
@"FBSSceneIdentityToken" _identityToken;
```

## Properties

```
@property (T@"FBScene",R,N,V_companionScene) companionScene;
@property (T@"FBSSceneIdentityToken",R,N,V_identityToken) identityToken;
@property (TB,R,N,GisActive) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCompanionSceneViewController deactivate];
-[SBCompanionSceneViewController dealloc];
-[SBCompanionSceneViewController viewDidLoad];
-[SBCompanionSceneViewController identityToken];
-[SBCompanionSceneViewController invalidate];
-[SBCompanionSceneViewController activate];
-[SBCompanionSceneViewController isActive];
-[SBCompanionSceneViewController companionScene];
-[SBCompanionSceneViewController initWithCompanionScene:];
```
