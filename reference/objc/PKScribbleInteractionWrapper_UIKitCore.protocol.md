# `PKScribbleInteractionWrapper` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 21 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",?,R,N) view;
@property (T@"UIView",?,R,N) interactionView;
@property (T@"<UIInteraction>",R,N) interaction;
```

## Instance methods

```
-[PKScribbleInteractionWrapper interaction];
-[PKScribbleInteractionWrapper beginSuppressingPlaceholderForElement:];
-[PKScribbleInteractionWrapper didFinishWritingInElement:];
-[PKScribbleInteractionWrapper endSuppressingPlaceholderForElement:];
-[PKScribbleInteractionWrapper focusElement:initialFocusSelectionReferencePoint:completion:];
-[PKScribbleInteractionWrapper focusWillTransformElement:];
-[PKScribbleInteractionWrapper frameForElement:];
-[PKScribbleInteractionWrapper hitToleranceInsetsWithDefaultInsets:element:];
-[PKScribbleInteractionWrapper isElementContainer];
-[PKScribbleInteractionWrapper isElementFocused:];
-[PKScribbleInteractionWrapper requestElementsInRect:completion:];
-[PKScribbleInteractionWrapper shouldBeginAtLocation:];
-[PKScribbleInteractionWrapper supportsIsElementFocused];
-[PKScribbleInteractionWrapper supportsShouldBegin];
-[PKScribbleInteractionWrapper willBeginWritingInElement:];
-[PKScribbleInteractionWrapper isEnabled];
-[PKScribbleInteractionWrapper view];
-[PKScribbleInteractionWrapper interactionView];
-[PKScribbleInteractionWrapper didTargetElement:forTouches:event:];
-[PKScribbleInteractionWrapper isEditableElement:];
-[PKScribbleInteractionWrapper shouldDisableInputAssistant];
```
