# `_UIVisualEffectHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualEffectViewSubviewMonitoring`
- 7 instance variables, 11 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _views;
B _contentViewRequired;
@"UIView<_UIVisualEffectViewParticipating>" _contentView;
@"_UIVisualEffectViewBackdropCaptureGroup" _primaryCaptureGroup;
@"_UIVisualEffectBackdropView" _captureView;
@"_UIVisualEffectDescriptor" _currentEffectDescriptor;
@"_UIVisualEffectDescriptor" _transitionEffectDescriptor;
```

## Properties

```
@property (T@"UIView<_UIVisualEffectViewParticipating>",R,N,V_contentView) contentView;
@property (TB,N,V_contentViewRequired) contentViewRequired;
@property (T@"NSArray",R,N,V_views) views;
@property (T@"_UIVisualEffectViewBackdropCaptureGroup",&,N,V_primaryCaptureGroup) primaryCaptureGroup;
@property (T@"_UIVisualEffectBackdropView",W,N,V_captureView) captureView;
@property (T@"_UIVisualEffectDescriptor",&,N,V_currentEffectDescriptor) currentEffectDescriptor;
@property (T@"_UIVisualEffectDescriptor",R,N,V_transitionEffectDescriptor) transitionEffectDescriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIVisualEffectHost views];
-[_UIVisualEffectHost _applyIdentityDescriptorEffectInvertingView:];
-[_UIVisualEffectHost initWithContentView:];
-[_UIVisualEffectHost beginTransition];
-[_UIVisualEffectHost primaryCaptureGroup];
-[_UIVisualEffectHost _cloneFilters:];
-[_UIVisualEffectHost _view:willMoveToWindow:];
-[_UIVisualEffectHost prepareToTransitionToEffectDescriptor:];
-[_UIVisualEffectHost willLoseDescendent:];
-[_UIVisualEffectHost currentEffectDescriptor];
-[_UIVisualEffectHost _updateAdjustTintColors];
-[_UIVisualEffectHost _iterateViews:];
-[_UIVisualEffectHost _evaluateInPlaceFiltering];
-[_UIVisualEffectHost setContentViewRequired:];
-[_UIVisualEffectHost endTransition];
-[_UIVisualEffectHost captureView];
-[_UIVisualEffectHost _applyEffectDescriptor:];
-[_UIVisualEffectHost setCurrentEffectDescriptor:];
-[_UIVisualEffectHost _viewForEntry:fromCapturePool:imagePool:otherPool:];
-[_UIVisualEffectHost monitorSubviewsOf:];
-[_UIVisualEffectHost contentView];
-[_UIVisualEffectHost transitionEffectDescriptor];
-[_UIVisualEffectHost contentViewRequired];
-[_UIVisualEffectHost description];
-[_UIVisualEffectHost _updateView:shouldDrawWithTintColor:];
-[_UIVisualEffectHost _view:willLoseDescendent:];
-[_UIVisualEffectHost willGainDescendent:];
-[_UIVisualEffectHost setCaptureView:];
-[_UIVisualEffectHost _applyRequestedDescriptorEffectInvertingView:];
-[_UIVisualEffectHost setPrimaryCaptureGroup:];
-[_UIVisualEffectHost _configureEffectDescriptor:];
-[_UIVisualEffectHost _view:willGainDescendent:];
```
