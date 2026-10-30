# `_UIScrollEdgeEffectViewInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`, `_UIScrollPocketRegistrationInteractionDelegate`, `UIInteraction_Internal`, `UIInteraction_Private`, `_UIGeometryChangeObserver`, `BSDescriptionStreaming`
- 19 instance variables, 22 properties, 53 instance methods, 1 class methods

## Instance variables

```
? _view;
@"UIScrollEdgeEffect" topEdgeEffect;
@"UIScrollEdgeEffect" leftEdgeEffect;
@"UIScrollEdgeEffect" bottomEdgeEffect;
@"UIScrollEdgeEffect" rightEdgeEffect;
B isEnabled;
B allowsPocketElementPassThrough;
B ordersBlurOverLuminanceAdjustment;
@"<UITraitChangeRegistration>" pocketsFrozenTraitRegistration;
@"<UITraitChangeRegistration>" userInterfaceStyleTraitRegistration;
hostUserInterfaceStyleOverrides;
@"_UIScrollPocketRegistrationInteraction" registrationInteraction;
@"UIView" effectView;
@"UIView" captureView;
@"_TtC5UIKit20ScrollEdgeEffectView" topPocket;
@"_TtC5UIKit20ScrollEdgeEffectView" leftPocket;
@"_TtC5UIKit20ScrollEdgeEffectView" bottomPocket;
@"_TtC5UIKit20ScrollEdgeEffectView" rightPocket;
{CGSize=dd} effectOffset;
```

## Properties

```
@property (T@"UIView",N,W,V_view) _view;
@property (T@"UIView",N,R) view;
@property (T@"UIScrollEdgeEffect",N,R,VtopEdgeEffect) topEdgeEffect;
@property (T@"UIScrollEdgeEffect",N,R,VleftEdgeEffect) leftEdgeEffect;
@property (T@"UIScrollEdgeEffect",N,R,VbottomEdgeEffect) bottomEdgeEffect;
@property (T@"UIScrollEdgeEffect",N,R,VrightEdgeEffect) rightEdgeEffect;
@property (TB,N,VisEnabled) isEnabled;
@property (TB,N,VallowsPocketElementPassThrough) allowsPocketElementPassThrough;
@property (TB,N,VordersBlurOverLuminanceAdjustment) ordersBlurOverLuminanceAdjustment;
@property (T@"<UITraitChangeRegistration>",N,&,VpocketsFrozenTraitRegistration) pocketsFrozenTraitRegistration;
@property (T@"<UITraitChangeRegistration>",N,&,VuserInterfaceStyleTraitRegistration) userInterfaceStyleTraitRegistration;
@property (T@"_UIScrollPocketRegistrationInteraction",N,&,VregistrationInteraction) registrationInteraction;
@property (T@"UIView",N,R,VeffectView) effectView;
@property (T@"UIView",N,R,VcaptureView) captureView;
@property (T@"_TtC5UIKit20ScrollEdgeEffectView",N,&,VtopPocket) topPocket;
@property (T@"_TtC5UIKit20ScrollEdgeEffectView",N,&,VleftPocket) leftPocket;
@property (T@"_TtC5UIKit20ScrollEdgeEffectView",N,&,VbottomPocket) bottomPocket;
@property (T@"_TtC5UIKit20ScrollEdgeEffectView",N,&,VrightPocket) rightPocket;
@property (TB,N,R) needsPockets;
@property (T{UIEdgeInsets=dddd},N,R) effectInsets;
@property (T{CGSize=dd},N,VeffectOffset) effectOffset;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[_UIScrollEdgeEffectViewInteraction updateFromPrototypeSettings];
```

## Instance methods

