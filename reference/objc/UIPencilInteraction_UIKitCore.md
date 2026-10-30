# `UIPencilInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `UIGestureRecognizerDelegate`, `BSDescriptionStreaming`, `UIInteraction`
- 13 instance variables, 10 properties, 24 instance methods, 9 class methods

## Instance variables

```
{?="registrationPendingDidMoveToWindow"b1"registrationPendingWindowMoveToScene"b1"delegateSupportsDidTap"b1"delegateSupportsDidReceiveTap"b1"delegateSupportsPrivateDidReceiveTap"b1"delegateSupportsDidReceiveSqueeze"b1"delegateSupportsPrivateDidReceiveSqueeze"b1"queriedDispatchBehavior"b1"lastEvaluatedAffectsSystemFocus"b1"evaluatedIfPencilKitFallbackAffectsFocus"b1"pencilKitFallbackAffectsFocus"b1} _interactionFlags;
B _enabled;
@"UIView" _view;
@"<BSInvalidatable>" _eventRegistrationToken;
Q _cachedDispatchBehavior;
@"UIHoverGestureRecognizer" _hoverGestureRecognizer;
d _lastKnownHoverZOffset;
d _lastKnownHoverAzimuthAngle;
d _lastKnownHoverAltitudeAngle;
d _lastKnownHoverRollAngle;
@"<UIPencilInteractionDelegate>" _delegate;
{CGVector="dx"d"dy"d} _lastKnownHoverAzimuthUnitVector;
{CAPoint3D="x"d"y"d"z"d} _lastKnownHoverLocation3D;
```

## Properties

```
@property (T@"UIHoverGestureRecognizer",R,N,V_hoverGestureRecognizer) _hoverGestureRecognizer;
@property (TQ,R,N) _dispatchBehavior;
@property (T@"<UIPencilInteractionDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPencilInteraction hasSeenPencilPairingUI];
+[UIPencilInteraction prefersPencilOnlyDrawing];
+[UIPencilInteraction preferredTapAction];
+[UIPencilInteraction _setPrefersPencilOnlyDrawing:];
+[UIPencilInteraction _preferredSqueezeAction];
+[UIPencilInteraction preferredSqueezeAction];
+[UIPencilInteraction _setHasUsedPassivePencil:];
+[UIPencilInteraction prefersHoverToolPreview];
+[UIPencilInteraction hasUsedPassivePencil];
```

## Instance methods

```
-[UIPencilInteraction _handleHoverGestureRecognizer:];
-[UIPencilInteraction _windowWillMoveToScene:];
-[UIPencilInteraction _willMoveFromWindow:toWindow:];
-[UIPencilInteraction _setNeedsEvaluationOfAffectsSystemFocus];
-[UIPencilInteraction initWithDelegate:];
-[UIPencilInteraction _shouldAffectSystemFocus];
-[UIPencilInteraction debugDescription];
-[UIPencilInteraction init];
-[UIPencilInteraction _dispatchBehavior];
-[UIPencilInteraction dealloc];
-[UIPencilInteraction _shouldReceiveGestureType:];
-[UIPencilInteraction _didMoveFromWindow:toWindow:];
-[UIPencilInteraction isEnabled];
-[UIPencilInteraction succinctDescription];
-[UIPencilInteraction view];
-[UIPencilInteraction setDelegate:];
-[UIPencilInteraction _windowDidMoveToScene:];
-[UIPencilInteraction setEnabled:];
-[UIPencilInteraction willMoveToView:];
-[UIPencilInteraction delegate];
-[UIPencilInteraction description];
-[UIPencilInteraction appendDescriptionToStream:];
-[UIPencilInteraction _hoverGestureRecognizer];
-[UIPencilInteraction didMoveToView:];
```
