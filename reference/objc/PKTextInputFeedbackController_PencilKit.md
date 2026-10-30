# `PKTextInputFeedbackController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _showingCustomFeedback;
@"<PKTextInputFeedbackControllerDelegate>" _delegate;
@"PKTextInputElementContent" _referenceElementContent;
q _feedbackType;
@"PKTextInputTextPlaceholder" _placeholder;
@"PKTextInputGestureFeedbackView" __feedbackView;
{_NSRange="location"Q"length"Q} _referenceTextRange;
```

## Properties

```
@property (T@"PKTextInputElementContent",&,N,V_referenceElementContent) referenceElementContent;
@property (T{_NSRange=QQ},N,V_referenceTextRange) referenceTextRange;
@property (T@"PKTextInputTextPlaceholder",&,N,V_placeholder) placeholder;
@property (Tq,N,V_feedbackType) feedbackType;
@property (TB,N,S_setShowingCustomFeedback:,V_showingCustomFeedback) showingCustomFeedback;
@property (T@"PKTextInputGestureFeedbackView",&,N,V__feedbackView) _feedbackView;
@property (T@"<PKTextInputFeedbackControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"PKTextInputTextPlaceholder",R,N) reserveSpacePlaceholder;
```

## Instance methods

```
-[PKTextInputFeedbackController placeholder];
-[PKTextInputFeedbackController setPlaceholder:];
-[PKTextInputFeedbackController feedbackType];
-[PKTextInputFeedbackController init];
-[PKTextInputFeedbackController setFeedbackType:];
-[PKTextInputFeedbackController dealloc];
-[PKTextInputFeedbackController setDelegate:];
-[PKTextInputFeedbackController delegate];
-[PKTextInputFeedbackController _feedbackView];
-[PKTextInputFeedbackController _placeholderChanged:];
-[PKTextInputFeedbackController _setShowingCustomFeedback:];
-[PKTextInputFeedbackController _shouldShowCustomFeedback];
-[PKTextInputFeedbackController _updateFeedbackState];
-[PKTextInputFeedbackController _updateFeedbackView];
-[PKTextInputFeedbackController beginDisplayForReserveSpacePlaceholder:];
-[PKTextInputFeedbackController cancelShowingReserveSpaceIntro];
-[PKTextInputFeedbackController endDisplayForReserveSpacePlaceholder:];
-[PKTextInputFeedbackController referenceElementContent];
-[PKTextInputFeedbackController referenceTextRange];
-[PKTextInputFeedbackController reserveSpacePlaceholder];
-[PKTextInputFeedbackController setReferenceElementContent:];
-[PKTextInputFeedbackController setReferenceElementContent:referenceRange:feedbackType:];
-[PKTextInputFeedbackController setReferenceTextRange:];
-[PKTextInputFeedbackController set_feedbackView:];
-[PKTextInputFeedbackController showingCustomFeedback];
```
