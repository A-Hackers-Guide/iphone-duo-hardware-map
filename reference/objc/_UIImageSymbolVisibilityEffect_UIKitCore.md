# `_UIImageSymbolVisibilityEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIImageSymbolEffect`
- 3 instance variables, 3 properties, 15 instance methods, 5 class methods

## Instance variables

```
B _byLayer;
q _visibility;
q _style;
```

## Properties

```
@property (Tq,N,V_visibility) visibility;
@property (Tq,N,V_style) style;
@property (TB,N,V_byLayer) byLayer;
```

## Class methods

```
+[_UIImageSymbolVisibilityEffect supportsSecureCoding];
+[_UIImageSymbolVisibilityEffect effect];
+[_UIImageSymbolVisibilityEffect disappearEffect];
+[_UIImageSymbolVisibilityEffect appearEffect];
+[_UIImageSymbolVisibilityEffect effectWithVisibility:];
```

## Instance methods

```
-[_UIImageSymbolVisibilityEffect setVisibility:];
-[_UIImageSymbolVisibilityEffect visibility];
-[_UIImageSymbolVisibilityEffect style];
-[_UIImageSymbolVisibilityEffect setStyle:];
-[_UIImageSymbolVisibilityEffect encodeWithCoder:];
-[_UIImageSymbolVisibilityEffect hash];
-[_UIImageSymbolVisibilityEffect initWithCoder:];
-[_UIImageSymbolVisibilityEffect copyWithZone:];
-[_UIImageSymbolVisibilityEffect isEqual:];
-[_UIImageSymbolVisibilityEffect byLayer];
-[_UIImageSymbolVisibilityEffect _desiredVisibility];
-[_UIImageSymbolVisibilityEffect _isValidAnimationPreset];
-[_UIImageSymbolVisibilityEffect _nsSymbolEffectRepresentation];
-[_UIImageSymbolVisibilityEffect _stateUpdateType];
-[_UIImageSymbolVisibilityEffect setByLayer:];
```
