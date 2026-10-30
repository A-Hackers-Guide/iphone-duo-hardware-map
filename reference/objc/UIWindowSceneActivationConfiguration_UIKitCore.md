# `UIWindowSceneActivationConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSUserActivity" _userActivity;
@"UIWindowSceneActivationRequestOptions" _options;
@"UITargetedPreview" _preview;
Q __animationSource;
@"<_UIWindowSceneActivator>" __sceneActivator;
```

## Properties

```
@property (TQ,N,S_setAnimationSource:,V__animationSource) _animationSource;
@property (T@"<_UIWindowSceneActivator>",W,N,S_setSceneActivator:,V__sceneActivator) _sceneActivator;
@property (T@"NSUserActivity",R,N,V_userActivity) userActivity;
@property (T@"UIWindowSceneActivationRequestOptions",&,N,V_options) options;
@property (T@"UITargetedPreview",&,N,V_preview) preview;
```

## Instance methods

```
-[UIWindowSceneActivationConfiguration preview];
-[UIWindowSceneActivationConfiguration setOptions:];
-[UIWindowSceneActivationConfiguration userActivity];
-[UIWindowSceneActivationConfiguration setPreview:];
-[UIWindowSceneActivationConfiguration initWithUserActivity:];
-[UIWindowSceneActivationConfiguration description];
-[UIWindowSceneActivationConfiguration options];
-[UIWindowSceneActivationConfiguration copyWithZone:];
-[UIWindowSceneActivationConfiguration _sceneActivator];
-[UIWindowSceneActivationConfiguration _animationSource];
-[UIWindowSceneActivationConfiguration _setAnimationSource:];
-[UIWindowSceneActivationConfiguration _setSceneActivator:];
```
