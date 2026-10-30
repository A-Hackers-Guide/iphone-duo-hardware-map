# `_UIPencilEventDisplayTracker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 3 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
{?="isEnabled"b1} _flags;
@"BSMutableIntegerSet" _foundEmbeddedDisplayIDs;
@"<BSInvalidatable>" _stateCaptureToken;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPencilEventDisplayTracker debugDescription];
-[_UIPencilEventDisplayTracker init];
-[_UIPencilEventDisplayTracker dealloc];
-[_UIPencilEventDisplayTracker _handleSceneWillConnectNotification:];
-[_UIPencilEventDisplayTracker succinctDescription];
-[_UIPencilEventDisplayTracker _handleSceneDidDisconnectNotification:];
-[_UIPencilEventDisplayTracker description];
-[_UIPencilEventDisplayTracker appendDescriptionToStream:];
-[_UIPencilEventDisplayTracker _handleSceneDidEnterBackgroundNotification:];
-[_UIPencilEventDisplayTracker _handleSceneWillEnterForegroundNotification:];
-[_UIPencilEventDisplayTracker _handleSceneWillMoveToScreenNotification:];
-[_UIPencilEventDisplayTracker _handleWindowDidBecomeHiddenNotification:];
-[_UIPencilEventDisplayTracker _handleWindowDidBecomeVisibleNotification:];
```
