# `_UITextChoiceAccelerationBubble`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 35 instance variables, 35 properties, 113 instance methods, 0 class methods

## Instance variables

```
B _shouldRejectCandidate;
B _needsRTLCheck;
B _isDismissing;
@"<_UITextChoiceAccelerationDictationPromptDelegate>" _dictationPromptDelegate;
@"UILayoutGuide" _textAnchor;
@"NSLayoutConstraint" _anchorLeading;
@"NSLayoutConstraint" _anchorTop;
@"NSLayoutConstraint" _anchorWidth;
@"NSLayoutConstraint" _anchorHeight;
@"NSArray" _boundaryConstraints;
@"NSLayoutConstraint" _leadingSpacing;
@"NSArray" _belowTextConstraints;
@"NSArray" _aboveTextConstraints;
@"TIKeyboardCandidate" _candidate;
d _secureCandidateHeight;
@"_UIReplacementCandidate" _replacement;
@"NSString" _selectedChoice;
@"TIKeyboardCandidate" _selectedCandidateChoice;
@"UIView" _parentView;
q _buttonType;
@"UIVisualEffectView" _backgroundView;
@"CAShapeLayer" _backgroundMaskLayer;
@"UIStackView" _contentsView;
@"UIScrollView" _backingScrollView;
@"_UITextOption" _sideButton;
@"NSArray" _buttonConstraints;
@"UIView" _textHighlightView;
@"UIDictationGlowEffect" _dictationGlowEffect;
q _promptStyle;
@"UIColor" _optionalTintColor;
Q _labelNumber;
@"BKSHIDEventAuthenticationMessage" _authenticationMessage;
{_NSRange="location"Q"length"Q} _deltaRange;
{_NSRange="location"Q"length"Q} _originalSelectedRange;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceRect;
```

## Properties

```
@property (T@"<_UITextChoiceAccelerationDictationPromptDelegate>",W,N,V_dictationPromptDelegate) dictationPromptDelegate;
@property (T@"UILayoutGuide",&,N,V_textAnchor) textAnchor;
@property (T@"NSLayoutConstraint",&,N,V_anchorLeading) anchorLeading;
@property (T@"NSLayoutConstraint",&,N,V_anchorTop) anchorTop;
@property (T@"NSLayoutConstraint",&,N,V_anchorWidth) anchorWidth;
@property (T@"NSLayoutConstraint",&,N,V_anchorHeight) anchorHeight;
@property (T@"NSArray",&,N,V_boundaryConstraints) boundaryConstraints;
@property (T@"NSLayoutConstraint",&,N,V_leadingSpacing) leadingSpacing;
@property (T@"NSArray",&,N,V_belowTextConstraints) belowTextConstraints;
@property (T@"NSArray",&,N,V_aboveTextConstraints) aboveTextConstraints;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_referenceRect) referenceRect;
@property (T@"TIKeyboardCandidate",&,N,V_candidate) candidate;
@property (Td,N,V_secureCandidateHeight) secureCandidateHeight;
@property (TB,N,V_shouldRejectCandidate) shouldRejectCandidate;
@property (T@"_UIReplacementCandidate",&,N,V_replacement) replacement;
@property (T@"NSString",R,N,V_selectedChoice) selectedChoice;
@property (T@"TIKeyboardCandidate",R,N,V_selectedCandidateChoice) selectedCandidateChoice;
@property (T@"UIView",W,N,V_parentView) parentView;
@property (Tq,N,V_buttonType) buttonType;
@property (T@"UIVisualEffectView",&,N,V_backgroundView) backgroundView;
@property (T@"CAShapeLayer",&,N,V_backgroundMaskLayer) backgroundMaskLayer;
@property (T@"UIStackView",&,N,V_contentsView) contentsView;
@property (T@"UIScrollView",&,N,V_backingScrollView) backingScrollView;
@property (T@"_UITextOption",&,N,V_sideButton) sideButton;
@property (T@"NSArray",&,N,V_buttonConstraints) buttonConstraints;
@property (T@"UIView",&,N,V_textHighlightView) textHighlightView;
@property (T@"UIDictationGlowEffect",&,N,V_dictationGlowEffect) dictationGlowEffect;
@property (TB,N,V_needsRTLCheck) needsRTLCheck;
@property (TB,N,V_isDismissing) isDismissing;
@property (Tq,V_promptStyle) promptStyle;
@property (T@"UIColor",N,V_optionalTintColor) optionalTintColor;
@property (TQ,N,V_labelNumber) labelNumber;
@property (T{_NSRange=QQ},N,V_deltaRange) deltaRange;
@property (T{_NSRange=QQ},N,V_originalSelectedRange) originalSelectedRange;
@property (T@"BKSHIDEventAuthenticationMessage",&,N,V_authenticationMessage) authenticationMessage;
```

