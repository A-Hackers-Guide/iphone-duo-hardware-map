# `_UIHomeAffordanceObserverProxyInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIGeometryChangeObserver`, `UIInteraction_Private`, `UIInteraction`, `_UIHomeAffordanceObserver`, `BSDescriptionStreaming`
- 9 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@? _proxyIntersectedFrameHandler;
@? _proxyDoubleTapGestureHandler;
{?="hasScheduledCoalescedFrameEvaluation"b1} _interactionFlags;
@"UIView" _view;
@"UIWindow" _window;
@"<_UIHomeAffordanceNotifying>" _homeAffordanceNotifier;
@"<_UIInvalidatable>" _homeAffordanceRegistrationToken;
@"CADisplayLink" _coalescedFrameEvaluationDisplayLink;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastNotifiedHomeAffordanceFrameIntersection;
```

## Properties

```
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHomeAffordanceObserverProxyInteraction _windowHostingSceneDidMoveToScreen:];
-[_UIHomeAffordanceObserverProxyInteraction _notifier:homeAffordanceFrameDidChange:];
-[_UIHomeAffordanceObserverProxyInteraction _notifier:homeAffordanceDoubleTapGestureDidSucceed:];
-[_UIHomeAffordanceObserverProxyInteraction debugDescription];
-[_UIHomeAffordanceObserverProxyInteraction init];
-[_UIHomeAffordanceObserverProxyInteraction dealloc];
-[_UIHomeAffordanceObserverProxyInteraction _didMoveFromWindow:toWindow:];
-[_UIHomeAffordanceObserverProxyInteraction _geometryChanged:forAncestor:];
-[_UIHomeAffordanceObserverProxyInteraction succinctDescription];
-[_UIHomeAffordanceObserverProxyInteraction view];
-[_UIHomeAffordanceObserverProxyInteraction _windowWillMoveToNilScene:];
-[_UIHomeAffordanceObserverProxyInteraction _windowDidMoveToScene:];
-[_UIHomeAffordanceObserverProxyInteraction willMoveToView:];
-[_UIHomeAffordanceObserverProxyInteraction description];
-[_UIHomeAffordanceObserverProxyInteraction appendDescriptionToStream:];
-[_UIHomeAffordanceObserverProxyInteraction didMoveToView:];
-[_UIHomeAffordanceObserverProxyInteraction _coalescedFrameEvaluationDisplayLinkTicked:];
```
