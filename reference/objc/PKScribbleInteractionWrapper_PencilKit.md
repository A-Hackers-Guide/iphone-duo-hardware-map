# `PKScribbleInteractionWrapper`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionWrapper`
- 1 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"PKScribbleInteraction" _interaction;
```

## Properties

```
@property (T@"UIView",?,R,N) view;
@property (T@"UIView",?,R,N) interactionView;
@property (T@"<UIInteraction>",R,N) interaction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKScribbleInteractionWrapper interaction];
-[PKScribbleInteractionWrapper isEnabled];
-[PKScribbleInteractionWrapper description];
-[PKScribbleInteractionWrapper isEqual:];
-[PKScribbleInteractionWrapper interactionView];
-[PKScribbleInteractionWrapper beginSuppressingPlaceholderForElement:];
-[PKScribbleInteractionWrapper didFinishWritingInElement:];
-[PKScribbleInteractionWrapper didTargetElement:forTouches:event:];
-[PKScribbleInteractionWrapper endSuppressingPlaceholderForElement:];
-[PKScribbleInteractionWrapper focusElement:initialFocusSelectionReferencePoint:completion:];
-[PKScribbleInteractionWrapper focusWillTransformElement:];
-[PKScribbleInteractionWrapper frameForElement:];
-[PKScribbleInteractionWrapper hitToleranceInsetsWithDefaultInsets:element:];
-[PKScribbleInteractionWrapper isEditableElement:];
-[PKScribbleInteractionWrapper isElementContainer];
-[PKScribbleInteractionWrapper isElementFocused:];
-[PKScribbleInteractionWrapper requestElementsInRect:completion:];
-[PKScribbleInteractionWrapper shouldBeginAtLocation:];
-[PKScribbleInteractionWrapper shouldDisableInputAssistant];
-[PKScribbleInteractionWrapper supportsIsElementFocused];
-[PKScribbleInteractionWrapper supportsShouldBegin];
-[PKScribbleInteractionWrapper willBeginWritingInElement:];
```
