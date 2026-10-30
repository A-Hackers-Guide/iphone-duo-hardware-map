# `_UIVisualEffectSubview`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIVisualEffectViewParticipating`
- 5 instance variables, 10 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _filters;
@"_UIVisualEffectViewBackdropCaptureGroup" _primaryCaptureGroup;
@"UIView<_UIVisualEffectViewParticipating>" _containedView;
@"NSArray" _viewEffects;
@"<_UIVisualEffectViewSubviewMonitoring>" _subviewMonitor;
```

## Properties

```
@property (T@"<_UIVisualEffectViewSubviewMonitoring>",W,N,V_subviewMonitor) subviewMonitor;
@property (TB,N) disableGroupFiltering;
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
-[_UIVisualEffectSubview primaryCaptureGroup];
-[_UIVisualEffectSubview applyIdentityViewEffects];
-[_UIVisualEffectSubview applyIdentityFilterEffects];
-[_UIVisualEffectSubview setFilters:];
-[_UIVisualEffectSubview layoutSubviews];
-[_UIVisualEffectSubview setContainedView:];
-[_UIVisualEffectSubview filters];
-[_UIVisualEffectSubview _monitoredView:willMoveFromSuperview:toSuperview:];
-[_UIVisualEffectSubview viewEffects];
-[_UIVisualEffectSubview willMoveToWindow:];
-[_UIVisualEffectSubview applyRequestedViewEffects];
-[_UIVisualEffectSubview disableGroupFiltering];
-[_UIVisualEffectSubview setDisableGroupFiltering:];
-[_UIVisualEffectSubview containedView];
-[_UIVisualEffectSubview setPrimaryCaptureGroup:];
-[_UIVisualEffectSubview _shouldAnimatePropertyWithKey:];
-[_UIVisualEffectSubview applyRequestedFilterEffects];
-[_UIVisualEffectSubview initWithFrame:];
-[_UIVisualEffectSubview setViewEffects:];
-[_UIVisualEffectSubview _initialValueForLayer:keyPath:usePresentationValue:];
-[_UIVisualEffectSubview setSubviewMonitor:];
-[_UIVisualEffectSubview subviewMonitor];
```
