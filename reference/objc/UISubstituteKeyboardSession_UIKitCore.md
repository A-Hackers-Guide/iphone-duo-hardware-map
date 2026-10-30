# `UISubstituteKeyboardSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIAdaptivePresentationControllerDelegate`, `UIDimmingViewDelegate`, `UIViewControllerTransitioningDelegate`
- 6 instance variables, 2 properties, 14 instance methods, 2 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 viewController;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 presentationController;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 animationController;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 traitChangeObservation;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 wasShowingInputOrAssistantViews;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 responder;
```

## Properties

```
@property (TB,N,R) isPresented;
@property (TB,N,R) isPresenting;
```

## Class methods

```
+[UISubstituteKeyboardSession sharedSession];
+[UISubstituteKeyboardSession activeSession];
```

## Instance methods

```
-[UISubstituteKeyboardSession hide];
-[UISubstituteKeyboardSession isPresented];
-[UISubstituteKeyboardSession animationControllerForDismissedController:];
-[UISubstituteKeyboardSession dimmingViewWasTapped:];
-[UISubstituteKeyboardSession presentationControllerDidDismiss:];
-[UISubstituteKeyboardSession animationControllerForPresentedController:presentingController:sourceController:];
-[UISubstituteKeyboardSession presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[UISubstituteKeyboardSession init];
-[UISubstituteKeyboardSession updateUserInterfaceStyle];
-[UISubstituteKeyboardSession firstResponderDidChange:];
-[UISubstituteKeyboardSession cancel];
-[UISubstituteKeyboardSession isPresenting];
-[UISubstituteKeyboardSession hideForResponder:];
-[UISubstituteKeyboardSession showForResponder:sender:];
```
