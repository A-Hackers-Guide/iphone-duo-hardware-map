# `TPButton`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 5 instance variables, 3 properties, 26 instance methods, 6 class methods

## Instance variables

```
i _color;
@"_UIBackdropView" _backdropView;
B _blursBackground;
B _roundsCorners;
B _usesOverlayBlendingForContents;
```

## Properties

```
@property (TB,N,V_blursBackground) blursBackground;
@property (TB,N,V_roundsCorners) roundsCorners;
@property (TB,N,V_usesOverlayBlendingForContents) usesOverlayBlendingForContents;
```

## Class methods

```
+[TPButton defaultHeight];
+[TPButton defaultHeightForColor:];
+[TPButton defaultStandardFont];
+[TPButton defaultWidthForCenterButton];
+[TPButton defaultWidthForSideButton];
+[TPButton maxWidthForCenterButton];
```

## Instance methods

```
-[TPButton buttonColor];
-[TPButton setRoundsCorners:];
-[TPButton setSelected:];
-[TPButton intrinsicContentSize];
-[TPButton drawRect:];
-[TPButton blursBackground];
-[TPButton layoutSubviews];
-[TPButton setBackgroundColor:];
-[TPButton setHighlighted:];
-[TPButton setEnabled:];
-[TPButton setImage:forState:];
-[TPButton roundsCorners];
-[TPButton setBlursBackground:];
-[TPButton initWithTitle:icon:color:frame:];
-[TPButton setButtonColor:];
-[TPButton _animationDidEnd];
-[TPButton _animationWillBegin];
-[TPButton setDisabledButtonColor:];
-[TPButton setIconVerticalOffset:];
-[TPButton setMinimumTitleFontSize:];
-[TPButton setMinimumTitleFontSize:maximumTitleFontSize:];
-[TPButton setPlusSeparatedTitle:];
-[TPButton setTitleImagePadding:];
-[TPButton setTitleVerticalOffset:];
-[TPButton setUsesOverlayBlendingForContents:];
-[TPButton usesOverlayBlendingForContents];
```
