# `PKTextInputHoverController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKHoverControllerDelegate`
- 23 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
B __shouldHoverFlashElements;
B __shouldMakeCursorStrong;
B __lineBreakWaitingForElement;
B __lineBreakIsAtValidLocation;
B __iBeamWaitingForElement;
@"<PKTextInputHoverControllerDelegate>" _delegate;
@"PKHoverController" __hoverController;
@"CAShapeLayer" __hoverDebugLayer;
@"PKTextInputElement" __hoverElementToFocus;
@"UIView" __hoverFlashElementsView;
@"NSArray" __hoverFlashElements;
@"UIView" __currentHoverFlashElementView;
d __lineBreakTimestamp;
q __lineBreakNumLines;
d __lineBreakIsAtValidLocationTimestamp;
@"PKTextInputElement" __lineBreakElement;
@"PKTextInputElement" __hidePlaceholderElement;
@"PKTextInputElement" __ibeamElement;
@"PKTextInputElementContent" __ibeamElementContent;
@"CALayer" __ibeamLayer;
d __ibeamLastTimestamp;
{CGPoint="x"d"y"d} __lineBreakPosition;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __ibeamFrame;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputHoverController hoverController:didBegin:];
-[PKTextInputHoverController hoverController:didUpdate:];
-[PKTextInputHoverController hoverController:holdGestureMeanInputPoint:latestInputPoint:];
-[PKTextInputHoverController hoverControllerDidEnd:fromTouch:];
-[PKTextInputHoverController hoverControllerDidLift:];
-[PKTextInputHoverController hoverControllerHoldGestureEnded:];
-[PKTextInputHoverController unhidePlaceholderElementIfNecessary];
```
