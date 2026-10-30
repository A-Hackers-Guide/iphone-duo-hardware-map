# `SBSystemUISceneResolutionStage`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBKeyboardFocusResolutionStage`
- 2 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<SBKeyboardFocusResolutionStageSceneProviding>" _sceneProvider;
@"<SBSystemUISceneResolutionStageDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBSystemUISceneResolutionStageDelegate>",W,N,V_delegate) delegate;
@property (T@"<SBKeyboardFocusResolutionStageSceneProviding>",W,N,V_sceneProvider) sceneProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemUISceneResolutionStage setDelegate:];
-[SBSystemUISceneResolutionStage delegate];
-[SBSystemUISceneResolutionStage resolveKeyboardFocusPolicy:context:stop:];
-[SBSystemUISceneResolutionStage sceneProvider];
-[SBSystemUISceneResolutionStage setSceneProvider:];
```
