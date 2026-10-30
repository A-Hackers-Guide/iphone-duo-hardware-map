# `SBFloatingDockBehaviorAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 8 instance variables, 13 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _animated;
B _gesturePossible;
Q _level;
d _progress;
d _dockAlpha;
@"NSString" _reason;
@"NSDate" _timestamp;
@"SBFloatingDockController" _floatingDockController;
```

## Properties

```
@property (T@"SBFloatingDockController",R,W,N,V_floatingDockController) floatingDockController;
@property (TQ,R,N,V_level) level;
@property (TB,N,GisAnimated,V_animated) animated;
@property (TB,R,N,GisPinned) pinned;
@property (TB,R,N,V_gesturePossible) gesturePossible;
@property (Td,R,N,V_progress) progress;
@property (Td,N,V_dockAlpha) dockAlpha;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (T@"NSDate",R,C,N,V_timestamp) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFloatingDockBehaviorAssertion isPinned];
-[SBFloatingDockBehaviorAssertion floatingDockController];
-[SBFloatingDockBehaviorAssertion succinctDescriptionBuilder];
-[SBFloatingDockBehaviorAssertion isAnimated];
-[SBFloatingDockBehaviorAssertion dealloc];
-[SBFloatingDockBehaviorAssertion timestamp];
-[SBFloatingDockBehaviorAssertion level];
-[SBFloatingDockBehaviorAssertion descriptionWithMultilinePrefix:];
-[SBFloatingDockBehaviorAssertion setAnimated:];
-[SBFloatingDockBehaviorAssertion progress];
-[SBFloatingDockBehaviorAssertion succinctDescription];
-[SBFloatingDockBehaviorAssertion invalidate];
-[SBFloatingDockBehaviorAssertion description];
-[SBFloatingDockBehaviorAssertion reason];
-[SBFloatingDockBehaviorAssertion descriptionBuilderWithMultilinePrefix:];
-[SBFloatingDockBehaviorAssertion invalidateWithCompletion:];
-[SBFloatingDockBehaviorAssertion gesturePossible];
-[SBFloatingDockBehaviorAssertion dockAlpha];
-[SBFloatingDockBehaviorAssertion initWithFloatingDockController:visibleProgress:animated:gesturePossible:atLevel:reason:withCompletion:];
-[SBFloatingDockBehaviorAssertion modifyProgress:interactive:completion:];
-[SBFloatingDockBehaviorAssertion setDockAlpha:];
```
