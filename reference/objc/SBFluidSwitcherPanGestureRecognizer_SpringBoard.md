# `SBFluidSwitcherPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBPanSystemGestureRecognizer`
- Protocols: `SBGestureRecognizerPanGestureProviding`, `SBGestureRecognizerTouchHistoryProviding`
- 7 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _installedAsSystemGesture;
B _hasEdgeResizeSeenTouchOutsideHittestedView;
@"SBFluidSwitcherViewController" _switcherViewController;
@"SBAppLayout" _initialTouchLeafAppLayout;
Q _selectedEdge;
@"SBTouchHistory" _touchHistory;
{CGPoint="x"d"y"d} _initialTouchLocation;
```

## Properties

```
@property (T@"SBTouchHistory",&,N,V_touchHistory) touchHistory;
@property (T@"SBFluidSwitcherViewController",W,N,V_switcherViewController) switcherViewController;
@property (TB,N,V_installedAsSystemGesture) installedAsSystemGesture;
@property (T{CGPoint=dd},R,N,V_initialTouchLocation) initialTouchLocation;
@property (T@"SBAppLayout",&,N,V_initialTouchLeafAppLayout) initialTouchLeafAppLayout;
@property (TQ,N,V_selectedEdge) selectedEdge;
@property (TB,N,V_hasEdgeResizeSeenTouchOutsideHittestedView) hasEdgeResizeSeenTouchOutsideHittestedView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherPanGestureRecognizer setTouchHistory:];
-[SBFluidSwitcherPanGestureRecognizer averageTouchPathAngleOverTimeDuration:];
-[SBFluidSwitcherPanGestureRecognizer touchesEnded:withEvent:];
-[SBFluidSwitcherPanGestureRecognizer conformsToSBGestureRecognizerTouchHistoryProviding];
-[SBFluidSwitcherPanGestureRecognizer initialTouchLocation];
-[SBFluidSwitcherPanGestureRecognizer peakSpeed];
-[SBFluidSwitcherPanGestureRecognizer touchHistory];
-[SBFluidSwitcherPanGestureRecognizer timeWithinRadius:];
-[SBFluidSwitcherPanGestureRecognizer setInstalledAsSystemGesture:];
-[SBFluidSwitcherPanGestureRecognizer reset];
-[SBFluidSwitcherPanGestureRecognizer setSelectedEdge:];
-[SBFluidSwitcherPanGestureRecognizer touchesBegan:withEvent:];
-[SBFluidSwitcherPanGestureRecognizer hasEdgeResizeSeenTouchOutsideHittestedView];
-[SBFluidSwitcherPanGestureRecognizer touchesMoved:withEvent:];
-[SBFluidSwitcherPanGestureRecognizer setInitialTouchLeafAppLayout:];
-[SBFluidSwitcherPanGestureRecognizer initWithTarget:action:];
-[SBFluidSwitcherPanGestureRecognizer initialTouchLeafAppLayout];
-[SBFluidSwitcherPanGestureRecognizer setHasEdgeResizeSeenTouchOutsideHittestedView:];
-[SBFluidSwitcherPanGestureRecognizer averageTouchVelocityOverTimeDuration:];
-[SBFluidSwitcherPanGestureRecognizer switcherViewController];
-[SBFluidSwitcherPanGestureRecognizer selectedEdge];
-[SBFluidSwitcherPanGestureRecognizer installedAsSystemGesture];
-[SBFluidSwitcherPanGestureRecognizer setSwitcherViewController:];
```
