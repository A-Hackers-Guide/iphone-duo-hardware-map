# `UIRemoteKeyboardWindow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextEffectsWindow`
- Protocols: `BSInvalidatable`
- 6 instance variables, 6 properties, 35 instance methods, 2 class methods

## Instance variables

```
B _arePlaceholdersInitialised;
@"FBSSceneLayer" _keyboardSceneLayer;
@"FBSScene" _activeScene;
B _resetRequired;
B _invalidated;
@"<_UIRemoteKeyboardWindowDelegate>" _rkwDelegate;
```

## Properties

```
@property (T@"FBSSceneIdentityToken",R,N) activeSceneIdentity;
@property (T@"<_UIRemoteKeyboardWindowDelegate>",W,N,V_rkwDelegate) _rkwDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIRemoteKeyboardWindow _isHostedInAnotherProcess];
+[UIRemoteKeyboardWindow remoteKeyboardWindowForScreen:create:];
```

## Instance methods

```
-[UIRemoteKeyboardWindow dealloc];
-[UIRemoteKeyboardWindow _alwaysGetsContexts];
-[UIRemoteKeyboardWindow hitTest:withEvent:];
-[UIRemoteKeyboardWindow initWithWindowScene:];
-[UIRemoteKeyboardWindow invalidate];
-[UIRemoteKeyboardWindow _shouldAutorotateToInterfaceOrientation:];
-[UIRemoteKeyboardWindow setWindowLevel:];
-[UIRemoteKeyboardWindow _adjustedWindowLevelFromLevel:];
-[UIRemoteKeyboardWindow _matchingOptions:];
-[UIRemoteKeyboardWindow _usesWindowServerHitTesting];
-[UIRemoteKeyboardWindow _isEligibleForFocusOcclusion];
-[UIRemoteKeyboardWindow isTransparentFocusItem];
-[UIRemoteKeyboardWindow isInternalWindow];
-[UIRemoteKeyboardWindow _isFullscreen];
-[UIRemoteKeyboardWindow _canIgnoreInteractionEvents];
-[UIRemoteKeyboardWindow _configureAlphaIfNecessary];
-[UIRemoteKeyboardWindow _isAlwaysKeyboardWindow];
-[UIRemoteKeyboardWindow _isHostedInAnotherProcess];
-[UIRemoteKeyboardWindow _isRemoteKeyboardWindow];
-[UIRemoteKeyboardWindow _isTextEffectsWindowNotificationOwner];
-[UIRemoteKeyboardWindow _layerForCoordinateSpaceConversion];
-[UIRemoteKeyboardWindow _orientationForClassicPresentation];
-[UIRemoteKeyboardWindow _orientationInSceneSpace];
-[UIRemoteKeyboardWindow _resetScene];
-[UIRemoteKeyboardWindow _rkwDelegate];
-[UIRemoteKeyboardWindow _setRotatableClient:toOrientation:updateStatusBar:duration:force:isRotating:];
-[UIRemoteKeyboardWindow activeSceneIdentity];
-[UIRemoteKeyboardWindow endDisablingInterfaceAutorotation];
-[UIRemoteKeyboardWindow keepContextInBackground];
-[UIRemoteKeyboardWindow legacy_attachBindable];
-[UIRemoteKeyboardWindow legacy_detachBindable];
-[UIRemoteKeyboardWindow legacy_shouldAttachBindable];
-[UIRemoteKeyboardWindow legacy_shouldDetachBindable];
-[UIRemoteKeyboardWindow resetScene];
-[UIRemoteKeyboardWindow set_rkwDelegate:];
```
