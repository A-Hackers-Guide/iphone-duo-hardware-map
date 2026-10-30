# `_UISceneHostingHierarchyInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIGeometryChangeObserver`, `_UIKeyboardInputScenePairingClientObserver`, `UIInteraction_Internal`, `UIInteraction`
- 12 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _reportedSceneFrame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _reportedSafeAreaInsets;
{_UICornerInsets="topLeft"{CGSize="width"d"height"d}"bottomLeft"{CGSize="width"d"height"d}"bottomRight"{CGSize="width"d"height"d}"topRight"{CGSize="width"d"height"d}} _reportedSafeAreaCornerInsets;
@"BSCornerRadiusConfiguration" _reportedCornerRadiusConfiguration;
@"_UISceneBarAlignmentsResolver" _reportedBarAlignmentResolver;
@"_UISceneBarSizeClassResolver" _reportedBarSizeClassResolver;
@"_UISceneBarPositionResolver" _reportedBarPositionResolver;
q _reportedOrientation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _reportedSceneFrameInKeyboardReferenceSpace;
@"_UIKeyboardInputScenePairingClientComponent" _observedHostPairing;
@"UIView" _view;
@"<_UISceneHostingHierarchyInteractionDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UISceneHostingHierarchyInteractionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UISceneHostingHierarchyInteraction updateIfNeeded];
-[_UISceneHostingHierarchyInteraction updateScene:];
-[_UISceneHostingHierarchyInteraction dealloc];
-[_UISceneHostingHierarchyInteraction keyboardInputScenePairingClientDidUpdateGeometry:];
-[_UISceneHostingHierarchyInteraction _geometryChanged:forAncestor:];
-[_UISceneHostingHierarchyInteraction view];
-[_UISceneHostingHierarchyInteraction setDelegate:];
-[_UISceneHostingHierarchyInteraction isParentSceneSized];
-[_UISceneHostingHierarchyInteraction willMoveToView:];
-[_UISceneHostingHierarchyInteraction delegate];
-[_UISceneHostingHierarchyInteraction _viewVisibilityDidChange];
-[_UISceneHostingHierarchyInteraction didMoveToView:];
```
