# `UIKBResizingKeyplaneCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIKBResizingKeyplanePanGestureRecognizerDelegate`
- 9 instance variables, 8 properties, 18 instance methods, 1 class methods

## Instance variables

```
d _prevResizingOffset;
d _resizingOffset;
d _foregroundOpacity;
@"_UIDynamicAnimationGroup" _resizingAnimationGroup;
@"UIView" _grabber;
@"UIColor" _grabberColor;
B _isResizing;
@"<UIKBResizingKeyplaneCoordinatorCoordinatorDelegate>" _delegate;
@"UIKBResizingKeyplanePanGestureRecognizer" _gestureRecognizer;
```

## Properties

```
@property (T@"UIKBResizingKeyplanePanGestureRecognizer",R,N,V_gestureRecognizer) gestureRecognizer;
@property (T@"<UIKBResizingKeyplaneCoordinatorCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (Td,R,N,V_resizingOffset) resizingOffset;
@property (TB,R,N) isResizing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBResizingKeyplaneCoordinator savedResizingOffset];
```

## Instance methods

```
-[UIKBResizingKeyplaneCoordinator stopResizing];
-[UIKBResizingKeyplaneCoordinator dimKeys:];
-[UIKBResizingKeyplaneCoordinator setRenderConfig:];
-[UIKBResizingKeyplaneCoordinator gestureRecognizer];
-[UIKBResizingKeyplaneCoordinator init];
-[UIKBResizingKeyplaneCoordinator handleResizeGesture:];
-[UIKBResizingKeyplaneCoordinator isResizing];
-[UIKBResizingKeyplaneCoordinator setDelegate:];
-[UIKBResizingKeyplaneCoordinator saveResizingStopIndex:];
-[UIKBResizingKeyplaneCoordinator gestureRecognizerShouldBegin:];
-[UIKBResizingKeyplaneCoordinator delegate];
-[UIKBResizingKeyplaneCoordinator updateGestureRecognizers];
-[UIKBResizingKeyplaneCoordinator resizeKeyplaneWithOffset:andRedraw:];
-[UIKBResizingKeyplaneCoordinator shouldStartResizeForTranslationY:];
-[UIKBResizingKeyplaneCoordinator updateGrabber];
-[UIKBResizingKeyplaneCoordinator resizingOffset];
-[UIKBResizingKeyplaneCoordinator reloadResizingOffset];
-[UIKBResizingKeyplaneCoordinator uninstallGestureRecognizers];
```
