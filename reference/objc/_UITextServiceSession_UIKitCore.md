# `_UITextServiceSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPopoverPresentationControllerDelegate`
- 7 instance variables, 5 properties, 10 instance methods, 9 class methods

## Instance variables

```
q _type;
@"UIViewController" _modalViewController;
@"UIView" _contextView;
@"UIResponder" _pinnedResponder;
@"UIKeyboardSceneDelegate" _keyboardSceneDelegate;
B _dismissed;
@? _dismissedHandler;
```

## Properties

```
@property (T@?,C,N,V_dismissedHandler) dismissedHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UITextServiceSession showServiceForType:withContext:];
+[_UITextServiceSession _canShowTextServiceForType:];
+[_UITextServiceSession _canShowTextServices];
+[_UITextServiceSession availableTextServices];
+[_UITextServiceSession shouldPresentServiceInSameWindowAsView:];
+[_UITextServiceSession showServiceForText:selectedTextRange:type:fromRect:inView:];
+[_UITextServiceSession showServiceForText:type:fromRect:inView:];
+[_UITextServiceSession textServiceIsDisplaying];
+[_UITextServiceSession textServiceSessionForType:];
```

## Instance methods

```
-[_UITextServiceSession presentationControllerDidDismiss:];
-[_UITextServiceSession init];
-[_UITextServiceSession initWithType:];
-[_UITextServiceSession type];
-[_UITextServiceSession _endSession];
-[_UITextServiceSession dismissTextServiceAnimated:];
-[_UITextServiceSession dismissedHandler];
-[_UITextServiceSession isDisplaying];
-[_UITextServiceSession sessionDidDismiss];
-[_UITextServiceSession setDismissedHandler:];
```
