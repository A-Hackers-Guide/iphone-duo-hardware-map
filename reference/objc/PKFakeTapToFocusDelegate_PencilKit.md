# `PKFakeTapToFocusDelegate`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionElementSource`, `PKScribbleInteractionDelegate`, `UIGestureRecognizerDelegate`
- 5 instance variables, 4 properties, 11 instance methods, 4 class methods

## Instance variables

```
@"UIView" _view;
@"_PKFakeTapToFocusInfo" _focusInfo;
@"NSUUID" _elementID;
@"UITapGestureRecognizer" _tapGesture;
@"PKFakeUITapGestureForRequirements" _gestureForRequirements;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKFakeTapToFocusDelegate _infoInProcess];
+[PKFakeTapToFocusDelegate _shouldAttachForView:];
+[PKFakeTapToFocusDelegate _tapGestureForView:];
+[PKFakeTapToFocusDelegate isPossibleForView:focusInfo:];
```

## Instance methods

```
-[PKFakeTapToFocusDelegate initWithView:];
-[PKFakeTapToFocusDelegate _scribbleInteraction:focusElement:initialFocusSelectionReferencePoint:completion:];
-[PKFakeTapToFocusDelegate _scribbleInteraction:focusWillTransformElement:];
-[PKFakeTapToFocusDelegate _scribbleInteraction:frameForElement:];
-[PKFakeTapToFocusDelegate _scribbleInteraction:shouldBeginAtLocation:];
-[PKFakeTapToFocusDelegate _scribbleInteraction:requestElementsInRect:completion:];
-[PKFakeTapToFocusDelegate _scribbleInteraction:didTargetElement:forTouches:event:];
-[PKFakeTapToFocusDelegate _scribbleInteractionIsEnabled:];
-[PKFakeTapToFocusDelegate _focusWithFocusInfo:];
-[PKFakeTapToFocusDelegate _shouldFocusBeforeObservingWithFocusInfo:];
-[PKFakeTapToFocusDelegate _waitForFirstResponderChangeWithFocusInfo:completion:];
```
