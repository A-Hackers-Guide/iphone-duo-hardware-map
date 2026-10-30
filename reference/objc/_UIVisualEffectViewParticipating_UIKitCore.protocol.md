# `_UIVisualEffectViewParticipating` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"_UIVisualEffectViewBackdropCaptureGroup",&,N) primaryCaptureGroup;
@property (T@"UIView<_UIVisualEffectViewParticipating>",&,N) containedView;
@property (T@"NSArray",C,N) viewEffects;
@property (T@"NSArray",C,N) filters;
```

## Instance methods

```
-[_UIVisualEffectViewParticipating primaryCaptureGroup];
-[_UIVisualEffectViewParticipating applyIdentityViewEffects];
-[_UIVisualEffectViewParticipating applyIdentityFilterEffects];
-[_UIVisualEffectViewParticipating setFilters:];
-[_UIVisualEffectViewParticipating setContainedView:];
-[_UIVisualEffectViewParticipating filters];
-[_UIVisualEffectViewParticipating viewEffects];
-[_UIVisualEffectViewParticipating applyRequestedViewEffects];
-[_UIVisualEffectViewParticipating containedView];
-[_UIVisualEffectViewParticipating setPrimaryCaptureGroup:];
-[_UIVisualEffectViewParticipating applyRequestedFilterEffects];
-[_UIVisualEffectViewParticipating setViewEffects:];
```
