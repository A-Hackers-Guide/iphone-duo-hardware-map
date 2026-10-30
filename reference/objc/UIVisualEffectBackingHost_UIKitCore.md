# `UIVisualEffectBackingHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 11 properties, 50 instance methods, 0 class methods

## Instance variables

```
{?="backgroundNeedsUpdate"b1"contentNeedsUpdate"b1"isUpdatingSubviews"b1"usingPlainViewForBackground"b1} _flags;
@"NSString" _captureGroupName;
@"UIVisualEffect" _visualEffect;
@"NSArray" _contentEffects;
@"NSArray" _backgroundEffects;
q _reentrantCount;
@"UIView" _view;
@"_UIVisualEffectEnvironment" _environment;
@"_UIVisualEffectViewBackdropCaptureGroup" _captureGroup;
@"_UIVisualEffectHost" _backgroundHost;
@"_UIVisualEffectHost" _contentHost;
@"NSArray" _visualEffectSubviews;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"_UIVisualEffectEnvironment",&,N,V_environment) environment;
@property (T@"_UIVisualEffectViewBackdropCaptureGroup",&,N,V_captureGroup) captureGroup;
@property (T@"_UIVisualEffectHost",&,N,V_backgroundHost) backgroundHost;
@property (T@"_UIVisualEffectHost",&,N,V_contentHost) contentHost;
@property (T@"NSArray",&,N,V_visualEffectSubviews) visualEffectSubviews;
@property (Tq,N,V_reentrantCount) reentrantCount;
@property (T@"UIVisualEffect",C,N,V_visualEffect) visualEffect;
@property (T@"NSArray",C,N,V_contentEffects) contentEffects;
@property (T@"NSArray",C,N,V_backgroundEffects) backgroundEffects;
@property (T@"NSString",C,N,S_setCaptureGroupName:,V_captureGroupName) _captureGroupName;
```

## Instance methods

```
-[UIVisualEffectBackingHost setEnvironment:];
-[UIVisualEffectBackingHost didMoveToWindow];
-[UIVisualEffectBackingHost setContentHost:];
-[UIVisualEffectBackingHost willMoveToSuperview:];
-[UIVisualEffectBackingHost backgroundEffects];
-[UIVisualEffectBackingHost _generateDeferredAnimations:];
-[UIVisualEffectBackingHost backgroundHost];
-[UIVisualEffectBackingHost setContentEffects:];
-[UIVisualEffectBackingHost _setCaptureGroupName:];
-[UIVisualEffectBackingHost dealloc];
-[UIVisualEffectBackingHost _updateEffectForAccessibilityChanges:];
-[UIVisualEffectBackingHost invalidateCaptureGroupName];
-[UIVisualEffectBackingHost willLoseDescendent:];
-[UIVisualEffectBackingHost setReentrantCount:];
-[UIVisualEffectBackingHost setView:];
-[UIVisualEffectBackingHost visualEffect];
-[UIVisualEffectBackingHost _mergedTraitCollection];
-[UIVisualEffectBackingHost _didMoveFromWindow:toWindow:];
-[UIVisualEffectBackingHost _updateSubviews];
-[UIVisualEffectBackingHost view];
-[UIVisualEffectBackingHost contentEffects];
-[UIVisualEffectBackingHost visualEffectSubviews];
-[UIVisualEffectBackingHost willMoveToWindow:];
-[UIVisualEffectBackingHost _generateBackgroundEffects:contentEffects:];
-[UIVisualEffectBackingHost _ensureBackgroundHost];
-[UIVisualEffectBackingHost setVisualEffectSubviews:];
-[UIVisualEffectBackingHost _updateContentViewVibrancyTraitOverride:];
-[UIVisualEffectBackingHost _ensureContentHost];
-[UIVisualEffectBackingHost setBackgroundEffects:];
-[UIVisualEffectBackingHost _configureEffects];
-[UIVisualEffectBackingHost _unregisterNotifications];
-[UIVisualEffectBackingHost _updateEnvironmentAndFlagUpdatesIfNecessary:];
-[UIVisualEffectBackingHost reentrantCount];
-[UIVisualEffectBackingHost _observeSuperviewContainerVibrancy];
-[UIVisualEffectBackingHost setCaptureGroup:];
-[UIVisualEffectBackingHost traitCollectionDidChange:];
-[UIVisualEffectBackingHost willGainDescendent:];
-[UIVisualEffectBackingHost _effectDescriptorForEffects:usage:];
-[UIVisualEffectBackingHost _registerNotifications];
-[UIVisualEffectBackingHost _shouldAnimatePropertyWithKey:];
-[UIVisualEffectBackingHost didMoveToSuperview];
-[UIVisualEffectBackingHost captureGroup];
-[UIVisualEffectBackingHost _initialValueForKey:];
-[UIVisualEffectBackingHost environment];
-[UIVisualEffectBackingHost contentHost];
-[UIVisualEffectBackingHost _captureGroupName];
-[UIVisualEffectBackingHost setBackgroundHost:];
-[UIVisualEffectBackingHost setVisualEffect:];
-[UIVisualEffectBackingHost initForView:];
-[UIVisualEffectBackingHost _hasDeferredAnimations];
```
