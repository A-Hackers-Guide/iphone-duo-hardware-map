# `_UIStatusBarLockItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarItem`
- Protocols: `_UIBasicAnimationFactory`
- 5 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _showsLock;
@"_UIStatusBarLockView" _lockView;
@"_UIExpandingGlyphsView" _stringView;
@"NSTimer" _lockDisappearanceTimer;
q _unlockFailureCount;
```

## Properties

```
@property (T@"_UIStatusBarLockView",&,N,V_lockView) lockView;
@property (T@"_UIExpandingGlyphsView",&,N,V_stringView) stringView;
@property (T@"NSTimer",&,N,V_lockDisappearanceTimer) lockDisappearanceTimer;
@property (TB,N,V_showsLock) showsLock;
@property (Tq,N,V_unlockFailureCount) unlockFailureCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarLockItem textDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarLockItem viewForIdentifier:];
-[_UIStatusBarLockItem additionAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarLockItem canEnableDisplayItem:fromData:];
-[_UIStatusBarLockItem removalAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarLockItem dependentEntryKeys];
-[_UIStatusBarLockItem applyUpdate:toDisplayItem:];
-[_UIStatusBarLockItem _basicAnimationForView:withKeyPath:];
-[_UIStatusBarLockItem _create_lockView];
-[_UIStatusBarLockItem _create_stringView];
-[_UIStatusBarLockItem lockDisappearanceTimer];
-[_UIStatusBarLockItem lockView];
-[_UIStatusBarLockItem setLockDisappearanceTimer:];
-[_UIStatusBarLockItem setLockView:];
-[_UIStatusBarLockItem setShowsLock:];
-[_UIStatusBarLockItem setStringView:];
-[_UIStatusBarLockItem setUnlockFailureCount:];
-[_UIStatusBarLockItem showsLock];
-[_UIStatusBarLockItem stringView];
-[_UIStatusBarLockItem unlockFailureCount];
```
