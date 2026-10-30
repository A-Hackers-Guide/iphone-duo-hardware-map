# `SBNonInteractiveDisplayWindowSceneDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBNonInteractiveDisplayControllerDelegate`, `UIWindowSceneDelegate`
- 2 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"SBNonInteractiveDisplayController" _nonInteractiveDisplayController;
@"UIWindow" _window;
```

## Properties

```
@property (TB,R,N) isRenderingContent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIWindow",?,&,N,V_window) window;
```

## Class methods

```
+[SBNonInteractiveDisplayWindowSceneDelegate _disallowCompanionSceneSupportForBundleIdentifiers];
```

## Instance methods

```
-[SBNonInteractiveDisplayWindowSceneDelegate sceneDidDisconnect:];
-[SBNonInteractiveDisplayWindowSceneDelegate window];
-[SBNonInteractiveDisplayWindowSceneDelegate scene:willConnectToSession:options:];
-[SBNonInteractiveDisplayWindowSceneDelegate setWindow:];
-[SBNonInteractiveDisplayWindowSceneDelegate isRenderingContent];
-[SBNonInteractiveDisplayWindowSceneDelegate nonInteractiveDisplayController:companionScenesSupportedForHostScene:];
-[SBNonInteractiveDisplayWindowSceneDelegate nonInteractiveDisplayController:shouldDismissView:];
-[SBNonInteractiveDisplayWindowSceneDelegate nonInteractiveDisplayController:shouldPresentView:];
```
