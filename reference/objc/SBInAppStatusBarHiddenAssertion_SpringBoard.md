# `SBInAppStatusBarHiddenAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _reason;
@? _invalidationBlock;
@"NSDictionary" _partAlphas;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_partAlphas) partAlphas;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInAppStatusBarHiddenAssertion setPartAlphas:];
-[SBInAppStatusBarHiddenAssertion dealloc];
-[SBInAppStatusBarHiddenAssertion partAlphas];
-[SBInAppStatusBarHiddenAssertion invalidate];
-[SBInAppStatusBarHiddenAssertion initWithIdentifier:forReason:invalidationBlock:];
-[SBInAppStatusBarHiddenAssertion initWithIdentifier:forReason:partAlphas:invalidationBlock:];
-[SBInAppStatusBarHiddenAssertion invalidateWithAnimation:];
```
