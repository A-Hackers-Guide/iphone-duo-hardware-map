# `_UIUCBGroupBarButtonVisualProviderIOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIUCBBarButtonVisualProviderIOS`
- 4 instance variables, 1 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"_UIUCBKBSelectionBackground" _selectionBackgroundView;
@"<_UIButtonBarAppearanceDelegate>" _appearanceDelegate;
B _lightKeyboard;
@"UIColor" _tintColor;
```

## Properties

```
@property (TB,N,V_lightKeyboard) lightKeyboard;
```

## Class methods

```
+[_UIUCBGroupBarButtonVisualProviderIOS darkKeyboardProvider];
+[_UIUCBGroupBarButtonVisualProviderIOS lightKeyboardProvider];
```

## Instance methods

```
-[_UIUCBGroupBarButtonVisualProviderIOS imageSymbolConfiguration];
-[_UIUCBGroupBarButtonVisualProviderIOS updateButton:forSelectedState:];
-[_UIUCBGroupBarButtonVisualProviderIOS shouldLift];
-[_UIUCBGroupBarButtonVisualProviderIOS menuAnchorPoint];
-[_UIUCBGroupBarButtonVisualProviderIOS configureButton:withAppearanceDelegate:fromBarItem:];
-[_UIUCBGroupBarButtonVisualProviderIOS updateButton:toUseButtonShapes:];
-[_UIUCBGroupBarButtonVisualProviderIOS setLightKeyboard:];
-[_UIUCBGroupBarButtonVisualProviderIOS setTintColor:];
-[_UIUCBGroupBarButtonVisualProviderIOS tintColor];
-[_UIUCBGroupBarButtonVisualProviderIOS lightKeyboard];
-[_UIUCBGroupBarButtonVisualProviderIOS copyWithZone:];
-[_UIUCBGroupBarButtonVisualProviderIOS isEqual:];
-[_UIUCBGroupBarButtonVisualProviderIOS _securePasteButtonSite];
```
