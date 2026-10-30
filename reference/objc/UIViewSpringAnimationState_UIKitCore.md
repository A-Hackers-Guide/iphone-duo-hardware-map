# `UIViewSpringAnimationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewAnimationState`
- 5 instance variables, 4 properties, 9 instance methods, 4 class methods

## Instance variables

```
d _mass;
d _stiffness;
d _damping;
d _velocity;
B _allowsOverdamping;
```

## Properties

```
@property (Td,R,N) mass;
@property (Td,R,N) stiffness;
@property (Td,R,N) damping;
@property (Td,R,N) velocity;
```

## Class methods

```
+[UIViewSpringAnimationState computeDerivedSpringParameters:zeta:mass:velocity:epsilon:stiffness:damping:debugging:];
+[UIViewSpringAnimationState defaultSpringAnimationForKey:mass:stiffness:damping:velocity:];
+[UIViewSpringAnimationState computeDerivedSpringParameters:zeta:mass:velocity:epsilon:stiffness:damping:];
+[UIViewSpringAnimationState defaultSpringAnimationForKey:mass:stiffness:damping:velocity:allowsOverdamping:];
```

## Instance methods

```
-[UIViewSpringAnimationState damping];
-[UIViewSpringAnimationState generateSpringPropertiesForPerceptualDuration:bounce:velocity:];
-[UIViewSpringAnimationState velocity];
-[UIViewSpringAnimationState stiffness];
-[UIViewSpringAnimationState animationForLayer:forKey:forView:];
-[UIViewSpringAnimationState _defaultAnimationForKey:];
-[UIViewSpringAnimationState generateSpringPropertiesForDuration:damping:velocity:];
-[UIViewSpringAnimationState mass];
-[UIViewSpringAnimationState setupWithDuration:delay:view:options:factory:parentState:start:completion:];
```
