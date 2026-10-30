# `_UISpringLoadedHysteresisBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISpringLoadedInteractionBehavior_Private`
- 6 instance variables, 10 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<UISpringLoadedInteractionBehaviorDelegate>" delegate;
d _beginningVelocityThreshold;
d _cancelingVelocityThreshold;
@"CADisplayLink" _displayLink;
@"_UIVelocityIntegrator" _velocityIntegrator;
@"<UISpringLoadedInteractionContext>" _context;
```

## Properties

```
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T@"_UIVelocityIntegrator",&,N,V_velocityIntegrator) velocityIntegrator;
@property (T@"<UISpringLoadedInteractionContext>",W,N,V_context) context;
@property (Td,N,V_beginningVelocityThreshold) beginningVelocityThreshold;
@property (Td,N,V_cancelingVelocityThreshold) cancelingVelocityThreshold;
@property (T@"<UISpringLoadedInteractionBehaviorDelegate>",W,N,Vdelegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISpringLoadedHysteresisBehavior displayLink];
-[_UISpringLoadedHysteresisBehavior cancelingVelocityThreshold];
-[_UISpringLoadedHysteresisBehavior setupDisplayLink];
-[_UISpringLoadedHysteresisBehavior shouldAllowInteraction:withContext:];
-[_UISpringLoadedHysteresisBehavior setDisplayLink:];
-[_UISpringLoadedHysteresisBehavior setCancelingVelocityThreshold:];
-[_UISpringLoadedHysteresisBehavior setDelegate:];
-[_UISpringLoadedHysteresisBehavior setContext:];
-[_UISpringLoadedHysteresisBehavior delegate];
-[_UISpringLoadedHysteresisBehavior interactionDidFinish:];
-[_UISpringLoadedHysteresisBehavior velocityIntegrator];
-[_UISpringLoadedHysteresisBehavior setBeginningVelocityThreshold:];
-[_UISpringLoadedHysteresisBehavior context];
-[_UISpringLoadedHysteresisBehavior setVelocityIntegrator:];
-[_UISpringLoadedHysteresisBehavior beginningVelocityThreshold];
-[_UISpringLoadedHysteresisBehavior _tick:];
```
