# `LAUIPearlGlyphView`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `LAUIMetalRenderLoopDelegate`
- 41 instance variables, 17 properties, 39 instance methods, 2 class methods

## Instance variables

```
@"LAUIPearlGlyphViewStaticResources" _sharedResources;
{configuration_t="_style"q"_reduce_blur"B} _configuration;
d _scale;
@"LAUICheckmarkLayer" _checkmarkLayer;
B _delegateRespondsToWillRender;
@"UIView" _containerView;
@"LAUIMetalRenderLoop" _renderLoop;
@"CALayer" _layer;
B _invalidated;
B _rendererPaused;
B _inWindow;
Q _externalAnimationCount;
d _overdrawRatio;
{CGSize="width"d"height"d} _boundsSize;
{CGSize="width"d"height"d} _drawableSize;
B _contentLayerNeedsMaskUpdate;
@"CAShapeLayer" _contentLayerMask;
{unique_ptr<LAUI_uniform_cubic_b_spline_renderer::renderer_t, std::default_delete<LAUI_uniform_cubic_b_spline_renderer::renderer_t>>=""{?="__ptr_"^{renderer_t}}} _renderer;
{unique_ptr<(anonymous namespace)::face_id_animator_t, std::default_delete<(anonymous namespace)::face_id_animator_t>>=""{?="__ptr_"^{face_id_animator_t}}} _animator;
B _modelDirty;
B _panning;
d _lastUpdateTime;
B _animating;
{overlayable_property_t<UIColor *, float __attribute__((ext_vector_type(4)))>="overlay_value"{optional<UIColor *>=""(?="__null_state_"c"__val_"@"UIColor")"__engaged_"B}"value"} _idleColor;
_defaultColor;
_oscillatingColor;
_successColor;
{overlayable_property_t<UIColor *, float __attribute__((ext_vector_type(4)))>="overlay_value"{optional<UIColor *>=""(?="__null_state_"c"__val_"@"UIColor")"__engaged_"B}"value"} _finishedColor;
q _priorState;
B _changingState;
B _stateChangeAnimated;
Q _stateChangeCounter;
{vector<void (^)(bool), std::allocator<void (^)(bool)>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _completionHandlers;
^{CGColorSpace=} _colorSpace;
B _paused;
B _shakeEnabled;
B _feedbackEnabled;
Q _faceVisibility;
q _state;
@"CALayer" _contentLayer;
@"<LAUIPearlGlyphViewDelegate>" _delegate;
```

## Properties

```
@property (TB,D,N) inApplicationContext;
@property (Tq,R,N) style;
@property (T@"UIColor",R,N) idleColor;
@property (T@"UIColor",R,N) finishedColor;
@property (TQ,R,N,V_faceVisibility) faceVisibility;
@property (TB,R,N) hideFace;
@property (Tq,R,N,V_state) state;
@property (TB,N,GisPaused,V_paused) paused;
@property (TB,N,V_shakeEnabled) shakeEnabled;
@property (TB,N,V_feedbackEnabled) feedbackEnabled;
@property (T@"CALayer",R,N,V_contentLayer) contentLayer;
@property (T@"NSNumber",R,N) remainingMinDisplayTimeInterval;
@property (T@"<LAUIPearlGlyphViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LAUIPearlGlyphView sharedStaticResources];
+[LAUIPearlGlyphView invokeSuccessFeedback];
```

## Instance methods

```
-[LAUIPearlGlyphView isPaused];
-[LAUIPearlGlyphView didMoveToWindow];
-[LAUIPearlGlyphView setState:animated:];
-[LAUIPearlGlyphView applicationDidBecomeActive:];
-[LAUIPearlGlyphView setStyle:animated:];
-[LAUIPearlGlyphView init];
-[LAUIPearlGlyphView dealloc];
-[LAUIPearlGlyphView layoutSubviews];
-[LAUIPearlGlyphView initWithStyle:];
-[LAUIPearlGlyphView initWithConfiguration:];
-[LAUIPearlGlyphView style];
-[LAUIPearlGlyphView invalidate];
-[LAUIPearlGlyphView setPaused:];
-[LAUIPearlGlyphView setDelegate:];
-[LAUIPearlGlyphView delegate];
-[LAUIPearlGlyphView contentLayer];
-[LAUIPearlGlyphView initWithFrame:];
-[LAUIPearlGlyphView state];
-[LAUIPearlGlyphView feedbackEnabled];
-[LAUIPearlGlyphView setFaceVisibility:animated:];
-[LAUIPearlGlyphView setFeedbackEnabled:];
-[LAUIPearlGlyphView setFinishedColor:animated:];
-[LAUIPearlGlyphView setState:animated:withCompletion:];
-[LAUIPearlGlyphView setIdleColor:animated:];
-[LAUIPearlGlyphView setInApplicationContext:];
-[LAUIPearlGlyphView renderLoop:drawAtTime:];
-[LAUIPearlGlyphView setShakeEnabled:];
-[LAUIPearlGlyphView remainingMinDisplayTimeInterval];
-[LAUIPearlGlyphView faceVisibility];
-[LAUIPearlGlyphView finishedColor];
-[LAUIPearlGlyphView hideFace];
-[LAUIPearlGlyphView idleColor];
-[LAUIPearlGlyphView inApplicationContext];
-[LAUIPearlGlyphView purgeBuffers];
-[LAUIPearlGlyphView reduceMotionDidChange:];
-[LAUIPearlGlyphView reduceTransparencyDidChange:];
-[LAUIPearlGlyphView renderLoop:drawableSizeDidChange:];
-[LAUIPearlGlyphView setHideFace:animated:];
-[LAUIPearlGlyphView shakeEnabled];
```
