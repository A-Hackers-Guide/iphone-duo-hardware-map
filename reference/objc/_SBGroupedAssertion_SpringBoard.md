# `_SBGroupedAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `BSInvalidatable`
- 2 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _assertions;
@"NSString" _reason;
```

## Properties

```
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBGroupedAssertion init];
-[_SBGroupedAssertion addAssertion:];
-[_SBGroupedAssertion appendDescriptionToFormatter:];
-[_SBGroupedAssertion initWithReason:];
-[_SBGroupedAssertion invalidate];
-[_SBGroupedAssertion description];
-[_SBGroupedAssertion reason];
-[_SBGroupedAssertion addAssertions:];
-[_SBGroupedAssertion initWithReason:assertions:];
```
