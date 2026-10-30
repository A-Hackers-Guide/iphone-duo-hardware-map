# `_UIStatusBarVisualProvider_Phone`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarVisualProvider_iOS`
- Protocols: `_UIStatusBarPillRegionVisualProvider`
- 1 instance variables, 10 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"_UIStatusBarVisualProvider_PillRegionCoordinator" _pillRegionCoordinator;
```

## Properties

```
@property (T@"_UIStatusBarVisualProvider_PillRegionCoordinator",&,N,V_pillRegionCoordinator) pillRegionCoordinator;
@property (TB,N) expanded;
@property (T@"_UIStatusBar",W,N) statusBar;
@property (TB,R,N) supportsIndirectPointerTouchActions;
@property (T@"UIFont",R,N) clockFont;
@property (TB,?,R,N) canFixupDisplayItemAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarVisualProvider_Phone visualProviderSubclassForScreen:visualProviderInfo:];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_Phone init];
-[_UIStatusBarVisualProvider_Phone actionable:highlighted:initialPress:];
-[_UIStatusBarVisualProvider_Phone additionAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_Phone pillRegionCoordinator];
-[_UIStatusBarVisualProvider_Phone removalAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_Phone setPillRegionCoordinator:];
-[_UIStatusBarVisualProvider_Phone willUpdateWithData:];
```
