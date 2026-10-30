# `UIScribbleInteractionWrapper`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionWrapper`
- 2 instance variables, 7 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"UIScribbleInteraction" _scribbleInteraction;
@"UIIndirectScribbleInteraction" _indirectInteraction;
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
-[UIScribbleInteractionWrapper interaction];
-[UIScribbleInteractionWrapper view];
-[UIScribbleInteractionWrapper description];
-[UIScribbleInteractionWrapper isEqual:];
-[UIScribbleInteractionWrapper suggestedStrokeColorForElement:];
-[UIScribbleInteractionWrapper beginSuppressingPlaceholderForElement:];
-[UIScribbleInteractionWrapper didFinishWritingInElement:];
-[UIScribbleInteractionWrapper endSuppressingPlaceholderForElement:];
-[UIScribbleInteractionWrapper focusElement:initialFocusSelectionReferencePoint:completion:];
-[UIScribbleInteractionWrapper focusWillTransformElement:];
-[UIScribbleInteractionWrapper frameForElement:];
-[UIScribbleInteractionWrapper hitToleranceInsetsWithDefaultInsets:element:];
-[UIScribbleInteractionWrapper initWithCustomScribbleInteraction:indirectScribbleInteraction:];
-[UIScribbleInteractionWrapper isElement:inFrontOf:];
-[UIScribbleInteractionWrapper isElementContainer];
-[UIScribbleInteractionWrapper isElementFocused:];
-[UIScribbleInteractionWrapper requestElementsInRect:completion:];
-[UIScribbleInteractionWrapper shouldBeginAtLocation:];
-[UIScribbleInteractionWrapper shouldDisableInputAssistant];
-[UIScribbleInteractionWrapper supportsIsElementFocused];
-[UIScribbleInteractionWrapper supportsIsElementInFrontOfElement];
-[UIScribbleInteractionWrapper supportsShouldBegin];
-[UIScribbleInteractionWrapper willBeginWritingInElement:];
```
