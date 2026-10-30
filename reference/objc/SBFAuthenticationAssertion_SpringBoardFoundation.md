# `SBFAuthenticationAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 6 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _activated;
B _invalidated;
@"NSDate" _activationDate;
q _type;
@"NSString" _identifier;
@"SBFUserAuthenticationController" _controller;
```

## Properties

```
@property (TB,R,D,N,GisValid) valid;
@property (Tq,R,N,V_type) type;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"SBFUserAuthenticationController",R,W,N,V_controller) controller;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFAuthenticationAssertion publicDescription];
-[SBFAuthenticationAssertion controller];
-[SBFAuthenticationAssertion identifier];
-[SBFAuthenticationAssertion succinctDescriptionBuilder];
-[SBFAuthenticationAssertion dealloc];
-[SBFAuthenticationAssertion descriptionWithMultilinePrefix:];
-[SBFAuthenticationAssertion succinctDescription];
-[SBFAuthenticationAssertion invalidate];
-[SBFAuthenticationAssertion type];
-[SBFAuthenticationAssertion isValid];
-[SBFAuthenticationAssertion activate];
-[SBFAuthenticationAssertion description];
-[SBFAuthenticationAssertion initWithIdentifier:type:withController:];
-[SBFAuthenticationAssertion descriptionBuilderWithMultilinePrefix:];
```
