# `_UIImageSymbolEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIImageSymbolAnimationPreset`, `NSCopying`, `NSSecureCoding`
- 1 instance variables, 5 properties, 16 instance methods, 2 class methods

## Instance variables

```
@? _completionHandler;
```

## Properties

```
@property (Tq,R,N) _stateUpdateType;
@property (Tq,R,N) _desiredScale;
@property (Tq,R,N) _desiredVisibility;
@property (TB,R,N,G_isValidAnimationPreset) _validAnimationPreset;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Class methods

```
+[_UIImageSymbolEffect supportsSecureCoding];
+[_UIImageSymbolEffect effect];
```

## Instance methods

```
-[_UIImageSymbolEffect setCompletionHandler:];
-[_UIImageSymbolEffect completionHandler];
-[_UIImageSymbolEffect init];
-[_UIImageSymbolEffect encodeWithCoder:];
-[_UIImageSymbolEffect hash];
-[_UIImageSymbolEffect initWithCoder:];
-[_UIImageSymbolEffect copyWithZone:];
-[_UIImageSymbolEffect isEqual:];
-[_UIImageSymbolEffect _isSymbolEffect];
-[_UIImageSymbolEffect _desiredScale];
-[_UIImageSymbolEffect _desiredVisibility];
-[_UIImageSymbolEffect _isSymbolTransition];
-[_UIImageSymbolEffect _isValidAnimationPreset];
-[_UIImageSymbolEffect _nsSymbolEffectRepresentation];
-[_UIImageSymbolEffect _performCompletionHandler];
-[_UIImageSymbolEffect _stateUpdateType];
```
