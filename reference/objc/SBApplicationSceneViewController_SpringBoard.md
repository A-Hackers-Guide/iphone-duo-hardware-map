# `SBApplicationSceneViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSceneViewController`
- Protocols: `SBApplicationSceneViewControlling`
- 3 instance variables, 17 properties, 9 instance methods, 0 class methods

## Instance variables

```
B __applicationStatusBarHidden;
@"<SBApplicationSceneViewControllingStatusBarDelegate>" _applicationSceneStatusBarDelegate;
@"SBStatusBarSettings" _overrideStatusBarSettings;
```

## Properties

```
@property (T@"SBApplicationSceneView",R,D,N,G_sceneView) sceneView;
@property (TB,R,N,G_isApplicationStatusBarHidden,V__applicationStatusBarHidden) _applicationStatusBarHidden;
@property (T@"SBStatusBarSettings",&,N,G_overrideStatusBarSettings,S_setOverrideStatusBarSettings:,V_overrideStatusBarSettings) overrideStatusBarSettings;
@property (T@"SBApplicationSceneHandle",R,N) sceneHandle;
@property (Td,R,N) statusBarAlpha;
@property (Tq,R,N) overrideStatusBarStyle;
@property (T@"<SBApplicationSceneViewControllingStatusBarDelegate>",W,N,V_applicationSceneStatusBarDelegate) applicationSceneStatusBarDelegate;
@property (Tq,R,N) displayMode;
@property (T@"<SBScenePlaceholderContentContext>",&,N) placeholderContentContext;
@property (T@"UIView",&,N) customContentView;
@property (T{CGSize=dd},R,N) contentReferenceSize;
@property (Tq,R,N) contentOrientation;
@property (Tq,R,N) containerOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationSceneViewController statusBarAlpha];
-[SBApplicationSceneViewController setApplicationSceneStatusBarDelegate:];
-[SBApplicationSceneViewController initWithSceneHandle:];
-[SBApplicationSceneViewController applicationSceneStatusBarDelegate];
-[SBApplicationSceneViewController overrideStatusBarStyle];
-[SBApplicationSceneViewController _applicationStatusBarAlpha];
-[SBApplicationSceneViewController _isApplicationStatusBarHidden];
-[SBApplicationSceneViewController _overrideStatusBarSettings];
-[SBApplicationSceneViewController _setOverrideStatusBarSettings:];
```
