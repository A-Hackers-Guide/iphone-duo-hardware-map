# `SBFloatingDockWindowLevelAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 4 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBFloatingDockController" _floatingDockController;
Q _priority;
d _level;
@"NSString" _reason;
```

## Properties

```
@property (T@"SBFloatingDockController",R,W,N,V_floatingDockController) floatingDockController;
@property (TQ,R,N,V_priority) priority;
@property (Td,R,N,V_level) level;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFloatingDockWindowLevelAssertion priority];
-[SBFloatingDockWindowLevelAssertion floatingDockController];
-[SBFloatingDockWindowLevelAssertion succinctDescriptionBuilder];
-[SBFloatingDockWindowLevelAssertion dealloc];
-[SBFloatingDockWindowLevelAssertion level];
-[SBFloatingDockWindowLevelAssertion descriptionWithMultilinePrefix:];
-[SBFloatingDockWindowLevelAssertion succinctDescription];
-[SBFloatingDockWindowLevelAssertion invalidate];
-[SBFloatingDockWindowLevelAssertion description];
-[SBFloatingDockWindowLevelAssertion reason];
-[SBFloatingDockWindowLevelAssertion descriptionBuilderWithMultilinePrefix:];
-[SBFloatingDockWindowLevelAssertion initWithFloatingDockController:priority:level:reason:];
```
