# `SBPIPCompoundAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _controllerToStashAssertionMap;
@"NSString" _identifier;
q _reason;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (Tq,R,N,V_reason) reason;
```

## Instance methods

```
-[SBPIPCompoundAssertion identifier];
-[SBPIPCompoundAssertion dealloc];
-[SBPIPCompoundAssertion invalidate];
-[SBPIPCompoundAssertion reason];
-[SBPIPCompoundAssertion initWithIdentifier:reason:];
-[SBPIPCompoundAssertion addAssertionForController:windowScene:];
-[SBPIPCompoundAssertion removeAssertionForController:];
```
