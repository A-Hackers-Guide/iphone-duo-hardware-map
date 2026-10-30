# `SBFAuthenticationAssertionTracker`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
^{__MKBAssertion=} _mkbAssertion;
@"NSHashTable" _assertions;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFAuthenticationAssertionTracker succinctDescriptionBuilder];
-[SBFAuthenticationAssertionTracker init];
-[SBFAuthenticationAssertionTracker addAssertion:];
-[SBFAuthenticationAssertionTracker dealloc];
-[SBFAuthenticationAssertionTracker descriptionWithMultilinePrefix:];
-[SBFAuthenticationAssertionTracker succinctDescription];
-[SBFAuthenticationAssertionTracker removeAssertion:];
-[SBFAuthenticationAssertionTracker description];
-[SBFAuthenticationAssertionTracker descriptionBuilderWithMultilinePrefix:];
-[SBFAuthenticationAssertionTracker hasActiveAssertions];
-[SBFAuthenticationAssertionTracker isAssertionValid:];
-[SBFAuthenticationAssertionTracker mkbAssertionOptions];
```
