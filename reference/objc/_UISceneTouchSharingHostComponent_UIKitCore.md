# `_UISceneTouchSharingHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UIGeometryChangeObserver`, `_UISceneTouchSharing`, `FBSceneComponent`
- 4 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
I _hostContextId;
@"NSMutableSet" _policyAssertions;
B _shareTouchesWithHost;
@"UIView" _targetView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,V_shareTouchesWithHost) shareTouchesWithHost;
@property (T@"UIView",&,N,V_targetView) targetView;
```

## Instance methods

```
-[_UISceneTouchSharingHostComponent targetView];
-[_UISceneTouchSharingHostComponent debugDescription];
-[_UISceneTouchSharingHostComponent setScene:];
-[_UISceneTouchSharingHostComponent dealloc];
-[_UISceneTouchSharingHostComponent _geometryChanged:forAncestor:];
-[_UISceneTouchSharingHostComponent succinctDescription];
-[_UISceneTouchSharingHostComponent setTargetView:];
-[_UISceneTouchSharingHostComponent _windowDidDetachContext:];
-[_UISceneTouchSharingHostComponent description];
-[_UISceneTouchSharingHostComponent appendDescriptionToStream:];
-[_UISceneTouchSharingHostComponent _windowDidAttachContext:];
-[_UISceneTouchSharingHostComponent scene:didUpdateClientSettings:];
-[_UISceneTouchSharingHostComponent cancelTouchesForCurrentEventInClient];
-[_UISceneTouchSharingHostComponent setShareTouchesWithHost:];
-[_UISceneTouchSharingHostComponent shareTouchesWithHost];
```
