# `_UIVisualEffectImageView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIImageView`
- Protocols: `_UIVisualEffectViewParticipatingInternal`
- 3 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"_UIVisualEffectViewBackdropCaptureGroup" _primaryCaptureGroup;
@"NSArray" _viewEffects;
@"NSArray" _filters;
```

## Properties

```
@property (T@"<_UIVisualEffectViewSubviewMonitoring>",W,N) subviewMonitor;
@property (TB,N) disableGroupFiltering;
@property (T@"_UIVisualEffectViewBackdropCaptureGroup",&,N,V_primaryCaptureGroup) primaryCaptureGroup;
@property (T@"NSArray",C,N,V_viewEffects) viewEffects;
@property (T@"NSArray",C,N,V_filters) filters;
@property (T@"UIView<_UIVisualEffectViewParticipating>",&,N) containedView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIVisualEffectImageView primaryCaptureGroup];
-[_UIVisualEffectImageView applyIdentityViewEffects];
-[_UIVisualEffectImageView applyIdentityFilterEffects];
-[_UIVisualEffectImageView setFilters:];
-[_UIVisualEffectImageView setContainedView:];
-[_UIVisualEffectImageView filters];
-[_UIVisualEffectImageView viewEffects];
-[_UIVisualEffectImageView applyRequestedViewEffects];
-[_UIVisualEffectImageView disableGroupFiltering];
-[_UIVisualEffectImageView setDisableGroupFiltering:];
-[_UIVisualEffectImageView containedView];
-[_UIVisualEffectImageView setPrimaryCaptureGroup:];
-[_UIVisualEffectImageView _shouldAnimatePropertyWithKey:];
-[_UIVisualEffectImageView applyRequestedFilterEffects];
-[_UIVisualEffectImageView setViewEffects:];
-[_UIVisualEffectImageView _initialValueForLayer:keyPath:usePresentationValue:];
-[_UIVisualEffectImageView setSubviewMonitor:];
-[_UIVisualEffectImageView subviewMonitor];
```
