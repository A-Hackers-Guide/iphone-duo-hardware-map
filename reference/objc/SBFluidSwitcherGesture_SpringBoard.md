# `SBFluidSwitcherGesture`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 6 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
@? _eventProvider;
q _state;
@"SBAppLayout" _selectedAppLayout;
@"UIGestureRecognizer" _gestureRecognizerForStudyLog;
q _type;
q _selectedLayoutRole;
```

## Properties

```
@property (Tq,N,S_setState:,V_state) state;
@property (T@"SBAppLayout",&,N,S_setSelectedAppLayout:,V_selectedAppLayout) selectedAppLayout;
@property (Tq,N,S_setSelectedLayoutRole:,V_selectedLayoutRole) selectedLayoutRole;
@property (T@"UIGestureRecognizer",&,N,S_setGestureRecognizerForStudyLog:,V_gestureRecognizerForStudyLog) gestureRecognizerForStudyLog;
@property (Tq,R,N,V_type) type;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherGesture _setState:];
-[SBFluidSwitcherGesture succinctDescriptionBuilder];
-[SBFluidSwitcherGesture selectedAppLayout];
-[SBFluidSwitcherGesture descriptionWithMultilinePrefix:];
-[SBFluidSwitcherGesture succinctDescription];
-[SBFluidSwitcherGesture type];
-[SBFluidSwitcherGesture description];
-[SBFluidSwitcherGesture studyLogData];
-[SBFluidSwitcherGesture state];
-[SBFluidSwitcherGesture descriptionBuilderWithMultilinePrefix:];
-[SBFluidSwitcherGesture _setGestureRecognizerForStudyLog:];
-[SBFluidSwitcherGesture _setSelectedAppLayout:];
-[SBFluidSwitcherGesture _setSelectedLayoutRole:];
-[SBFluidSwitcherGesture gestureEvent];
-[SBFluidSwitcherGesture gestureRecognizerForStudyLog];
-[SBFluidSwitcherGesture initWithType:eventProvider:];
-[SBFluidSwitcherGesture selectedLayoutRole];
```
