# `UIKeyboardTrackingCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"UIInputWindowController" _controllerForTrackingElements;
@"UIWindowScene" _windowScene;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastSentEndFrame;
```

## Properties

```
@property (T@"UIInputWindowController",&,N,V_controllerForTrackingElements) controllerForTrackingElements;
@property (T@"UIWindowScene",&,N,V_windowScene) windowScene;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_lastSentEndFrame) lastSentEndFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) previousEndFrame;
```

## Class methods

```
+[UIKeyboardTrackingCoordinator trackingCoordinatorForScene:];
```

## Instance methods

```
-[UIKeyboardTrackingCoordinator setWindowScene:];
-[UIKeyboardTrackingCoordinator keyboardTrackingProvider];
-[UIKeyboardTrackingCoordinator initWithWindowScene:];
-[UIKeyboardTrackingCoordinator windowScene];
-[UIKeyboardTrackingCoordinator animateTrackingElementsFromStart:toEnd:duration:forShow:];
-[UIKeyboardTrackingCoordinator controllerForTrackingElements];
-[UIKeyboardTrackingCoordinator lastSentEndFrame];
-[UIKeyboardTrackingCoordinator moveKeyboardTrackingElementsFromStartFrame:endFrame:duration:isStart:forShow:];
-[UIKeyboardTrackingCoordinator notificationInfoForStartFrame:endFrame:animationDuration:];
-[UIKeyboardTrackingCoordinator previousEndFrame];
-[UIKeyboardTrackingCoordinator setControllerForTrackingElements:];
-[UIKeyboardTrackingCoordinator setLastSentEndFrame:];
```
