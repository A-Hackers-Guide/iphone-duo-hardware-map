# `PKResponderState`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _toolPickerVisibility;
@"PKToolPicker" _activeToolPicker;
@"UIResponder" __responder;
q __focusDepth;
```

## Properties

```
@property (T@"UIResponder",W,N,V__responder) _responder;
@property (Tq,N,V__focusDepth) _focusDepth;
@property (Tq,N,V_toolPickerVisibility) toolPickerVisibility;
@property (T@"PKToolPicker",&,N,V_activeToolPicker) activeToolPicker;
```

## Instance methods

```
-[PKResponderState copy];
-[PKResponderState _responder];
-[PKResponderState set_focusDepth:];
-[PKResponderState _currentActiveToolPicker];
-[PKResponderState _currentToolPickerVisibility];
-[PKResponderState _focusDepth];
-[PKResponderState _requestToolPickerVisibilityUpdate];
-[PKResponderState activeToolPicker];
-[PKResponderState setActiveToolPicker:];
-[PKResponderState setToolPickerVisibility:];
-[PKResponderState set_responder:];
-[PKResponderState toolPickerVisibility];
```
