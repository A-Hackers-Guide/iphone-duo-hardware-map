# `_UICampoLightweightDebugHighlighter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"_UICampoLightweightDebugOverlayView" _overlayView;
@"_UICampoLightweightDebugPickerWindow" _pickerWindow;
@"UIView" _outlinedContainerView;
@"UIView" _outlinedPresentedView;
@"UIView" _outlinedPopoverView;
@"UIPopoverPresentationController" _lastPopoverPresentationController;
@"_UICampoLightweightConfiguration" _lastConfiguration;
q _lastState;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastPresentationRegion;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastAffordanceRegion;
```

## Properties

```
@property (T@"_UICampoLightweightDebugOverlayView",&,N,V_overlayView) overlayView;
@property (T@"_UICampoLightweightDebugPickerWindow",&,N,V_pickerWindow) pickerWindow;
@property (T@"UIView",W,N,V_outlinedContainerView) outlinedContainerView;
@property (T@"UIView",W,N,V_outlinedPresentedView) outlinedPresentedView;
@property (T@"UIView",W,N,V_outlinedPopoverView) outlinedPopoverView;
@property (T@"UIPopoverPresentationController",W,N,V_lastPopoverPresentationController) lastPopoverPresentationController;
@property (T@"_UICampoLightweightConfiguration",W,N,V_lastConfiguration) lastConfiguration;
@property (Tq,N,V_lastState) lastState;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_lastPresentationRegion) lastPresentationRegion;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_lastAffordanceRegion) lastAffordanceRegion;
```

## Class methods

```
+[_UICampoLightweightDebugHighlighter isEnabled];
```

## Instance methods

```
-[_UICampoLightweightDebugHighlighter lastConfiguration];
-[_UICampoLightweightDebugHighlighter overlayView];
-[_UICampoLightweightDebugHighlighter setLastConfiguration:];
-[_UICampoLightweightDebugHighlighter remove];
-[_UICampoLightweightDebugHighlighter setOverlayView:];
-[_UICampoLightweightDebugHighlighter _addOutlineToOverlay:forView:item:labelRow:];
-[_UICampoLightweightDebugHighlighter _addOutlineToOverlay:rect:fromView:item:label:dashed:labelRow:];
-[_UICampoLightweightDebugHighlighter _draw];
-[_UICampoLightweightDebugHighlighter _removePickerWindow];
-[_UICampoLightweightDebugHighlighter _updateBorderOfView:item:];
-[_UICampoLightweightDebugHighlighter _updatePickerWindowForScene:];
-[_UICampoLightweightDebugHighlighter lastAffordanceRegion];
-[_UICampoLightweightDebugHighlighter lastPopoverPresentationController];
-[_UICampoLightweightDebugHighlighter lastPresentationRegion];
-[_UICampoLightweightDebugHighlighter lastState];
-[_UICampoLightweightDebugHighlighter outlinedContainerView];
-[_UICampoLightweightDebugHighlighter outlinedPopoverView];
-[_UICampoLightweightDebugHighlighter outlinedPresentedView];
-[_UICampoLightweightDebugHighlighter pickerWindow];
-[_UICampoLightweightDebugHighlighter setLastAffordanceRegion:];
-[_UICampoLightweightDebugHighlighter setLastPopoverPresentationController:];
-[_UICampoLightweightDebugHighlighter setLastPresentationRegion:];
-[_UICampoLightweightDebugHighlighter setLastState:];
-[_UICampoLightweightDebugHighlighter setOutlinedContainerView:];
-[_UICampoLightweightDebugHighlighter setOutlinedPopoverView:];
-[_UICampoLightweightDebugHighlighter setOutlinedPresentedView:];
-[_UICampoLightweightDebugHighlighter setPickerWindow:];
-[_UICampoLightweightDebugHighlighter updateWithPopoverPresentationController:configuration:state:presentationRegion:affordanceRegion:];
```
