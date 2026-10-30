# `_UIKBLightEffectsBackground`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBInputBackdropView`
- 22 instance variables, 22 properties, 72 instance methods, 0 class methods

## Instance variables

```
B _clientBackdropInUse;
B _isUsingAnimatedBackdrop;
B _isAnimating;
B _useLightConfigEffects;
@"UILayoutGuide" _fullBackdropLayoutGuide;
@"UILayoutGuide" _assistantLayoutGuide;
@"UIView" _fullBackdropMaskView;
@"UIView" _assistantBarMaskView;
@"_UIGradientView" _backdropGradientMaskView;
@"UIView" _behindFullBackdropView;
@"UIView" _behindAssistantView;
@"UIView" _mirroredShadowView;
@"UIView" _mirroredLightBorderView;
@"UILayoutGuide" _aboveKeyboardLayoutGuide;
@"NSLayoutConstraint" _minimumAboveKeyboardHeightConstraint;
@"UIView" _backdropClippingView;
@"NSArray" _backdropClippingConstraints;
@"UIKBBackgroundShapeView" _backdropMask;
@"NSMutableArray" _lightSourceConstraints;
@"UIKBBackdropView" _transitionStartBackdropView;
q _clippingStyle;
{CGSize="width"d"height"d} _candidateBarSize;
```

## Properties

```
@property (T@"UIView",&,N,V_fullBackdropMaskView) fullBackdropMaskView;
@property (T@"UIView",&,N,V_assistantBarMaskView) assistantBarMaskView;
@property (T@"_UIGradientView",&,N,V_backdropGradientMaskView) backdropGradientMaskView;
@property (T@"UIView",&,N,V_behindFullBackdropView) behindFullBackdropView;
@property (T@"UIView",&,N,V_behindAssistantView) behindAssistantView;
@property (T@"UIView",&,N,V_mirroredShadowView) mirroredShadowView;
@property (T@"UIView",&,N,V_mirroredLightBorderView) mirroredLightBorderView;
@property (T@"UILayoutGuide",&,N,V_fullBackdropLayoutGuide) fullBackdropLayoutGuide;
@property (T@"UILayoutGuide",&,N,V_assistantLayoutGuide) assistantLayoutGuide;
@property (T@"UILayoutGuide",&,N,V_aboveKeyboardLayoutGuide) aboveKeyboardLayoutGuide;
@property (T@"NSLayoutConstraint",&,N,V_minimumAboveKeyboardHeightConstraint) minimumAboveKeyboardHeightConstraint;
@property (T@"UIView",&,N,V_backdropClippingView) backdropClippingView;
@property (T@"NSArray",&,N,V_backdropClippingConstraints) backdropClippingConstraints;
@property (T@"UIKBBackgroundShapeView",&,N,V_backdropMask) backdropMask;
@property (T{CGSize=dd},N,V_candidateBarSize) candidateBarSize;
@property (T@"NSMutableArray",&,N,V_lightSourceConstraints) lightSourceConstraints;
@property (T@"UIKBBackdropView",&,N,V_transitionStartBackdropView) transitionStartBackdropView;
@property (Tq,N,V_clippingStyle) clippingStyle;
@property (TB,N,V_isUsingAnimatedBackdrop) isUsingAnimatedBackdrop;
@property (TB,N,V_isAnimating) isAnimating;
@property (TB,N,V_useLightConfigEffects) useLightConfigEffects;
@property (TB,N,V_clientBackdropInUse) clientBackdropInUse;
```

## Instance methods

