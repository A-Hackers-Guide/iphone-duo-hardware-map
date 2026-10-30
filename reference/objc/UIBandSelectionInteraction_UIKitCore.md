# `UIBandSelectionInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `UIPointerInteractionDelegate`, `UIGestureRecognizerDelegate`, `UIInteraction`
- 14 instance variables, 17 properties, 40 instance methods, 0 class methods

## Instance variables

```
Q _internalState;
{CGPoint="x"d"y"d} _initialLocation;
B _hidesVisuals;
B _enabled;
B __debugUIEnabled;
@"UIView" _view;
q _state;
q _initialModifierFlags;
@? _shouldBeginHandler;
@? _selectionHandler;
@"UIHoverGestureRecognizer" _hoverGR;
@"UILongPressGestureRecognizer" _pressGR;
@"<_UISelectionBandVisualProviding>" _visualProvider;
@? __bandVisibilityHandler;
```

## Properties

```
@property (T@?,C,N,V_selectionHandler) selectionHandler;
@property (T@"UIHoverGestureRecognizer",&,N,V_hoverGR) hoverGR;
@property (T@"UILongPressGestureRecognizer",&,N,V_pressGR) pressGR;
@property (T@"<_UISelectionBandVisualProviding>",&,N,V_visualProvider) visualProvider;
@property (TB,N,V__debugUIEnabled) _debugUIEnabled;
@property (T@?,C,N,S_setBandVisibilityHandler:,V__bandVisibilityHandler) _bandVisibilityHandler;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Tq,R,N,V_state) state;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) selectionRect;
@property (Tq,R,N,V_initialModifierFlags) initialModifierFlags;
@property (T@?,C,N,V_shouldBeginHandler) shouldBeginHandler;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIBandSelectionInteraction selectionRect];
-[UIBandSelectionInteraction setSelectionHandler:];
-[UIBandSelectionInteraction visualProvider];
-[UIBandSelectionInteraction _updateInteractionEnabled];
-[UIBandSelectionInteraction _isSelecting];
-[UIBandSelectionInteraction _debugUIEnabled];
-[UIBandSelectionInteraction _locationInView:];
-[UIBandSelectionInteraction gestureRecognizer:shouldReceiveTouch:];
-[UIBandSelectionInteraction _handleDidMove];
-[UIBandSelectionInteraction selectionHandler];
-[UIBandSelectionInteraction _handleDidEndFromState:];
-[UIBandSelectionInteraction _handlePressGesture:];
-[UIBandSelectionInteraction dealloc];
-[UIBandSelectionInteraction _updateDebugUIWithGesture:];
-[UIBandSelectionInteraction _handleBeginEvent];
-[UIBandSelectionInteraction _callHandlerWithState:];
-[UIBandSelectionInteraction set_debugUIEnabled:];
-[UIBandSelectionInteraction pressGR];
-[UIBandSelectionInteraction _selectionRectWithLocation:];
-[UIBandSelectionInteraction hoverGR];
-[UIBandSelectionInteraction initialModifierFlags];
-[UIBandSelectionInteraction _bandVisibilityHandler];
-[UIBandSelectionInteraction isEnabled];
-[UIBandSelectionInteraction view];
-[UIBandSelectionInteraction _gestureRecognizer:canBePreventedByGestureRecognizer:];
-[UIBandSelectionInteraction setPressGR:];
-[UIBandSelectionInteraction setEnabled:];
-[UIBandSelectionInteraction willMoveToView:];
-[UIBandSelectionInteraction _setBandVisibilityHandler:];
-[UIBandSelectionInteraction _gestureRecognizer:canPreventGestureRecognizer:];
-[UIBandSelectionInteraction setHoverGR:];
-[UIBandSelectionInteraction _handleHoverGesture:];
-[UIBandSelectionInteraction setVisualProvider:];
-[UIBandSelectionInteraction shouldBeginHandler];
-[UIBandSelectionInteraction setShouldBeginHandler:];
-[UIBandSelectionInteraction _viewTraitCollectionDidChange:];
-[UIBandSelectionInteraction didMoveToView:];
-[UIBandSelectionInteraction initWithSelectionHandler:];
-[UIBandSelectionInteraction state];
-[UIBandSelectionInteraction _handleDidBegin];
```
