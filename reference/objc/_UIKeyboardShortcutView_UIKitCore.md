# `_UIKeyboardShortcutView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 18 instance variables, 21 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _shouldDisplayGlobeModifierAsGlobeSymbol;
B _shouldDisplayEscShortcutAlternative;
B _shouldMirrorShortcutInputs;
B _shouldAlignShortcutModifiersAndInputInColumn;
B _wantsCompressedWidth;
B _inputStyledAsSingleCharacterOrSymbol;
@"_UIMenuLeafKeyboardShortcut" _shortcut;
@"UIFont" _standardFont;
@"UIFont" _inputCharacterFont;
@"UILabel" _modifiersLabel;
@"UILabel" _inputLabel;
@"UIView" _inputLabelContainer;
@"UIStackView" _labelStackView;
@"NSLayoutConstraint" _reservedInputWidthConstraint;
@"NSLayoutConstraint" _reservedInputWidthSpacingConstraint;
@"NSLayoutConstraint" _modifiersLabelWidthConstraint;
@"NSLayoutConstraint" _inputLabelWidthConstraint;
@"NSLayoutConstraint" _inputHorizontalAlignmentConstraint;
```

## Properties

```
@property (T@"UILabel",&,N,V_modifiersLabel) modifiersLabel;
@property (T@"UILabel",&,N,V_inputLabel) inputLabel;
@property (T@"UIView",&,N,V_inputLabelContainer) inputLabelContainer;
@property (T@"UIStackView",&,N,V_labelStackView) labelStackView;
@property (T@"NSLayoutConstraint",&,N,V_reservedInputWidthConstraint) reservedInputWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_reservedInputWidthSpacingConstraint) reservedInputWidthSpacingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_modifiersLabelWidthConstraint) modifiersLabelWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_inputLabelWidthConstraint) inputLabelWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_inputHorizontalAlignmentConstraint) inputHorizontalAlignmentConstraint;
@property (TB,N,GisInputStyledAsSingleCharacterOrSymbol,V_inputStyledAsSingleCharacterOrSymbol) inputStyledAsSingleCharacterOrSymbol;
@property (T@"_UIMenuLeafKeyboardShortcut",W,N,V_shortcut) shortcut;
@property (T@"UIColor",W,N) textColor;
@property (T@"UIFont",&,N,V_standardFont) standardFont;
@property (T@"UIFont",&,N,V_inputCharacterFont) inputCharacterFont;
@property (TB,N,V_shouldDisplayGlobeModifierAsGlobeSymbol) shouldDisplayGlobeModifierAsGlobeSymbol;
@property (TB,N,V_shouldDisplayEscShortcutAlternative) shouldDisplayEscShortcutAlternative;
@property (TB,N,V_shouldMirrorShortcutInputs) shouldMirrorShortcutInputs;
@property (TB,N,V_shouldAlignShortcutModifiersAndInputInColumn) shouldAlignShortcutModifiersAndInputInColumn;
@property (Td,R,N) modifiersLabelWidth;
@property (Td,R,N) inputLabelWidth;
@property (TB,N,V_wantsCompressedWidth) wantsCompressedWidth;
```

## Instance methods

```
-[_UIKeyboardShortcutView _commonInit];
-[_UIKeyboardShortcutView textColor];
-[_UIKeyboardShortcutView dealloc];
-[_UIKeyboardShortcutView setTextColor:];
-[_UIKeyboardShortcutView setShortcut:];
-[_UIKeyboardShortcutView _defaultTextColor];
-[_UIKeyboardShortcutView setLabelStackView:];
-[_UIKeyboardShortcutView initWithCoder:];
-[_UIKeyboardShortcutView shortcut];
-[_UIKeyboardShortcutView labelStackView];
-[_UIKeyboardShortcutView initWithFrame:];
-[_UIKeyboardShortcutView setFont:];
-[_UIKeyboardShortcutView inputLabelWidth];
-[_UIKeyboardShortcutView _defaultInputCharacterFont];
-[_UIKeyboardShortcutView _defaultStandardFont];
-[_UIKeyboardShortcutView _discoverabilityCombinationForShortcut:shouldDisplayEscShortcutAlternative:];
-[_UIKeyboardShortcutView _getHardwareKeyboardIsArabic:globeKeyLabelHasGlobeSymbol:];
-[_UIKeyboardShortcutView _setupInputHorizontalAlignmentConstraint];
-[_UIKeyboardShortcutView _updateInputLabelSpacing:];
-[_UIKeyboardShortcutView _updateInputLabelStyle:];
-[_UIKeyboardShortcutView _updateInputLabelText];
-[_UIKeyboardShortcutView _updateModifiersLabelText];
-[_UIKeyboardShortcutView inputAttributedStringForMenuLeafShortcut:symbolFont:shouldDisplayEscShortcutAlternative:shouldMirrorShortcutInputs:shouldStyleAsSingleCharacterOrSymbol:];
-[_UIKeyboardShortcutView inputCharacterFont];
-[_UIKeyboardShortcutView inputHorizontalAlignmentConstraint];
-[_UIKeyboardShortcutView inputLabel];
-[_UIKeyboardShortcutView inputLabelContainer];
-[_UIKeyboardShortcutView inputLabelWidthConstraint];
-[_UIKeyboardShortcutView isInputStyledAsSingleCharacterOrSymbol];
-[_UIKeyboardShortcutView modifiersAttributedStringForMenuLeafShortcut:font:shouldDisplayGlobeModiferAsGlobeSymbol:];
-[_UIKeyboardShortcutView modifiersLabel];
-[_UIKeyboardShortcutView modifiersLabelWidth];
-[_UIKeyboardShortcutView modifiersLabelWidthConstraint];
-[_UIKeyboardShortcutView reservedInputWidthConstraint];
-[_UIKeyboardShortcutView reservedInputWidthSpacingConstraint];
-[_UIKeyboardShortcutView setInputCharacterFont:];
-[_UIKeyboardShortcutView setInputHorizontalAlignmentConstraint:];
-[_UIKeyboardShortcutView setInputLabel:];
-[_UIKeyboardShortcutView setInputLabelContainer:];
-[_UIKeyboardShortcutView setInputLabelWidthConstraint:];
-[_UIKeyboardShortcutView setInputStyledAsSingleCharacterOrSymbol:];
-[_UIKeyboardShortcutView setModifiersLabel:];
-[_UIKeyboardShortcutView setModifiersLabelWidthConstraint:];
-[_UIKeyboardShortcutView setModifiersWidth:inputWidth:];
-[_UIKeyboardShortcutView setReservedInputWidthConstraint:];
-[_UIKeyboardShortcutView setReservedInputWidthSpacingConstraint:];
-[_UIKeyboardShortcutView setShouldAlignShortcutModifiersAndInputInColumn:];
-[_UIKeyboardShortcutView setShouldDisplayEscShortcutAlternative:];
-[_UIKeyboardShortcutView setShouldDisplayGlobeModifierAsGlobeSymbol:];
-[_UIKeyboardShortcutView setShouldMirrorShortcutInputs:];
-[_UIKeyboardShortcutView setStandardFont:];
-[_UIKeyboardShortcutView setWantsCompressedWidth:];
-[_UIKeyboardShortcutView shouldAlignShortcutModifiersAndInputInColumn];
-[_UIKeyboardShortcutView shouldDisplayEscShortcutAlternative];
-[_UIKeyboardShortcutView shouldDisplayGlobeModifierAsGlobeSymbol];
-[_UIKeyboardShortcutView shouldMirrorShortcutInputs];
-[_UIKeyboardShortcutView standardFont];
-[_UIKeyboardShortcutView wantsCompressedWidth];
```
