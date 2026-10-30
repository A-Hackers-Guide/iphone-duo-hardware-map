# `UIKeyboardCandidateViewConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 12 properties, 19 instance methods, 3 class methods

## Instance variables

```
B _darkKeyboard;
B _shouldAlwaysShowSortControl;
B _shouldUsePredictionViewSecureRenderTraits;
```

## Properties

```
@property (T@"UIColor",R,N) highlightedBackgroundColor;
@property (TB,N,V_darkKeyboard) darkKeyboard;
@property (TQ,R,N) rowsToExtend;
@property (TQ,R,N) maxNumberOfProactiveCandidates;
@property (TB,R,N) shouldResizeKeyboardBackdrop;
@property (TB,R,N,V_shouldAlwaysShowSortControl) shouldAlwaysShowSortControl;
@property (TB,R,N) shouldAnimateStateTransition;
@property (TB,R,N,V_shouldUsePredictionViewSecureRenderTraits) shouldUsePredictionViewSecureRenderTraits;
@property (TB,R,N) willCoverKeyboardLayout;
@property (TB,R,N) allowsPullDownGesture;
@property (T{CGSize=dd},R,N) preferredInlineFloatingViewSize;
@property (Ti,R,N) inlineFloatingViewAdjustMode;
```

## Class methods

```
+[UIKeyboardCandidateViewConfiguration lineHeightMultiplierForCurrentLanguage];
+[UIKeyboardCandidateViewConfiguration configuration];
+[UIKeyboardCandidateViewConfiguration fontSizeMultiplierForCurrentLanguage];
```

## Instance methods

```
-[UIKeyboardCandidateViewConfiguration setDarkKeyboard:];
-[UIKeyboardCandidateViewConfiguration darkKeyboard];
-[UIKeyboardCandidateViewConfiguration initialState];
-[UIKeyboardCandidateViewConfiguration preferredInlineFloatingViewSize];
-[UIKeyboardCandidateViewConfiguration candidateFontWithSize:language:];
-[UIKeyboardCandidateViewConfiguration allowsPullDownGesture];
-[UIKeyboardCandidateViewConfiguration candidateDefaultFontSize];
-[UIKeyboardCandidateViewConfiguration candidateFontWithSize:];
-[UIKeyboardCandidateViewConfiguration extendedScrolledState];
-[UIKeyboardCandidateViewConfiguration extendedState];
-[UIKeyboardCandidateViewConfiguration highlightedBackgroundColor];
-[UIKeyboardCandidateViewConfiguration inlineFloatingViewAdjustMode];
-[UIKeyboardCandidateViewConfiguration maxNumberOfProactiveCandidates];
-[UIKeyboardCandidateViewConfiguration rowsToExtend];
-[UIKeyboardCandidateViewConfiguration shouldAlwaysShowSortControl];
-[UIKeyboardCandidateViewConfiguration shouldAnimateStateTransition];
-[UIKeyboardCandidateViewConfiguration shouldResizeKeyboardBackdrop];
-[UIKeyboardCandidateViewConfiguration shouldUsePredictionViewSecureRenderTraits];
-[UIKeyboardCandidateViewConfiguration willCoverKeyboardLayout];
```
