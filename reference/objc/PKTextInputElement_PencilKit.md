# `PKTextInputElement`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 1 properties, 19 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastKnownFrame;
@"<UICoordinateSpace>" _coordinateSpace;
B __requestingPlaceholderSuppression;
B __waitingForMatchingDidFinishWriting;
B _legacyHasBeenFocusedWithinContainer;
q __elementType;
@"UIView" _elementTextInputView;
@"<PKScribbleInteractionWrapper>" __viewScribbleInteraction;
@"<PKScribbleInteractionWrapper>" __containerInteraction;
q __orderInContainer;
@"PKTextInputWritingSession" __writingSession;
@"<UITextInput>" _textInput;
@"NSNumber" _recognitionIdentifier;
@"<NSObject><NSCopying>" _containerElementIdentifier;
```

## Properties

```
@property (T{_NSRange=QQ},R,N) activeAffectedRange;
```

## Instance methods

```
-[PKTextInputElement selectionHighlightColor];
-[PKTextInputElement dealloc];
-[PKTextInputElement showSelectionCommands];
-[PKTextInputElement description];
-[PKTextInputElement activePreviewRange];
-[PKTextInputElement _beginSuppressingFieldPlaceholder];
-[PKTextInputElement _finishSuppressingFieldPlaceholderIfNeeded];
-[PKTextInputElement activeAffectedRange];
-[PKTextInputElement beginSuppressingPlaceholderIfNecessary];
-[PKTextInputElement clearActivePreview];
-[PKTextInputElement didEndWriting];
-[PKTextInputElement didInsertText];
-[PKTextInputElement didMoveToWritingSession:];
-[PKTextInputElement endSuppressingPlaceholderIfNecessary];
-[PKTextInputElement notifyTextInputTextDidChange];
-[PKTextInputElement notifyTextInputTextWillChange];
-[PKTextInputElement selectionClipRectInCoordinateSpace:];
-[PKTextInputElement swapWritingStateWithElement:];
-[PKTextInputElement willBeginWriting];
```
