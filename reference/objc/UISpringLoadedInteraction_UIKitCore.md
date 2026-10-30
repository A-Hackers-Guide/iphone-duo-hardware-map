# `UISpringLoadedInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISpringLoadedInteractionBehaviorDelegate`, `UIInteraction_Internal`, `UIDragGestureRecognizerDelegate`, `UIInteraction`
- 8 instance variables, 12 properties, 29 instance methods, 4 class methods

## Instance variables

```
@"UIView" _view;
d _possibleStateDuration;
@"<UISpringLoadedInteractionBehavior>" _interactionBehavior;
@"<UISpringLoadedInteractionEffect>" _interactionEffect;
@"UISpringLoadedInteractionContextImpl" _context;
@? _handler;
@"UIDelayedAction" _emphasizeAction;
@"UIDelayedAction" _activateAction;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"UISpringLoadedInteractionContextImpl",&,N,V_context) context;
@property (T@?,C,N,V_handler) handler;
@property (T@"UIDelayedAction",&,N,V_emphasizeAction) emphasizeAction;
@property (T@"UIDelayedAction",&,N,V_activateAction) activateAction;
@property (Td,N,S_setPossibleStateDuration:,V_possibleStateDuration) _possibleStateDuration;
@property (T@"<UISpringLoadedInteractionBehavior>",R,N,V_interactionBehavior) interactionBehavior;
@property (T@"<UISpringLoadedInteractionEffect>",R,N,V_interactionEffect) interactionEffect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISpringLoadedInteraction _blinkEffect];
+[UISpringLoadedInteraction _defaultInteractionBehavior];
+[UISpringLoadedInteraction hysteresisBehaviorWithBeginningVelocity:cancelingVelocity:];
+[UISpringLoadedInteraction springLoadedInteractionWithHandler:];
```

## Instance methods

```
-[UISpringLoadedInteraction _cancelActions];
-[UISpringLoadedInteraction _dynamicGestureRecognizersForEvent:];
-[UISpringLoadedInteraction setState:];
-[UISpringLoadedInteraction interactionEffect];
-[UISpringLoadedInteraction _startActivateAction];
-[UISpringLoadedInteraction activateAction];
-[UISpringLoadedInteraction interactionBehavior];
-[UISpringLoadedInteraction _emphasizeSpringLoading:];
-[UISpringLoadedInteraction initWithActivationHandler:];
-[UISpringLoadedInteraction _activateSpringLoading:];
-[UISpringLoadedInteraction setHandler:];
-[UISpringLoadedInteraction setView:];
-[UISpringLoadedInteraction _setPossibleStateDuration:];
-[UISpringLoadedInteraction emphasizeAction];
-[UISpringLoadedInteraction _reloadSpringLoadedInteractionBehavior];
-[UISpringLoadedInteraction view];
-[UISpringLoadedInteraction initWithInteractionBehavior:interactionEffect:activationHandler:];
-[UISpringLoadedInteraction setContext:];
-[UISpringLoadedInteraction setEmphasizeAction:];
-[UISpringLoadedInteraction handler];
-[UISpringLoadedInteraction _startEmphasizeAction];
-[UISpringLoadedInteraction willMoveToView:];
-[UISpringLoadedInteraction _resetBehavior];
-[UISpringLoadedInteraction _springloadedStateChanged:];
-[UISpringLoadedInteraction context];
-[UISpringLoadedInteraction _possibleStateDuration];
-[UISpringLoadedInteraction _shouldAllowInteractionWithContext:];
-[UISpringLoadedInteraction setActivateAction:];
-[UISpringLoadedInteraction didMoveToView:];
```
