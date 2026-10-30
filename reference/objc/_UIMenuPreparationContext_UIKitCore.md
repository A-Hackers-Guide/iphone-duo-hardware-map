# `_UIMenuPreparationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _supportsCustomViewMenuElements;
B _useSenderAsResponderSender;
B _supportsHeaderView;
B _tracksSelection;
@ _preparer;
@"UIResponder" _firstResponderTarget;
@"<UIDeferredMenuElementDelegate>" _deferredElementDelegate;
@ _sender;
@? _shouldTrackVisibleSelection;
@? _elementSizeSolver;
```

## Properties

```
@property (T@,R,W,N,V_preparer) preparer;
@property (T@"UIResponder",R,W,N,V_firstResponderTarget) firstResponderTarget;
@property (T@"<UIDeferredMenuElementDelegate>",W,N,V_deferredElementDelegate) deferredElementDelegate;
@property (T@,W,N,V_sender) sender;
@property (TB,N,V_supportsCustomViewMenuElements) supportsCustomViewMenuElements;
@property (TB,N,V_useSenderAsResponderSender) useSenderAsResponderSender;
@property (TB,N,V_supportsHeaderView) supportsHeaderView;
@property (TB,N,V_tracksSelection) tracksSelection;
@property (T@?,C,N,V_shouldTrackVisibleSelection) shouldTrackVisibleSelection;
@property (T@?,C,N,V_elementSizeSolver) elementSizeSolver;
```

## Class methods

```
+[_UIMenuPreparationContext contextWithPreparer:firstResponderTarget:];
```

## Instance methods

```
-[_UIMenuPreparationContext preparer];
-[_UIMenuPreparationContext supportsCustomViewMenuElements];
-[_UIMenuPreparationContext firstResponderTarget];
-[_UIMenuPreparationContext setSupportsHeaderView:];
-[_UIMenuPreparationContext supportsHeaderView];
-[_UIMenuPreparationContext elementSizeSolver];
-[_UIMenuPreparationContext useSenderAsResponderSender];
-[_UIMenuPreparationContext setShouldTrackVisibleSelection:];
-[_UIMenuPreparationContext sender];
-[_UIMenuPreparationContext shouldTrackSelectionForVisibleIndex:elementSize:];
-[_UIMenuPreparationContext setTracksSelection:];
-[_UIMenuPreparationContext setUseSenderAsResponderSender:];
-[_UIMenuPreparationContext tracksSelection];
-[_UIMenuPreparationContext setSender:];
-[_UIMenuPreparationContext copyWithZone:];
-[_UIMenuPreparationContext setDeferredElementDelegate:];
-[_UIMenuPreparationContext shouldTrackVisibleSelection];
-[_UIMenuPreparationContext deferredElementDelegate];
-[_UIMenuPreparationContext setElementSizeSolver:];
-[_UIMenuPreparationContext setSupportsCustomViewMenuElements:];
```
