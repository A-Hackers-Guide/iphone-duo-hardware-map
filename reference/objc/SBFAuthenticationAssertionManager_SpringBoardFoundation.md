# `SBFAuthenticationAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBFAuthenticationAssertionTracker" _preventLockTracker;
@"SBFAuthenticationAssertionTracker" _transientTracker;
@"<BSInvalidatable>" _stateCaptureToken;
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
-[SBFAuthenticationAssertionManager succinctDescriptionBuilder];
-[SBFAuthenticationAssertionManager init];
-[SBFAuthenticationAssertionManager addAssertion:];
-[SBFAuthenticationAssertionManager dealloc];
-[SBFAuthenticationAssertionManager descriptionWithMultilinePrefix:];
-[SBFAuthenticationAssertionManager succinctDescription];
-[SBFAuthenticationAssertionManager removeAssertion:];
-[SBFAuthenticationAssertionManager description];
-[SBFAuthenticationAssertionManager descriptionBuilderWithMultilinePrefix:];
-[SBFAuthenticationAssertionManager hasActiveAssertions];
-[SBFAuthenticationAssertionManager isAssertionValid:];
```
