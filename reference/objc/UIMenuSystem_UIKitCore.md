# `UIMenuSystem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"UIMenu" _cachedInitialRootMenu;
B _building;
```

## Properties

```
@property (TB,R,N,G_isBuilding,V_building) _building;
```

## Class methods

```
+[UIMenuSystem contextSystem];
+[UIMenuSystem mainSystem];
```

## Instance methods

```
-[UIMenuSystem _overrideApplicationName];
-[UIMenuSystem _defaultRootMenuChildren];
-[UIMenuSystem _setOverrideApplicationName:];
-[UIMenuSystem _init];
-[UIMenuSystem setNeedsRebuild];
-[UIMenuSystem _buildMenuWithBuilder:fromResponderChain:atLocation:inCoordinateSpace:];
-[UIMenuSystem _setInitialBuildingResponder:];
-[UIMenuSystem _invalidateCachedInitialRootMenu];
-[UIMenuSystem _isBuilding];
-[UIMenuSystem _newBuilderFromResponderChain:atLocation:inCoordinateSpace:];
-[UIMenuSystem setNeedsRevalidate];
```
