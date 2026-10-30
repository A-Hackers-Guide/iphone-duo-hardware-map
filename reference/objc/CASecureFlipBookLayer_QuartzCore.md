# `CASecureFlipBookLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 7 instance variables, 7 properties, 14 instance methods, 3 class methods

## Instance variables

```
^{SILStateMachine=} _machine;
@"NSString" _type;
@"NSString" _currentState;
@"NSString" _nextState;
S _currentFrame;
S _commitedFrame;
@"NSArray" _states;
```

## Properties

```
@property (T@"NSArray",R,V_states) states;
@property (T@"NSString",R) type;
@property (T@"NSString",R) currentState;
@property (T@"NSString",R) nextState;
@property (T@"NSArray",R) validPositions;
@property (T@"NSArray",R) validDynamicPositions;
@property (T@"NSDictionary",R) userInfo;
```

## Class methods

```
+[CASecureFlipBookLayer _hasRenderLayerSubclass];
+[CASecureFlipBookLayer CA_automaticallyNotifiesObservers:];
+[CASecureFlipBookLayer secureFlipBookWithType:];
```

## Instance methods

```
-[CASecureFlipBookLayer nextState];
-[CASecureFlipBookLayer transitionToState:];
-[CASecureFlipBookLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CASecureFlipBookLayer userInfo];
-[CASecureFlipBookLayer dealloc];
-[CASecureFlipBookLayer type];
-[CASecureFlipBookLayer currentState];
-[CASecureFlipBookLayer states];
-[CASecureFlipBookLayer canTransitionToState:];
-[CASecureFlipBookLayer forceTransitionToState:];
-[CASecureFlipBookLayer tick:];
-[CASecureFlipBookLayer validDynamicPositions];
-[CASecureFlipBookLayer validPositions];
-[CASecureFlipBookLayer validTransitionFromState:toState:];
```