## Instance methods

```
-[_UITextChoiceAccelerationBubble buttonType];
-[_UITextChoiceAccelerationBubble parentView];
-[_UITextChoiceAccelerationBubble authenticationMessage];
-[_UITextChoiceAccelerationBubble setParentView:];
-[_UITextChoiceAccelerationBubble inputModeDidChange:];
-[_UITextChoiceAccelerationBubble init];
-[_UITextChoiceAccelerationBubble endTrackingWithTouch:withEvent:];
-[_UITextChoiceAccelerationBubble continueTrackingWithTouch:withEvent:];
-[_UITextChoiceAccelerationBubble textHighlightView];
-[_UITextChoiceAccelerationBubble dealloc];
-[_UITextChoiceAccelerationBubble candidate];
-[_UITextChoiceAccelerationBubble reset];
-[_UITextChoiceAccelerationBubble layoutSubviews];
-[_UITextChoiceAccelerationBubble hitTest:withEvent:];
-[_UITextChoiceAccelerationBubble setAuthenticationMessage:];
-[_UITextChoiceAccelerationBubble setTextHighlightView:];
-[_UITextChoiceAccelerationBubble beginTrackingWithTouch:withEvent:];
-[_UITextChoiceAccelerationBubble setButtonConstraints:];
-[_UITextChoiceAccelerationBubble isDismissing];
-[_UITextChoiceAccelerationBubble setCandidate:];
-[_UITextChoiceAccelerationBubble setButtonType:];
-[_UITextChoiceAccelerationBubble removeFromSuperview];
-[_UITextChoiceAccelerationBubble backgroundView];
-[_UITextChoiceAccelerationBubble buttonConstraints];
-[_UITextChoiceAccelerationBubble backgroundImageView];
-[_UITextChoiceAccelerationBubble pointInside:withEvent:];
-[_UITextChoiceAccelerationBubble setPromptStyle:];
-[_UITextChoiceAccelerationBubble initWithFrame:];
-[_UITextChoiceAccelerationBubble textEffectsVisibilityLevel];
-[_UITextChoiceAccelerationBubble setBackgroundView:];
-[_UITextChoiceAccelerationBubble setLabelNumber:];
-[_UITextChoiceAccelerationBubble setReplacement:];
-[_UITextChoiceAccelerationBubble removeAnimated:];
-[_UITextChoiceAccelerationBubble setAnchorWidth:];
-[_UITextChoiceAccelerationBubble aboveTextConstraints];
-[_UITextChoiceAccelerationBubble anchorHeight];
-[_UITextChoiceAccelerationBubble anchorLeading];
-[_UITextChoiceAccelerationBubble anchorToTextIfNeeded];
-[_UITextChoiceAccelerationBubble anchorTop];
-[_UITextChoiceAccelerationBubble anchorWidth];
-[_UITextChoiceAccelerationBubble backgroundMaskLayer];
-[_UITextChoiceAccelerationBubble backingScrollView];
-[_UITextChoiceAccelerationBubble belowTextConstraints];
-[_UITextChoiceAccelerationBubble boundaryConstraints];
-[_UITextChoiceAccelerationBubble bubblePathInRect:];
-[_UITextChoiceAccelerationBubble cancelLightingEffect];
-[_UITextChoiceAccelerationBubble contentsView];
-[_UITextChoiceAccelerationBubble deltaRange];
-[_UITextChoiceAccelerationBubble dictationGlowEffect];
-[_UITextChoiceAccelerationBubble dictationHighlightViewForPoint:withEvent:];
-[_UITextChoiceAccelerationBubble dictationPromptDelegate];
-[_UITextChoiceAccelerationBubble dismissWithCancel];
-[_UITextChoiceAccelerationBubble dismissWithCandidate:];
-[_UITextChoiceAccelerationBubble dismissWithRevert:];
-[_UITextChoiceAccelerationBubble dismissWithText:];
-[_UITextChoiceAccelerationBubble hideForNow];
-[_UITextChoiceAccelerationBubble labelNumber];
-[_UITextChoiceAccelerationBubble leadingSpacing];
-[_UITextChoiceAccelerationBubble needsRTLCheck];
-[_UITextChoiceAccelerationBubble optionForPoint:withEvent:];
-[_UITextChoiceAccelerationBubble optionalTintColor];
-[_UITextChoiceAccelerationBubble originalSelectedRange];
-[_UITextChoiceAccelerationBubble promptStyle];
-[_UITextChoiceAccelerationBubble promptWillCollideWithKeyboard:];
-[_UITextChoiceAccelerationBubble referenceRect];
-[_UITextChoiceAccelerationBubble removeAnimated:withDuration:];
-[_UITextChoiceAccelerationBubble replacement];
-[_UITextChoiceAccelerationBubble secureCandidateHeight];
-[_UITextChoiceAccelerationBubble selectedCandidateChoice];
-[_UITextChoiceAccelerationBubble selectedChoice];
-[_UITextChoiceAccelerationBubble setAboveTextConstraints:];
-[_UITextChoiceAccelerationBubble setAnchorHeight:];
-[_UITextChoiceAccelerationBubble setAnchorLeading:];
-[_UITextChoiceAccelerationBubble setAnchorTop:];
-[_UITextChoiceAccelerationBubble setBackgroundMaskLayer:];
-[_UITextChoiceAccelerationBubble setBackingScrollView:];
-[_UITextChoiceAccelerationBubble setBelowTextConstraints:];
-[_UITextChoiceAccelerationBubble setBoundaryConstraints:];
-[_UITextChoiceAccelerationBubble setContentsView:];
-[_UITextChoiceAccelerationBubble setDeltaRange:];
-[_UITextChoiceAccelerationBubble setDictationGlowEffect:];
-[_UITextChoiceAccelerationBubble setDictationPromptDelegate:];
-[_UITextChoiceAccelerationBubble setIsDismissing:];
-[_UITextChoiceAccelerationBubble setLeadingSpacing:];
-[_UITextChoiceAccelerationBubble setNeedsRTLCheck:];
-[_UITextChoiceAccelerationBubble setOptionalTintColor:];
-[_UITextChoiceAccelerationBubble setOriginalSelectedRange:];
-[_UITextChoiceAccelerationBubble setReferenceRect:];
-[_UITextChoiceAccelerationBubble setSecureCandidateHeight:];
-[_UITextChoiceAccelerationBubble setShouldRejectCandidate:];
-[_UITextChoiceAccelerationBubble setSideButton:];
-[_UITextChoiceAccelerationBubble setTextAnchor:];
-[_UITextChoiceAccelerationBubble shouldRejectCandidate];
-[_UITextChoiceAccelerationBubble showChoices:];
-[_UITextChoiceAccelerationBubble showTextHighlightView:];
-[_UITextChoiceAccelerationBubble showingAutocorrectHighlight];
-[_UITextChoiceAccelerationBubble sideButton];
-[_UITextChoiceAccelerationBubble squaredOffBubblePathInRect:];
-[_UITextChoiceAccelerationBubble squaredPathInRect:];
-[_UITextChoiceAccelerationBubble textAnchor];
-[_UITextChoiceAccelerationBubble textEffectsVisibilityLevelInKeyboardWindow];
-[_UITextChoiceAccelerationBubble textOptionWithText:type:];
-[_UITextChoiceAccelerationBubble updateBubbleShapeInRect:withCornerRadius:forSquaredOffBubble:];
-[_UITextChoiceAccelerationBubble updateButtonForType:];
-[_UITextChoiceAccelerationBubble updateButtonName:placement:originalText:];
-[_UITextChoiceAccelerationBubble updateForSingleWord:textAnchorRect:inTextView:parentView:highlightColor:];
-[_UITextChoiceAccelerationBubble updateSelfWithRect:];
-[_UITextChoiceAccelerationBubble updateTextAnchorForParentView:];
-[_UITextChoiceAccelerationBubble updateTextBoxHighlightForRect:inTextView:parentView:highlightColor:];
-[_UITextChoiceAccelerationBubble updateTextHighlightViewWithColor:convertedRect:];
-[_UITextChoiceAccelerationBubble updateViewForOptions:];
-[_UITextChoiceAccelerationBubble updateWithChoices:fromParentView:referenceTextView:presentedFromRect:textHighlightColor:];
-[_UITextChoiceAccelerationBubble usingRTLInputMode];
```
