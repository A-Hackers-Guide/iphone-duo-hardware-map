# `_UIStatusBarVisualProvider_Fallback`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarVisualProvider`
- 2 instance variables, 9 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"_UIStatusBar" _statusBar;
@"NSArray" _placements;
```

## Properties

```
@property (T@"NSArray",&,N,V_placements) placements;
@property (T@"_UIStatusBar",W,N,V_statusBar) statusBar;
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
+[_UIStatusBarVisualProvider_Fallback requiresIterativeOverflowLayout];
+[_UIStatusBarVisualProvider_Fallback intrinsicContentSizeForOrientation:];
+[_UIStatusBarVisualProvider_Fallback scalesWithScreenNativeScale];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_Fallback statusBar];
-[_UIStatusBarVisualProvider_Fallback setStatusBar:];
-[_UIStatusBarVisualProvider_Fallback styleAttributesForStyle:];
-[_UIStatusBarVisualProvider_Fallback clockFont];
-[_UIStatusBarVisualProvider_Fallback orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider_Fallback placements];
-[_UIStatusBarVisualProvider_Fallback setPlacements:];
-[_UIStatusBarVisualProvider_Fallback setupInContainerView:];
-[_UIStatusBarVisualProvider_Fallback supportsIndirectPointerTouchActions];
```
