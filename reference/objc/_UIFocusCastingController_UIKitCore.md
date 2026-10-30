# `_UIFocusCastingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusCasting`
- 8 instance variables, 12 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _isRememberingEntryPoint;
@"UIFocusSystem" focusSystem;
d _entryPointMemorizationTimeout;
Q _entryPointAxis;
@"UIView" _focusMovementIndicator;
@"UIView" _focusEntryIndicator;
@"UIView" _focusCastingIndicator;
{CGPoint="x"d"y"d} _screenEntryPoint;
```

## Properties

```
@property (T{CGPoint=dd},N,V_screenEntryPoint) screenEntryPoint;
@property (TQ,N,V_entryPointAxis) entryPointAxis;
@property (TB,N,V_isRememberingEntryPoint) isRememberingEntryPoint;
@property (T@"UIView",&,N,V_focusMovementIndicator) focusMovementIndicator;
@property (T@"UIView",&,N,V_focusEntryIndicator) focusEntryIndicator;
@property (T@"UIView",&,N,V_focusCastingIndicator) focusCastingIndicator;
@property (Td,N,V_entryPointMemorizationTimeout) entryPointMemorizationTimeout;
@property (T@"UIFocusSystem",W,N,VfocusSystem) focusSystem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusCastingController focusEntryIndicator];
-[_UIFocusCastingController _castingPointInNormalizedFrame:forHeading:];
-[_UIFocusCastingController isRememberingEntryPoint];
-[_UIFocusCastingController _createFocusMovementIndicator];
-[_UIFocusCastingController _normalizedCoordinateSpace];
-[_UIFocusCastingController entryPointMemorizationTimeout];
-[_UIFocusCastingController focusCastingIndicator];
-[_UIFocusCastingController init];
-[_UIFocusCastingController forceUpdateFocusCastingFocusedRect:coordinateSpace:heading:];
-[_UIFocusCastingController _destroyFocusMovementIndicator];
-[_UIFocusCastingController screenEntryPoint];
-[_UIFocusCastingController setIsRememberingEntryPoint:];
-[_UIFocusCastingController _focusEffectsControllerForFocusedItem];
-[_UIFocusCastingController setEntryPointMemorizationTimeout:];
-[_UIFocusCastingController _updateFocusMovementIndicatorDisplay];
-[_UIFocusCastingController setFocusSystem:];
-[_UIFocusCastingController _updateFocusItemFromNormalizedFrame:toNormalizedFrame:withHeading:];
-[_UIFocusCastingController _axisForHeading:];
-[_UIFocusCastingController _entryPointInNormalizedFrame:forHeading:];
-[_UIFocusCastingController setScreenEntryPoint:];
-[_UIFocusCastingController _stopRememberingEntryPoint];
-[_UIFocusCastingController _castingFrameForFocusedNormalizedFrame:heading:];
-[_UIFocusCastingController _startRememberingEntryPoint];
-[_UIFocusCastingController entryPointAxis];
-[_UIFocusCastingController focusSystem];
-[_UIFocusCastingController setFocusMovementIndicator:];
-[_UIFocusCastingController setEntryPointAxis:];
-[_UIFocusCastingController forgetEntryPoint];
-[_UIFocusCastingController updateFocusCastingWithContext:];
-[_UIFocusCastingController castingFrameForFocusedItem:heading:inCoordinateSpace:];
-[_UIFocusCastingController focusMovementIndicator];
-[_UIFocusCastingController focusEffectsController:updateMovementDirection:];
-[_UIFocusCastingController setFocusCastingIndicator:];
-[_UIFocusCastingController teardown];
-[_UIFocusCastingController _movementPointInNormalizedFrame:];
-[_UIFocusCastingController _positionFocusMovementIndicators];
-[_UIFocusCastingController setFocusEntryIndicator:];
```
