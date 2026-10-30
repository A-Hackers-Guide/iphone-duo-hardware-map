# `UIFlickingAssistantViewSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardMotionSupport`
- Protocols: `_UIGeometryChangeObserver`
- 10 instance variables, 4 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"UIPanGestureRecognizer" _panRecognizer;
q _position;
q _lastMinimizedPosition;
q _visualState;
{CGPoint="x"d"y"d} _initalTouchPoint;
B _shouldNotifyCompletion;
B _isHandlingGeometryChange;
B _isCompact;
@"UIInputViewSetPlacement" _remotePlacement;
q _draggingState;
```

## Properties

```
@property (Tq,N,V_draggingState) draggingState;
@property (TB,N,SsetCompact:,V_isCompact) isCompact;
@property (T@"UIInputViewSetPlacement",&,N,V_remotePlacement) remotePlacement;
@property (TB,R,N) handlingFlickGesture;
```

## Instance methods

```
-[UIFlickingAssistantViewSupport setCompact:];
-[UIFlickingAssistantViewSupport isCompact];
-[UIFlickingAssistantViewSupport assistantPosition];
-[UIFlickingAssistantViewSupport draggingState];
-[UIFlickingAssistantViewSupport setRemotePlacement:];
-[UIFlickingAssistantViewSupport assistantFrame];
-[UIFlickingAssistantViewSupport observeValueForKeyPath:ofObject:change:context:];
-[UIFlickingAssistantViewSupport setDraggingState:];
-[UIFlickingAssistantViewSupport updateTransition:animated:];
-[UIFlickingAssistantViewSupport didUpdateTransition];
-[UIFlickingAssistantViewSupport remotePlacement];
-[UIFlickingAssistantViewSupport rectEdgeFromPosition:];
-[UIFlickingAssistantViewSupport _connectController:];
-[UIFlickingAssistantViewSupport _geometryChanged:forAncestor:];
-[UIFlickingAssistantViewSupport setPositionAndVisualStateByPersistentLocation:minimize:];
-[UIFlickingAssistantViewSupport keyboardOriginFromAssistantViewPosition:];
-[UIFlickingAssistantViewSupport _initalizePosition];
-[UIFlickingAssistantViewSupport projectedLandingPointForGestureRecognizerEnd:];
-[UIFlickingAssistantViewSupport _disconnectingController:];
-[UIFlickingAssistantViewSupport _updateKeyboardLayoutGuideForCurrentAssistantFrame];
-[UIFlickingAssistantViewSupport transitToDraggingVisualState:withTouchLocation:];
-[UIFlickingAssistantViewSupport _updatedController];
-[UIFlickingAssistantViewSupport panGestureHandler:];
-[UIFlickingAssistantViewSupport _updateTrackingCoordinatorForFloatingAssistant];
-[UIFlickingAssistantViewSupport barOriginFromTouchPoint:];
-[UIFlickingAssistantViewSupport isInputAssistantItemHidden];
-[UIFlickingAssistantViewSupport calculatedAssistantFrame];
-[UIFlickingAssistantViewSupport isRTL];
-[UIFlickingAssistantViewSupport handlingFlickGesture];
-[UIFlickingAssistantViewSupport _updateKeyboardLayoutGuideForAssistantFrame:];
```
