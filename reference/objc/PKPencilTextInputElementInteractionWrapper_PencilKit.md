# `PKPencilTextInputElementInteractionWrapper`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionWrapper`
- 2 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"PKPencilTextInputElementInteraction" _elementInteraction;
@"NSMutableDictionary" _knownElementsByID;
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
-[PKPencilTextInputElementInteractionWrapper interaction];
-[PKPencilTextInputElementInteractionWrapper isEnabled];
-[PKPencilTextInputElementInteractionWrapper description];
-[PKPencilTextInputElementInteractionWrapper isEqual:];
-[PKPencilTextInputElementInteractionWrapper interactionView];
-[PKPencilTextInputElementInteractionWrapper beginSuppressingPlaceholderForElement:];
-[PKPencilTextInputElementInteractionWrapper didFinishWritingInElement:];
-[PKPencilTextInputElementInteractionWrapper endSuppressingPlaceholderForElement:];
-[PKPencilTextInputElementInteractionWrapper focusElement:initialFocusSelectionReferencePoint:completion:];
-[PKPencilTextInputElementInteractionWrapper focusWillTransformElement:];
-[PKPencilTextInputElementInteractionWrapper frameForElement:];
-[PKPencilTextInputElementInteractionWrapper hitToleranceInsetsWithDefaultInsets:element:];
-[PKPencilTextInputElementInteractionWrapper isElementContainer];
-[PKPencilTextInputElementInteractionWrapper isElementFocused:];
-[PKPencilTextInputElementInteractionWrapper requestElementsInRect:completion:];
-[PKPencilTextInputElementInteractionWrapper shouldBeginAtLocation:];
-[PKPencilTextInputElementInteractionWrapper supportsIsElementFocused];
-[PKPencilTextInputElementInteractionWrapper supportsShouldBegin];
-[PKPencilTextInputElementInteractionWrapper willBeginWritingInElement:];
-[PKPencilTextInputElementInteractionWrapper initWithElementInteraction:];
```
