# `PKPaletteKeyboardButton`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteButton`
- 5 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIImage" _indicatorImage;
@"PKTextInputLanguageSelectionToken" _observerToken;
B _enableKeyboardToggle;
q _floatingKeyboardType;
@"UIMenu" _keyboardSelectionMenu;
```

## Properties

```
@property (Tq,N,V_floatingKeyboardType) floatingKeyboardType;
@property (TB,N,V_enableKeyboardToggle) enableKeyboardToggle;
@property (T@"UIMenu",&,N,V_keyboardSelectionMenu) keyboardSelectionMenu;
```

## Instance methods

```
-[PKPaletteKeyboardButton initWithImage:];
-[PKPaletteKeyboardButton contextMenuInteraction:configurationForMenuAtLocation:];
-[PKPaletteKeyboardButton dealloc];
-[PKPaletteKeyboardButton _updateButtonImage];
-[PKPaletteKeyboardButton _updateKeyboardToggleState];
-[PKPaletteKeyboardButton enableKeyboardToggle];
-[PKPaletteKeyboardButton floatingKeyboardType];
-[PKPaletteKeyboardButton keyboardSelectionMenu];
-[PKPaletteKeyboardButton setEnableKeyboardToggle:];
-[PKPaletteKeyboardButton setFloatingKeyboardType:];
-[PKPaletteKeyboardButton setKeyboardSelectionMenu:];
```
