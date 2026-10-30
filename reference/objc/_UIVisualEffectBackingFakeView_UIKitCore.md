# `_UIVisualEffectBackingFakeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIVisualEffectViewParticipating`
- 5 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIView<_UIVisualEffectViewParticipating>" _containedView;
@"NSArray" _filters;
@"_UIVisualEffectViewBackdropCaptureGroup" _primaryCaptureGroup;
@"NSArray" _viewEffects;
@"UIView" _clientView;
```

## Properties

```
@property (T@"UIView",W,N,V_clientView) clientView;
@property (T@"_UIVisualEffectViewBackdropCaptureGroup",&,N,V_primaryCaptureGroup) primaryCaptureGroup;
@property (T@"UIView<_UIVisualEffectViewParticipating>",&,N,V_containedView) containedView;
@property (T@"NSArray",C,N,V_viewEffects) viewEffects;
@property (T@"NSArray",C,N,V_filters) filters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIVisualEffectBackingFakeView setClientView:];
-[_UIVisualEffectBackingFakeView primaryCaptureGroup];
-[_UIVisualEffectBackingFakeView initWithClientView:];
-[_UIVisualEffectBackingFakeView clientView];
-[_UIVisualEffectBackingFakeView applyIdentityViewEffects];
-[_UIVisualEffectBackingFakeView applyIdentityFilterEffects];
-[_UIVisualEffectBackingFakeView setFilters:];
-[_UIVisualEffectBackingFakeView setContainedView:];
-[_UIVisualEffectBackingFakeView filters];
-[_UIVisualEffectBackingFakeView viewEffects];
-[_UIVisualEffectBackingFakeView applyRequestedViewEffects];
-[_UIVisualEffectBackingFakeView _receiveVisitor:];
-[_UIVisualEffectBackingFakeView containedView];
-[_UIVisualEffectBackingFakeView setPrimaryCaptureGroup:];
-[_UIVisualEffectBackingFakeView applyRequestedFilterEffects];
-[_UIVisualEffectBackingFakeView setViewEffects:];
```
