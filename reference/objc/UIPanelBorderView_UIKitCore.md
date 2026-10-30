# `UIPanelBorderView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _draggable;
B _renderAsShadow;
B _observesTime;
q _statusBarAvoidance;
@"UIPanelBorderReplicatingView" _replicatingView;
@"NSString" _backdropGroupName;
```

## Properties

```
@property (T@"UIPanelBorderReplicatingView",&,N,V_replicatingView) replicatingView;
@property (TB,N,V_observesTime) observesTime;
@property (T@"NSString",&,N,V_backdropGroupName) backdropGroupName;
@property (Tq,N,V_statusBarAvoidance) statusBarAvoidance;
@property (TB,N,GisDraggable,V_draggable) draggable;
@property (TB,N,V_renderAsShadow) renderAsShadow;
```

## Instance methods

```
-[UIPanelBorderView backdropGroupName];
-[UIPanelBorderView layoutSubviews];
-[UIPanelBorderView setBackdropGroupName:];
-[UIPanelBorderView setDraggable:];
-[UIPanelBorderView isDraggable];
-[UIPanelBorderView initWithFrame:];
-[UIPanelBorderView replicatingView];
-[UIPanelBorderView _cachedBackdropGroupName];
-[UIPanelBorderView observesTime];
-[UIPanelBorderView renderAsShadow];
-[UIPanelBorderView setObservesTime:];
-[UIPanelBorderView setRenderAsShadow:];
-[UIPanelBorderView setReplicatingView:];
-[UIPanelBorderView setStatusBarAvoidance:];
-[UIPanelBorderView statusBarAvoidance];
```
