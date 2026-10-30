# `_UIViewAnimationAttributes`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSXPCSecureCoding`
- 10 instance variables, 15 properties, 15 instance methods, 2 class methods

## Instance variables

```
d _duration;
d _delay;
Q _options;
{CAFrameRateRange="minimum"f"maximum"f"preferred"f} _preferredFrameRateRange;
I _updateReason;
B _hasSpringAttributes;
d _springDamping;
d _springVelocity;
d _springMass;
d _springStiffness;
```

## Properties

```
@property (Td,R,N,G_duration,V_duration) duration;
@property (Td,R,N,G_delay,V_delay) delay;
@property (Td,R,N,G_frameInterval) frameInterval;
@property (T{CAFrameRateRange=fff},R,N,G_preferredFrameRateRange) preferredFrameRateRange;
@property (TI,R,N,G_updateReason) updateReason;
@property (Tq,R,N,G_curve) curve;
@property (TB,R,N,G_hasSpringAttributes,V_hasSpringAttributes) hasSpringAttributes;
@property (Td,R,N,G_springDamping,V_springDamping) springDamping;
@property (Td,R,N,G_springVelocity,V_springVelocity) springVelocity;
@property (Td,R,N,G_springMass,V_springMass) springMass;
@property (Td,R,N,G_springStiffness,V_springStiffness) springStiffness;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIViewAnimationAttributes supportsBSXPCSecureCoding];
+[_UIViewAnimationAttributes supportsSecureCoding];
```

## Instance methods

```
-[_UIViewAnimationAttributes _duration];
-[_UIViewAnimationAttributes _springStiffness];
-[_UIViewAnimationAttributes _delay];
-[_UIViewAnimationAttributes _springDamping];
-[_UIViewAnimationAttributes _curve];
-[_UIViewAnimationAttributes _frameInterval];
-[_UIViewAnimationAttributes _springMass];
-[_UIViewAnimationAttributes encodeWithCoder:];
-[_UIViewAnimationAttributes _springVelocity];
-[_UIViewAnimationAttributes initWithCoder:];
-[_UIViewAnimationAttributes _updateReason];
-[_UIViewAnimationAttributes encodeWithBSXPCCoder:];
-[_UIViewAnimationAttributes initWithBSXPCCoder:];
-[_UIViewAnimationAttributes _preferredFrameRateRange];
-[_UIViewAnimationAttributes _hasSpringAttributes];
```
