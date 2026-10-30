# `FBSSceneEvent`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneMessage`
- 4 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
q _source;
@"FBSSceneSettingsDiff" _settingsDiff;
@"FBSSceneClientSettingsDiff" _clientSettingsDiff;
@"FBSSceneTransitionContext" _transitionContext;
```

## Properties

```
@property (Tq,N,V_source) source;
@property (T@"FBSSceneSettingsDiff",&,N,V_settingsDiff) settingsDiff;
@property (T@"FBSSceneClientSettingsDiff",&,N,V_clientSettingsDiff) clientSettingsDiff;
@property (T@"FBSSceneTransitionContext",&,N,V_transitionContext) transitionContext;
@property (T@"NSSet",R,N) actions;
```

## Instance methods

```
-[FBSSceneEvent settingsDiff];
-[FBSSceneEvent succinctDescriptionBuilder];
-[FBSSceneEvent transitionContext];
-[FBSSceneEvent init];
-[FBSSceneEvent setClientSettingsDiff:];
-[FBSSceneEvent setTransitionContext:];
-[FBSSceneEvent descriptionWithMultilinePrefix:];
-[FBSSceneEvent actions];
-[FBSSceneEvent setSource:];
-[FBSSceneEvent succinctDescription];
-[FBSSceneEvent setSettingsDiff:];
-[FBSSceneEvent description];
-[FBSSceneEvent source];
-[FBSSceneEvent clientSettingsDiff];
-[FBSSceneEvent descriptionBuilderWithMultilinePrefix:];
```
