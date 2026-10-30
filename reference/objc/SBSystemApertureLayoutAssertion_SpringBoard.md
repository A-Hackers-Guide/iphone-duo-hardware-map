# `SBSystemApertureLayoutAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAInvalidatable`
- 4 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
@? _invalidationHandler;
@"NSMutableSet" _invalidationBlocks;
q _maximumPermittedLayoutMode;
@"NSString" _reason;
```

## Properties

```
@property (Tq,R,N,V_maximumPermittedLayoutMode) maximumPermittedLayoutMode;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TB,R,N,GisValid) valid;
@property (T@"NSDate",?,R,C,N) creationDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureLayoutAssertion invalidateWithReason:];
-[SBSystemApertureLayoutAssertion addInvalidationBlock:];
-[SBSystemApertureLayoutAssertion dealloc];
-[SBSystemApertureLayoutAssertion isValid];
-[SBSystemApertureLayoutAssertion description];
-[SBSystemApertureLayoutAssertion reason];
-[SBSystemApertureLayoutAssertion initWithMaximumPermittedLayoutMode:reason:invalidationHandler:];
-[SBSystemApertureLayoutAssertion maximumPermittedLayoutMode];
```
