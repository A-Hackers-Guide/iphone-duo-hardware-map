# `_UIHostedWindow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindow`
- 10 instance variables, 6 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _wantsTraitPropagation;
B __hostViewUnderlapsStatusBar;
B _hostIsInternal;
q _hostTintAdjustmentMode;
@"UIColor" __hostTintColor;
@"UITraitCollection" _hostTraitCollection;
@"NSString" _hostSDKVersion;
@"<_UIHostedWindowDelegate>" __hostedWindowDelegate;
@"NSString" __hostBundleIdentifier;
{?="val"[8I]} _hostAuditToken;
```

## Properties

```
@property (Tq,N,S_setHostTintAdjustmentMode:,V_hostTintAdjustmentMode) _hostTintAdjustmentMode;
@property (T@"UITraitCollection",&,N,S_setHostTraitCollection:,V_hostTraitCollection) _hostTraitCollection;
@property (TB,N,S_setWantsTraitPropagation:,V_wantsTraitPropagation) _wantsTraitPropagation;
@property (T@"UIColor",&,N,S_setHostTintColor:,V__hostTintColor) _hostTintColor;
@property (T@"<_UIHostedWindowDelegate>",W,N,V__hostedWindowDelegate) _hostedWindowDelegate;
@property (T@"_UIHostedWindowHostingHandle",R,N) hostingHandle;
```

## Instance methods

```
-[_UIHostedWindow _extendsScreenSceneLifetime];
-[_UIHostedWindow dealloc];
-[_UIHostedWindow _setFirstResponder:];
-[_UIHostedWindow hitTest:withEvent:];
-[_UIHostedWindow _normalInheritedTintColor];
-[_UIHostedWindow _usesWindowServerHitTesting];
-[_UIHostedWindow _configureContextOptions:];
-[_UIHostedWindow contextID];
-[_UIHostedWindow initWithFrame:];
-[_UIHostedWindow _preventsRootPresentationController];
-[_UIHostedWindow __hostViewUnderlapsStatusBar];
-[_UIHostedWindow __setHostViewUnderlapsStatusBar:];
-[_UIHostedWindow _allowsLinkPreviewInteractionInViewServices];
-[_UIHostedWindow _canPromoteFromKeyWindowStack];
-[_UIHostedWindow _defaultTintAdjustmentMode];
-[_UIHostedWindow _didCreateRootPresentationController];
-[_UIHostedWindow _hostTintAdjustmentMode];
-[_UIHostedWindow _hostTintColor];
-[_UIHostedWindow _hostTraitCollection];
-[_UIHostedWindow _hostedWindowDelegate];
-[_UIHostedWindow _isWindowServerHostingManaged];
-[_UIHostedWindow _needsShakesWhenInactive];
-[_UIHostedWindow _orientationForRootTransform];
-[_UIHostedWindow _orientationForSceneTransform];
-[_UIHostedWindow _orientationForViewTransform];
-[_UIHostedWindow _registerScrollToTopView:];
-[_UIHostedWindow _remoteContentParent];
-[_UIHostedWindow _setHostTintAdjustmentMode:];
-[_UIHostedWindow _setHostTintColor:];
-[_UIHostedWindow _setHostTraitCollection:];
-[_UIHostedWindow _setWantsTraitPropagation:];
-[_UIHostedWindow _shouldPropagateTraitCollectionChanges];
-[_UIHostedWindow _suppressFirstResponderWhenUserInteractionDisabled];
-[_UIHostedWindow _systemReferenceAngle];
-[_UIHostedWindow _systemReferenceAngleMode];
-[_UIHostedWindow _systemReferenceAngleProvider];
-[_UIHostedWindow _traitCollectionForSize:parentCollection:];
-[_UIHostedWindow _unregisterScrollToTopView:];
-[_UIHostedWindow _updateStrictTouchVerificationIfNecessary];
-[_UIHostedWindow _updateWindowTraitsAndNotify:];
-[_UIHostedWindow _updatesSafeAreaInsetsOnRead];
-[_UIHostedWindow _usableBounds];
-[_UIHostedWindow _wantsTraitPropagation];
-[_UIHostedWindow hostingHandle];
-[_UIHostedWindow set_hostedWindowDelegate:];
```
