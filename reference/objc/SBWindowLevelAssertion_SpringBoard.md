# `SBWindowLevelAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 4 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@? _invalidationHandler;
d _windowLevel;
q _priority;
@"NSString" _reason;
```

## Properties

```
@property (Td,R,N,V_windowLevel) windowLevel;
@property (Tq,R,N,V_priority) priority;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowLevelAssertion windowLevel];
-[SBWindowLevelAssertion priority];
-[SBWindowLevelAssertion succinctDescriptionBuilder];
-[SBWindowLevelAssertion descriptionWithMultilinePrefix:];
-[SBWindowLevelAssertion succinctDescription];
-[SBWindowLevelAssertion invalidate];
-[SBWindowLevelAssertion description];
-[SBWindowLevelAssertion reason];
-[SBWindowLevelAssertion descriptionBuilderWithMultilinePrefix:];
-[SBWindowLevelAssertion initWithPriority:windowLevel:reason:invalidationHandler:];
```
