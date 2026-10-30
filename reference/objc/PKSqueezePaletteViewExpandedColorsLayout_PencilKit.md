# `PKSqueezePaletteViewExpandedColorsLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSqueezePaletteViewLayout`
- 9 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
{CGSize="width"d"height"d} _buttonSize;
^d _buttonAngles;
d _interButtonSpace;
d _backButtonAngle;
@"PKSqueezePaletteView" _paletteView;
@"PKSqueezePaletteViewExpandedColorsLayoutContext" _context;
@"NSArray" _colorButtons;
Q _selectedColorIndex;
@"UIButton" _backButton;
```

## Properties

```
@property (T@"PKSqueezePaletteView",W,N,V_paletteView) paletteView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKSqueezePaletteViewExpandedColorsLayout dealloc];
-[PKSqueezePaletteViewExpandedColorsLayout setupUI];
-[PKSqueezePaletteViewExpandedColorsLayout updateUI];
-[PKSqueezePaletteViewExpandedColorsLayout setPaletteView:];
-[PKSqueezePaletteViewExpandedColorsLayout _didTapBackButton:];
-[PKSqueezePaletteViewExpandedColorsLayout _didTapColorButton:];
-[PKSqueezePaletteViewExpandedColorsLayout _didTapMulticolorButton:];
-[PKSqueezePaletteViewExpandedColorsLayout colorAppearanceDidChange];
-[PKSqueezePaletteViewExpandedColorsLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewExpandedColorsLayout paletteView];
-[PKSqueezePaletteViewExpandedColorsLayout willTransitionToLayout:];
```
