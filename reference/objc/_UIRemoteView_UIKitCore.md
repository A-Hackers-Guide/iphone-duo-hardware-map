# `_UIRemoteView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UILayerHostView`
- 2 instance variables, 4 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"_UIHostedWindowHostingHandle" _hostedWindowHostingHandle;
@"_UIRemoteViewController" _remoteViewController;
```

## Properties

```
@property (T#,N,R) _intelligenceBaseClass;
@property (TB,N,S_setInheritsSecurity:) _inheritsSecurity;
@property (T@"_UIRemoteViewController",W,N,V_remoteViewController) remoteViewController;
@property (T@"_UIHostedWindowHostingHandle",&,N,V_hostedWindowHostingHandle) hostedWindowHostingHandle;
```

## Class methods

```
+[_UIRemoteView _requiresWindowTouches];
+[_UIRemoteView viewWithHostedWindowHostingHandle:];
```

## Instance methods

```
-[_UIRemoteView initWithFrame:pid:contextID:];
-[_UIRemoteView _intelligenceCollectContentIn:collector:];
-[_UIRemoteView remoteViewController];
-[_UIRemoteView _inheritsSecurity];
-[_UIRemoteView hostedWindowHostingHandle];
-[_UIRemoteView tintColorDidChange];
-[_UIRemoteView applyTransformUndoingRemoteRootLayerTransform:frame:];
-[_UIRemoteView setHostedWindowHostingHandle:];
-[_UIRemoteView setRemoteViewController:];
-[_UIRemoteView _hitTest:withEvent:windowServerHitTestWindow:];
-[_UIRemoteView _intelligenceBaseClass];
-[_UIRemoteView _intelligenceCollectRemoteContentIn:remoteContextWrapper:];
-[_UIRemoteView _setInheritsSecurity:];
```
