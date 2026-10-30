# `UIRootSceneWindow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRootWindow`
- Protocols: `UIMutableTransformerDelegate`
- 3 instance variables, 7 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"FBSDisplayConfiguration" _displayConfiguration;
@"UIView" _sceneContainerView;
@"UIMutableTransformer" _sceneTransformer;
```

## Properties

```
@property (T@"UIView",R,N,V_sceneContainerView) _sceneContainerView;
@property (T@"FBSDisplayConfiguration",R,N,V_displayConfiguration) displayConfiguration;
@property (T@"UIMutableTransformer",R,N,V_sceneTransformer) sceneTransformer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIRootSceneWindow _isSecure];
+[UIRootSceneWindow definesDisplayBounds];
```

## Instance methods

```
-[UIRootSceneWindow initWithScreen:];
-[UIRootSceneWindow initWithDisplay:];
-[UIRootSceneWindow displayConfiguration];
-[UIRootSceneWindow _focusResponder];
-[UIRootSceneWindow dealloc];
-[UIRootSceneWindow sceneTransformer];
-[UIRootSceneWindow initWithDisplayConfiguration:];
-[UIRootSceneWindow hitTest:withEvent:];
-[UIRootSceneWindow _shouldPrepareScreenForWindow];
-[UIRootSceneWindow canBecomeKeyWindow];
-[UIRootSceneWindow _appearsInLoupe];
-[UIRootSceneWindow transformsDidChange:];
-[UIRootSceneWindow _usesWindowServerHitTesting];
-[UIRootSceneWindow setFrame:];
-[UIRootSceneWindow _configureContextOptions:];
-[UIRootSceneWindow _updateTransforms];
-[UIRootSceneWindow _sceneContainerView];
```
