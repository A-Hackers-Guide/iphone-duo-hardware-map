# `_UISelectionInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
{?="delegateImplementsDidBeginHinting"b1"delegateImplementsDidCancelHinting"b1"delegateImplementsShouldBegin"b1} _flags;
B _enabled;
B _simulatePressesCallbacksForLegacyBehavior;
@"UITapGestureRecognizer" _selectGestureRecognizer;
@"_UIFocusSelectObserverGestureRecognizer" _selectHighlightRecognizer;
@"<_UISelectionInteractionDelegate>" _delegate;
@"UIView" _view;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"UITapGestureRecognizer",R,N,V_selectGestureRecognizer) selectGestureRecognizer;
@property (T@"_UIFocusSelectObserverGestureRecognizer",R,N,V_selectHighlightRecognizer) selectHighlightRecognizer;
@property (TB,N,V_simulatePressesCallbacksForLegacyBehavior) simulatePressesCallbacksForLegacyBehavior;
@property (T@"<_UISelectionInteractionDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,R,N,GisHinting) hinting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISelectionInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UISelectionInteraction init];
-[_UISelectionInteraction selectHighlightRecognizer];
-[_UISelectionInteraction setView:];
-[_UISelectionInteraction simulatePressesCallbacksForLegacyBehavior];
-[_UISelectionInteraction isEnabled];
-[_UISelectionInteraction view];
-[_UISelectionInteraction setDelegate:];
-[_UISelectionInteraction gestureRecognizerShouldBegin:];
-[_UISelectionInteraction setEnabled:];
-[_UISelectionInteraction willMoveToView:];
-[_UISelectionInteraction selectGestureRecognizer];
-[_UISelectionInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UISelectionInteraction delegate];
-[_UISelectionInteraction selectGestureHandler:];
-[_UISelectionInteraction didMoveToView:];
-[_UISelectionInteraction highlightGestureHandler:];
-[_UISelectionInteraction isHinting];
-[_UISelectionInteraction setSimulatePressesCallbacksForLegacyBehavior:];
```
