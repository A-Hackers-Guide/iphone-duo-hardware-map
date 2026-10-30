# `UIAutocorrectInlinePrompt`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 1 properties, 29 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} m_originalTypedTextRect;
@"NSString" m_typedText;
@"NSString" m_correction;
@"NSMutableArray" m_typedTextViews;
@"UIView" m_correctionView;
@"UIView" m_correctionAnimationView;
@"UIView" m_typedTextAnimationView;
@"UIView" m_correctionShadowView;
B m_fits;
B m_mouseDown;
d m_originalTypedTextRectCorrectionAmount;
I m_usageTrackingMask;
```

## Properties

```
@property (TI,N,Vm_usageTrackingMask) usageTrackingMask;
```

## Instance methods

```
-[UIAutocorrectInlinePrompt touchesEnded:withEvent:];
-[UIAutocorrectInlinePrompt usageTrackingMask];
-[UIAutocorrectInlinePrompt pointInside:forEvent:];
-[UIAutocorrectInlinePrompt touchesCancelled:withEvent:];
-[UIAutocorrectInlinePrompt dismiss];
-[UIAutocorrectInlinePrompt typedText];
-[UIAutocorrectInlinePrompt dealloc];
-[UIAutocorrectInlinePrompt touchesBegan:withEvent:];
-[UIAutocorrectInlinePrompt setUsageTrackingMask:];
-[UIAutocorrectInlinePrompt touchesMoved:withEvent:];
-[UIAutocorrectInlinePrompt gestureRecognizerShouldBegin:];
-[UIAutocorrectInlinePrompt pointInside:withEvent:];
-[UIAutocorrectInlinePrompt initWithFrame:];
-[UIAutocorrectInlinePrompt textEffectsVisibilityLevel];
-[UIAutocorrectInlinePrompt addTypedTextRect:];
-[UIAutocorrectInlinePrompt correction];
-[UIAutocorrectInlinePrompt correctionAnimationView];
-[UIAutocorrectInlinePrompt correctionFrameFromDesiredFrame:textHeight:withExtraGap:];
-[UIAutocorrectInlinePrompt correctionShadowView];
-[UIAutocorrectInlinePrompt correctionView];
-[UIAutocorrectInlinePrompt horizontallySquishedCorrectionFrame:];
-[UIAutocorrectInlinePrompt isAcceptableTextEffectsFrame:afterScrollBy:];
-[UIAutocorrectInlinePrompt prepareForAnimation:];
-[UIAutocorrectInlinePrompt removePromptSubviews];
-[UIAutocorrectInlinePrompt setCorrection:typedText:inRect:maxX:];
-[UIAutocorrectInlinePrompt shadowFrameForFrame:];
-[UIAutocorrectInlinePrompt textEffectsVisibilityLevelInKeyboardWindow];
-[UIAutocorrectInlinePrompt typedTextAnimationView];
-[UIAutocorrectInlinePrompt typedTextView];
```
