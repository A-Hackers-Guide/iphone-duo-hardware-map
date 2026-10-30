# `_UIFlexInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`, `UIGestureRecognizerDelegate`, `_UIViewMultiLayerDelegate`
- 24 instance variables, 24 properties, 52 instance methods, 0 class methods

## Instance variables

```
animationContext;
Q preferredActivationMode;
Q preferredFlexSources;
q preferredVariant;
glassInfo;
? _view;
interactionSignpost;
settlingSignpost;
@"UIUpdateLink" updateLink;
B shouldUsePresentationLayers;
B isMatchingRadii;
@"_UIVelocityIntegrator" velocityIntegrator;
$__lazy_storage_$__panGesture;
gestureMultiplexerToken;
{CGPoint=dd} translation;
{CGPoint=dd} internalTranslation;
{CGPoint=dd} initialTouchLocation;
@"_UIFlexInteractionGlowContainerView" glowContainer;
@"_TtC5UIKit28_UIDebouncingAnimatableFloat" scaleX;
@"_TtC5UIKit28_UIDebouncingAnimatableFloat" scaleY;
@"_TtC5UIKit28_UIDebouncingAnimatableFloat" driftX;
@"_TtC5UIKit28_UIDebouncingAnimatableFloat" driftY;
@"_TtC5UIKit28_UIDebouncingAnimatableFloat" translationY;
@"_UIGroupCompletion" glowCleanupCompletion;
```

## Properties

```
@property (T@"<_UIFlexInteractionDelegate>",N,W) delegate;
@property (TQ,N,VpreferredActivationMode) preferredActivationMode;
@property (TQ,N,VpreferredFlexSources) preferredFlexSources;
@property (Tq,N,VpreferredVariant) preferredVariant;
@property (TQ,N,R) resolvedActivationMode;
@property (T@"UIView",N,R) view;
@property (T@"UIView",N,W,V_view) _view;
@property (T@"UIUpdateLink",N,&,VupdateLink) updateLink;
@property (TB,N,VshouldUsePresentationLayers) shouldUsePresentationLayers;
@property (TB,N,VisMatchingRadii) isMatchingRadii;
@property (T@"_UIVelocityIntegrator",N,R,VvelocityIntegrator) velocityIntegrator;
@property (T@"_UIFlexInteractionPanGestureRecognizer",N,&) _panGesture;
@property (T@"_UIFlexInteractionPanGestureRecognizer",N,R) panGesture;
@property (T{CGPoint=dd},N,Vtranslation) translation;
@property (T{CGPoint=dd},N,VinternalTranslation) internalTranslation;
@property (T{CGPoint=dd},N,VinitialTouchLocation) initialTouchLocation;
@property (T@"_UIFlexInteractionGlowContainerView",N,R,VglowContainer) glowContainer;
@property (T@"_TtC5UIKit28_UIDebouncingAnimatableFloat",N,R,VscaleX) scaleX;
@property (T@"_TtC5UIKit28_UIDebouncingAnimatableFloat",N,R,VscaleY) scaleY;
@property (T@"_TtC5UIKit28_UIDebouncingAnimatableFloat",N,R,VdriftX) driftX;
@property (T@"_TtC5UIKit28_UIDebouncingAnimatableFloat",N,R,VdriftY) driftY;
@property (T@"_TtC5UIKit28_UIDebouncingAnimatableFloat",N,R,VtranslationY) translationY;
@property (TB,N,R) supportsMultiLayer;
@property (T@"_UIGroupCompletion",N,R,VglowCleanupCompletion) glowCleanupCompletion;
```

## Instance methods

```
-[_UIFlexInteraction _view];
-[_UIFlexInteraction preferredActivationMode];
-[_UIFlexInteraction initialTouchLocation];
-[_UIFlexInteraction _willMoveFromWindow:toWindow:];
-[_UIFlexInteraction glowContainer];
-[_UIFlexInteraction deactivate];
-[_UIFlexInteraction setInitialTouchLocation:];
-[_UIFlexInteraction updateFlex];
-[_UIFlexInteraction init];
-[_UIFlexInteraction setPreferredFlexSources:];
-[_UIFlexInteraction shouldUsePresentationLayers];
-[_UIFlexInteraction _panGesture];
-[_UIFlexInteraction setPreferredActivationMode:];
-[_UIFlexInteraction setPreferredVariant:];
-[_UIFlexInteraction handlePan:];
-[_UIFlexInteraction isMatchingRadii];
-[_UIFlexInteraction setUpdateLink:];
-[_UIFlexInteraction setShouldUsePresentationLayers:];
-[_UIFlexInteraction view];
-[_UIFlexInteraction _outermostLayerDidChange:];
-[_UIFlexInteraction setDelegate:];
-[_UIFlexInteraction showGlowAt:];
-[_UIFlexInteraction panGesture];
-[_UIFlexInteraction gestureRecognizerShouldBegin:];
-[_UIFlexInteraction preferredVariant];
-[_UIFlexInteraction preferredFlexSources];
-[_UIFlexInteraction setIsMatchingRadii:];
-[_UIFlexInteraction willMoveToView:];
-[_UIFlexInteraction hideGlow];
-[_UIFlexInteraction glowCleanupCompletion];
-[_UIFlexInteraction translationY];
-[_UIFlexInteraction set_view:];
-[_UIFlexInteraction driftY];
-[_UIFlexInteraction delegate];
-[_UIFlexInteraction setTranslation:];
-[_UIFlexInteraction setInternalTranslation:];
-[_UIFlexInteraction resolvedActivationMode];
-[_UIFlexInteraction scaleX];
-[_UIFlexInteraction velocityIntegrator];
-[_UIFlexInteraction updateLink];
-[_UIFlexInteraction supportsMultiLayer];
-[_UIFlexInteraction configureGlowCorners];
-[_UIFlexInteraction teardownGlowCorners];
-[_UIFlexInteraction translation];
-[_UIFlexInteraction activateIfPermitted];
-[_UIFlexInteraction internalTranslation];
-[_UIFlexInteraction didMoveToView:];
-[_UIFlexInteraction moveGlowTo:shouldDissipate:];
-[_UIFlexInteraction updateWithInteractionPulse];
-[_UIFlexInteraction scaleY];
-[_UIFlexInteraction driftX];
-[_UIFlexInteraction set_panGesture:];
```
