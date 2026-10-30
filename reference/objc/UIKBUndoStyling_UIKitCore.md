# `UIKBUndoStyling`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 19 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _undoRedoIconOnly;
B _isRTL;
B _cutCopyPasteIconOnly;
B _tooSmallForInstructionalText;
@"UIBlurEffect" _backgroundBlurEffect;
@"UIVibrancyEffect" _backgroundVibrancyEffect;
@"UIColor" _HUDbackgroundColor;
@"UIColor" _HUDShadowColor;
@"UIColor" _buttonGlyphColorEnabled;
@"UIColor" _buttonGlyphColorPressed;
@"UIColor" _buttonGlyphColorDisabled;
@"UIColor" _elementBackgroundColor;
@"UIColor" _elementCoverColor;
d _undoControlMinWidth;
d _cutControlMinWidth;
q _appearance;
```

## Properties

```
@property (T@"UIBlurEffect",&,N,V_backgroundBlurEffect) backgroundBlurEffect;
@property (T@"UIVibrancyEffect",&,N,V_backgroundVibrancyEffect) backgroundVibrancyEffect;
@property (T@"UIColor",&,N,V_HUDbackgroundColor) HUDbackgroundColor;
@property (T@"UIColor",&,N,V_HUDShadowColor) HUDShadowColor;
@property (T@"UIColor",&,N,V_buttonGlyphColorEnabled) buttonGlyphColorEnabled;
@property (T@"UIColor",&,N,V_buttonGlyphColorPressed) buttonGlyphColorPressed;
@property (T@"UIColor",&,N,V_buttonGlyphColorDisabled) buttonGlyphColorDisabled;
@property (T@"UIColor",&,N,V_elementBackgroundColor) elementBackgroundColor;
@property (T@"UIColor",&,N,V_elementCoverColor) elementCoverColor;
@property (TB,N,V_undoRedoIconOnly) undoRedoIconOnly;
@property (TB,N,V_cutCopyPasteIconOnly) cutCopyPasteIconOnly;
@property (TB,N,V_tooSmallForInstructionalText) tooSmallForInstructionalText;
@property (TB,N,V_isRTL) isRTL;
@property (Td,N,V_undoControlMinWidth) undoControlMinWidth;
@property (Td,N,V_cutControlMinWidth) cutControlMinWidth;
@property (Tq,N,V_appearance) appearance;
@property (T@"UIFont",R,N) undoInteractiveControlLabelFont;
@property (T@"UIFont",R,N) undoStateControlLabelFont;
@property (T@"UIFont",R,N) undoStateControlUnavailableLabelFont;
```

## Instance methods

```
-[UIKBUndoStyling setAppearance:];
-[UIKBUndoStyling appearance];
-[UIKBUndoStyling setIsRTL:];
-[UIKBUndoStyling isRTL];
-[UIKBUndoStyling HUDbackgroundColor];
-[UIKBUndoStyling undoInteractiveControlLabelFont];
-[UIKBUndoStyling HUDShadowColor];
-[UIKBUndoStyling backgroundBlurEffect];
-[UIKBUndoStyling backgroundVibrancyEffect];
-[UIKBUndoStyling buttonGlyphColorDisabled];
-[UIKBUndoStyling buttonGlyphColorEnabled];
-[UIKBUndoStyling buttonGlyphColorPressed];
-[UIKBUndoStyling createDynamicColors];
-[UIKBUndoStyling cutControlMinWidth];
-[UIKBUndoStyling cutCopyPasteIconOnly];
-[UIKBUndoStyling elementBackgroundColor];
-[UIKBUndoStyling elementCoverColor];
-[UIKBUndoStyling initWithKeyboardAppearance:isRTL:];
-[UIKBUndoStyling setBackgroundBlurEffect:];
-[UIKBUndoStyling setBackgroundVibrancyEffect:];
-[UIKBUndoStyling setButtonGlyphColorDisabled:];
-[UIKBUndoStyling setButtonGlyphColorEnabled:];
-[UIKBUndoStyling setButtonGlyphColorPressed:];
-[UIKBUndoStyling setCutControlMinWidth:];
-[UIKBUndoStyling setCutCopyPasteIconOnly:];
-[UIKBUndoStyling setElementBackgroundColor:];
-[UIKBUndoStyling setElementCoverColor:];
-[UIKBUndoStyling setHUDShadowColor:];
-[UIKBUndoStyling setHUDbackgroundColor:];
-[UIKBUndoStyling setTooSmallForInstructionalText:];
-[UIKBUndoStyling setUndoControlMinWidth:];
-[UIKBUndoStyling setUndoRedoIconOnly:];
-[UIKBUndoStyling tooSmallForInstructionalText];
-[UIKBUndoStyling undoControlMinWidth];
-[UIKBUndoStyling undoRedoIconOnly];
-[UIKBUndoStyling undoStateControlLabelFont];
-[UIKBUndoStyling undoStateControlUnavailableLabelFont];
-[UIKBUndoStyling vibrancyEffectForBlur:];
```