```
-[_UIKBLightEffectsBackground _setRenderConfig:];
-[_UIKBLightEffectsBackground setAssistantLayoutGuide:];
-[_UIKBLightEffectsBackground layoutSubviews];
-[_UIKBLightEffectsBackground setIsAnimating:];
-[_UIKBLightEffectsBackground updateConstraints];
-[_UIKBLightEffectsBackground isAnimating];
-[_UIKBLightEffectsBackground initWithFrame:];
-[_UIKBLightEffectsBackground assistantLayoutGuide];
-[_UIKBLightEffectsBackground setTransitionStartBackdropView:];
-[_UIKBLightEffectsBackground setBackdropClippingConstraints:];
-[_UIKBLightEffectsBackground _addContentEffectsForConfig:];
-[_UIKBLightEffectsBackground _adjustMaskForCandidateViewSize:collapsedState:];
-[_UIKBLightEffectsBackground aboveKeyboardLayoutGuide];
-[_UIKBLightEffectsBackground addLayoutGuidesIfNeeded];
-[_UIKBLightEffectsBackground addLightSourceViews];
-[_UIKBLightEffectsBackground animatedTransitionToRenderConfig:];
-[_UIKBLightEffectsBackground assistantBarMaskView];
-[_UIKBLightEffectsBackground backdropClippingConstraints];
-[_UIKBLightEffectsBackground backdropClippingView];
-[_UIKBLightEffectsBackground backdropGradientMaskView];
-[_UIKBLightEffectsBackground backdropMask];
-[_UIKBLightEffectsBackground behindAssistantView];
-[_UIKBLightEffectsBackground behindFullBackdropView];
-[_UIKBLightEffectsBackground bringupWaveEffectViewForDisplayScale:];
-[_UIKBLightEffectsBackground candidateBarSize];
-[_UIKBLightEffectsBackground changeClippingStyle:];
-[_UIKBLightEffectsBackground clientBackdropInUse];
-[_UIKBLightEffectsBackground clippingStyle];
-[_UIKBLightEffectsBackground completeTransitionToRenderConfig:];
-[_UIKBLightEffectsBackground extendForCandidateViewHeight:width:];
-[_UIKBLightEffectsBackground extraBackdropViewForConfig:];
-[_UIKBLightEffectsBackground fullBackdropLayoutGuide];
-[_UIKBLightEffectsBackground fullBackdropMaskView];
-[_UIKBLightEffectsBackground isClientBackdropInUse];
-[_UIKBLightEffectsBackground isUsingAnimatedBackdrop];
-[_UIKBLightEffectsBackground layerForPositionMatchMove];
-[_UIKBLightEffectsBackground layoutInputBackdropToFullWithRect:];
-[_UIKBLightEffectsBackground lightSourceConstraints];
-[_UIKBLightEffectsBackground maskEffectsBackdrop];
-[_UIKBLightEffectsBackground minimumAboveKeyboardHeightConstraint];
-[_UIKBLightEffectsBackground mirroredLightBorderView];
-[_UIKBLightEffectsBackground mirroredShadowView];
-[_UIKBLightEffectsBackground performTransitionToRenderConfig:fromRenderConfig:alongsideAnimations:completion:];
-[_UIKBLightEffectsBackground removeAnimatedBackdropEffects];
-[_UIKBLightEffectsBackground setAboveKeyboardLayoutGuide:];
-[_UIKBLightEffectsBackground setAssistantBarMaskView:];
-[_UIKBLightEffectsBackground setBackdropClippingView:];
-[_UIKBLightEffectsBackground setBackdropGradientMaskView:];
-[_UIKBLightEffectsBackground setBackdropMask:];
-[_UIKBLightEffectsBackground setBehindAssistantView:];
-[_UIKBLightEffectsBackground setBehindFullBackdropView:];
-[_UIKBLightEffectsBackground setCandidateBarSize:];
-[_UIKBLightEffectsBackground setClientBackdropInUse:];
-[_UIKBLightEffectsBackground setClippingStyle:];
-[_UIKBLightEffectsBackground setFullBackdropLayoutGuide:];
-[_UIKBLightEffectsBackground setFullBackdropMaskView:];
-[_UIKBLightEffectsBackground setIsUsingAnimatedBackdrop:];
-[_UIKBLightEffectsBackground setLightSourceConstraints:];
-[_UIKBLightEffectsBackground setMinimumAboveKeyboardHeightConstraint:];
-[_UIKBLightEffectsBackground setMirroredLightBorderView:];
-[_UIKBLightEffectsBackground setMirroredShadowView:];
-[_UIKBLightEffectsBackground setUseLightConfigEffects:];
-[_UIKBLightEffectsBackground shouldShowBackdrop];
-[_UIKBLightEffectsBackground shouldShowWaveView];
-[_UIKBLightEffectsBackground supportsLightEffects];
-[_UIKBLightEffectsBackground transitionStartBackdropView];
-[_UIKBLightEffectsBackground transitionToStyle:isSplit:];
-[_UIKBLightEffectsBackground updateAlphaForAnimationStart:];
-[_UIKBLightEffectsBackground updateCornersWithRadius:forVisualState:];
-[_UIKBLightEffectsBackground updateEffectsForLightKeyboard:forceUpdate:];
-[_UIKBLightEffectsBackground useLightConfigEffects];
-[_UIKBLightEffectsBackground useMaskedKeyplaneBackdrop:assistantBackdrop:];
```
