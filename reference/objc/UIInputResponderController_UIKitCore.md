# `UIInputResponderController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 17 instance methods, 4 class methods

## Instance variables

```
B _isOnScreen;
B _automaticAppearanceEnabled;
B _shouldSuppressInputAssistantUpdates;
@"UIWindowScene" _scene;
@"UIResponder" _responder;
```

## Properties

```
@property (T@"UIWindowScene",R,N,V_scene) scene;
@property (T@"UIResponder",R,N,V_responder) responder;
@property (TB,R,N,V_isOnScreen) isOnScreen;
@property (TB,N,V_automaticAppearanceEnabled) automaticAppearanceEnabled;
@property (TB,N,V_shouldSuppressInputAssistantUpdates) shouldSuppressInputAssistantUpdates;
```

## Class methods

```
+[UIInputResponderController interfaceOrientation];
+[UIInputResponderController setInterfaceOrientation:];
+[UIInputResponderController performOnControllers:];
+[UIInputResponderController activeInputResponderController];
```

## Instance methods

```
-[UIInputResponderController _beginDisablingAnimations];
-[UIInputResponderController automaticAppearanceEnabled];
-[UIInputResponderController _endDisablingAnimations];
-[UIInputResponderController setAutomaticAppearanceEnabled:];
-[UIInputResponderController verticalOverlapForView:usingKeyboardInfo:];
-[UIInputResponderController isOnScreen];
-[UIInputResponderController responder];
-[UIInputResponderController setShouldSuppressInputAssistantUpdates:];
-[UIInputResponderController _textInputSessionAnalytics];
-[UIInputResponderController visibleInputViewFrameInView:];
-[UIInputResponderController visibleFrameInView:];
-[UIInputResponderController scene];
-[UIInputResponderController refreshWithLocalMinimumKeyboardHeight:];
-[UIInputResponderController shouldSuppressInputAssistantUpdates];
-[UIInputResponderController removeVisibilityObserver:];
-[UIInputResponderController addVisibilityObserver:];
-[UIInputResponderController assertNo];
```
