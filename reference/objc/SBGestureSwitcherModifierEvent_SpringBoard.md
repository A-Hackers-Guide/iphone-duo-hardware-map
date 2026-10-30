# `SBGestureSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEvent`
- Protocols: `SBGestureRecognizerTouchHistoryProviding`
- 16 instance variables, 20 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _pointerTouch;
B _mouseEvent;
B _canceled;
@"NSUUID" _gestureID;
@"SBAppLayout" _selectedAppLayout;
q _gestureType;
Q _phase;
q _modifierFlags;
q _touchType;
d _lastTouchTimestamp;
d _hysteresis;
Q _hidEventSenderID;
@"<SBGestureRecognizerTouchHistoryProviding>" _touchHistoryProvider;
{CGPoint="x"d"y"d} _locationInContainerView;
{CGPoint="x"d"y"d} _translationInContainerView;
{CGPoint="x"d"y"d} _velocityInContainerView;
```

## Properties

```
@property (TQ,N,V_phase) phase;
@property (Tq,N,V_touchType) touchType;
@property (TB,N,GisMouseEvent,V_mouseEvent) mouseEvent;
@property (TB,N,GisPointerTouch,V_pointerTouch) pointerTouch;
@property (TQ,N,V_hidEventSenderID) hidEventSenderID;
@property (TB,N,GisCanceled,V_canceled) canceled;
@property (Td,N,V_lastTouchTimestamp) lastTouchTimestamp;
@property (T{CGPoint=dd},N,V_locationInContainerView) locationInContainerView;
@property (T{CGPoint=dd},N,V_translationInContainerView) translationInContainerView;
@property (T{CGPoint=dd},N,V_velocityInContainerView) velocityInContainerView;
@property (Td,N,V_hysteresis) hysteresis;
@property (T@"<SBGestureRecognizerTouchHistoryProviding>",&,N,V_touchHistoryProvider) touchHistoryProvider;
@property (T@"NSUUID",R,N,V_gestureID) gestureID;
@property (T@"SBAppLayout",R,N,V_selectedAppLayout) selectedAppLayout;
@property (Tq,R,N,V_gestureType) gestureType;
@property (Tq,R,N,V_modifierFlags) modifierFlags;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBGestureSwitcherModifierEvent setHysteresis:];
-[SBGestureSwitcherModifierEvent averageTouchPathAngleOverTimeDuration:];
-[SBGestureSwitcherModifierEvent conformsToSBGestureRecognizerTouchHistoryProviding];
-[SBGestureSwitcherModifierEvent hysteresis];
-[SBGestureSwitcherModifierEvent peakSpeed];
-[SBGestureSwitcherModifierEvent timeWithinRadius:];
-[SBGestureSwitcherModifierEvent isCanceled];
-[SBGestureSwitcherModifierEvent phase];
-[SBGestureSwitcherModifierEvent selectedAppLayout];
-[SBGestureSwitcherModifierEvent modifierFlags];
-[SBGestureSwitcherModifierEvent setCanceled:];
-[SBGestureSwitcherModifierEvent type];
-[SBGestureSwitcherModifierEvent gestureType];
-[SBGestureSwitcherModifierEvent setPhase:];
-[SBGestureSwitcherModifierEvent averageTouchVelocityOverTimeDuration:];
-[SBGestureSwitcherModifierEvent copyWithZone:];
-[SBGestureSwitcherModifierEvent descriptionBuilderWithMultilinePrefix:];
-[SBGestureSwitcherModifierEvent lastTouchTimestamp];
-[SBGestureSwitcherModifierEvent setTouchType:];
-[SBGestureSwitcherModifierEvent touchType];
-[SBGestureSwitcherModifierEvent gestureID];
-[SBGestureSwitcherModifierEvent hidEventSenderID];
-[SBGestureSwitcherModifierEvent initWithGestureID:selectedAppLayout:gestureType:phase:];
-[SBGestureSwitcherModifierEvent initWithGestureID:selectedAppLayout:gestureType:phase:modifierFlags:];
-[SBGestureSwitcherModifierEvent isGestureEvent];
-[SBGestureSwitcherModifierEvent isMouseEvent];
-[SBGestureSwitcherModifierEvent isPointerTouch];
-[SBGestureSwitcherModifierEvent locationInContainerView];
-[SBGestureSwitcherModifierEvent setHidEventSenderID:];
-[SBGestureSwitcherModifierEvent setLastTouchTimestamp:];
-[SBGestureSwitcherModifierEvent setLocationInContainerView:];
-[SBGestureSwitcherModifierEvent setMouseEvent:];
-[SBGestureSwitcherModifierEvent setPointerTouch:];
-[SBGestureSwitcherModifierEvent setTouchHistoryProvider:];
-[SBGestureSwitcherModifierEvent setTranslationInContainerView:];
-[SBGestureSwitcherModifierEvent setVelocityInContainerView:];
-[SBGestureSwitcherModifierEvent touchHistoryProvider];
-[SBGestureSwitcherModifierEvent translationInContainerView];
-[SBGestureSwitcherModifierEvent velocityInContainerView];
```
