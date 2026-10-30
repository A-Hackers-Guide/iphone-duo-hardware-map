# `SBCaptureApplicationLaunchAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 4 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@? _invalidationHandler;
@"NSUUID" _identifier;
@"NSString" _bundleIdentifier;
@"NSString" _reason;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_identifier) identifier;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureApplicationLaunchAssertion identifier];
-[SBCaptureApplicationLaunchAssertion succinctDescriptionBuilder];
-[SBCaptureApplicationLaunchAssertion bundleIdentifier];
-[SBCaptureApplicationLaunchAssertion descriptionWithMultilinePrefix:];
-[SBCaptureApplicationLaunchAssertion succinctDescription];
-[SBCaptureApplicationLaunchAssertion invalidate];
-[SBCaptureApplicationLaunchAssertion description];
-[SBCaptureApplicationLaunchAssertion reason];
-[SBCaptureApplicationLaunchAssertion descriptionBuilderWithMultilinePrefix:];
-[SBCaptureApplicationLaunchAssertion initWithIdentifier:bundleIdentifier:reason:invalidationHandler:];
```
