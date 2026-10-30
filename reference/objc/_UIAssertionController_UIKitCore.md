# `_UIAssertionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _activeAssertionRecords;
@"<_UIAssertionControllerSubject>" _subject;
```

## Properties

```
@property (T@"<_UIAssertionControllerSubject>",R,W,N,V_subject) subject;
```

## Instance methods

```
-[_UIAssertionController _endTrackingAssertion:];
-[_UIAssertionController subject];
-[_UIAssertionController debugDescription];
-[_UIAssertionController hasAssertionsForReason:];
-[_UIAssertionController vendAssertionOfType:initialState:reason:requiresExplicitInvalidation:];
-[_UIAssertionController vendAssertionOfType:initialState:];
-[_UIAssertionController vendAssertionOfType:initialState:reason:];
-[_UIAssertionController _beginTrackingAssertion:];
-[_UIAssertionController initWithAssertionSubject:];
-[_UIAssertionController _enforceSubjectAwarenessOfAssertionState:forAssertionType:];
-[_UIAssertionController hasAssertionsOfType:];
```
