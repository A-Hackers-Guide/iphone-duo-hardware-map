# `_UITextOption`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIViewMultiLayerDelegate`
- 19 instance variables, 23 properties, 60 instance methods, 1 class methods

## Instance variables

```
Q _state;
q _type;
@"NSString" _originalText;
@"UIColor" _optionalTintColor;
@"TIKeyboardCandidate" _sourceCandidate;
@"NSLayoutConstraint" _symbolImageViewYConstraint;
@"NSString" _textChoice;
@"UILabel" _contentsLabel;
@"UIImageView" _symbolImageView;
@"UIView" _lineView;
@"UIView" _secureCandidateLabel;
@"UIVisualEffectView" _selectionVibrancyView;
@"TUIGradientView" _contentsLabelEffectView;
d _horizontalPadding;
@"NSArray" _insetConstraints;
@"NSLayoutConstraint" _minimumLabelWidth;
@"UILayoutGuide" _accessorySymbolSpacingGuide;
{CGSize="width"d"height"d} _secureCandidateSize;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _currentEdgeInsets;
```

## Properties

```
@property (T@"NSString",&,N,V_textChoice) textChoice;
@property (T@"UILabel",&,N,V_contentsLabel) contentsLabel;
@property (T@"UIImageView",&,N,V_symbolImageView) symbolImageView;
@property (T@"UIView",&,N,V_lineView) lineView;
@property (T@"UIView",&,N,V_secureCandidateLabel) secureCandidateLabel;
@property (T@"UIVisualEffectView",&,N,V_selectionVibrancyView) selectionVibrancyView;
@property (T@"TUIGradientView",&,N,V_contentsLabelEffectView) contentsLabelEffectView;
@property (Td,N,V_horizontalPadding) horizontalPadding;
@property (T@"NSArray",&,N,V_insetConstraints) insetConstraints;
@property (T@"NSLayoutConstraint",&,N,V_minimumLabelWidth) minimumLabelWidth;
@property (T@"UILayoutGuide",&,N,V_accessorySymbolSpacingGuide) accessorySymbolSpacingGuide;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_currentEdgeInsets) currentEdgeInsets;
@property (TQ,N,V_state) state;
@property (Tq,N,V_type) type;
@property (T@"NSString",N,V_originalText) originalText;
@property (T@"UIColor",N,V_optionalTintColor) optionalTintColor;
@property (T@"TIKeyboardCandidate",&,N,V_sourceCandidate) sourceCandidate;
@property (T{CGSize=dd},N,V_secureCandidateSize) secureCandidateSize;
@property (T@"NSLayoutConstraint",&,N,V_symbolImageViewYConstraint) symbolImageViewYConstraint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UITextOption baseSymbolSize];
```

## Instance methods

```
-[_UITextOption setState:];
-[_UITextOption intrinsicContentSize];
-[_UITextOption symbolImageView];
-[_UITextOption horizontalPadding];
-[_UITextOption textColor];
-[_UITextOption setHorizontalPadding:];
-[_UITextOption viewForLastBaselineLayout];
-[_UITextOption hitTest:withEvent:];
-[_UITextOption imageName];
-[_UITextOption _outermostLayerDidChange:];
-[_UITextOption setType:];
-[_UITextOption type];
-[_UITextOption lineView];
-[_UITextOption state];
-[_UITextOption setAccessorySymbolSpacingGuide:];
-[_UITextOption sourceCandidate];
-[_UITextOption accessorySymbolSpacingGuide];
-[_UITextOption buttonImage];
-[_UITextOption contentInsetsForType:dividerWidth:];
-[_UITextOption contentsLabel];
-[_UITextOption contentsLabelEffectView];
-[_UITextOption createSelectionVibrancyView];
-[_UITextOption currentEdgeInsets];
-[_UITextOption fontForLabel];
-[_UITextOption initWithTitle:type:];
-[_UITextOption initWithTitle:type:optionalTintColor:];
-[_UITextOption insetConstraints];
-[_UITextOption insetMultiplierForContentSizeCategory:];
-[_UITextOption isImageOnlySuggestion];
-[_UITextOption leadingSpace];
-[_UITextOption minimumLabelWidth];
-[_UITextOption optionalTintColor];
-[_UITextOption originalText];
-[_UITextOption secureCandidateLabel];
-[_UITextOption secureCandidateSize];
-[_UITextOption selectionVibrancyView];
-[_UITextOption selectionVisibilityForState:];
-[_UITextOption setContentsLabel:];
-[_UITextOption setContentsLabelEffectView:];
-[_UITextOption setCurrentEdgeInsets:];
-[_UITextOption setInsetConstraints:];
-[_UITextOption setLightingEffectEnabled:atPosition:];
-[_UITextOption setLineView:];
-[_UITextOption setMinimumLabelWidth:];
-[_UITextOption setOptionalTintColor:];
-[_UITextOption setOriginalText:];
-[_UITextOption setSecureCandidateLabel:];
-[_UITextOption setSecureCandidateSize:];
-[_UITextOption setSelectionVibrancyView:];
-[_UITextOption setSourceCandidate:];
-[_UITextOption setSymbolImageView:];
-[_UITextOption setSymbolImageViewYConstraint:];
-[_UITextOption setTextChoice:];
-[_UITextOption showSeparator:];
-[_UITextOption symbolImageViewYConstraint];
-[_UITextOption textChoice];
-[_UITextOption textToUse];
-[_UITextOption updateContentView];
-[_UITextOption updateSourceCandidate:secureCandidateHeight:];
-[_UITextOption updateText:type:];
```
