# `_UIButtonSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- Protocols: `PTSettingsKeyObserver`
- 5 instance variables, 9 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _highlightMode;
B _highlightSubclasses;
B _highlightIgnoresBars;
B _highlightBelow;
B _highlightAlternateColor;
```

## Properties

```
@property (TB,N,V_highlightMode) highlightMode;
@property (TB,N,V_highlightSubclasses) highlightSubclasses;
@property (TB,N,V_highlightIgnoresBars) highlightIgnoresBars;
@property (TB,N,V_highlightBelow) highlightBelow;
@property (TB,N,V_highlightAlternateColor) highlightAlternateColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIButtonSettings settingsControllerModule];
```

## Instance methods

```
-[_UIButtonSettings highlightMode];
-[_UIButtonSettings setHighlightIgnoresBars:];
-[_UIButtonSettings highlightIgnoresBars];
-[_UIButtonSettings settings:changedValueForKey:];
-[_UIButtonSettings setHighlightMode:];
-[_UIButtonSettings setDefaultValues];
-[_UIButtonSettings setHighlightSubclasses:];
-[_UIButtonSettings initWithDefaultValues];
-[_UIButtonSettings highlightBelow];
-[_UIButtonSettings highlightSubclasses];
-[_UIButtonSettings highlightAlternateColor];
-[_UIButtonSettings setHighlightAlternateColor:];
-[_UIButtonSettings setHighlightBelow:];
```
