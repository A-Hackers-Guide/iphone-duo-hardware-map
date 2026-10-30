# `_UIImageSymbolTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIImageSymbolAnimationPreset`, `NSCopying`, `NSSecureCoding`
- 1 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
@? _completionHandler;
```

## Properties

```
@property (TB,R,N,G_isValidAnimationPreset) _validAnimationPreset;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Class methods

```
+[_UIImageSymbolTransition transition];
+[_UIImageSymbolTransition supportsSecureCoding];
```

## Instance methods

```
-[_UIImageSymbolTransition setCompletionHandler:];
-[_UIImageSymbolTransition completionHandler];
-[_UIImageSymbolTransition init];
-[_UIImageSymbolTransition encodeWithCoder:];
-[_UIImageSymbolTransition hash];
-[_UIImageSymbolTransition initWithCoder:];
-[_UIImageSymbolTransition copyWithZone:];
-[_UIImageSymbolTransition isEqual:];
-[_UIImageSymbolTransition _isSymbolEffect];
-[_UIImageSymbolTransition _isSymbolTransition];
-[_UIImageSymbolTransition _isValidAnimationPreset];
-[_UIImageSymbolTransition _nsSymbolContentTransitionRepresentation];
-[_UIImageSymbolTransition _performCompletionHandler];
```
