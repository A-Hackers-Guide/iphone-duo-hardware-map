# `_UIVisibilityPropagationInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `UIInteraction`
- 17 instance variables, 6 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"RBSTarget" _visibilityLock_target;
@"UIView" _visibilityLock_view;
@"UIWindow" _visibilityLock_window;
@"NSMutableArray" _visibilityLock_windowChangeNotifications;
@"NSString" _visibilityLock_windowEnvironment;
@"NSString" _visibilityLock_sourceEnvironment;
@"RBSTarget" _visibilityProcessingLock_target;
@"NSString" _visibilityProcessingLock_sourceEnvironment;
@"BSServiceConnectionEndpointInjector" _visibilityProcessingLock_endpointInjector;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _visibilityLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _visibilityProcessingLock;
B _visibilityLock_enabled;
B _visibilityLock_isTrackingView;
B _visibilityLock_isViewVisible;
B _visibilityLock_isTrackingWindow;
B _visibilityLock_updateEnqueued;
B _visibilityLock_invalidated;
```

## Properties

```
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIVisibilityPropagationInteraction interactionWithPID:environmentIdentifier:];
```

## Instance methods

```
-[_UIVisibilityPropagationInteraction dealloc];
-[_UIVisibilityPropagationInteraction _didMoveFromWindow:toWindow:];
-[_UIVisibilityPropagationInteraction view];
-[_UIVisibilityPropagationInteraction willMoveToView:];
-[_UIVisibilityPropagationInteraction _viewVisibilityDidChange];
-[_UIVisibilityPropagationInteraction didMoveToView:];
```
