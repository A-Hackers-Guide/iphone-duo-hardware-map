# `_UIFocusEffectsController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"_UIDynamicValueConvergenceAnimation" _rollbackAnimation;
@"NSHashTable" _observers;
{CGPoint="x"d"y"d} _displayOffset;
d _displayMovementAdjustment;
B _displayOffsetAccumulatorEnabled;
{CGPoint="x"d"y"d} _currentOffset;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_currentOffset) currentOffset;
@property (T{CGPoint=dd},R,N) displayOffset;
@property (TB,N,V_displayOffsetAccumulatorEnabled) displayOffsetAccumulatorEnabled;
```

## Instance methods

```
-[_UIFocusEffectsController removeObserver:];
-[_UIFocusEffectsController init];
-[_UIFocusEffectsController reset];
-[_UIFocusEffectsController currentOffset];
-[_UIFocusEffectsController addObserver:];
-[_UIFocusEffectsController displayOffsetAccumulatorEnabled];
-[_UIFocusEffectsController _notifyObserversForMovementDirection:];
-[_UIFocusEffectsController adjustDisplayOffsetAccumulationFactorForFocusTransfer];
-[_UIFocusEffectsController cancelRollbackAnimation];
-[_UIFocusEffectsController displayOffset];
-[_UIFocusEffectsController resetDisplayOffsetAccumulationFactor];
-[_UIFocusEffectsController setDisplayOffsetAccumulatorEnabled:];
-[_UIFocusEffectsController startRollbackAnimation];
-[_UIFocusEffectsController updateCurrentOffset:];
-[_UIFocusEffectsController updateCurrentOffset:overrideDisplayOffset:];
```
