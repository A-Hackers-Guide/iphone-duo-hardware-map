# `UIWebRotatingNodePopover`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPopoverControllerDelegate`
- 5 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isRotating;
@"DOMNode" _node;
{CGPoint="x"d"y"d} _presentationPoint;
@"UIPopoverController" _popoverController;
@"<UIWebRotatingNodePopoverDelegate>" _dismissDelegate;
```

## Properties

```
@property (T@"DOMNode",&,N,V_node) node;
@property (T{CGPoint=dd},N,V_presentationPoint) presentationPoint;
@property (T@"UIPopoverController",&,N,V_popoverController) popoverController;
@property (T@"<UIWebRotatingNodePopoverDelegate>",N,V_dismissDelegate) dismissDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebRotatingNodePopover dealloc];
-[UIWebRotatingNodePopover setNode:];
-[UIWebRotatingNodePopover node];
-[UIWebRotatingNodePopover dismissDelegate];
-[UIWebRotatingNodePopover didRotate:];
-[UIWebRotatingNodePopover dismissPopoverAnimated:];
-[UIWebRotatingNodePopover initWithDOMNode:];
-[UIWebRotatingNodePopover popoverArrowDirections];
-[UIWebRotatingNodePopover popoverController];
-[UIWebRotatingNodePopover popoverControllerDidDismissPopover:];
-[UIWebRotatingNodePopover presentPopoverAnimated:];
-[UIWebRotatingNodePopover presentationPoint];
-[UIWebRotatingNodePopover setDismissDelegate:];
-[UIWebRotatingNodePopover setPopoverController:];
-[UIWebRotatingNodePopover setPresentationPoint:];
-[UIWebRotatingNodePopover willRotate:];
```
