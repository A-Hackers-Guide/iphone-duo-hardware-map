# `PKSqueezePaletteViewExpandedOptionsLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSqueezePaletteViewLayout`
- 12 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
{CGSize="width"d"height"d} _buttonSize;
d _interButtonSpace;
@"NSArray" _buttons;
^d _buttonAngles;
@"PKSqueezePaletteView" _paletteView;
@"PKSqueezePaletteViewExpandedOptionsLayoutContext" _context;
@"UIButton" _backButton;
@"UIButton" _textBoxButton;
@"UIButton" _signatureButton;
@"UIButton" _shapesButton;
@"UIButton" _stickersButton;
@"UIButton" _gearButton;
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
-[PKSqueezePaletteViewExpandedOptionsLayout dealloc];
-[PKSqueezePaletteViewExpandedOptionsLayout setupUI];
-[PKSqueezePaletteViewExpandedOptionsLayout updateUI];
-[PKSqueezePaletteViewExpandedOptionsLayout _didTapButton:];
-[PKSqueezePaletteViewExpandedOptionsLayout setPaletteView:];
-[PKSqueezePaletteViewExpandedOptionsLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewExpandedOptionsLayout paletteView];
-[PKSqueezePaletteViewExpandedOptionsLayout willTransitionToLayout:];
```
