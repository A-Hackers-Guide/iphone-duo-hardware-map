# `UIPointerEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `UIHoverEffect`
- 1 instance variables, 26 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"UITargetedPreview" _preview;
```

## Properties

```
@property (T@"UITargetedPreview",C,N,V_preview) preview;
@property (TQ,R,N) options;
@property (TQ,R,N) constrainedAxes;
@property (T@"NSValue",R,N) overrideSlipPoints;
@property (T{CGPoint=dd},R,N) slipFactor;
@property (Td,R,N) maxSlip;
@property (Td,R,N) parallaxAmount;
@property (Td,R,N) scaleUpPoints;
@property (Td,R,N) defaultPointerCornerRadius;
@property (Td,R,N) scaleUpAnimationResponse;
@property (Td,R,N) scaleUpAnimationDampingRatio;
@property (Td,R,N) dampedAnimationResponse;
@property (Td,R,N) dampedAnimationDampingRatio;
@property (Td,R,N) liftProgressFloor;
@property (Td,R,N) liftForceExponent;
@property (T@"UIViewSpringAnimationBehavior",R,N) liftProgressSpring;
@property (TB,R,N) useSoftShadow;
@property (TB,R,N) allowsSanitization;
@property (T@?,R,N) tintColorMatrixProvider;
@property (T{CGPoint=dd},R,N) _plasmaRubberbandFactor;
@property (Td,R,N) _plasmaLensParallaxFactor;
@property (Td,R,N) _plasmaParallaxFactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPointerEffect effectWithPreview:];
```

## Instance methods

```
-[UIPointerEffect preview];
-[UIPointerEffect parallaxAmount];
-[UIPointerEffect settings];
-[UIPointerEffect setPreview:];
-[UIPointerEffect hash];
-[UIPointerEffect options];
-[UIPointerEffect copyWithZone:];
-[UIPointerEffect isEqual:];
-[UIPointerEffect constrainedAxes];
-[UIPointerEffect maxSlip];
-[UIPointerEffect _plasmaLensParallaxFactor];
-[UIPointerEffect _plasmaParallaxFactor];
-[UIPointerEffect _plasmaRubberbandFactor];
-[UIPointerEffect allowsSanitization];
-[UIPointerEffect dampedAnimationDampingRatio];
-[UIPointerEffect dampedAnimationResponse];
-[UIPointerEffect defaultPointerCornerRadius];
-[UIPointerEffect liftForceExponent];
-[UIPointerEffect liftProgressFloor];
-[UIPointerEffect liftProgressSpring];
-[UIPointerEffect overrideSlipPoints];
-[UIPointerEffect scaleUpAnimationDampingRatio];
-[UIPointerEffect scaleUpAnimationResponse];
-[UIPointerEffect scaleUpPoints];
-[UIPointerEffect slipFactor];
-[UIPointerEffect tintColorMatrixProvider];
-[UIPointerEffect useSoftShadow];
```
