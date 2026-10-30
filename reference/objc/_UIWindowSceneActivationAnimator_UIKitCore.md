# `_UIWindowSceneActivationAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 47 instance methods, 0 class methods

## Instance variables

```
B _deparented;
B _isDeallocating;
@"_UIMagicMorphAnimation" _morphAnimation;
@"UIWindowSceneActivationConfiguration" _configuration;
@"FBSScene" _sourceFBSScene;
@"_UIPortalView" _incomingScenePortalView;
@"UIView" _morphContainerView;
@"UIView" _deparentingWrapper;
@"UIView" _deparentingPortalAlphaSourceView;
q _state;
@"NSMutableArray" _alongsideAnimations;
@"NSMutableArray" _alongsideCompletions;
@"CAMatchMoveAnimation" _incomingSceneAnchorAnimation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _expectedFrame;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _expectedCornerRadii;
```

## Properties

```
@property (T@"UIWindowSceneActivationConfiguration",&,N,V_configuration) configuration;
@property (T@"FBSScene",W,N,V_sourceFBSScene) sourceFBSScene;
@property (T@"_UIMagicMorphAnimation",R,N,V_morphAnimation) morphAnimation;
@property (T@"_UIPortalView",&,N,V_incomingScenePortalView) incomingScenePortalView;
@property (T@"UIView",&,N,V_morphContainerView) morphContainerView;
@property (T@"UIView",&,N,V_deparentingWrapper) deparentingWrapper;
@property (T@"UIView",&,N,V_deparentingPortalAlphaSourceView) deparentingPortalAlphaSourceView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_expectedFrame) expectedFrame;
@property (T{UIRectCornerRadii=dddd},N,V_expectedCornerRadii) expectedCornerRadii;
@property (Tq,N,V_state) state;
@property (T@"NSMutableArray",R,N,V_alongsideAnimations) alongsideAnimations;
@property (T@"NSMutableArray",R,N,V_alongsideCompletions) alongsideCompletions;
@property (T@"CAMatchMoveAnimation",&,N,V_incomingSceneAnchorAnimation) incomingSceneAnchorAnimation;
@property (TB,N,V_deparented) deparented;
@property (TB,N,V_isDeallocating) isDeallocating;
```

## Instance methods

```
-[_UIWindowSceneActivationAnimator addAnimations:];
-[_UIWindowSceneActivationAnimator addCompletion:];
-[_UIWindowSceneActivationAnimator setState:];
-[_UIWindowSceneActivationAnimator _cleanUp];
-[_UIWindowSceneActivationAnimator morphAnimation];
-[_UIWindowSceneActivationAnimator dealloc];
-[_UIWindowSceneActivationAnimator setConfiguration:];
-[_UIWindowSceneActivationAnimator initWithConfiguration:];
-[_UIWindowSceneActivationAnimator isDeallocating];
-[_UIWindowSceneActivationAnimator configuration];
-[_UIWindowSceneActivationAnimator prewarmWithCompletion:];
-[_UIWindowSceneActivationAnimator cancel];
-[_UIWindowSceneActivationAnimator setIsDeallocating:];
-[_UIWindowSceneActivationAnimator state];
-[_UIWindowSceneActivationAnimator _performAllAlongsideAnimations:];
-[_UIWindowSceneActivationAnimator _performAllAlongsideCompletions];
-[_UIWindowSceneActivationAnimator _preferredCollapsedShadowStyle];
-[_UIWindowSceneActivationAnimator _previewForIncomingScenePortal];
-[_UIWindowSceneActivationAnimator _runAnimationWithSourcePreview:velocity:];
-[_UIWindowSceneActivationAnimator _runLegacyAnimationWithSourcePreview:velocity:];
-[_UIWindowSceneActivationAnimator _sendBSAction:];
-[_UIWindowSceneActivationAnimator _sendCompletionActionCallingAlongsideCompletions:];
-[_UIWindowSceneActivationAnimator _sourceViewContainer];
-[_UIWindowSceneActivationAnimator _startingShadowIntensity];
-[_UIWindowSceneActivationAnimator alongsideAnimations];
-[_UIWindowSceneActivationAnimator alongsideCompletions];
-[_UIWindowSceneActivationAnimator animateWithSourcePreview:velocity:];
-[_UIWindowSceneActivationAnimator deparent];
-[_UIWindowSceneActivationAnimator deparented];
-[_UIWindowSceneActivationAnimator deparentingPortalAlphaSourceView];
-[_UIWindowSceneActivationAnimator deparentingWrapper];
-[_UIWindowSceneActivationAnimator expectedCornerRadii];
-[_UIWindowSceneActivationAnimator expectedFrame];
-[_UIWindowSceneActivationAnimator incomingSceneAnchorAnimation];
-[_UIWindowSceneActivationAnimator incomingScenePortalView];
-[_UIWindowSceneActivationAnimator morphContainerView];
-[_UIWindowSceneActivationAnimator reparent];
-[_UIWindowSceneActivationAnimator setDeparented:];
-[_UIWindowSceneActivationAnimator setDeparentingPortalAlphaSourceView:];
-[_UIWindowSceneActivationAnimator setDeparentingWrapper:];
-[_UIWindowSceneActivationAnimator setExpectedCornerRadii:];
-[_UIWindowSceneActivationAnimator setExpectedFrame:];
-[_UIWindowSceneActivationAnimator setIncomingSceneAnchorAnimation:];
-[_UIWindowSceneActivationAnimator setIncomingScenePortalView:];
-[_UIWindowSceneActivationAnimator setMorphContainerView:];
-[_UIWindowSceneActivationAnimator setSourceFBSScene:];
-[_UIWindowSceneActivationAnimator sourceFBSScene];
```