```
-[_UIScrollEdgeEffectViewInteraction _view];
-[_UIScrollEdgeEffectViewInteraction effectOffset];
-[_UIScrollEdgeEffectViewInteraction ordersBlurOverLuminanceAdjustment];
-[_UIScrollEdgeEffectViewInteraction bottomEdgeEffect];
-[_UIScrollEdgeEffectViewInteraction setPocketsFrozenTraitRegistration:];
-[_UIScrollEdgeEffectViewInteraction _scrollPocketRegistrationInteractionDidInvalidatePosition:];
-[_UIScrollEdgeEffectViewInteraction update];
-[_UIScrollEdgeEffectViewInteraction init];
-[_UIScrollEdgeEffectViewInteraction updateWithContentRect:shouldAnimateVisibility:];
-[_UIScrollEdgeEffectViewInteraction setIsEnabled:];
-[_UIScrollEdgeEffectViewInteraction registrationInteraction];
-[_UIScrollEdgeEffectViewInteraction setLeftPocket:];
-[_UIScrollEdgeEffectViewInteraction dealloc];
-[_UIScrollEdgeEffectViewInteraction needsPockets];
-[_UIScrollEdgeEffectViewInteraction bottomPocket];
-[_UIScrollEdgeEffectViewInteraction updateEffectAndCaptureViewFrames];
-[_UIScrollEdgeEffectViewInteraction setRegistrationInteraction:];
-[_UIScrollEdgeEffectViewInteraction allowsPocketElementPassThrough];
-[_UIScrollEdgeEffectViewInteraction topEdgeEffect];
-[_UIScrollEdgeEffectViewInteraction leftEdgeEffect];
-[_UIScrollEdgeEffectViewInteraction _geometryChanged:forAncestor:];
-[_UIScrollEdgeEffectViewInteraction isEnabled];
-[_UIScrollEdgeEffectViewInteraction view];
-[_UIScrollEdgeEffectViewInteraction captureView];
-[_UIScrollEdgeEffectViewInteraction updatePrototypeSettingsObservation];
-[_UIScrollEdgeEffectViewInteraction setAllowsPocketElementPassThrough:];
-[_UIScrollEdgeEffectViewInteraction effectView];
-[_UIScrollEdgeEffectViewInteraction debugInfoVerbose:];
-[_UIScrollEdgeEffectViewInteraction setUserInterfaceStyleTraitRegistration:];
-[_UIScrollEdgeEffectViewInteraction willMoveToView:];
-[_UIScrollEdgeEffectViewInteraction setRightPocket:];
-[_UIScrollEdgeEffectViewInteraction edgeEffectFor:];
-[_UIScrollEdgeEffectViewInteraction set_view:];
-[_UIScrollEdgeEffectViewInteraction rightPocket];
-[_UIScrollEdgeEffectViewInteraction leftPocket];
-[_UIScrollEdgeEffectViewInteraction existingPocketFor:];
-[_UIScrollEdgeEffectViewInteraction rightEdgeEffect];
-[_UIScrollEdgeEffectViewInteraction forcingPocketFor:];
-[_UIScrollEdgeEffectViewInteraction description];
-[_UIScrollEdgeEffectViewInteraction setTopPocket:];
-[_UIScrollEdgeEffectViewInteraction backgroundColorDidChange];
-[_UIScrollEdgeEffectViewInteraction userInterfaceStyleTraitRegistration];
-[_UIScrollEdgeEffectViewInteraction appendDescriptionToStream:];
-[_UIScrollEdgeEffectViewInteraction _viewVisibilityDidChange];
-[_UIScrollEdgeEffectViewInteraction effectInsets];
-[_UIScrollEdgeEffectViewInteraction updateScrollPocketCollectorModelHidden];
-[_UIScrollEdgeEffectViewInteraction topPocket];
-[_UIScrollEdgeEffectViewInteraction didMoveToView:];
-[_UIScrollEdgeEffectViewInteraction updatePocket:contentRect:shouldAnimateVisibility:];
-[_UIScrollEdgeEffectViewInteraction setOrdersBlurOverLuminanceAdjustment:];
-[_UIScrollEdgeEffectViewInteraction pocketsFrozenTraitRegistration];
-[_UIScrollEdgeEffectViewInteraction setEffectOffset:];
-[_UIScrollEdgeEffectViewInteraction setBottomPocket:];
```
