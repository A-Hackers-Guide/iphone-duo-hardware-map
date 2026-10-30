# `_UIUnflockItemAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
q _type;
@"_UIMorphingPlatterView" _platterView;
@"UITargetedPreview" _destination;
@"UIView" _positionReferenceView;
@"_UIUnflockReparentingView" _reparentingContainerView;
@"_UIPortalView" _reparentingPortalView;
@"UIViewFloatAnimatableProperty" _positionTrackingProperty;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"_UIMorphingPlatterView",&,N,V_platterView) platterView;
@property (T@"UITargetedPreview",&,N,V_destination) destination;
@property (T@"UIView",&,N,V_positionReferenceView) positionReferenceView;
@property (T@"_UIUnflockReparentingView",&,N,V_reparentingContainerView) reparentingContainerView;
@property (T@"_UIPortalView",&,N,V_reparentingPortalView) reparentingPortalView;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_positionTrackingProperty) positionTrackingProperty;
```

## Class methods

```
+[_UIUnflockItemAnimation animationWithPlatterView:destination:positionReferenceView:type:];
```

## Instance methods

```
-[_UIUnflockItemAnimation platterView];
-[_UIUnflockItemAnimation destination];
-[_UIUnflockItemAnimation play];
-[_UIUnflockItemAnimation setPlatterView:];
-[_UIUnflockItemAnimation complete];
-[_UIUnflockItemAnimation setDestination:];
-[_UIUnflockItemAnimation setType:];
-[_UIUnflockItemAnimation type];
-[_UIUnflockItemAnimation positionReferenceView];
-[_UIUnflockItemAnimation positionTrackingProperty];
-[_UIUnflockItemAnimation reparentingContainerView];
-[_UIUnflockItemAnimation reparentingPortalView];
-[_UIUnflockItemAnimation setPositionReferenceView:];
-[_UIUnflockItemAnimation setPositionTrackingProperty:];
-[_UIUnflockItemAnimation setReparentingContainerView:];
-[_UIUnflockItemAnimation setReparentingPortalView:];
```
