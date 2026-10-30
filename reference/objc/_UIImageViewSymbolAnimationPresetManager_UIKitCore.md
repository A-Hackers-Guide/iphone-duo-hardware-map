# `_UIImageViewSymbolAnimationPresetManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _activeSymbolEffects;
@"NSMutableArray" _pendingSymbolEffects;
@"NSSymbolContentTransition" _activeSymbolContentTransition;
@"_UIImageViewPendingSymbolContentTransition" _pendingSymbolContentTransition;
@"<_UIImageViewSymbolAnimationPresetClient>" _client;
```

## Properties

```
@property (T@"<_UIImageViewSymbolAnimationPresetClient>",W,N,V_client) client;
```

## Class methods

```
+[_UIImageViewSymbolAnimationPresetManager managerForClient:];
```

## Instance methods

```
-[_UIImageViewSymbolAnimationPresetManager init];
-[_UIImageViewSymbolAnimationPresetManager pendingSymbolContentTransitionForSettingSymbolImage:];
-[_UIImageViewSymbolAnimationPresetManager activatePendingSymbolContentTransition:];
-[_UIImageViewSymbolAnimationPresetManager _symbolEffect:collidesWithSymbolEffect:forAddingEffect:];
-[_UIImageViewSymbolAnimationPresetManager _removeSymbolEffectsOfType:options:animated:completion:forAddingNewEffect:];
-[_UIImageViewSymbolAnimationPresetManager setClient:];
-[_UIImageViewSymbolAnimationPresetManager hasPendingAnimationsForImage:];
-[_UIImageViewSymbolAnimationPresetManager activatePendingSymbolEffects];
-[_UIImageViewSymbolAnimationPresetManager activeSymbolEffectDidComplete:];
-[_UIImageViewSymbolAnimationPresetManager removeSymbolEffectsOfType:options:animated:completion:];
-[_UIImageViewSymbolAnimationPresetManager activeSymbolContentTransitionDidComplete:];
-[_UIImageViewSymbolAnimationPresetManager removeAllSymbolEffectsWithOptions:animated:];
-[_UIImageViewSymbolAnimationPresetManager hasPendingContentTransition];
-[_UIImageViewSymbolAnimationPresetManager _activateActiveSymbolEffectEntry:];
-[_UIImageViewSymbolAnimationPresetManager addPendingSymbolEffect:options:animated:completion:];
-[_UIImageViewSymbolAnimationPresetManager discardPendingSymbolContentTransitions];
-[_UIImageViewSymbolAnimationPresetManager addActiveSymbolEffect:options:animated:completion:];
-[_UIImageViewSymbolAnimationPresetManager client];
-[_UIImageViewSymbolAnimationPresetManager addPendingSymbolContentTransition:fromSymbolImage:toSymbolImage:options:completion:];
```
