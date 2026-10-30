# `_UIImageSymbolBounceEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIImageSymbolEffect`
- 3 instance variables, 3 properties, 13 instance methods, 2 class methods

## Instance variables

```
B _byLayer;
q _bounceDirection;
@"_UIImageSymbolEffectRepeatBehavior" _repeatBehavior;
```

## Properties

```
@property (T@"_UIImageSymbolEffectRepeatBehavior",&,N,V_repeatBehavior) repeatBehavior;
@property (Tq,N,V_bounceDirection) bounceDirection;
@property (TB,N,V_byLayer) byLayer;
```

## Class methods

```
+[_UIImageSymbolBounceEffect supportsSecureCoding];
+[_UIImageSymbolBounceEffect effect];
```

## Instance methods

```
-[_UIImageSymbolBounceEffect encodeWithCoder:];
-[_UIImageSymbolBounceEffect hash];
-[_UIImageSymbolBounceEffect initWithCoder:];
-[_UIImageSymbolBounceEffect copyWithZone:];
-[_UIImageSymbolBounceEffect isEqual:];
-[_UIImageSymbolBounceEffect byLayer];
-[_UIImageSymbolBounceEffect bounceDirection];
-[_UIImageSymbolBounceEffect _isValidAnimationPreset];
-[_UIImageSymbolBounceEffect _nsSymbolEffectRepresentation];
-[_UIImageSymbolBounceEffect repeatBehavior];
-[_UIImageSymbolBounceEffect setBounceDirection:];
-[_UIImageSymbolBounceEffect setByLayer:];
-[_UIImageSymbolBounceEffect setRepeatBehavior:];
```
