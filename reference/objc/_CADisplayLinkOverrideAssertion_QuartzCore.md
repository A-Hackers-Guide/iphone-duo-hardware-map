# `_CADisplayLinkOverrideAssertion`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAInvalidatable`
- 5 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
I _displayId;
@"NSString" _systemIdentifier;
@"CADisplay" _originalDisplay;
@"NSHashTable" _originalLinks;
B _invalidated;
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
-[_CADisplayLinkOverrideAssertion displayId];
-[_CADisplayLinkOverrideAssertion _applyOverrideToLink:];
-[_CADisplayLinkOverrideAssertion dealloc];
-[_CADisplayLinkOverrideAssertion invalidate];
-[_CADisplayLinkOverrideAssertion _initWithDisplayId:originalDisplay:systemIdentifier:];
-[_CADisplayLinkOverrideAssertion _applyOverride];
-[_CADisplayLinkOverrideAssertion _recordOverriddenLink:];
-[_CADisplayLinkOverrideAssertion _restoreDisplayIfInvalidated];
```
